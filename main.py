import time
import json
from curl_cffi import requests

# ==========================================
# ⚙️ কনফিগারেশন
# ==========================================

MNIT_API_KEY = "M_A4UFFVM8R"
MNIT_API_URL = "https://x.mnitnetwork.com/mapi/v1/mdashboard/console/info"

# আপনার কুকি এবং ইউজার এজেন্ট (কুকি রিফ্রেশ করার পর দিলে ভালো হয়)
MY_COOKIE = "mauthtoken=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1aWQiOiJNX0k0VkE3RkU2UiIsInJvbGUiOiJ1c2VyIiwiYWNjZXNzX3BhdGgiOlsiL2Rhc2hib2FyZCJdLCJleHBpcnkiOjE3NzY3OTM3MzgsImNyZWF0ZWQiOjE3NzY3MDczMzgsIjJvbzkiOiJNc0giLCJleHAiOjE3NzY3OTM3MzgsImlhdCI6MTc3NjcwNzMzOCwic3ViIjoiTV9JNFZBN0ZFNlIifQ.dRSK-FIaePK7YlQiJBx_CB-vFKhNvsPBulzfxF5iLww; cf_clearance=rk9VuWZnHn9r_gzr_F3aofU6j0Zge56QpP.HN9WEsC4-1776708657-1.2.1.1-sDHvjSoTc8TKziNPo4Jg4HZkDlFz9L.gEOCUHiQjpvEN02erQj43_4KCeZwg5tuYumnFjLHiQE748OU20rr0uukGS1yGWI33raFpeiy70LoeMyNz9AYYdj41GgUSr2vor36a2yVaJKbEGeImAR5jenEYzQ.dYdINYjbb3054GBUN3D06U959t2vE1P6d52IK9.oOxYQl.eJUjhbvcZFCvx_ot9Rnr2dgeJdxaTPaDPCEsH_.B9HV3DPd0JlPDnK213tJPjDHubRcFMiUYU_2K7_Bq6uoTFni9GsxVlIrEdi28jhmson_Vp_rQ0pTI3.x7s1DOyJjBQcV8EMDKRd9vw; TawkConnectionTime=0; twk_uuid_681787a55d55ef191a9da720=%7B%22uuid%22%3A%221.Ws5ekyCufN7FIkjVzGqnYI9ew966WPdxfiZovrEdz6t1olxJ4kMjqSq4Vnyf9PEkMYxcx9FUxkLZiqDgMWuAonkjeVCK52pX8mOWCPbKOORTIloUFixXGJvC3%22%2C%22version%22%3A3%2C%22domain%22%3A%22mnitnetwork.com%22%2C%22ts%22%3A1776709371835%7D"

MY_USER_AGENT = "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"

TELEGRAM_BOT_TOKEN = "8671692396:AAGzZfZPNfC5ZRmSnRxaFQcbAjT3s3X_nug"
TELEGRAM_CHAT_ID = "-1003768340075"

# ==========================================

seen_ids = set()

def fetch_data():
    headers = {
        "mapikey": MNIT_API_KEY,
        "Cookie": MY_COOKIE,
        "User-Agent": MY_USER_AGENT,
        "Referer": "https://x.mnitnetwork.com/mdashboard/console",
        "Accept": "application/json, text/plain, */*",
        "X-Requested-With": "XMLHttpRequest",
        "Origin": "https://x.mnitnetwork.com"
    }
    
    try:
        # impersonate="chrome110" এর বদলে "safari_ios_16_5" বা "chrome110" ট্রাই করছি
        # এটি TLS Fingerprint একদম ব্রাউজারের মতো করবে
        session = requests.Session()
        response = session.get(
            MNIT_API_URL, 
            headers=headers, 
            impersonate="chrome110", # এখানে safari_ios_16_5 ও দিয়ে দেখতে পারেন
            timeout=30
        )
        
        if response.status_code == 200:
            return response.json()
        elif response.status_code == 403:
            print("❌ 403 Forbidden! IP ব্লক হতে পারে। Airplane mode অন-অফ করুন।")
        else:
            print(f"❌ Status Code: {response.status_code}")
    except Exception as e:
        print(f"❌ Error: {e}")
    return None

def main():
    print("🚀 Advanced Cloudflare Bypass (TLS v3) চালু হচ্ছে...")
    
    while True:
        json_data = fetch_data()
        
        if json_data:
            items = []
            if isinstance(json_data, list): items = json_data
            elif isinstance(json_data, dict):
                for k in ['logs', 'data', 'otps']:
                    if k in json_data and isinstance(json_data[k], list):
                        items = json_data[k]
                        break
            
            for item in reversed(items):
                nid = item.get("nid") or item.get("id") or item.get("number")
                if nid and nid not in seen_ids:
                    num = str(item.get("number", "Unknown"))
                    rng = num[:-3] + "XXX" if len(num) > 3 else num
                    
                    # টেলিগ্রাম মেসেজ
                    msg = f"🚀 <b>LIVE RANGE:</b> <code>{rng}</code>"
                    tg_url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
                    payload = {
                        "chat_id": TELEGRAM_CHAT_ID,
                        "text": msg,
                        "parse_mode": "HTML",
                        "reply_markup": {"inline_keyboard": [[{"text": f"📋 Copy {rng}", "copy_text": {"text": rng}}]]}
                    }
                    # টেলিগ্রামের জন্য সাধারণ রিকোয়েস্ট
                    import requests as tg_req
                    tg_req.post(tg_url, json=payload)
                    print(f"✅ ফরোয়ার্ড হয়েছে: {rng}")
                    seen_ids.add(nid)
        
        time.sleep(10) # গ্যাপ একটু বাড়ালে ব্লক খাওয়ার সম্ভাবনা কমে

if __name__ == "__main__":
    main()
