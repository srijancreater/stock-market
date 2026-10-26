from agents.core.base_agent import BaseAgent, logger

class AlgoTrader(BaseAgent):
    """Agent 9: Algo Trading - Execution of trades."""
    
    def process(self, data: dict):
        logger.info("Calculating trade execution strategy...")
        # Final decision based on signals
        signals = [data.get("sentiment"), data.get("technical_signal"), data.get("pattern_signal")]
        bullish_count = sum(1 for s in signals if s in ["Bullish", "Buy"])
        
        decision = "BUY" if bullish_count >= 2 else "HOLD" if bullish_count == 1 else "SELL"
        data["final_decision"] = decision
        
        logger.info(f"Algo Decision: {decision}")
        return data
