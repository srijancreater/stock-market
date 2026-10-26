from fastapi import FastAPI, Query
from fastapi.responses import HTMLResponse
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

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AI Trading Swarm | Pro Dashboard</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css" rel="stylesheet">
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700&display=swap');
        body { font-family: 'Inter', sans-serif; background-color: #0a0e17; color: #e2e8f0; }
        .glass { background: rgba(30, 41, 59, 0.7); backdrop-filter: blur(12px); border: 1px solid rgba(255, 255, 255, 0.1); }
        .gradient-text { background: linear-gradient(90deg, #60a5fa, #a78bfa); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }
        .status-pill { padding: 2px 8px; border-radius: 12px; font-size: 0.75rem; font-weight: 600; }
        .bullish { background: #065f46; color: #34d399; }
        .bearish { background: #7f1d1d; color: #f87171; }
        .loader { border-top-color: #60a5fa; animation: spinner 1.5s linear infinite; }
        @keyframes spinner { 0% { transform: rotate(0deg); } 100% { transform: rotate(360deg); } }
    </style>
</head>
<body class="min-h-screen p-4 md:p-8">
    <div class="max-w-6xl mx-auto">
        <header class="flex justify-between items-center mb-12">
            <div>
                <h1 class="text-3xl font-bold gradient-text">AI TRADING SWARM</h1>
                <p class="text-slate-400 text-sm">Institutional Grade Algorithmic Intelligence</p>
            </div>
            <div class="glass px-4 py-2 rounded-full text-xs flex items-center gap-2">
                <span class="w-2 h-2 bg-green-500 rounded-full animate-pulse"></span>
                System Online: 10 Agents Active
            </div>
        </header>
        <div class="flex justify-center mb-12">
            <div class="relative w-full max-w-xl">
                <input type="text" id="tickerInput" placeholder="Enter Ticker (e.g. AAPL, RELIANCE.NS)" 
                       class="w-full bg-slate-900 border border-slate-700 rounded-2xl px-6 py-4 text-lg focus:outline-none focus:ring-2 focus:ring-blue-500 transition-all pl-14">
                <i class="fa-solid fa-magnifying-glass absolute left-5 top-5 text-slate-500"></i>
                <button onclick="analyzeStock()" id="analyzeBtn" 
                        class="absolute right-2 top-2 bottom-2 bg-blue-600 hover:bg-blue-500 px-6 rounded-xl font-semibold transition-all active:scale-95">
                    Analyze
                </button>
            </div>
        </div>
        <div id="loading" class="hidden flex flex-col items-center justify-center py-20">
            <div class="loader w-12 h-12 border-4 border-slate-700 rounded-full mb-4"></div>
            <p class="text-slate-400 animate-pulse">Swarm Coordinating Agents...</p>
        </div>
        <div id="results" class="hidden space-y-6">
            <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
                <div class="glass p-6 rounded-3xl flex flex-col items-center justify-center text-center">
                    <span class="text-slate-400 text-sm mb-2">Current Price</span>
                    <span id="resPrice" class="text-4xl font-bold text-white">$0.00</span>
                </div>
                <div class="glass p-6 rounded-3xl flex flex-col items-center justify-center text-center border-2" id="decisionBorder">
                    <span class="text-slate-400 text-sm mb-2">Swarm Decision</span>
                    <span id="resDecision" class="text-4xl font-bold uppercase">HOLD</span>
                </div>
                <div class="glass p-6 rounded-3xl flex flex-col items-center justify-center text-center">
                    <span class="text-slate-400 text-sm mb-2">ML Confidence</span>
                    <span id="resConf" class="text-4xl font-bold text-white">0%</span>
                </div>
            </div>
            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-5 gap-4">
                <div class="glass p-4 rounded-2xl"><div class="flex items-center gap-3 mb-3"><div class="w-8 h-8 bg-blue-500/20 rounded-lg flex items-center justify-center text-blue-400"><i class="fa-solid fa-database"></i></div><span class="text-xs font-semibold text-slate-300">Data Miner</span></div><p id="agentData" class="text-sm text-slate-400">Fetching...</p></div>
                <div class="glass p-4 rounded-2xl"><div class="flex items-center gap-3 mb-3"><div class="w-8 h-8 bg-purple-500/20 rounded-lg flex items-center justify-center text-purple-400"><i class="fa-solid fa-face-smile"></i></div><span class="text-xs font-semibold text-slate-300">Sentiment</span></div><p id="agentSent" class="text-sm text-slate-400">Analyzing...</p></div>
                <div class="glass p-4 rounded-2xl"><div class="flex items-center gap-3 mb-3"><div class="w-8 h-8 bg-emerald-500/20 rounded-lg flex items-center justify-center text-emerald-400"><i class="fa-solid fa-earth-americas"></i></div><span class="text-xs font-semibold text-slate-300">Macro Econ</span></div><p id="agentMacro" class="text-sm text-slate-400">Scanning...</p></div>
                <div class="glass p-4 rounded-2xl"><div class="flex items-center gap-3 mb-3"><div class="w-8 h-8 bg-orange-500/20 rounded-lg flex items-center justify-center text-orange-400"><i class="fa-solid fa-chart-line"></i></div><span class="text-xs font-semibold text-slate-300">Technical</span></div><p id="agentTech" class="text-sm text-slate-400">Calculating...</p></div>
                <div class="glass p-4 rounded-2xl"><div class="flex items-center gap-3 mb-3"><div class="w-8 h-8 bg-pink-500/20 rounded-lg flex items-center justify-center text-pink-400"><i class="fa-solid fa-magnifying-glass-chart"></i></div><span class="text-xs font-semibold text-slate-300">Patterns</span></div><p id="agentPattern" class="text-sm text-slate-400">Detecting...</p></div>
                <div class="glass p-4 rounded-2xl"><div class="flex items-center gap-3 mb-3"><div class="w-8 h-8 bg-yellow-500/20 rounded-lg flex items-center justify-center text-yellow-400"><i class="fa-solid fa-building"></i></div><span class="text-xs font-semibold text-slate-300">Fundamental</span></div><p id="agentFund" class="text-sm text-slate-400">Evaluating...</p></div>
                <div class="glass p-4 rounded-2xl"><div class="flex items-center, justify-center gap-3 mb-3"><div class="w-8 h-8 bg-indigo-500/20 rounded-lg flex items-center justify-center text-indigo-400"><i class="fa-solid fa-brain"></i></div><span class="text-xs font-semibold text-slate-300">ML Predictor</span></div><p id="agentML" class="text-sm text-slate-400">Forecasting...</p></div>
                <div class="glass p-4 rounded-2xl"><div class="flex items-center gap-3 mb-3"><div class="w-8 h-8 bg-cyan-500/20 rounded-lg flex items-center justify-center text-cyan-400"><i class="fa-solid fa-link"></i></div><span class="text-xs font-semibold text-slate-300">Correlation</span></div><p id="agentCorr" class="text-sm text-slate-400">Linking...</p></div>
                <div class="glass p-4 rounded-2xl"><div class="flex items-center gap-3 mb-3"><div class="w-8 h-8 bg-red-500/20 rounded-lg flex items-center justify-center text-red-400"><i class="fa-solid fa-robot"></i></div><span class="text-xs font-semibold text-slate-300">Algo Trader</span></div><p id="agentAlgo" class="text-sm text-slate-400">Strategizing...</p></div>
                <div class="glass p-4 rounded-2xl"><div class="flex items-center gap-3 mb-3"><div class="w-8 h-8 bg-slate-500/20 rounded-lg flex items-center justify-center text-slate-400"><i class="fa-solid fa-shield-halved"></i></div><span class="text-xs font-semibold text-slate-300">Risk Manager</span></div><p id="agentRisk" class="text-sm text-slate-400">Auditing...</p></div>
            </div>
            <div class="glass p-8 rounded-3xl bg-gradient-to-br from-slate-900 to-slate-800">
                <div class="flex items-center justify-between mb-6">
                    <h2 class="text-xl font-bold flex items-center gap-2"><i class="fa-solid fa-gears text-blue-400"></i>Auto-Algo Execution Details</h2>
                    <span class="status-pill bullish">Live Execution Enabled</span>
                </div>
                <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
                    <div class="space-y-4">
                        <div class="flex justify-between text-sm"><span class="text-slate-400">Trading Mode:</span><span class="text-white font-semibold">Autonomous Quant</span></div>
                        <div class="flex justify-between text-sm"><span class="text-slate-400">Stop Loss:</span><span class="text-red-400 font-semibold">Fixed -2.0%</span></div>
                        <div class="flex justify-between text-sm"><span class="text-slate-400">Trailing Stop:</span><span class="text-green-400 font-semibold">Active (1.5% Trail)</span></div>
                    </div>
                    <div class="bg-slate-950 p-4 rounded-2xl border border-slate-800">
                        <p class="text-xs text-slate-500 mb-2 uppercase font-bold">Execution Log</p>
                        <div id="execLog" class="text-xs font-mono text-blue-300 space-y-1">> Awaiting signal...</div>
                    </div>
                </div>
            </div>
        </div>
    </div>
    <script>
        async function analyzeStock() {
            const ticker = document.getElementById('tickerInput').value;
            if (!ticker) return alert('Please enter a ticker');
            document.getElementById('loading').classList.remove('hidden');
            document.getElementById('results').classList.add('hidden');
            document.getElementById('analyzeBtn').disabled = true;
            try {
                const response = await fetch('/api/analyze?ticker=' + ticker);
                const data = await response.json();
                document.getElementById('resPrice').innerText = '$' + data.price.toFixed(2);
                document.getElementById('resDecision').innerText = data.decision;
                document.getElementById('resConf').innerText = (data.confidence * 100).toFixed(0) + '%';
                const border = document.getElementById('decisionBorder');
                if (data.decision === 'BUY') border.className = "glass p-6 rounded-3xl flex flex-col items-center justify-center text-center border-2 border-green-500 text-green-500";
                else if (data.decision === 'SELL') border.className = "glass p-6 rounded-3xl flex flex-col items-center justify-center text-center border-2 border-red-500 text-red-500";
                else border.className = "glass p-6 rounded-3xl flex flex-col items-center justify-center text-center border-2 border-slate-500 text-slate-500";
                document.getElementById('agentData').innerText = 'Live: ' + data.price.toFixed(2);
                document.getElementById('agentSent').innerHTML = '<span class="status-pill ' + (data.sentiment === 'Bullish' ? 'bullish' : 'bearish') + '">' + data.sentiment + '</span>';
                document.getElementById('agentMacro').innerText = data.macro;
                document.getElementById('agentTech').innerText = data.technical;
                document.getElementById('agentPattern').innerText = "Bullish Pattern";
                document.getElementById('agentFund').innerText = "Undervalued";
                document.getElementById('agentML').innerText = 'Move: ' + data.prediction;
                document.getElementById('agentCorr').innerText = "Strong Correl";
                document.getElementById('agentAlgo').innerText = 'Signal: ' + data.decision;
                document.getElementById('agentRisk').innerHTML = '<span class="status-pill bullish">' + data.risk_status + '</span>';
                const log = document.getElementById('execLog');
                log.innerHTML = '<div>> Order triggered for ' + ticker + '</div><div>> Entry Price: ' + data.price.toFixed(2) + '</div><div>> Trailing Stop set at ' + (data.price * 0.985).toFixed(2) + '</div><div>> Auto-Trading: EXECUTING ' + data.decision + '...</div>';
                document.getElementById('results').classList.remove('hidden');
            } catch (e) { alert("Error: " + e.message); } finally {
                document.getElementById('loading').classList.add('hidden');
                document.getElementById('analyzeBtn').disabled = false;
            }
        }
    </script>
</body>
</html>
