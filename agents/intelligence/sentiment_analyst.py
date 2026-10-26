from agents.core.base_agent import BaseAgent, logger

class SentimentAnalyst(BaseAgent):
    """Agent 2: Sentiment Analysis - Scans social media/news."""
    
    def process(self, data: dict):
        ticker = data["ticker"]
        logger.info(f"Analyzing sentiment for {ticker}...")
        # Simulation of NLP analysis
        sentiment_score = 0.75  # 0.0 to 1.0 (Bullish)
        data["sentiment"] = "Bullish" if sentiment_score > 0.5 else "Bearish"
        data["sentiment_score"] = sentiment_score
        logger.info(f"Sentiment for {ticker}: {data['sentiment']}")
        return data
