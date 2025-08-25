# student.py
# Student Data Management System (Basic Version)

students = []  # list to store student records

def add_student(name, roll, marks):
    """Add a new student"""
    student = {"name": name, "roll": roll, "marks": marks}
    students.append(student)

def view_students():
    """View all students"""
    for s in students:
        print(f"Name: {s['name']}, Roll: {s['roll']}, Marks: {s['marks']}")

def search_student(roll):
    """Search student by roll number"""
    for s in students:
        if s['roll'] == roll:
            return s
    return None

# ---- Demo (you can delete later) ----
add_student("Selva", 101, 90)
add_student("Lakshmi", 102, 85)

view_students()
print("Search Roll 101:", search_student(101))
