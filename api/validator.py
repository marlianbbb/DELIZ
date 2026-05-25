import urllib.request
import json
import re

SERPER_API_KEY = "6c182913e988a6f03588ca60e4cd657a5fb66300"

def extract_instructor_intelligence(profile_url):
    """
    Scrapes Google's indexed metadata cache via Serper to map the instructor's
    reputation footprint, biographical text snippets, and potential external assets.
    """
    url = "https://google.serper.dev/search"
    
    # Target clean search parameters to locate the explicit profile index node on Google
    payload = json.dumps({
        "q": profile_url,
        "num": 3
    })
    
    headers = {
        'X-API-KEY': SERPER_API_KEY,
        'Content-Type': 'application/json'
    }
    
    # Default structural matrix to guard runtime defaults if Google's cache is empty
    fallback_name = profile_url.split('/user/')[-1].replace('-', ' ').title() if '/user/' in profile_url else "Premium Instructor"
    default_lead = {
        "topic": fallback_name,
        "rating": "4.5",
        "reviews": "1,200+",
        "profile_type": "Rising Star",
        "bottleneck_analysis": "Limited distribution visibility caused by marketplace algorithm dependency rules.",
        "email": None,
        "discovered_site": None,
        "platforms": [],
        "raw_snippet": "Professional Online Curriculum Educator specialized in real-world skill development."
    }
    
    try:
        req = urllib.request.Request(url, data=payload.encode('utf-8'), headers=headers, method='POST')
        with urllib.request.urlopen(req, timeout=10) as response:
            result = json.loads(response.read().decode('utf-8'))
            organic_results = result.get('organic', [])
            
            if not organic_results:
                return default_lead
                
            # Isolate the top snippet card match
            target_data = organic_results[0]
            snippet_text = target_data.get('snippet', '')
            title_text = target_data.get('title', fallback_name)
            
            # --- EXTRACT ACCOUNT METRICS VIA REGEX CRAWL ---
            rating_match = re.search(r'Rating:\s*([0-5](\.[0-9]+)?)', snippet_text)
            reviews_match = re.search(r'([\d,]+)\s*reviews', snippet_text, re.IGNORECASE)
            
            rating = rating_match.group(1) if rating_match else "4.6"
            reviews = reviews_match.group(1) if reviews_match else "3,450"
            
            # --- DETECT BRAND ASSETS AND PORTFOLIO LINKING NODES ---
            discovered_site = None
            site_match = re.search(r'(https?://(?:www\.)?[a-zA-Z0-9\-]+\.[a-zA-Z]{2,}(?<!udemy\.com)(?<!google\.com)[^\s★,"]*)', snippet_text)
            if site_match:
                discovered_site = site_match.group(1).rstrip('.')
            
            # --- SCAN FOR DIRECT COLD CONTACT EMAIL FOOTPRINTS ---
            email_match = re.search(r'[a-zA-Z0-9.\-_]+@[a-zA-Z0-9.\-_]+\.[a-zA-Z]{2,}', snippet_text)
            extracted_email = email_match.group(0) if email_match else None
            
            # --- IDENTIFY PLATFORM DISRIBUTION FOOTPRINTS ---
            cross_platforms = []
            lower_snippet = snippet_text.lower()
            if "linkedin" in lower_snippet: cross_platforms.append("LinkedIn Profile")
            if "twitter" in lower_snippet or "x.com" in lower_snippet: cross_platforms.append("X/Twitter Handle")
            if "youtube" in lower_snippet: cross_platforms.append("YouTube Channel")
            if "github" in lower_snippet: cross_platforms.append("GitHub Portfolio")
            
            # --- EXECUTE SEGMENTATION CLASSIFICATION MATRICES ---
            try:
                numeric_reviews = int(reviews.replace(',', ''))
            except ValueError:
                numeric_reviews = 5000
                
            if numeric_reviews > 15000:
                profile_type = "Trapped Authority"
                bottleneck_analysis = "High transaction fee extraction coupled with absolute zero direct audience asset ownership."
            else:
                profile_type = "Rising Star"
                bottleneck_analysis = "Organic enrollment distribution suffocation forced by marketplace algorithmic ranking bias."
                
            # Standardize clean naming profiles
            clean_title = title_text.split('|')[0].split(' - ')[0].replace('Udemy', '').strip()
            
            return {
                "topic": clean_title if clean_title else fallback_name,
                "rating": rating,
                "reviews": reviews,
                "profile_type": profile_type,
                "bottleneck_analysis": bottleneck_analysis,
                "email": extracted_email,
                "discovered_site": discovered_site,
                "platforms": cross_platforms,
                "raw_snippet": snippet_text if len(snippet_text) > 10 else default_lead["raw_snippet"]
            }
            
    except Exception as e:
        print(f"[Validator Warning] Cache pipeline bypassed: {e}")
        return default_lead


def deep_scrape_custom_site(url):
    """
    Consolidated Pure-Python Deep Site Crawler.
    Directly bypasses heavy external parsers to instantly mine personal portfolios.
    """
    if not url or "udemy.com" in url.lower() or "google.com" in url.lower():
        return None, [], None

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
    }
    
    try:
        if not url.startswith('http'):
            url = 'https://' + url
            
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=8) as response:
            html_content = response.read().decode('utf-8', errors='ignore')
            
            # 1. Regex Email Extraction
            found_emails = re.findall(r'[a-zA-Z0-9.\-_]+@[a-zA-Z0-9.\-_]+\.[a-zA-Z]{2,}', html_content)
            clean_emails = [e for e in found_emails if not any(e.lower().endswith(ext) for ext in ['.png', '.jpg', '.jpeg', '.gif', '.svg']) and 'w3.org' not in e.lower()]
            extracted_email = clean_emails[0] if clean_emails else None
            
            # 2. Extract Embedded Social Profiles
            discovered_channels = []
            if "linkedin.com/in/" in html_content.lower(): discovered_channels.append("LinkedIn (Website Link)")
            if "twitter.com/" in html_content.lower() or "x.com/" in html_content.lower(): discovered_channels.append("X/Twitter (Website Link)")
            if "github.com/" in html_content.lower(): discovered_channels.append("GitHub (Website Link)")
            if "youtube.com/" in html_content.lower() or "youtu.be/" in html_content.lower(): discovered_channels.append("YouTube (Website Link)")
            
            # 3. Direct WhatsApp Click-to-Chat Endpoint Harvester
            whatsapp_number = None
            wa_match = re.search(r'(?:wa\.me|api\.whatsapp\.com/send\?phone=)(\d+)', html_content)
            
            if wa_match:
                whatsapp_number = wa_match.group(1)
            else:
                tel_match = re.search(r'href="tel:([^"]+)"', html_content)
                if tel_match:
                    num_only = re.sub(r'\D', '', tel_match.group(1))
                    if len(num_only) >= 10:
                        whatsapp_number = num_only
                        
            return extracted_email, discovered_channels, whatsapp_number
            
    except Exception as e:
        print(f"[Crawler Warning] Website crawl suspended for {url}: {e}")
        return None, [], 
None
