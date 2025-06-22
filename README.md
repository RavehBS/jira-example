# Jira Cloud API – Python Example 👩‍💻

A minimal, opinionated starter project that shows how to call the **Jira Cloud
REST API** using the new `https://api.atlassian.com/ex/jira/<cloud-id>/...`
endpoint pattern — no PATs, no basic-auth, just an OAuth 2.0 access token.  
It grew out of internal workshops and is intentionally simple so that students
can see “just enough” Python, logging, and error-handling without the usual
framework noise.

---

## ✨ What you get

| Feature | File | Notes |
|---------|------|-------|
| Thin, reusable API wrapper | `src/jira_client.py` | Centralises headers,  retry-free but **status-aware** requests, and structured logging. |
| Environment-driven config | `.env.example` | Keeps tokens & IDs out of source control. |
| Ready-to-run demo script | `src/example_list_projects.py` | Prints all projects to the console – your first quick win! |
| Reproducible deps | `requirements.txt` | Only `requests`, `python-dotenv`, and `loguru`. |

---

## 🚀 Quick start

```bash
# 1) Clone and create a virtual environment
git clone https://github.com/RavehBS/jira-example.git
cd jira-example
python -m venv .venv && source .venv/bin/activate   # Windows: .venv\Scripts\activate

# 2) Install requirements
pip install -r requirements.txt

# 3) Configure secrets
cp .env.example .env
#   ↳ Fill in JIRA_ACCESS_TOKEN and JIRA_CLOUD_ID

# 4) Test it!
python -m src.example_list_projects
