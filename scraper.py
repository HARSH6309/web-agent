import requests
from bs4 import BeautifulSoup

class Scraper:
    def fetch(self, url):
        res = requests.get(url, timeout=5)
        soup = BeautifulSoup(res.text, "html.parser")
        paragraphs = soup.find_all('p')
        text = " ".join(p.get_text() for p in paragraphs)
        return {"text": text}
