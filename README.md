# CF-Problem-Scraper 🚀

A modular Python project that fetches Codeforces problems based on user-specified tags and rating ranges, and tracks which problems you've solved! 🧩

## Features 🌟

- 📡 Fetches problems and user submissions via the Codeforces API
- 🔍 Filters problems by:
  - User-defined tags (e.g., `implementation`, `math`, `greedy`)
  - User-defined rating range (e.g., 800–3500)
  - Option to exclude already solved problems 🚫
- ✅ Validates user handle, tags, and rating inputs
- 💾 Caches API responses to reduce redundant requests and respect rate limits
- 📄 Saves results to both JSON and CSV files with unique filenames
- 📈 Sorts problems by rating in ascending order
- 🧩 Modular design with separate files for API handling, input validation, and problem filtering

## Project Structure 📂

```
project/
├── api.py              # Handles Codeforces API interactions
├── input_validation.py # Manages user input and validation 
├── problem_filter.py   # Filters problems and saves output
├── main.py             # Orchestrates the program flow
├── README.md           # Project documentation
```

## Requirements 🛠️

- Python 3.9+ 🐍
- Required libraries:
  - `requests`
  - `requests-cache`
- Install dependencies via:
  ```bash
  pip install -r requirements.txt
  ```

## Setup ⚙️

1. Clone or download the project files to a directory 📥
2. Install the required libraries:
   ```bash
   pip install requests requests-cache
   ```
3. Ensure all Python files (`api.py`, `input_validation.py`, `problem_filter.py`, `main.py`) are in the same directory 📂

## Usage 🎮

1. Run the main script:
   ```bash
   python main.py
   ```
2. Follow the prompts to:
   - Enter your Codeforces handle 👤
   - Specify desired tags (comma-separated, e.g., `math,greedy`) 🏷️
   - Enter minimum and maximum rating (e.g., 800 and 1000) 📏
   - Choose whether to exclude solved problems (y/n) 🚫
3. The script will:
   - Validate inputs ✅
   - Fetch and filter problems based on your criteria 🔍
   - Save results to uniquely named JSON and CSV files (e.g., `filtered_problems_<uuid>.json`, `filtered_problems_<uuid>.csv`) 💾

## Output 📊

The script generates two files:
- **JSON file**: Contains problem details (name, link, rating, status) in a structured format 📜
- **CSV file**: Contains the same details in a tabular format, suitable for spreadsheets 📋

Each problem entry includes:
- **Name**: Contest ID, index, and problem name (e.g., `1000A - Codeforces Rating`) 🏷️
- **Link**: URL to the problem on Codeforces 🔗
- **Rating**: Problem difficulty rating 📈
- **Status**: "solved" ✅ or "unsolved" ⬜ based on your submission history

## Configuration 🔧

Inputs are provided interactively at runtime. The following are validated:
- **Handle**: Must be a valid Codeforces handle 👤
- **Tags**: Must be from the list of supported Codeforces tags (see below) 🏷️
- **Rating Range**: Must be within 800–3500, with minimum ≤ maximum 📏

To modify default behavior (e.g., default tags or ratings), edit `input_validation.py` or extend the code to read from a configuration file 📝

## Available Tags 🏷️

The script supports all standard Codeforces tags, including:
- 2-sat
- binary search 🔍
- bitmasks
- brute force 💪
- chinese remainder theorem
- combinatorics
- constructive algorithms 🛠️
- data structures 📚
- dfs and similar
- divide and conquer
- dp
- dsu
- expression parsing
- fft
- flows
- games 🎲
- geometry 📐
- graph matchings
- graphs 🌐
- greedy
- hashing
- implementation 🖥️
- interactive
- math ➕
- matrices
- meet-in-the-middle
- number theory 🔢
- probabilities
- schedules
- shortest paths 🛤️
- sortings
- string suffix structures
- strings 📜
- ternary search
- trees 🌳
- two pointers

## Notes 📌

- **API Rate Limits**: The Codeforces API has rate limits (e.g., 1 request per second for some endpoints). The project uses `requests-cache` to cache responses for 1 hour, reducing API calls ⏳
- **Caching**: Cached responses are stored in a local `codeforces_cache.sqlite` file 💾
- **Error Handling**: The script handles network errors, invalid inputs, and API failures gracefully, with user-friendly error messages 🚨
- **Extensibility**: The modular structure makes it easy to add features like GUI support, visualization, or integration with other platforms 🌐

## Example 🌟

```bash
$ python main.py
Enter your Codeforces handle: MIDORIYA_
Enter desired tags (comma-separated, e.g., math,greedy): math,greedy
Enter minimum rating: 800
Enter maximum rating: 1000
Exclude solved problems? (y/n): y
Successfully fetched data
Saved 42 problems to 'filtered_problems_123e4567-e89b-12d3-a456-426614174000.json'
Saved 42 problems to 'filtered_problems_123e4567-e89b-12d3-a456-426614174000.csv'
```

## Contributing 🤝

Feel free to fork the project and submit pull requests for new features or improvements! Suggestions for enhancements include:
- Adding a GUI or web interface 🖥️
- Visualizing problem distribution (e.g., rating histograms) 📊
- Tracking progress with a local database 📚
- Supporting other platforms like LeetCode or AtCoder 🌐
