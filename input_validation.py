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


def validate_handle(handle, session, max_attempts=5):
    attempts = 0
    while attempts < max_attempts:
        handle = handle.strip()
        if not handle:
            return False, "You must enter a handle"
        from api import check_handle_exists

        if not check_handle_exists(handle, session):
            return False, "The handle not found"
        return True, handle
    return False, f"Too many invalid attempts ({max_attempts})"


def validate_rating(min_rating, max_rating, max_attempts=5):
    try:
        min_rating = int(min_rating)
        max_rating = int(max_rating)
        if min_rating < 800 or max_rating > 3500:
            return False, "Ratings must be between 800 and 3500."
        if min_rating > max_rating:
            return False, "Minimum rating must be less than or equal to maximum rating."
        return True, (min_rating, max_rating)
    except ValueError:
        return False, "Please enter valid integer numbers for ratings."
