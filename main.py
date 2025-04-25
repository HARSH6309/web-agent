from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from duckduckgo_search import DDGS
import requests
from bs4 import BeautifulSoup
import openai  # Replace with your preferred LLM API if needed

app = FastAPI()

# Set your OpenAI key
openai.api_key = "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"

class QueryRequest(BaseModel):
    query: str

class ResearchReport(BaseModel):
    summary: str
    sources: List[str]

def search_web(query: str, max_results: int = 5) -> List[str]:
    with DDGS() as ddgs:
        results = ddgs.text(query, max_results=max_results)
        return [r["href"] for r in results if "href" in r]

def scrape_text_from_url(url: str) -> str:
    try:
        response = requests.get(url, timeout=10)
        soup = BeautifulSoup(response.text, 'html.parser')
        paragraphs = soup.find_all('p')
        return ' '.join([p.get_text() for p in paragraphs])
    except Exception:
        return ""

def summarize_with_gpt(query: str, contents: List[str]) -> str:
    joined_content = "\n\n".join(contents)
    prompt = (
        f"Based on the following web content, write a clear and accurate research summary for the query: '{query}'.\n\n"
        f"{joined_content}\n\nSummary:"
    )
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # Or gpt-4 if available
        messages=[{"role": "user", "content": prompt}],
        temperature=0.5,
        max_tokens=500
    )
    return response['choices'][0]['message']['content'].strip()

@app.post("/research", response_model=ResearchReport)
async def generate_research_report(request: QueryRequest):
    query = request.query

    try:
        print(f"🔍 Searching for: {query}")
        urls = search_web(query)
        print(f"🌐 Found URLs: {urls}")
        if not urls:
            raise HTTPException(status_code=500, detail="No search results found.")

        scraped_contents = []
        for url in urls:
            text = scrape_text_from_url(url)
            if text.strip():
                scraped_contents.append(text)
        print(f"📝 Scraped {len(scraped_contents)} pages")

        if not scraped_contents:
            raise HTTPException(status_code=500, detail="Scraped content is empty.")

        summary = summarize_with_gpt(query, scraped_contents)
        print(f"✅ Summary generated.")

        return ResearchReport(summary=summary, sources=urls)

    except openai.error.OpenAIError as e:
        print(f"❌ OpenAI API error: {e}")
        raise HTTPException(status_code=500, detail=f"OpenAI API error: {str(e)}")

    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        raise HTTPException(status_code=500, detail=f"Internal error: {str(e)}")
