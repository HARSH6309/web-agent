import requests
from bs4 import BeautifulSoup

class SearchTool:
    def search(self, keywords, num_results=5):
        query = "+".join(keywords)
        url = f"https://duckduckgo.com/search?q={query}&num={num_results}"
        headers = {"User-Agent": "Mozilla/5.0"}
        res = requests.get(url, headers=headers)

        soup = BeautifulSoup(res.text, "html.parser")
        results = []
        for g in soup.select(".tF2Cxc"):
            title = g.select_one("h3")
            link = g.select_one("a")["href"]
            if title and link:
                results.append({"title": title.text, "link": link})
        return results
