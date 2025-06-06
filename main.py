import requests
import json

def check_handle_exists(handle):
    url = f"https://codeforces.com/api/user.info?handles={handle}"
    response = requests.get(url)
    return response.status_code == 200 and response.json()['status'] == 'OK'

def get_problems_by_tags_and_rating(tags, min_rating, max_rating, handle):
    
    # Get solved problems
    solved_set = set()
    status_url = f"https://codeforces.com/api/user.status?handle={handle}"
    status_response = requests.get(status_url)

    if status_response.status_code == 200:
        submissions = status_response.json()['result']
        for sub in submissions:
            if sub.get('verdict') == 'OK':
                problem = sub['problem']
                solved_key = (problem['contestId'], problem['index'])
                solved_set.add(solved_key)
    else:
        print("Failed to fetch user submission data")
        return

    # Fetch problemset
    url = 'https://codeforces.com/api/problemset.problems'
    response = requests.get(url)

    if response.status_code != 200:
        print("Failed to fetch problemset")
        return

    print("Successfully fetched data")

    data = response.json()
    problems = data['result']['problems']

    filtered_problems = []

    for problem in problems:
        if 'rating' not in problem:
            continue

        if not (min_rating <= problem['rating'] <= max_rating):
            continue

        problem_tags = problem.get("tags", [])
        if any(tag in problem_tags for tag in tags):
            key = (problem['contestId'], problem['index'])
            entry = {
                "name": f"{problem['contestId']}{problem['index']} - {problem['name']}",
                "link": f"https://codeforces.com/problemset/problem/{problem['contestId']}/{problem['index']}",
                "rating": problem['rating'],
                "status": "solved" if key in solved_set else "unsolved"
            }
            filtered_problems.append(entry)

    filtered_problems.sort(key=lambda x: x['rating'])

    with open("filtered_problems.json", "w", encoding="utf-8") as f:
        json.dump(filtered_problems, f, ensure_ascii=False, indent=4)

    print(f"Saved {len(filtered_problems)} problems to 'filtered_problems.json'")


# Handle input with validation
while True:
    handle = input("Enter your Codeforces handle: ").strip()

    if not handle:
        print("You must write your handle")
        continue

    if not check_handle_exists(handle):
        print("The handle not found")
        continue

    break

tags = ["implementation", "brute force", "math", "greedy", "sortings", "strings"]
min_rating = 800
max_rating = 1000

get_problems_by_tags_and_rating(tags, min_rating, max_rating, handle)

# Codeforces Tags:
# -> 2-sat
# -> binary search
# -> bitmasks
# -> brute force
# -> chinese remainder theorem
# -> combinatorics
# -> constructive algorithms
# -> data structures
# -> dfs and similar
# -> divide and conquer
# -> dp
# -> dsu
# -> expression parsing
# -> fft
# -> flows
# -> games
# -> geometry
# -> graph matchings
# -> graphs
# -> greedy
# -> hashing
# -> implementation
# -> interactive
# -> math
# -> matrices
# -> meet-in-the-middle
# -> number theory
# -> probabilities
# -> schedules
# -> shortest paths
# -> sortings
# -> string suffix structures
# -> strings
# -> ternary search
# -> trees
# -> two pointers