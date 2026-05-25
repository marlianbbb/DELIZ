import urllib.request
import json

# Your verified active Telegram configuration channels
TELEGRAM_BOT_TOKEN = "8056637318:AAG7S78Y4U6SloA_8g7m8Wj2q8V8bV78V8"
TELEGRAM_CHAT_ID = "7449591461"

def send_telegram_ping(message_text):
    """
    Dispatches a structured high-value markdown payload straight to your Telegram bot channel.
    Features robust character length splitting to ensure massive proposals never get dropped by the Telegram API.
    """
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    
    # Telegram API has a hard ceiling limitation of 4,096 characters per single message dispatch.
    # Since Gemini produces long, thorough executive proposals, we chunk the text safely if it runs over.
    max_length = 4000
    message_chunks = [message_text[i:i+max_length] for i in range(0, len(message_text), max_length)]
    
    all_chunks_successful = True
    
    for chunk in message_chunks:
        payload = json.dumps({
            "chat_id": TELEGRAM_CHAT_ID,
            "text": chunk,
            "parse_mode": "Markdown",
            "disable_web_page_preview": False
        })
        
        headers = {
            'Content-Type': 'application/json'
        }
        
        try:
            req = urllib.request.Request(url, data=payload.encode('utf-8'), headers=headers, method='POST')
            # 10-second timeout shield to maintain Vercel edge delivery speeds
            with urllib.request.urlopen(req, timeout=10) as response:
                result = json.loads(response.read().decode('utf-8'))
                if not result.get("ok"):
                    print(f"[Notifier Error] Telegram transmission rejected: {result.get('description')}")
                    all_chunks_successful = False
                    
        except Exception as e:
            print(f"[Notifier Critical Error] Courier route disconnected: {e}")
            all_chunks_successful = False
            
    return all_chunks_successfu
  l
