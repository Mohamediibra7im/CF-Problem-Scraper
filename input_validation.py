VALID_TAGS = [
    "2-sat",
    "binary search",
    "bitmasks",
    "brute force",
    "chinese remainder theorem",
    "combinatorics",
    "constructive algorithms",
    "data structures",
    "dfs and similar",
    "divide and conquer",
    "dp",
    "dsu",
    "expression parsing",
    "fft",
    "flows",
    "games",
    "geometry",
    "graph matchings",
    "graphs",
    "greedy",
    "hashing",
    "implementation",
    "interactive",
    "math",
    "matrices",
    "meet-in-the-middle",
    "number theory",
    "probabilities",
    "schedules",
    "shortest paths",
    "sortings",
    "string suffix structures",
    "strings",
    "ternary search",
    "trees",
    "two pointers",
]


def get_handle_input(session):
    while True:
        handle = input("Enter your Codeforces handle: ").strip()
        if not handle:
            print("You must write your handle")
            continue
        from api import check_handle_exists

        if not check_handle_exists(handle, session):
            print("The handle not found")
            continue
        return handle


def get_tags_input():
    while True:
        print("Available tags:")
        for tag in VALID_TAGS:
            print(f"  - {tag}")
        
        tags_input = input(
            "Enter desired tags (comma-separated, e.g., math,greedy): "
        ).strip()
        tags = [tag.strip() for tag in tags_input.split(",") if tag.strip()]
        if not tags:
            print("You must enter at least one tag")
            continue
        if not all(tag in VALID_TAGS for tag in tags):
            print(f"Invalid tags. Choose from: {', '.join(VALID_TAGS)}")
            continue
        return tags


def get_rating_input():
    while True:
        try:
            min_rating = int(input("Enter minimum rating: "))
            max_rating = int(input("Enter maximum rating: "))
            if min_rating <= max_rating and min_rating >= 800 and max_rating <= 3500:
                return min_rating, max_rating
            print(
                "Minimum rating must be less than or equal to maximum rating, and within 800-3500."
            )
        except ValueError:
            print("Please enter valid numbers for ratings.")


def get_exclude_solved_input():
    return input("Exclude solved problems? (y/n): ").lower() == "y"
