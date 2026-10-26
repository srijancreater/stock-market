from agents.core.base_agent import BaseAgent, logger

class FundamentalAnalyst(BaseAgent):
    """Agent 6: Fundamental Analysis - P/E, Balance Sheets."""
    
    def process(self, data: dict):
        logger.info(f"Analyzing fundamentals for {data['ticker']}...")
        # Simulation of fundamental check
        pe_ratio = 15.5
        data["fundamental_value"] = "Undervalued" if pe_ratio < 20 else "Overvalued"
        logger.info(f"Fundamental Value: {data['fundamental_value']}")
        return data
