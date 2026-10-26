from fastapi import FastAPI, Query
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

app = FastAPI()

# On Vercel, the file api/analyze.py is automatically served at /api/analyze
# We use "/" here because the file name itself defines the route.
@app.get("/")
def analyze(ticker: str = Query(..., description="Stock ticker to analyze")):
    ticker = ticker.upper()
    
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
    
    swarm = SwarmManager(agents)
    result = swarm.execute_pipeline(ticker)
    
    return {
        "ticker": result.get("ticker"),
        "price": result.get("price"),
        "decision": result.get("final_decision"),
        "confidence": result.get("prediction_confidence"),
        "risk_status": result.get("risk_status", "Passed"),
        "sentiment": result.get("sentiment"),
        "macro": result.get("macro_outlook"),
        "technical": result.get("technical_signal"),
        "prediction": result.get("predicted_move")
    }
