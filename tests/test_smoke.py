"""Offline checks using fresh simulated state, never the project's CSV files."""
import importlib.util
from pathlib import Path
import ssl
import sys

import pytest


@pytest.fixture
def client(tmp_path, monkeypatch):
    source = Path(__file__).resolve().parents[1] / "app.py"
    monkeypatch.chdir(tmp_path)
    original_context = ssl._create_default_https_context
    spec = importlib.util.spec_from_file_location("hedgex_smoke_app", source)
    module = importlib.util.module_from_spec(spec)
    monkeypatch.setitem(sys.modules, spec.name, module)
    spec.loader.exec_module(module)
    assert ssl._create_default_https_context is original_context
    module.app.config.update(TESTING=True)

    def no_quotes(*args, **kwargs):
        raise AssertionError("Offline smoke checks must not request market data")

    monkeypatch.setattr(module.yf, "Ticker", no_quotes)
    return module.app.test_client()


@pytest.mark.parametrize("path", ["/", "/learn", "/practice", "/simulator", "/analysis"])
def test_pages_render(client, path):
    response = client.get(path)
    assert response.status_code == 200
    assert b"<html" in response.data.lower()


def test_fresh_simulated_balance(client):
    assert client.get("/balance").get_json() == {"balance": 100000.0}


def test_equation_requires_input_before_fetching_data(client):
    response = client.post("/evaluate_equation", json={})
    assert response.status_code == 400
    assert "error" in response.get_json()
