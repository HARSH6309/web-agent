class Synthesizer:
    def summarize(self, docs, query):
        combined = " ".join(doc["text"] for doc in docs)
        return combined[:1000] + "..." if len(combined) > 1000 else combined
