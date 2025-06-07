# CF-Problem-Scraper 🚀

A modular Python project that fetches Codeforces problems based on user-specified tags and rating ranges, with a PyQt GUI for an interactive experience! 🧩

## Features 🌟

- 🖥️ **PyQt GUI**: Input criteria through a user-friendly form and view filtered problems in a sortable table with columns for Name, Link, Rating, and Status.
- 📋 **Table Sorting**: Sort problems by clicking column headers (Name, Link, Rating, Status) in ascending or descending order.
- 🔗 **Copy Link**: Copy the URL of a selected problem to the clipboard with a single click.
- 📚 **Saved User Profiles**: Save and load input preferences (handle, tags, rating range, exclude solved) for quick reuse.
- 🧹 **Clear Cache**: Clear cached API responses to fetch fresh data.
- 📡 Fetches problems and user submissions via the Codeforces API.
- 🔍 Filters problems by:
  - User-defined tags (e.g., `implementation`, `math`, `greedy`) selected from a list.
  - User-defined rating range (800–3500) via spin boxes.
  - Option to exclude already solved problems via a checkbox 🚫.
- ✅ Validates user inputs:
  - Ensures valid Codeforces handle.
  - Requires at least one tag selection.
  - Enforces rating range (800–3500, min ≤ max).
- 💾 Caches API responses to reduce redundant requests and respect rate limits.
- 📄 Saves results to JSON and CSV files named based on selected tags (e.g., `filtered_problems_math_greedy.json`).
- 📈 Sorts problems by rating in ascending order by default.
- 🧩 Modular design with separate files for API handling, input validation, problem filtering, and GUI.

## Project Structure 📂

```
project/
├── api.py              # Handles Codeforces API interactions
├── input_validation.py # Manages input validation logic
├── problem_filter.py   # Filters problems and saves output
├── gui.py              # PyQt GUI implementation
├── main.py             # Launches the GUI application
├── requirements.txt    # Lists required Python libraries
├── profiles.json       # Stores user profiles (generated at runtime)
├── README.md           # Project documentation
```

## Requirements 🛠️

- Python 3.9+ 🐍
- Required libraries:
  - `requests==2.32.3`
  - `requests-cache==1.2.1`
  - `PyQt5==5.15.11`
- Install dependencies via:
  ```bash
  pip install -r requirements.txt
  ```

## Setup ⚙️

1. Clone or download the project files to a directory 📥.
2. Install the required libraries:
   ```bash
   pip install requests==2.32.3 requests-cache==1.2.1 PyQt5==5.15.11
   ```
3. Ensure all Python files (`api.py`, `input_validation.py`, `problem_filter.py`, `gui.py`, `main.py`) and `requirements.txt` are in the same directory 📂.

## Usage 🎮

1. Run the main script to launch the GUI:
   ```bash
   python main.py
   ```
2. In the GUI window:
   - **Load a profile** from the "Load Profile" dropdown to auto-fill fields, or select "None" to enter new inputs.
   - **Enter your Codeforces handle** in the text field (e.g., `MIDORIYA_`) 👤.
   - **Select tags** from the list by clicking (hold Ctrl for multiple selections) 🏷️.
   - **Set minimum and maximum ratings** using the spin boxes (800–3500) 📏.
   - **Check/uncheck** the "Exclude solved problems" box 🚫.
   - Click **Save Profile** to store the current inputs (requires valid inputs).
   - Click **Clear Cache** to refresh API data 🧹.
   - Click **Filter Problems** to fetch and display problems in the table.
   - **Sort the table** by clicking column headers (Name, Link, Rating, Status) to toggle ascending/descending order.
   - Select a row and click **Copy Link** to copy the problem URL to the clipboard.
   - Click **Save Results** to save the filtered problems to JSON and CSV files.
3. The GUI will:
   - Validate inputs and show error messages if invalid (e.g., invalid handle, no tags selected) ✅.
   - Fetch and filter problems based on your criteria 🔍.
   - Display results in a sortable table with problem details 📊.
   - Save results to files like `filtered_problems_math_greedy.json` and `.csv` 💾.

## Output 📊

The script generates two files when you click "Save Results":
- **JSON file**: Contains problem details (name, link, rating, status) in a structured format 📜.
- **CSV file**: Contains the same details in a tabular format, suitable for spreadsheets 📋.

Each problem entry includes:
- **Name**: Contest ID, index, and problem name (e.g., `1000A - Codeforces Rating`) 🏷️.
- **Link**: URL to the problem on Codeforces 🔗.
- **Rating**: Problem difficulty rating 📈.
- **Status**: "solved" ✅ or "unsolved" ⬜ based on your submission history.

## Configuration 🔧

Inputs are provided through the GUI, with validation enforced:
- **Handle**: Must be a valid Codeforces handle, verified via API 👤.
- **Tags**: At least one tag must be selected from the supported list 🏷️.
- **Rating Range**: Must be within 800–3500, with minimum ≤ maximum 📏.
- **Exclude Solved**: Checkbox defaults to unchecked (False) if not selected.
- **Profiles**: Saved to `profiles.json` and loaded via the dropdown menu.

To modify default behavior (e.g., default rating range), edit `gui.py` (e.g., change `QSpinBox` defaults) or extend the code to read from a configuration file 📝.

## Available Tags 🏷️

The GUI displays all standard Codeforces tags for selection, including:
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

- **API Rate Limits**: The Codeforces API has rate limits (e.g., 1 request per second for some endpoints). The project uses `requests-cache` to cache responses for 1 hour, reducing API calls ⏳.
- **Caching**: Cached responses are stored in a local `codeforces_cache.sqlite` file. Use the "Clear Cache" button to refresh API data 💾.
- **Profiles**: User profiles are stored in `profiles.json`, created dynamically when saving a profile. Do not delete this file to retain saved profiles 📚.
- **Error Handling**: The GUI displays user-friendly error messages for invalid inputs or API failures 🚨.
- **PyQt5 Requirements**: PyQt5 requires a compatible system environment (e.g., X11 on Linux, macOS, or Windows). Ensure your system supports GUI applications.
- **Extensibility**: The modular structure supports adding features like visualizations, additional filters, or integration with other platforms 🌐.

## Example 🌟

1. Run `python main.py`.
2. In the GUI:
   - Select profile "MIDORIYA_" or enter new inputs.
   - Enter handle: `MIDORIYA_`
   - Select tags: `math`, `greedy`
   - Set rating range: 800–1000
   - Check "Exclude solved problems"
   - Click "Save Profile" to store settings
   - Click "Clear Cache" if fresh data is needed
   - Click "Filter Problems" to display 42 problems in the table
   - Click the "Rating" column header to sort by rating in descending order
   - Select a problem row and click "Copy Link" to copy its URL
   - Click "Save Results" to generate:
     - `filtered_problems_math_greedy.json`
     - `filtered_problems_math_greedy.csv`

## Video Tutorial 📹
Check out this video tutorial for a walkthrough of the project: [CF-Problem Scraper Video](https://drive.google.com/file/d/1mOd4NQ6jyPIZywjyLrvwGAnbN9EfOob2/view?usp=sharing) 🎥