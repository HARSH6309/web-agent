# web-agent
Web Research AI Agent
Requirements - 
fastapi
uvicorn
openai
serpapi
requests
beautifulsoup4
python-dotenv


An AI-powered FastAPI application that:
- Performs web searches
- Extracts relevant data
- Analyzes content using GPT
- Summarizes into a research report

To run -
open terminal & type - 
uvicorn main:app --reload
Wait unitl it says process complete.

Go to any browser in your system and search for this query
http://127.0.0.1:8000/docs.

Then go to reserch section and type query in following format.
{
  "query": "latest AI trends",
  "mode": "combined"
}

Wait for the results to display.
You can also download the results.
Thank You.
