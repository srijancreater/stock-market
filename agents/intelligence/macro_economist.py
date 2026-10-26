from agents.core.base_agent import BaseAgent, logger

class MacroEconomist(BaseAgent):
    """Agent 3: Macro Economics - Monitors global trends."""
    
    def process(self, data: dict):
        logger.info("Evaluating macroeconomic conditions...")
        # Simulation of Macro analysis (Inflation, Interest rates)
        macro_outlook = "Positive" 
        data["macro_outlook"] = macro_outlook
        logger.info(f"Macro Outlook: {macro_outlook}")
        return data
