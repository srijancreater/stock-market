import yfinance as yf
from agents.core.base_agent import BaseAgent, logger

class DataMiner(BaseAgent):
    """Agent 1: Data Acquisition - Fetches real-time stock data using yfinance."""
    
    def process(self, ticker: str):
        logger.info(f"Mining real-time data for {ticker} using yfinance...")
        try:
            stock = yf.Ticker(ticker)
            hist = stock.history(period="1mo")
            
            if hist.empty:
                raise ValueError(f"No data found for ticker {ticker}")

            current_price = hist['Close'].iloc[-1]
            volume = hist['Volume'].iloc[-1]
            
            data = {
                "ticker": ticker,
                "price": float(current_price),
                "volume": int(volume),
                "history": hist['Close'].tolist()
            }
            logger.info(f"Live Data collected for {ticker}: Price {data['price']:.2f}")
            return data
        except Exception as e:
            logger.error(f"Error mining data for {ticker}: {e}")
            # Fallback to simulation if API fails so the swarm doesn't crash
            return {"ticker": ticker, "price": 150.0, "volume": 1000000, "history": [145, 148, 150], "simulated": True}
