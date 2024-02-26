class Student:
    def __init__(self, id, name, age):
        self.id = id
        self.name = name
        self.age = age

    def __str__(self):
        return f"Student(id={self.id}, name='{self.name}', age={self.age})"

class StudentDatabase:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)
        print("Student added successfully!")

    def display_students(self):
        if not self.students:
            print("No students in the database.")
        else:
            print("Student Database:")
            for student in self.students:
                print(student)

    def find_student_by_id(self, id):
        for student in self.students:
            if student.id == id:
                return student
        return None

    def update_student(self, updated_student):
        for i, student in enumerate(self.students):
            if student.id == updated_student.id:
                self.students[i] = updated_student
                print("Student updated successfully!")
                return
        print("Student not found.")

    def delete_student(self, id):
        student = self.find_student_by_id(id)
        if student:
            self.students.remove(student)
            print("Student deleted successfully!")
        else:
            print("Student not found.")

if __name__ == "__main__":
    import sys
    import re

    def input_integer(prompt):
        while True:
            try:
                num = int(input(prompt))
                return num
            except ValueError:
                print("Invalid input. Please enter an integer.")

    def input_string(prompt):
        while True:
            user_input = input(prompt)
            if re.match(r'^[a-zA-Z\s]+$', user_input):
                return user_input
            else:
                print("Invalid input. Please enter a valid name.")

    database = StudentDatabase()

    while True:
        print("\nCRUD Application Menu:")
        print("1. Add Student")
        print("2. Display Students")
        print("3. Find Student by ID")
        print("4. Update Student")
        print("5. Delete Student")
        print("0. Exit")
        choice = input_integer("Enter your choice: ")

        if choice == 1:
            id = input_integer("Enter student ID: ")
            name = input_string("Enter student name: ")
            age = input_integer("Enter student age: ")
            student = Student(id, name, age)
            database.add_student(student)
        elif choice == 2:
            database.display_students()
        elif choice == 3:
            id = input_integer("Enter student ID: ")
            found_student = database.find_student_by_id(id)
            if found_student:
                print("Student found:", found_student)
            else:
                print("Student not found.")
        elif choice == 4:
            id = input_integer("Enter student ID to update: ")
            found_student = database.find_student_by_id(id)
            if found_student:
                name = input_string("Enter updated student name: ")
                age = input_integer("Enter updated student age: ")
                updated_student = Student(id, name, age)
                database.update_student(updated_student)
            else:
                print("Student not found.")
        elif choice == 5:
            id = input_integer("Enter student ID to delete: ")
            database.delete_student(id)
        elif choice == 0:
            sys.exit(0)
        else:
            print("Invalid choice.")
