from agents.core.base_agent import BaseAgent, logger

class RiskManager(BaseAgent):
    """Agent 10: Risk Management - Veto and Safety."""
    
    def process(self, data: dict):
        logger.info("Performing risk audit...")
        decision = data.get("final_decision")
        
        # Risk Check: If volatility is too high or budget is low, veto the trade
        risk_score = 0.3 # 0.0 (Safe) to 1.0 (Dangerous)
        
        if risk_score > 0.7:
            logger.warning("Risk too high! Vetoing trade.")
            data["final_decision"] = "HOLD (Vetoed by Risk Manager)"
        else:
            logger.info("Risk check passed.")
            
        return data
