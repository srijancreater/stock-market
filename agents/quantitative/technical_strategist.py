from agents.core.base_agent import BaseAgent, logger

class TechnicalStrategist(BaseAgent):
    """Agent 4: Technical Analysis - RSI, MACD, etc."""
    
    def process(self, data: dict):
        logger.info(f"Running technical analysis on {data['ticker']}...")
        # Simulation of technical indicators
        rsi = 45 
        data["rsi"] = rsi
        data["technical_signal"] = "Buy" if rsi < 30 else "Sell" if rsi > 70 else "Neutral"
        logger.info(f"Technical Signal: {data['technical_signal']} (RSI: {rsi})")
        return data
