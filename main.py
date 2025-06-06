from requests_cache import CachedSession
from api import get_solved_problems, get_problemset
from input_validation import (
    get_handle_input,
    get_tags_input,
    get_rating_input,
    get_exclude_solved_input,
)
from problem_filter import filter_problems, save_problems


def main():
    # Initialize cached session
    # Create a cached session to avoid hitting the API too frequently
    session = CachedSession("codeforces_cache", expire_after=3600)  # Cache for 1 hour

    # Get user inputs
    handle = get_handle_input(session)
    tags = get_tags_input()
    min_rating, max_rating = get_rating_input()
    exclude_solved = get_exclude_solved_input()

    # Fetch data
    solved_set = get_solved_problems(handle, session)
    problems = get_problemset(session)

    if not problems:
        print("No problems fetched. Exiting.")
        session.close()
        return

    # Filter and save problems
    filtered_problems = filter_problems(
        problems, tags, min_rating, max_rating, solved_set, exclude_solved
    )
    if filtered_problems:
        save_problems(filtered_problems)
    else:
        print("No problems found matching the criteria.")

    session.close()


if __name__ == "__main__":
    main()
