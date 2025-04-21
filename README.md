# CF-Problem-Scraper

A Python script that fetches Codeforces problems based on specified tags and rating range, while also checking which problems have been solved by a given user.

## Features

- Fetches problems from Codeforces API
- Filters problems by:
  - Tags (e.g., "implementation", "math", "greedy")
  - Rating range (e.g., 800-3500)
- Checks which problems have been solved by the specified user
- Saves results to a JSON file
- Validates user handle before processing

## Requirements

- Python 3.x
- `requests` library (install via `pip install -r requirements.txt`)

## Usage

1. Run the script: `python main.py`
2. Enter your Codeforces handle when prompted
3. The script will:
   - Fetch all problems matching the predefined tags and rating range
   - Check which problems you've already solved
   - Save the results to `filtered_problems.json`

## Configuration

You can modify the following variables in `main.py` to customize your search:

```python
tags = ["implementation", "brute force", "math", "greedy", "sortings", "strings"]
min_rating = 800
max_rating = 1000
```

## Output

The script generates a JSON file (`filtered_problems.json`) containing:
- Problem name (with contest ID and index)
- Problem link
- Problem rating
- Solution status ("solved" or "unsolved")

Problems are sorted by rating in ascending order.

## Available Tags

The script supports all standard Codeforces tags, including:
- binary search
- data structures
- dp
- graphs
- greedy
- math
- strings
- trees
- and many more (see full list in the code comments)

## Note

The Codeforces API has rate limits. Please use this script responsibly and avoid making too many requests in a short period.