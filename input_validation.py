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


def get_handle_input(session, max_attempts=5):
    attempts = 0
    while attempts < max_attempts:
        handle = input("Enter your Codeforces handle: ").strip()
        if not handle:
            print("You must write your handle")
            attempts += 1
            continue
        from api import check_handle_exists

        if not check_handle_exists(handle, session):
            print("The handle not found")
            attempts += 1
            continue
        return handle
    print(f"Too many invalid attempts ({max_attempts}). Exiting.")
    exit(1)


def get_tags_input(max_attempts=5):
    attempts = 0
    while attempts < max_attempts:
        print("Available tags:")
        for tag in VALID_TAGS:
            print(f"  - {tag}")
        tags_input = input(
            "Enter desired tags (comma-separated, e.g., math,greedy): "
        ).strip()
        if not tags_input:
            print("You must enter at least one tag")
            attempts += 1
            continue
        tags = [tag.strip() for tag in tags_input.split(",") if tag.strip()]
        if not tags:
            print("You must enter at least one tag")
            attempts += 1
            continue
        if not all(tag in VALID_TAGS for tag in tags):
            print(f"Invalid tags. Choose from: {', '.join(VALID_TAGS)}")
            attempts += 1
            continue
        return tags
    print(f"Too many invalid attempts ({max_attempts}). Exiting.")
    exit(1)


def get_rating_input(max_attempts=5):
    attempts = 0
    while attempts < max_attempts:
        try:
            min_rating = int(input("Enter minimum rating: "))
            max_rating = int(input("Enter maximum rating: "))
            if min_rating < 800 or max_rating > 3500:
                print("Ratings must be between 800 and 3500.")
                attempts += 1
                continue
            if min_rating > max_rating:
                print("Minimum rating must be less than or equal to maximum rating.")
                attempts += 1
                continue
            return min_rating, max_rating
        except ValueError:
            print("Please enter valid integer numbers for ratings.")
            attempts += 1
    print(f"Too many invalid attempts ({max_attempts}). Exiting.")
    exit(1)


def get_exclude_solved_input(max_attempts=5):
    attempts = 0
    while attempts < max_attempts:
        response = input("Exclude solved problems? (y/n): ").lower().strip()
        if response in ["y", "n"]:
            return response == "y"
        print("Please enter 'y' or 'n'.")
        attempts += 1
    print(f"Too many invalid attempts ({max_attempts}). Exiting.")
    exit(1)


def confirm_inputs(handle, tags, min_rating, max_rating, exclude_solved):
    print("\nPlease confirm your inputs:")
    print(f"Handle: {handle}")
    print(f"Tags: {', '.join(tags)}")
    print(f"Rating range: {min_rating} - {max_rating}")
    print(f"Exclude solved problems: {'Yes' if exclude_solved else 'No'}")
    return input("Is this correct? (y/n): ").lower().strip() == "y"
