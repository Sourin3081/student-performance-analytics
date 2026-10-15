# Student Performance Analytics System

## 1. Project Title
* **Project Name:** Student Performance Analytics System[cite: 1]
* **Developer:** Sourin Kar

## 2. Objective
The objective of this project is to build a Python-based data analysis tool that reads student records, processes marks and attendance using NumPy and Pandas, and generates meaningful academic metrics such as individual averages, grades, pass/fail status, subject-wise trends, and top performers[cite: 1].

## 3. Technologies Used
* **Python**[cite: 1]
* **NumPy** (for efficient numerical matrix operations and calculations)[cite: 1, 2]
* **Pandas** (for tabular data loading, manipulation, and summary statistics)[cite: 1, 2]

## 4. Dataset Description
* **File Name:** `students.csv`[cite: 2]
* **Records:** 16 student rows
* **Key Fields:** `StudentID`, `Name`, `Department`, `Math`, `Science`, `English`, `Attendance`[cite: 1, 2]

## 5. Implementation Steps
1. **Data Loading:** Read student records using Pandas DataFrames[cite: 2].
2. **Numerical Processing:** Leveraged NumPy to compute total marks and average scores across subjects[cite: 1, 2].
3. **Logic & Grading:** Implemented custom rules and conditions using loops and conditional functions to assign letter grades ('A', 'B', 'C', 'F') and Pass/Fail statuses[cite: 2].
4. **Analytics Extraction:** Answered key performance queries such as class averages, subject performance, and top student rankings[cite: 2].

## 6. Key Features
* Automated total and average calculation via NumPy arrays[cite: 1, 2].
* Dynamic letter-grade assignment and attendance/marks-based pass/fail filtering[cite: 2].
* Subject-wise performance breakdown[cite: 1, 2].
* Identification of top-performing students[cite: 1, 2].

## 7. Final Outcome
The system successfully processes raw CSV datasets, executes backend computations smoothly, and outputs a clean, structured summary of student performance without requiring manual calculation[cite: 1, 2].

## 8. Challenges & Learnings
* **Challenge:** Handling multi-column mathematical operations cleanly.
* **Solution:** Used NumPy's axis-based summation and mean calculations to simplify matrix operations.
* **Learning:** Gained hands-on experience structuring data projects into modular files (`main.py` and `functions.py`) for better readability and maintainability[cite: 2].
