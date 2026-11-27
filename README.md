<div align="center">

```
██╗  ██╗███████╗██████╗  ██████╗ ███████╗██╗  ██╗
██║  ██║██╔════╝██╔══██╗██╔════╝ ██╔════╝╚██╗██╔╝
███████║█████╗  ██║  ██║██║  ███╗█████╗   ╚███╔╝ 
██╔══██║██╔══╝  ██║  ██║██║   ██║██╔══╝   ██╔██╗ 
██║  ██║███████╗██████╔╝╚██████╔╝███████╗██╔╝ ██╗
╚═╝  ╚═╝╚══════╝╚═════╝  ╚═════╝ ╚══════╝╚═╝  ╚═╝
```

**A full-stack financial literacy platform built to make investing education accessible to everyone.**

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat-square&logo=python&logoColor=white)](https://python.org)
[![Flask](https://img.shields.io/badge/Flask-2.x-000000?style=flat-square&logo=flask&logoColor=white)](https://flask.palletsprojects.com)
[![yfinance](https://img.shields.io/badge/yfinance-real--time-purple?style=flat-square)](https://github.com/ranaroussi/yfinance)
[![JavaScript](https://img.shields.io/badge/JavaScript-ES6+-F7DF1E?style=flat-square&logo=javascript&logoColor=black)](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
[![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)](LICENSE)
[![Congressional App Challenge](https://img.shields.io/badge/Congressional%20App%20Challenge-D--26%20Winner-gold?style=flat-square)](https://www.congressionalappchallenge.us/)

[Live Demo](https://github.com/TanishC4444/PCIS_FantasySMG) · [Report a Bug](https://github.com/TanishC4444/PCIS_FantasySMG/issues) · [Request a Feature](https://github.com/TanishC4444/PCIS_FantasySMG/issues)

</div>

---

## What is Hedgex?

Hedgex is a paper trading and financial education platform that gives anyone — regardless of background or experience — a real environment to learn how markets work. Start with **$100,000 in virtual capital**, trade real stocks during market hours with live Yahoo Finance prices, backtest algorithmic strategies, and study investing fundamentals through structured lessons.

Built by a high school student as a DECA capstone project. Won **Congressional App Challenge District 26**. Used to teach 200+ DECA members and 350+ CISP students how to invest.

> *"Most active strategies fail to beat Buy & Hold long-term — find out if yours does."*

---

## Features

### Paper Trading
Trade any real stock ticker during market hours (8:30 AM – 3:00 PM CST) with live prices from Yahoo Finance. Your portfolio tracks unrealized P&L, cost basis per position, total value, and full transaction history — mirroring a real brokerage account. No real money, no real risk.

### Strategy Backtester
Pick any ticker, time period (1–10 years), and starting capital, then run one of 10 algorithmic strategies against real historical data. Every backtest shows cumulative returns, max drawdown, trade-by-trade P&L, and a full log of every buy and sell signal.

**Available strategies:**
| Strategy | Type | Description |
|---|---|---|
| MA Crossover 20/50 | Trend | Buy when 20-day MA crosses above 50-day MA |
| Golden/Death Cross 50/200 | Trend | Institutional-grade long-term crossover |
| RSI Reversal | Mean Reversion | Buy oversold (RSI < 30), sell overbought (RSI > 70) |
| RSI Trend Filter | Momentum | Combine RSI momentum with trend confirmation |
| MACD Signal | Momentum | Trade the MACD line crossing its signal line |
| Momentum Breakout | Breakout | Enter on price strength, exit on ATR stop |
| Bollinger Reversion | Mean Reversion | Fade moves outside the Bollinger Bands |
| Volatility Breakout | Breakout | Trade expansion out of low-volatility ranges |
| Dollar Cost Averaging | Passive | Fixed investment every 20 trading days |
| Buy & Hold | Benchmark | The strategy most professionals fail to beat |

### Fund Comparison
Build a custom fund of up to 20 tickers with custom weights, then benchmark it against the S&P 500 (SPY) over any date range. Prices are date-aligned — each ticker maps to the exact same trading days as SPY so returns are always accurate. Results include alpha, beta, max drawdown, per-holding contribution, and a live alpha chart.

**Built-in presets:** Mag 7, FAANG, Semiconductor, Dividend Growth, Energy, Finance, Healthcare.

### Stock Analysis
Search any ticker for a full research dashboard — live price chart with multiple timeframes, P/E, EV/EBITDA, revenue, margins, analyst ratings, 52-week range, dividend yield, and more. Powered entirely by Yahoo Finance.

### Structured Learning
Two tracks (Beginner and Advanced) covering how markets work, how to read financial statements, what ratios actually mean, and how to build a strategy. Lessons include definitions, formulas, and real examples.

---

## Tech Stack

| Layer | Technology |
|---|---|
| Backend | Python, Flask |
| Market Data | yfinance (Yahoo Finance API) |
| Frontend | HTML, CSS, JavaScript (vanilla) |
| Charts | Chart.js |
| Data Storage | CSV (pandas) |
| Packaging | PyInstaller |

---

## Getting Started

### Prerequisites

- Python 3.10+
- pip

### Installation

```bash
# Clone the repository
git clone https://github.com/TanishC4444/PCIS_FantasySMG.git
cd PCIS_FantasySMG

# Install dependencies
pip install -r requirements.txt

# Run the app
python app.py
```

The app will open automatically at `http://127.0.0.1:5000`.

### Verify installed module versions

After installing, confirm everything is set up correctly:

```bash
# Check all dependencies at once
pip show flask yfinance pandas requests pytz

# Or check one at a time
pip show flask

# See every installed package and version
pip list
```

---

## Using the Repo

### If you're a collaborator

```bash
# Always pull latest changes before you start working
git pull origin main

# After making changes, push them up
git add .
git commit -m "describe what you changed"
git push origin main
```

### If you want to suggest changes without direct access

1. Click **Fork** on the GitHub repo page to copy it to your account
2. Make your changes in your fork
3. Open a **Pull Request** to submit them for review

### Keeping your data local (recommended)

The CSV files and `balance.txt` store your portfolio state. To avoid pushing your data or overwriting someone else's, create a `.gitignore` file in the root:

```
users.csv
sold.csv
transactions.csv
balance.txt
__pycache__/
*.pyc
```

For a fresh install, `balance.txt` should contain `100000.0` and the CSVs should have headers only.

---

## How It Works

```
Browser (HTML/JS)
      │
      │  fetch("/trade"), fetch("/stock_chart"), fetch("/fund_chart"), ...
      ▼
Flask Backend (app.py)
      │
      │  yf.Ticker(ticker).history(...)
      ▼
Yahoo Finance API
      │
      ▼
Response → CSV storage (users.csv, transactions.csv, sold.csv, balance.txt)
```

Trading is gated to market hours via a CST timezone check on every `/trade` and `/sell_stock` request. Portfolio values update in real time by re-fetching current prices on each `/update_holdings` call.

---

## Pages

| Route | Page | Description |
|---|---|---|
| `/` | Home | Overview, features, how-it-works |
| `/practice` | Practice | Live paper trading dashboard |
| `/learn` | Learn | Structured investing lessons |
| `/simulator` | Simulator | Backtester + Fund Comparison |
| `/analysis` | Analysis | Deep dive stock research |

---

## Project Structure

```
hedgex/
├── app.py               # Flask server, all API routes
├── main.html            # Home page
├── practice.html        # Paper trading UI
├── learn.html           # Learning modules
├── simulator.html       # Backtester + Fund Comparison
├── analysis.html        # Stock analysis dashboard
├── users.csv            # Open positions
├── sold.csv             # Closed position history
├── transactions.csv     # Full transaction log
├── balance.txt          # Current virtual cash balance
└── requirements.txt     # Python dependencies
```

---

## Impact

- **200+ users** across DECA chapters
- **350+ students** taught investing fundamentals through the CISP program
- **Won Congressional App Challenge District 26** (Texas D-26)
- Helped increase DECA Stock Market Event participation by **250%** (59 total teams)
- Featured as a capstone project for the Prosper Career Independent Study Program

---

## Roadmap

- [ ] User accounts and persistent portfolios
- [ ] Options trading simulation
- [ ] Watchlists and price alerts
- [ ] Mobile-responsive practice page
- [ ] Leaderboard for classroom competitions
- [ ] More backtesting strategies (Pairs Trading, Sector Rotation)

---

## Disclaimer

Hedgex is a financial **education** tool. All trading is simulated with virtual money. Nothing on this platform constitutes real investment advice. Past backtest performance does not guarantee future results.

---

## Author

**Tanish Chauhan**  
Prosper High School · Prosper, TX  
[tanishchauhan4444@gmail.com](mailto:tanishchauhan4444@gmail.com) · [GitHub](https://github.com/TanishC4444)

---

<div align="center">

Built with Python, Flask, and a lot of curiosity about how markets work.

⭐ Star this repo if Hedgex helped you learn something.

</div>