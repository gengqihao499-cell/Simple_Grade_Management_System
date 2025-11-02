# -*- coding: utf-8 -*-
# Student Grade Management System
# Author: ChatGPT Example

import os
import time

# ==================== Student Class ====================
class Student:
    def __init__(self, sid, name, score, subject):
        self.sid = sid
        self.name = name
        self.score = float(score)
        self.subject = subject

    def __str__(self):
        return f"{self.sid},{self.name},{self.subject},{self.score}"

# ==================== Manager Class ====================
class StudentManager:
    def __init__(self, filename='students.txt'):
        self.filename = filename
        self.students = []
        self.load_data()

    # ---------- Load data from file ----------
    def load_data(self):
        if not os.path.exists(self.filename):
            print(f"⚠️ File {self.filename} not found. Creating a new one...")
            open(self.filename, 'w').close()
        try:
            with open(self.filename, 'r', encoding='utf-8') as f:
                for line in f:
                    line = line.strip()
                    if line:
                        sid, name, subject, score = line.split(',')
                        self.students.append(Student(sid, name, score, subject))
            print(f"✅ Loaded {len(self.students)} student record(s).")
        except Exception as e:
            print(f"❌ Error reading file: {e}")

    # ---------- Save data to file ----------
    def save_data(self):
        try:
            with open(self.filename, 'w', encoding='utf-8') as f:
                for stu in self.students:
                    f.write(str(stu) + '\n')
            print("✅ All data saved successfully.")
        except Exception as e:
            print(f"❌ Error saving file: {e}")

    # ---------- Add a new student ----------
    def add_student(self):
        sid = input("Enter Student ID: ").strip()
        if self.find_student_by_id(sid):
            print("❌ Student ID already exists.")
            return
        name = input("Enter Name: ").strip()
        subject = input("Enter Subject: ").strip()
        try:
            score = float(input("Enter Score: ").strip())
        except ValueError:
            print("❌ Score must be a number.")
            return

        self.students.append(Student(sid, name, score, subject))
        print(f"✅ Student {name} added successfully.")

    # ---------- Display all students ----------
    def show_all(self):
        if not self.students:
            print("No student data available.")
            return
        print("\n=== Student List ===")
        print("{:<10} {:<15} {:<15} {:<10}".format("ID", "Name", "Subject", "Score"))
        print("-" * 50)
        for stu in self.students:
            print("{:<10} {:<15} {:<15} {:<10}".format(stu.sid, stu.name, stu.subject, stu.score))
        print("=" * 50 + "\n")

    # ---------- Search student ----------
    def search_student(self):
        keyword = input("Enter Student ID or Name to search: ").strip()
        found = [stu for stu in self.students if keyword.lower() in stu.sid.lower() or keyword.lower() in stu.name.lower()]
        if not found:
            print("No matching student found.")
        else:
            print(f"\nFound {len(found)} record(s):")
            for stu in found:
                print(f"ID: {stu.sid} | Name: {stu.name} | Subject: {stu.subject} | Score: {stu.score}")

    # ---------- Modify score ----------
    def modify_score(self):
        sid = input("Enter Student ID to modify: ").strip()
        stu = self.find_student_by_id(sid)
        if not stu:
            print("Student not found.")
            return
        try:
            new_score = float(input(f"Enter new score for {stu.name}: ").strip())
            stu.score = new_score
            print(f"✅ Updated score for {stu.name} to {new_score}.")
        except ValueError:
            print("Invalid input. Score must be a number.")

    # ---------- Delete student ----------
    def delete_student(self):
        sid = input("Enter Student ID to delete: ").strip()
        stu = self.find_student_by_id(sid)
        if not stu:
            print("Student not found.")
            return
        confirm = input(f"Are you sure you want to delete {stu.name}? (y/n): ").lower()
        if confirm == 'y':
            self.students.remove(stu)
            print(f"✅ Student {stu.name} deleted successfully.")
        else:
            print("Operation cancelled.")

    # ---------- Sort by score ----------
    def sort_students(self):
        if not self.students:
            print("No data to sort.")
            return
        print("1. Sort by Score Ascending")
        print("2. Sort by Score Descending")
        choice = input("Choose option (1/2): ").strip()
        reverse = True if choice == '2' else False
        self.students.sort(key=lambda s: s.score, reverse=reverse)
        print("✅ Students sorted successfully.")
        self.show_all()

    # ---------- Calculate statistics ----------
    def show_statistics(self):
        if not self.students:
            print("No data to analyze.")
            return
        scores = [stu.score for stu in self.students]
        avg = sum(scores) / len(scores)
        max_score = max(scores)
        min_score = min(scores)
        print("\n=== Score Statistics ===")
        print(f"Total Students: {len(scores)}")
        print(f"Average Score: {avg:.2f}")
        print(f"Highest Score: {max_score}")
        print(f"Lowest Score: {min_score}")
        print("=========================\n")

    # ---------- Export report ----------
    def export_report(self):
        filename = input("Enter report file name (default: report.txt): ").strip()
        if filename == "":
            filename = "report.txt"
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write("=== Student Report ===\n")
                f.write("{:<10} {:<15} {:<15} {:<10}\n".format("ID", "Name", "Subject", "Score"))
                f.write("-" * 50 + "\n")
                for stu in self.students:
                    f.write("{:<10} {:<15} {:<15} {:<10}\n".format(stu.sid, stu.name, stu.subject, stu.score))
                f.write("-" * 50 + "\n")
            print(f"✅ Report exported successfully to {filename}")
        except Exception as e:
            print(f"❌ Error exporting report: {e}")

    # ---------- Find by ID ----------
    def find_student_by_id(self, sid):
        for stu in self.students:
            if stu.sid == sid:
                return stu
        return None

    # ---------- Pause for readability ----------
    def pause(self):
        input("\nPress Enter to continue...")

# ==================== Main Program ====================
def main():
    manager = StudentManager()

    while True:
        print("""
========= Student Grade Management System =========
1. Show all students
2. Add a new student
3. Modify student score
4. Delete student
5. Search student
6. Sort students by score
7. View statistics
8. Export report
9. Save and Exit
===================================================
""")
        choice = input("Enter your choice (1-9): ").strip()

        if choice == '1':
            manager.show_all()
        elif choice == '2':
            manager.add_student()
        elif choice == '3':
            manager.modify_score()
        elif choice == '4':
            manager.delete_student()
        elif choice == '5':
            manager.search_student()
        elif choice == '6':
            manager.sort_students()
        elif choice == '7':
            manager.show_statistics()
        elif choice == '8':
            manager.export_report()
        elif choice == '9':
            manager.save_data()
            print("💾 Exiting system... Goodbye!")
            time.sleep(1)
            break
        else:
            print("❌ Invalid choice, please try again.")
        manager.pause()

if __name__ == "__main__":
    main()
