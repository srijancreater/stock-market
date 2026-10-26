import sys
from agents.core.swarm_manager import SwarmManager
from agents.intelligence.data_miner import DataMiner
from agents.intelligence.sentiment_analyst import SentimentAnalyst
from agents.intelligence.macro_economist import MacroEconomist
from agents.quantitative.technical_strategist import TechnicalStrategist
from agents.quantitative.pattern_recognition import PatternRecognitionAgent
from agents.quantitative.fundamental_analyst import FundamentalAnalyst
from agents.prediction.ml_predictor import MLPredictor
from agents.prediction.correlation_specialist import CorrelationSpecialist
from agents.execution.algo_trader import AlgoTrader
from agents.execution.risk_manager import RiskManager

def main():
    # Check if a ticker was provided as a command line argument
    # Example: python3 main.py RELIANCE.NS
    if len(sys.argv) > 1:
        ticker = sys.argv[1].upper()
    else:
        # Default to Reliance if no ticker is provided
        ticker = "RELIANCE.NS"

    # Initialize the 10 AI agents
    agents = [
        DataMiner("Miner"),
        SentimentAnalyst("Sentiment"),
        MacroEconomist("Macro"),
        TechnicalStrategist("Tech"),
        PatternRecognitionAgent("Pattern"),
        FundamentalAnalyst("Fund"),
        MLPredictor("ML"),
        CorrelationSpecialist("Corr"),
        AlgoTrader("Algo"),
        RiskManager("Risk")
    ]
    
    # Initialize the Swarm Manager
    swarm = SwarmManager(agents)
    
    # Run the pipeline
    result = swarm.execute_pipeline(ticker)
    
    print("\n" + "="*30)
    print("📊 FINAL TRADING REPORT")
    print("="*30)
    print(f"Ticker:     {result['ticker']}")
    print(f"Price:      {result['price']:.2f}")
    print(f"Decision:   {result['final_decision']}")
    print(f"Confidence:  {result['prediction_confidence']}")
    print(f"Risk Status: {result.get('risk_status', 'Passed')}")
    print("="*30 + "\n")

if __name__ == "__main__":
    main()
