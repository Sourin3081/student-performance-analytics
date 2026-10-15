import os
import numpy as np
import pandas as pd

def create_default_csv_if_missing(file_path):
    """Automatically creates the student dataset if it doesn't exist."""
    if not os.path.exists(file_path):
        csv_data = """StudentID,Name,Department,Math,Science,English,Attendance
101,Aarav Sharma,Computer Science,85,90,78,92
102,Ananya Roy,Electronics,72,65,80,85
103,Rohan Das,Mechanical,60,55,50,70
104,Priya Sen,Computer Science,95,92,88,96
105,Vikram Ghosh,Civil,45,50,60,65
106,Neha Mukherjee,Electronics,80,82,75,88
107,Arjun Chatterjee,Computer Science,88,85,90,91
108,Sneha Paul,Mechanical,70,75,72,80
109,Rahul Banerjee,Civil,55,60,58,72
110,Puja Sarkar,Electronics,91,89,94,95
111,Abhishek Dey,Computer Science,78,74,80,82
112,Megha Ghosh,Civil,65,68,70,78
113,Subham Roy,Mechanical,82,80,85,89
114,Tanaya Bose,Electronics,48,52,55,60
115,Kunal Sen,Computer Science,90,94,92,97
116,Rimi Dutta,Civil,75,72,70,84
"""
        with open(file_path, "w") as f:
            f.write(csv_data)

def calculate_totals_and_averages(df):
    """Calculates total and average marks for each student using NumPy[cite: 1, 2]."""
    marks_columns = ['Math', 'Science', 'English']
    marks_matrix = df[marks_columns].values
    
    df['Total_Marks'] = np.sum(marks_matrix, axis=1)
    df['Average_Marks'] = np.mean(marks_matrix, axis=1)
    return df

def assign_grade(avg):
    """Assigns letter grades based on average marks[cite: 1, 2]."""
    if avg >= 85:
        return 'A'
    elif avg >= 70:
        return 'B'
    elif avg >= 50:
        return 'C'
    else:
        return 'F'

def process_student_performance(df):
    """Processes grades and pass/fail statuses[cite: 1, 2]."""
    df['Grade'] = df['Average_Marks'].apply(assign_grade)
    # Pass condition: Average marks >= 50 and Attendance >= 75
    df['Status'] = np.where((df['Average_Marks'] >= 50) & (df['Attendance'] >= 75), 'Pass', 'Fail')
    return df

def get_summary_statistics(df):
    """Computes overall statistics using NumPy and Pandas[cite: 1, 2]."""
    summary = {
        "highest_avg": df['Average_Marks'].max(),
        "lowest_avg": df['Average_Marks'].min(),
        "class_avg": df['Average_Marks'].mean(),
        "total_students": len(df),
        "passed_students": (df['Status'] == 'Pass').sum(),
        "failed_students": (df['Status'] == 'Fail').sum()
    }
    return summary

def get_subject_averages(df):
    """Calculates subject-wise performance analysis[cite: 1, 2]."""
    marks_columns = ['Math', 'Science', 'English']
    return df[marks_columns].mean()

def get_top_performers(df, n=3):
    """Identifies top-performing students based on average marks[cite: 1, 2]."""
    return df.nlargest(n, 'Average_Marks')[['StudentID', 'Name', 'Department', 'Average_Marks', 'Grade']]

def main():
    file_path = "students.csv"
    
    # Ensure dataset is present
    create_default_csv_if_missing(file_path)
    
    print("=" * 60)
    print("         STUDENT PERFORMANCE ANALYTICS SYSTEM         ")
    print("=" * 60)
    
    # Step 1: Load Data using Pandas[cite: 1, 2]
    try:
        df = pd.read_csv(file_path)
        print(f"\n[INFO] Successfully loaded {len(df)} student records from '{file_path}'.\n")
    except Exception as e:
        print(f"[ERROR] Could not load data: {e}")
        return

    # Step 2: Process Data using NumPy & Pandas[cite: 1, 2]
    df = calculate_totals_and_averages(df)
    df = process_student_performance(df)
    
    print("--- Snapshot of Processed Student Data ---")
    print(df[['StudentID', 'Name', 'Total_Marks', 'Average_Marks', 'Grade', 'Status']].head(), "\n")
    
    # Step 3: Analytics & Summary[cite: 1, 2]
    summary = get_summary_statistics(df)
    subject_avg = get_subject_averages(df)
    top_students = get_top_performers(df, n=3)
    
    print("=" * 60)
    print("                  PERFORMANCE SUMMARY                 ")
    print("=" * 60)
    print(f"Total Students        : {summary['total_students']}")
    print(f"Students Passed       : {summary['passed_students']}")
    print(f"Students Failed       : {summary['failed_students']}")
    print(f"Overall Class Average : {summary['class_avg']:.2f}")
    print(f"Highest Average Marks : {summary['highest_avg']:.2f}")
    print(f"Lowest Average Marks  : {summary['lowest_avg']:.2f}")
    
    print("\n--- Subject-wise Average Performance ---")
    for subject, avg in subject_avg.items():
        print(f"{subject:10s} : {avg:.2f}")
        
    print("\n--- Top 3 Performing Students ---")
    print(top_students.to_string(index=False))
    print("=" * 60)

if __name__ == "__main__":
    main()