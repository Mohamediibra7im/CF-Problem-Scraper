import requests
from requests_cache import CachedSession


def check_handle_exists(handle, session):
    url = f"https://codeforces.com/api/user.info?handles={handle}"
    try:
        response = session.get(url, timeout=5)
        response.raise_for_status()
        data = response.json()
        return data["status"] == "OK"
    except requests.exceptions.RequestException as e:
        print(f"Error checking handle: {e}")
        return False


def get_solved_problems(handle, session):
    solved_set = set()
    status_url = f"https://codeforces.com/api/user.status?handle={handle}"
    try:
        response = session.get(status_url, timeout=5)
        response.raise_for_status()
        submissions = response.json()["result"]
        for sub in submissions:
            if sub.get("verdict") == "OK":
                problem = sub["problem"]
                solved_key = (problem["contestId"], problem["index"])
                solved_set.add(solved_key)
        return solved_set
    except requests.exceptions.RequestException as e:
        print(f"Failed to fetch user submission data: {e}")
        return set()


def get_problemset(session):
    url = "https://codeforces.com/api/problemset.problems"
    try:
        response = session.get(url, timeout=5)
        response.raise_for_status()
        return response.json()["result"]["problems"]
    except requests.exceptions.RequestException as e:
        print(f"Failed to fetch problemset: {e}")
        return []
