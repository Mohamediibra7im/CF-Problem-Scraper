from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QListWidget,
    QSpinBox,
    QCheckBox,
    QPushButton,
    QTableWidget,
    QTableWidgetItem,
    QMessageBox,
    QComboBox,
)
from PyQt5.QtCore import Qt
from requests_cache import CachedSession
from api import get_solved_problems, get_problemset
from input_validation import VALID_TAGS, validate_handle, validate_rating
from problem_filter import filter_problems, save_problems
import json


class CodeforcesProblemFilterApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Codeforces Problem Filter")
        self.setGeometry(100, 100, 800, 600)
        self.session = CachedSession("codeforces_cache", expire_after=3600)
        self.profiles = self.load_profiles()
        self.sort_column = -1
        self.sort_order = Qt.AscendingOrder
        self.init_ui()

    def init_ui(self):
        # Main widget and layout
        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        layout = QVBoxLayout()
        main_widget.setLayout(layout)

        # Welcome message
        layout.addWidget(QLabel("Welcome to the CF Problem Scraper!"))
        layout.addWidget(QLabel("Enter your criteria to filter problems."))

        # Profile selection
        profile_layout = QHBoxLayout()
        profile_layout.addWidget(QLabel("Load Profile:"))
        self.profile_combo = QComboBox()
        self.profile_combo.addItem("None")
        self.profile_combo.addItems(self.profiles.keys())
        self.profile_combo.currentTextChanged.connect(self.load_profile)
        profile_layout.addWidget(self.profile_combo)
        layout.addLayout(profile_layout)

        # Handle input
        handle_layout = QHBoxLayout()
        handle_layout.addWidget(QLabel("Codeforces Handle:"))
        self.handle_input = QLineEdit()
        self.handle_input.setPlaceholderText("e.g., MIDORIYA_")
        handle_layout.addWidget(self.handle_input)
        layout.addLayout(handle_layout)

        # Tags selection
        layout.addWidget(QLabel("Select Tags:"))
        self.tags_list = QListWidget()
        self.tags_list.addItems(VALID_TAGS)
        self.tags_list.setSelectionMode(QListWidget.MultiSelection)
        layout.addWidget(self.tags_list)

        # Rating inputs
        rating_layout = QHBoxLayout()
        rating_layout.addWidget(QLabel("Rating Range:"))
        self.min_rating_input = QSpinBox()
        self.min_rating_input.setRange(800, 3500)
        self.min_rating_input.setValue(800)
        rating_layout.addWidget(QLabel("Min:"))
        rating_layout.addWidget(self.min_rating_input)
        self.max_rating_input = QSpinBox()
        self.max_rating_input.setRange(800, 3500)
        self.max_rating_input.setValue(3500)
        rating_layout.addWidget(QLabel("Max:"))
        rating_layout.addWidget(self.max_rating_input)
        layout.addLayout(rating_layout)

        # Exclude solved checkbox
        self.exclude_solved = QCheckBox("Exclude solved problems")
        layout.addWidget(self.exclude_solved)

        # Action buttons
        button_layout = QHBoxLayout()
        self.submit_button = QPushButton("Filter Problems")
        self.submit_button.clicked.connect(self.filter_problems)
        button_layout.addWidget(self.submit_button)
        self.save_profile_button = QPushButton("Save Profile")
        self.save_profile_button.clicked.connect(self.save_profile)
        button_layout.addWidget(self.save_profile_button)
        self.clear_cache_button = QPushButton("Clear Cache")
        self.clear_cache_button.clicked.connect(self.clear_cache)
        button_layout.addWidget(self.clear_cache_button)
        layout.addLayout(button_layout)

        # Results table
        self.results_table = QTableWidget()
        self.results_table.setColumnCount(4)
        self.results_table.setHorizontalHeaderLabels(
            ["Name", "Link", "Rating", "Status"]
        )
        self.results_table.setColumnWidth(0, 300)
        self.results_table.setColumnWidth(1, 200)
        self.results_table.setColumnWidth(2, 100)
        self.results_table.setColumnWidth(3, 100)
        self.results_table.setSortingEnabled(True)
        self.results_table.horizontalHeader().sectionClicked.connect(self.sort_table)
        self.results_table.itemSelectionChanged.connect(self.update_copy_button_state)
        layout.addWidget(self.results_table)

        # Results action buttons
        results_button_layout = QHBoxLayout()
        self.save_button = QPushButton("Save Results")
        self.save_button.setEnabled(False)
        self.save_button.clicked.connect(self.save_results)
        results_button_layout.addWidget(self.save_button)
        self.copy_link_button = QPushButton("Copy Link")
        self.copy_link_button.setEnabled(False)
        self.copy_link_button.clicked.connect(self.copy_link)
        results_button_layout.addWidget(self.copy_link_button)
        layout.addLayout(results_button_layout)

        self.filtered_problems = []
        self.tags = []

    def load_profiles(self):
        try:
            with open("profiles.json", "r", encoding="utf-8") as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return {}

    def save_profile(self):
        handle = self.handle_input.text()
        valid, message = validate_handle(handle, self.session)
        if not valid:
            QMessageBox.critical(self, "Error", message)
            return

        tags = [item.text() for item in self.tags_list.selectedItems()]
        if not tags:
            QMessageBox.critical(
                self, "Error", "You must select at least one tag to save a profile"
            )
            return

        min_rating = self.min_rating_input.value()
        max_rating = self.max_rating_input.value()
        valid, result = validate_rating(min_rating, max_rating)
        if not valid:
            QMessageBox.critical(self, "Error", result)
            return
        min_rating, max_rating = result

        profile_name = handle
        self.profiles[profile_name] = {
            "handle": handle,
            "tags": tags,
            "min_rating": min_rating,
            "max_rating": max_rating,
            "exclude_solved": self.exclude_solved.isChecked(),
        }

        with open("profiles.json", "w", encoding="utf-8") as f:
            json.dump(self.profiles, f, indent=4)

        self.profile_combo.clear()
        self.profile_combo.addItem("None")
        self.profile_combo.addItems(self.profiles.keys())
        QMessageBox.information(self, "Success", f"Profile '{profile_name}' saved.")

    def load_profile(self, profile_name):
        if profile_name == "None":
            self.handle_input.clear()
            self.tags_list.clearSelection()
            self.min_rating_input.setValue(800)
            self.max_rating_input.setValue(3500)
            self.exclude_solved.setChecked(False)
            return

        profile = self.profiles.get(profile_name, {})
        self.handle_input.setText(profile.get("handle", ""))
        self.tags_list.clearSelection()
        for tag in profile.get("tags", []):
            for i in range(self.tags_list.count()):
                if self.tags_list.item(i).text() == tag:
                    self.tags_list.item(i).setSelected(True)
        self.min_rating_input.setValue(profile.get("min_rating", 800))
        self.max_rating_input.setValue(profile.get("max_rating", 3500))
        self.exclude_solved.setChecked(profile.get("exclude_solved", False))

    def clear_cache(self):
        self.session.cache.clear()
        QMessageBox.information(self, "Success", "Cache cleared successfully.")

    def sort_table(self, column):
        if self.sort_column == column:
            self.sort_order = (
                Qt.DescendingOrder
                if self.sort_order == Qt.AscendingOrder
                else Qt.AscendingOrder
            )
        else:
            self.sort_column = column
            self.sort_order = Qt.AscendingOrder
        self.results_table.sortItems(column, self.sort_order)

    def update_copy_button_state(self):
        selected_rows = self.results_table.selectionModel().selectedRows()
        self.copy_link_button.setEnabled(len(selected_rows) == 1)

    def copy_link(self):
        selected_rows = self.results_table.selectionModel().selectedRows()
        if len(selected_rows) != 1:
            QMessageBox.critical(
                self, "Error", "Please select exactly one row to copy the link."
            )
            return
        row = selected_rows[0].row()
        link_item = self.results_table.item(row, 1)
        if link_item:
            QApplication.clipboard().setText(link_item.text())
            QMessageBox.information(self, "Success", "Link copied to clipboard.")
        else:
            QMessageBox.critical(self, "Error", "No link found in the selected row.")

    def filter_problems(self):
        # Validate handle
        handle = self.handle_input.text()
        valid, message = validate_handle(handle, self.session)
        if not valid:
            QMessageBox.critical(self, "Error", message)
            return

        # Validate tags
        tags = [item.text() for item in self.tags_list.selectedItems()]
        if not tags:
            QMessageBox.critical(self, "Error", "You must select at least one tag")
            return

        # Validate ratings
        min_rating = self.min_rating_input.value()
        max_rating = self.max_rating_input.value()
        valid, result = validate_rating(min_rating, max_rating)
        if not valid:
            QMessageBox.critical(self, "Error", result)
            return
        min_rating, max_rating = result

        # Get exclude solved
        exclude_solved = self.exclude_solved.isChecked()

        # Fetch data
        self.statusBar().showMessage("Fetching solved problems...")
        solved_set = get_solved_problems(handle, self.session)
        problems = get_problemset(self.session)

        if not problems:
            QMessageBox.critical(self, "Error", "No problems fetched from Codeforces.")
            self.session.close()
            return

        # Filter problems
        self.filtered_problems = filter_problems(
            problems, tags, min_rating, max_rating, solved_set, exclude_solved
        )
        self.tags = tags

        # Update table
        self.results_table.setRowCount(len(self.filtered_problems))
        for row, problem in enumerate(self.filtered_problems):
            self.results_table.setItem(row, 0, QTableWidgetItem(problem["Name"]))
            self.results_table.setItem(row, 1, QTableWidgetItem(problem["Link"]))
            self.results_table.setItem(row, 2, QTableWidgetItem(str(problem["Rating"])))
            self.results_table.setItem(row, 3, QTableWidgetItem(problem["Status"]))

        self.statusBar().showMessage(
            f"Found {len(self.filtered_problems)} problems matching the criteria."
        )
        self.save_button.setEnabled(bool(self.filtered_problems))
        self.update_copy_button_state()

    def save_results(self):
        if self.filtered_problems:
            save_problems(self.filtered_problems, self.tags)
            QMessageBox.information(
                self, "Success", "Results saved to JSON and CSV files."
            )
        else:
            QMessageBox.critical(self, "Error", "No problems to save.")

    def closeEvent(self, event):
        self.session.close()
        event.accept()
