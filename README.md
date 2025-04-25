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

If Open AI Key not set, then kindly set you own Open AI API Key and Serp API as well.
Although I have already included them in the code, if they dont work then kindly set them in your virtual environment.

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
