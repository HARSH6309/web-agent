class QueryParser:
    def parse(self, query):
        return {
            "intent": "research",
            "keywords": query.lower().split(),  # Simple split; expand later
            "type": "general"
        }
