import abc
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("TradingSwarm")

class BaseAgent(abc.ABC):
    """Base class for all AI agents in the trading swarm."""
    
    def __init__(self, name):
        self.name = name
        logger.info(f"Agent {self.name} initialized.")

    @abc.abstractmethod
    def process(self, data):
        """
        Process the input data and return a result.
        :param data: Input data from the previous agent or manager.
        :return: Processed information/signal.
        """
        pass

    def __repr__(self):
        return f"<{self.name}Agent>"
