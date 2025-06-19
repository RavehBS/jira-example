"""Run a couple of read‑only Jira operations interactively."""
from pprint import pprint
import jira_client as jc

def main():
    print("\n== Projects you can access ==")
    for p in jc.list_projects():
        print(f"{p['key']:<8} │ {p['name']}")

    key = input("\nEnter an issue key to inspect (e.g., PROJ-1): ").strip()
    if key:
        issue = jc.get_issue(key)
        print("\n== Issue details (truncated) ==")
        pprint({
            "key": issue["key"],
            "summary": issue["fields"]["summary"],
            "status": issue["fields"]["status"]["name"],
        })

        project_key = key.split("-")[0]
        print(f"\n== Latest issues for project {project_key} ==")
        for i in jc.search_jql(f"project = {project_key} ORDER BY created DESC", 10):
            print(f"{i['key']:<8} │ {i['fields']['summary']}")

if __name__ == "__main__":
    main()