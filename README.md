# Student Grade Manager

This project is a simple Python-based student grade management system created as part of the Day 2 GenAI learning task. It allows the user to add student records, calculate grades, and display the class summary with average, highest, and lowest marks.

## Project Overview

The application is implemented in `grade_manager.py` and provides a small console menu with the following options:

- Add a student name and mark
- View all student records
- Exit the application

Each student is assigned a grade based on the score range:

- 90 to 100 -> A
- 80 to 89 -> B
- 70 to 79 -> C
- 60 to 69 -> D
- Below 60 -> E

## Features

- Validates student names to avoid duplicates or blank entries
- Validates mark input to ensure it is between 0 and 100
- Automatically assigns a grade based on the mark
- Displays a summary table with:
  - Student name
  - Student mark
  - Grade
  - Average mark
  - Highest mark
  - Lowest mark

## File Structure

- `grade_manager.py` - Main application logic
- `README.md` - Project documentation
- `venv/` - Virtual environment (if created locally)

## How to Run

1. Open a terminal in the project directory.
2. Ensure Python is installed on your system.
3. Run the program using:

```bash
python grade_manager.py
```

## Example Workflow

- Choose option `1` to add a student
- Enter the student's name
- Enter their mark from `0` to `100`
- Choose option `2` to view all records and summary
- Choose option `3` to exit

## Notes

This is a beginner-friendly Python project intended to practice input validation, conditional logic, list handling, and basic console application development.
