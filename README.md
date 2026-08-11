# finalSMGHedgex

A Flask-based stock-market simulation project for exploring paper trading, portfolio management, and financial data.

## Overview

This repository contains an early implementation of the Hedgex stock-market simulation. It provides a web interface backed by Python and Flask, with local files used for portfolio and transaction state.

## Features

- Flask web application
- Stock-market data integration
- Virtual portfolio and cash balance
- Buy and sell transaction workflows
- Transaction and portfolio persistence
- Development test script

## Prerequisites

- Python 3
- pip

## Installation

```bash
git clone https://github.com/TanishC4444/finalSMGHedgex.git
cd finalSMGHedgex
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\\Scripts\\activate
pip install -r requirements.txt
```

## Quick Start

```bash
python app.py
```

Open the local address printed by Flask.

## Project Structure

```text
finalSMGHedgex/
├── app.py
├── index.html
├── templates/
├── requirements.txt
├── req.txt
└── test.py
```

## Testing

```bash
python test.py
```

## Status

Development project.

## License

No license file is currently specified in the repository.

## Contact

Use GitHub Issues for questions and bug reports.
