from http.server import BaseHTTPRequestHandler
import json
import urllib.parse

# Direct flat-folder imports to ensure Vercel never runs into import directory errors
from api.validator import extract_instructor_intelligence, deep_scrape_custom_site
from api.copywriter import generate_ai_outreach
from api.notifier import send_telegram_ping

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        """
        Consolidated Serverless Orchestrator.
        Listens for target parameters and renders a live, modern web dashboard.
        """
        # Parse query string arguments from the incoming browser address bar
        parsed_url = urllib.parse.urlparse(self.path)
        query_params = urllib.parse.parse_qs(parsed_url.query)
        target_profile_url = query_params.get('url', [None])[0]
        
        # --- PROTECTION LAYER: RENDER MANUAL AWAITING SCREEN ---
        if not target_profile_url:
            self.send_response(200)
            self.send_header('Content-type', 'text/html; charset=utf-8')
            self.end_headers()
            
            awaiting_html = """
            <!DOCTYPE html>
            <html>
            <head>
                <meta charset="utf-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>Partner Engine Standby</title>
                <style>
                    body { font-family: -apple-system, sans-serif; background: #0a0b0d; color: #b9bbbe; padding: 30px; text-align: center; }
                    .box { max-width: 550px; margin: 80px auto; background: #121318; padding: 40px; border-radius: 12px; border: 1px solid #1f2026; }
                    h2 { color: #5865f2; margin-top: 0; font-size: 22px; }
                    code { background: #1a1b22; color: #00ffcc; padding: 8px 12px; border-radius: 6px; font-family: monospace; display: block; margin: 20px 0; word-break: break-all; font-size: 13px; }
                </style>
            </head>
            <body>
                <div class="box">
                    <h2>🚀 Superite Partner Engine Active</h2>
                    <p>The serverless background pipeline is standing by. Drop a target instructor URL parameter into your mobile address bar to execute a run.</p>
                    <code>?url=https://www.udemy.com/user/lindsay-marsh/</code>
                </div>
            </body>
            </html>
            """
            self.wfile.write(awaiting_html.encode('utf-8'))
            return

        # Force browser rendering directly on your screen to destroy the download loop glitch
        self.send_response(200)
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()

        print(f"[Core Initialization] Harvesting pipeline running on target: {target_profile_url}")

        # --- STEP 1: SCAN GOOGLE CACHE PLATFORM FOOTPRINTS ---
        parsed_lead = extract_instructor_intelligence(target_profile_url)
        
        # --- STEP 2: LAUNCH DEEP DOMAIN WEBSITE CRAWLER ---
        custom_site_target = parsed_lead.get('discovered_site')
        deep_email = None
        deep_channels = []
        verified_whatsapp_num = None
        
        if custom_site_target:
            print(f"[Deep Scan Run] Strip-mining HTML contents on: {custom_site_target}")
            deep_email, deep_channels, verified_whatsapp_num = deep_scrape_custom_site(custom_site_target)
            
        # Consolidation matrix: prefer deep scraped targets over broad fallback metadata search strings
        final_email = deep_email if deep_email else parsed_lead['email']
        all_channels = list(set(parsed_lead['platforms'] + deep_channels))
        
        contact_display = final_email if final_email and "@" in final_email else "No email uncovered in bio text"
        site_display = custom_site_target if custom_site_target else "No personal external portfolio link found"
        channel_display = ", ".join(all_channels) if all_channels else "Direct Udemy Profile Footprint Only"
        
        # --- STEP 3: CONSTRUCT ENTERPRISE PROPOSAL VIA GEMINI ---
        email_pitch, whatsapp_workspace_link = generate_ai_outreach(
            parsed_lead['topic'],
            parsed_lead['rating'],
            parsed_lead['reviews'],
            parsed_lead['profile_type'],
            parsed_lead['bottleneck_analysis'],
            parsed_lead['raw_snippet'],
            verified_whatsapp_num
        )
        
        # --- STEP 4: PACKAGE TELEGRAM TELEMETRY METRICS ---
        whatsapp_section = ""
        if whatsapp_workspace_link:
            whatsapp_section = f"📱 *Verified WhatsApp Link:* [Launch Click-to-Chat Workspace]({whatsapp_workspace_link})\n\n"
            
        telegram_message = (
            f"🎯 *Targeted Premium Client Profile Generated*\n\n"
            f"👤 *Instructor Name:* {parsed_lead['topic']}\n"
            f"📊 *Estimated Metrics:* {parsed_lead['rating']} ⭐ ({parsed_lead['reviews']} reviews)\n"
            f"🏷️ *Classification:* `[{parsed_lead['profile_type']}]`\n"
            f"⚠️ *Strategic Bottleneck:* {parsed_lead['bottleneck_analysis']}\n\n"
            f"📧 *Direct Contact Email:* `{contact_display}`\n"
            f"🌐 *Personal Website:* {site_display}\n"
            f"🗂️ *Identified Platforms:* {channel_display}\n"
            f"🔗 *Target Source Link:* [Open Udemy Profile]({target_profile_url})\n\n"
            f"{whatsapp_section}"
            f"📝 *Executive Proposal Blueprint (Davies Emmanuel):*\n```\n{email_pitch}\n```"
        )
        
        # --- STEP 5: DEPLOY INTELLIGENCE ALERT TO TELEGRAM BOT ---
        telegram_status = send_telegram_ping(telegram_message)
        telegram_display_status = "✅ DISPATCHED SUCCESS" if telegram_status else "❌ DELIVERY FAILED (Check Bot Token Config)"

        # --- STEP 6: RENDER PREMIUM SYSTEM MANAGEMENT DASHBOARD ---
        success_html = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="utf-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Target System Success</title>
            <style>
                body {{ font-family: -apple-system, BlinkMacSystemFont, sans-serif; background: #0c0d12; color: #e4e6eb; padding: 15px; line-height: 1.5; }}
                .card {{ max-width: 600px; margin: 20px auto; background: #161720; padding: 25px; border-radius: 12px; border: 1px solid #242736; box-shadow: 0 10px 30px rgba(0,0,0,0.4); }}
                h2 {{ color: #4ade80; margin-top: 0; display: flex; justify-content: space-between; align-items: center; font-size: 19px; }}
                .status-badge {{ background: rgba(74, 222, 128, 0.1); color: #4ade80; padding: 4px 12px; border-radius: 20px; font-size: 11px; border: 1px solid rgba(74,222,128,0.2); }}
                .meta-row {{ background: #1e202e; padding: 14px; border-radius: 8px; margin-bottom: 12px; font-size: 14px; border-left: 4px solid #3b82f6; }}
                .label {{ color: #9ca3af; font-weight: 600; display: inline-block; width: 130px; }}
                .value {{ color: #ffffff; font-family: monospace; word-break: break-all; }}
                .btn {{ display: block; text-align: center; background: #2563eb; color: white; text-decoration: none; padding: 14px; border-radius: 8px; font-weight: 600; margin-top: 25px; }}
            </style>
        </head>
        <body>
            <div class="card">
                <h2><span>🎯 Intel Harvest Complete</span> <span class="status-badge">LIVE RUN</span></h2>
                <hr style="border:0; border-top:1px solid #242736; margin-bottom:20px;">
                
                <div class="meta-row"><span class="label">Target Lead:</span> <span class="value">{parsed_lead['topic']}</span></div>
                <div class="meta-row"><span class="label">Reputation:</span> <span class="value">{parsed_lead['rating']} ⭐ ({parsed_lead['reviews']} reviews)</span></div>
                <div class="meta-row"><span class="label">Classification:</span> <span class="value">[{parsed_lead['profile_type']}]</span></div>
                <div class="meta-row"><span class="label">Contact Email:</span> <span class="value">{contact_display}</span></div>
                <div class="meta-row"><span class="label">Telegram Courier:</span> <span class="value" style="color:#4ade80;">{telegram_display_status}</span></div>
                
                <p style="font-size:12px; color:#6b7280; text-align:center; margin-top:20px; padding:0 10px;">
                    Intelligence has been organized, processed by Gemini, and pushed directly to your active chat channel.
                </p>
                <a href="{target_profile_url}" target="_blank" class="btn">View Source Udemy Profile</a>
            </div>
        </body>
        </html>
        """
        
        self.wfile.write(success_html.encode('utf
-8'))
