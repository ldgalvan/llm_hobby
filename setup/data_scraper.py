# wikipedia_scraper.py

import requests
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor, as_completed

BASE_URL = "https://en.wikipedia.org/wiki/"

def fetch_wikipedia_text(title):
    url = BASE_URL + title
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')

        content_div = soup.find("div", {"class": "mw-parser-output"})
        if not content_div:
            return title, "No content found"

        paragraphs = content_div.find_all("p", recursive=False)
        text = "\n".join(
            p.get_text(strip=True)
            for p in paragraphs
            if p.get_text(strip=True)
        )
        return title, text if text else "No clean content found"
    except Exception as e:
        return title, f"Error: {str(e)}"

def scrape_wikipedia_articles(titles, max_workers=10):
    results = []
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = [executor.submit(fetch_wikipedia_text, title) for title in titles]
        for future in as_completed(futures):
            title, text = future.result()
            results.append({"title": title, "text": text})
    return results

