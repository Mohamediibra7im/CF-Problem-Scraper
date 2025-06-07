import json
import csv
from uuid import uuid4

def filter_problems(problems, tags, min_rating, max_rating, solved_set, exclude_solved):
    filtered_problems = []
    for problem in problems:
        if "rating" not in problem:
            continue
        if not (min_rating <= problem["rating"] <= max_rating):
            continue
        problem_tags = problem.get("tags", [])
        if not any(tag in problem_tags for tag in tags):
            continue
        key = (problem["contestId"], problem["index"])
        if exclude_solved and key in solved_set:
            continue
        entry = {
            "Name": f"{problem['contestId']}{problem['index']} - {problem['name']}",
            "Link": f"https://codeforces.com/problemset/problem/{problem['contestId']}/{problem['index']}",
            "Rating": problem["rating"],
            "Status": "solved" if key in solved_set else "unsolved",
        }
        filtered_problems.append(entry)
    filtered_problems.sort(key=lambda x: x["Rating"])
    return filtered_problems

def save_problems(filtered_problems):
    # Save to JSON
    json_filename = f"filtered_problems_{uuid4()}.json"
    with open(json_filename, "w", encoding="utf-8") as f:
        json.dump(filtered_problems, f, ensure_ascii=False, indent=4)
    print(f"Saved {len(filtered_problems)} problems to '{json_filename}'")

    # Save to CSV
    csv_filename = f"filtered_problems_{uuid4()}.csv"
    with open(csv_filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["Name", "Link", "Rating", "Status"])
        writer.writeheader()
        writer.writerows(filtered_problems)
    print(f"Saved {len(filtered_problems)} problems to '{csv_filename}'")
