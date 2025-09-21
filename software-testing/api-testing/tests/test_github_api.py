import requests
import pytest

BASE = "https://api.github.com"

def test_user_repos():
    res = requests.get(f"{BASE}/users/Q1cxx/repos")
    assert res.status_code == 200
    json_data = res.json()
    repo_names = [r["name"] for r in json_data]
    assert "automation-testing-showcase" in repo_names