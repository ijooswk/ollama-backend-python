from aiohttp import ClientSession
from bs4 import BeautifulSoup
import os
from datetime import datetime
from app.services.ollamaLocal import OllamaAPI

async def url_summary(url):
    print(f"url: {url}")

    api = OllamaAPI("http://192.168.68.107:11434", "llama3.2")
    prompt = f"Summarise the news from the link in Korean langauge within 500 words."
    summary = api.call_api(f"{prompt}. URL: {url}")

    today = datetime.now().strftime('%Y-%m-%d')
    folder_path = os.path.join('/home/sehun/Documents/synology-folder', today)
    os.makedirs(folder_path, exist_ok=True)
    file_name = f"{datetime.now().strftime('%H%M%S')}.txt"
    file_path = os.path.join(folder_path, file_name)
    print(f"Saving description to {file_path}")
    with open(file_path, 'w') as file:
        file.write(summary)
        print(f"Description saved to {file_path}")
    
    return summary if summary else 'No description available'