"""Tiny Jira REST client (read‑only)."""
from __future__ import annotations
import os, base64, requests
from typing import Any, Dict, List
from dotenv import load_dotenv

load_dotenv()  # reads .env in project root

BASE_URL = os.getenv("JIRA_BASE_URL", "").rstrip("/")
EMAIL = os.getenv("JIRA_EMAIL")
TOKEN = os.getenv("JIRA_TOKEN")

if not all([BASE_URL, EMAIL, TOKEN]):
    raise RuntimeError("Missing JIRA_BASE_URL, JIRA_EMAIL or JIRA_TOKEN in environment")

# PAT uses basic‑auth: base64("email:token")
auth_str = f"{EMAIL}:{TOKEN}".encode()
HEADERS = {
    "Authorization": "Basic " + base64.b64encode(auth_str).decode(),
    "Accept": "application/json",
}

def _get(path: str, params: Dict[str, Any] | None = None):
    """Internal helper that performs a GET and returns parsed JSON."""
    url = f"{BASE_URL}/rest/api/3/{path.lstrip('/')}"
    resp = requests.get(url, headers=HEADERS, params=params, timeout=10)
    resp.raise_for_status()
    return resp.json()

# Public helper functions ↓

def list_projects() -> List[dict]:
    """Return a list of all projects the token can see."""
    data = _get("project/search")
    return data.get("values", [])

def get_issue(key: str) -> dict:
    """Fetch a single issue by key (e.g., PROJ-1)."""
    return _get(f"issue/{key}")

def search_jql(jql: str, max_results: int = 50) -> List[dict]:
    """Run a JQL query and return issues."""
    params = {"jql": jql, "maxResults": max_results}
    data = _get("search", params)
    return data.get("issues", [])