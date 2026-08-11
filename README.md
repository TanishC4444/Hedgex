# Hedgex

A full-stack financial-literacy platform that combines paper trading, strategy backtesting, fund comparison, stock analysis, and structured investing lessons.

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-2.x-000000)](https://flask.palletsprojects.com/)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)

## Overview

Hedgex provides a risk-free environment for learning market concepts with simulated capital and real market data. Users can trade paper portfolios, compare investment strategies against historical data, and study investing concepts through structured lessons.

## Features

- Paper trading with virtual capital
- Historical strategy backtesting
- Fund comparison against SPY
- Stock research and market metrics
- Beginner and advanced learning tracks
- Transaction and portfolio tracking

## Prerequisites

- Python 3.10+
- pip
- Internet access for Yahoo Finance market data

## Installation

```bash
git clone https://github.com/TanishC4444/Hedgex.git
cd Hedgex
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\\Scripts\\activate
pip install -r requirements.txt
```

## Quick Start

```bash
python app.py
```

Open `http://127.0.0.1:5000` in your browser.

## Project Structure

```text
Hedgex/
├── app.py
├── main.html
├── practice.html
├── learn.html
├── simulator.html
├── analysis.html
├── users.csv
├── sold.csv
├── transactions.csv
├── balance.txt
└── requirements.txt
```

## Data and Privacy

The application uses local CSV/text files for portfolio and transaction state. Do not commit real credentials or private user data. A production deployment should replace shared local files with a concurrency-safe persistence layer.

## Testing

Run the project's available test suite or development checks before deployment. The repository does not currently document a single canonical test command.

## Roadmap

- Persistent user accounts
- Options-trading simulation
- Watchlists and price alerts
- Mobile-responsive trading interface
- Classroom leaderboard
- Additional backtesting strategies

## Disclaimer

Hedgex is an educational simulation. It does not provide investment advice, and historical backtest performance does not guarantee future results.

## License

MIT

## Support

Use GitHub Issues for bugs, questions, and feature requests.
