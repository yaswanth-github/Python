import os.path
from datetime import datetime

def mark_attendance(class_name, student_name):
    date = datetime.today().strftime('%Y-%m-%d')
    filename = f"{class_name}_{date}.txt"
    if not os.path.exists(filename):
        with open(filename, 'w') as f:
            f.write("Student Name,Present/Absent\n")
    with open(filename, 'a') as f:
        f.write(f"{student_name},Present\n")

def get_attendance(class_name, date):
    filename = f"{class_name}_{date}.txt"
    if not os.path.exists(filename):
        return "No attendance records found"
    with open(filename, 'r') as f:
        return f.read()

# Example usage:
mark_attendance("Maths", "John Doe")
mark_attendance("Maths", "Jane Smith")
mark_attendance("Science", "John Doe")
mark_attendance("Science", "Bob Johnson")

print(get_attendance("Maths", "2023-05-03"))
print(get_attendance("Science", "2023-05-03"))
