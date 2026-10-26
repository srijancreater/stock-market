from typing import List, Any
from agents.core.base_agent import BaseAgent, logger

class SwarmManager:
    """Coordinates the flow of information between the 10 AI agents."""
    
    def __init__(self, agents: List[BaseAgent]):
        self.agents = agents

    def execute_pipeline(self, initial_data: Any):
        """
        Passes data through the agent pipeline sequentially.
        """
        current_data = initial_data
        logger.info("Starting Trading Swarm Pipeline...")
        
        for agent in self.agents:
            logger.info(f"Passing data to {agent.name}...")
            current_data = agent.process(current_data)
            if current_data is None:
                logger.error(f"Pipeline broken at {agent.name}: returned None")
                break
        
        logger.info("Pipeline execution complete.")
        return current_data

    def __repr__(self):
        return f"<SwarmManager with {len(self.agents)} agents>"
