# HedgeX

Explore stock research, paper trading, strategy ideas, and investing lessons in a local Flask app. Trades use simulated funds; quotes and historical prices require internet access.

![HedgeX running locally with simulated account state](docs/local-preview.jpg)

## Run locally

Requires Python 3.10+ and Git. Run these commands in a terminal:

```sh
git clone --filter=blob:none https://github.com/TanishC4444/Hedgex.git
cd Hedgex
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python app.py
```

On Windows, activate with `.venv\Scripts\activate`. Open <http://127.0.0.1:5000>. No API key is required for the checked public market-data path.

The app keeps simulated holdings, transactions, and balances in local CSV/text files. Use synthetic state for demonstrations. This is a single-user prototype; shared files, expression evaluation, and account isolation need further work before public hosting.

## Check your setup

```sh
python -m pip install -r requirements-dev.txt
python -m pytest -q
```

Seven offline tests cover page rendering, initial balance, and input validation. A separate live stock-page check returned 78 historical price records for AAPL. Provider availability and market data can change; these checks do not validate every strategy or financial calculation.

If installation fails, confirm the virtual environment is active and use the required Python version. If market data is unavailable, check connectivity and retry later. Stop the local server with Ctrl+C.

## Project details

- `app.py`: routes, analysis, and simulation logic.
- `templates/`: learning, trading, and analysis interfaces.
- [Portfolio analysis](PORTFOLIO_ANALYSIS.md).
- [Earlier variants and preserved history](docs/consolidation/README.md). This is the maintained repo; `finalSMGHedgex` and `PCIS_FantasySMG` are archived.
- [MIT license](LICENSE).
