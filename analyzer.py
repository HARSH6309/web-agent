class Analyzer:
    def score_relevance(self, text, query):
        query_words = set(query.lower().split())
        text_words = set(text.lower().split())
        overlap = query_words.intersection(text_words)
        return len(overlap) / len(query_words)
