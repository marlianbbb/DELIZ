import json
import urllib.request
import urllib.parse

GEMINI_API_KEY = "AIzaSyBowKwwEg16zM2H9_B_VAE3xPU196q30Pw"

def generate_ai_outreach(topic, rating, reviews, profile_type, bottleneck_analysis, raw_snippet, verified_wa):
    """
    Advanced Copywriting Engine. Coordinates with Gemini 2.5 Flash to generate
    deeply contextual, long-form cold acquisition proposals signed by Davies Emmanuel.
    """
    # Strips away marketplace title noise to cleanly address the instructor
    clean_topic = topic.replace("Udemy:", "").strip()
    
    # Premium enterprise-level prompt engineering framework
    prompt_text = (
        f"Role: You are an elite, high-ticket B2B business growth consultant and enterprise marketing engineer.\n"
        f"Task: Write a thorough, comprehensive, long-form cold acquisition proposal to a professional online educator specializing in '{clean_topic}'.\n\n"
        f"Target Profile Intelligence:\n"
        f"- Educator Focus: {clean_topic}\n"
        f"- Performance Baseline: {rating} out of 5 stars across {reviews} verified student reviews.\n"
        f"- Segment: {profile_type}\n"
        f"- Operational Bottleneck: {bottleneck_analysis}\n"
        f"- Biography Profile Text: \"{raw_snippet}\"\n\n"
        f"Strict Copywriting Directives:\n"
        f"1. Zero Conversation Fluff: Never open with sentences like 'I hope you are doing well', 'My name is...', or any variant of cold email pleasantries. Drop straight into business.\n"
        f"2. Paragraph 1 (Bespoke Calibration): Study the 'Biography Profile Text'. Synthesize their exact professional background, real-world industry experience, or specific phrases they used into your opening lines. Anchor this contextual praise directly to their live metrics ({rating} stars over {reviews} reviews) to prove this is a deeply researched, hand-crafted evaluation.\n"
        f"3. Paragraph 2 (The Structural Pain Point): Aggressively break down the financial flaws of their current positioning. If they are a Rising Star, explain how third-party marketplace algorithms systematically suffocate high-quality independent creators to protect established legacy institutions. If they are a Trapped Authority, break down the severe risk of zero asset ownership, explaining how giving up 100% of student data control and losing massive percentage cuts on every transaction limits their true business scale.\n"
        f"4. Paragraph 3 (The Freelance Strategic Solution): Position yourself as an elite consultant who fixes these core flaws. For Rising Stars, introduce your custom external lead generation pipelines and high-intent social traffic frameworks designed to bypass platform algorithms. For Trapped Authorities, introduce your independent off-platform audience funnels, automated backend systems, and custom web infrastructure.\n"
        f"5. The Call To Action & Sign-off: End with a sharp, highly confident, one-sentence close asking if they are open to examining a detailed 2-minute growth blueprint for their brand this week. Sign off the proposal formally as: 'Best regards,\\nDavies Emmanuel'.\n\n"
        f"Output Specification: Output ONLY the high-value text copy. Begin directly with 'Subject:' and nothing else."
    )

    url = f"https://generativelanguage.googleapis.com/v1/models/gemini-2.5-flash:generateContent?key={GEMINI_API_KEY}"
    
    payload = json.dumps({
        "contents": [{
            "parts": [{
                "text": prompt_text
            }]
        }]
    })
    
    headers = {'Content-Type': 'application/json'}
    
    try:
        req = urllib.request.Request(url, data=payload.encode('utf-8'), headers=headers, method='POST')
        with urllib.request.urlopen(req, timeout=12) as response:
            res = json.loads(response.read().decode('utf-8'))
            email_body = res['candidates'][0]['content']['parts'][0]['text'].strip()
    except Exception:
        # Standard fallback matrix if the API handshake experiences latency drops
        if profile_type == "Rising Star":
            email_body = (
                f"Subject: Scale framework for your professional {clean_topic} curriculum\n\n"
                f"Your established track record in the {clean_topic} landscape paired with an exceptional {rating}★ rating demonstrates incredible educational value. "
                f"However, keeping this content isolated inside third-party marketplaces means your enrollment acceleration is entirely dependent on internal search visibility. With reviews currently holding at {reviews}, the platform's core algorithm naturally funnels traffic to legacy multi-instructor monopolies.\n\n"
                f"To solve this distribution chokehold, I engineer dedicated external lead generation systems tailored specifically for high-tier instructors. By capturing high-intent professional and enterprise leads directly from networks like LinkedIn and X, we can create an independent enrollment velocity that forces your courses to scale rapidly.\n\n"
                f"Are you open to reviewing a targeted 2-minute promotional traffic blueprint I mapped out for your curriculum this week?\n\n"
                f"Best regards,\nDavies Emmanuel"
            )
        else:
            email_body = (
                f"Subject: Direct distribution infrastructure and audience control for {clean_topic}\n\n"
                f"Maintaining an elite {rating}★ average across a massive base of {reviews} student reviews is undeniable proof of your authority in the {clean_topic} sector. "
                f"Yet, under current marketplace operating frameworks, you are facing a critical structural vulnerability: complete separation from your customer assets. Giving up 100% of your student data control while absorbing massive platform transaction cuts severely limits your long-term revenue backend.\n\n"
                f"I specialize in architecting independent, off-platform audience funnel systems and custom landing environments for premier educators. My framework deploys automated email capture systems and independent payment routes, allowing you to bypass third-party restrictions and capture direct high-ticket backend value.\n\n"
                f"Are you open to a brief text exchange to look over a 2-minute audience ownership blueprint this week?\n\n"
                f"Best regards,\nDavies Emmanuel"
            )

    # --- ADVANCED WHATSAPP TARGET GENERATION ---
    whatsapp_link = None
    if verified_wa:
        if profile_type == "Rising Star":
            whatsapp_pitch = f"Hello! I was reviewing your {clean_topic} course footprint ({rating}⭐). Your background looks solid, but internal visibility looks restricted by the marketplace algorithm. Can I drop a quick note here showing how we deploy external lead gen traffic to scale your enrollments? - Davies Emmanuel"
        else:
            whatsapp_pitch = f"Hello! Incredible work tracking {reviews} reviews on your {clean_topic} curriculum. I noticed a massive data-ownership risk with third-party networks. Can I send a 2-minute note showing how we build direct standalone student channels off-platform? - Davies Emmanuel"
            
        whatsapp_link = f"https://wa.me/{verified_wa}?text={urllib.parse.quote(whatsapp_pitch)}"

    return email_body, whatsapp_
  link
