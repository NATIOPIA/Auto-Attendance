import json
from datetime import datetime

class Student:
    def __init__(self, name):
        self.name = name
        self.attendance = []

    def mark_attendance(self, date, present):
        self.attendance.append({"date": date, "present": present})

class AttendanceSystem:
    def __init__(self):
        self.students = {}

    def add_students(self, names):
        for name in names:
            name = name.strip()  # Remove any leading/trailing whitespace
            if name and name not in self.students:
                self.students[name] = Student(name)
                # Automatically mark attendance as Present when a student is added
                date = datetime.now().strftime("%Y-%m-%d")
                present = True  # Mark as present
                self.students[name].mark_attendance(date, present)
                print(f"Student {name} added. Attendance marked as Present.")
            elif name in self.students:
                print(f"Student {name} already exists.")

    def save_attendance(self, filename):
        with open(filename, 'w') as file:
            json_data = {name: student.attendance for name, student in self.students.items()}
            json.dump(json_data, file, indent=4)
            print(f"Attendance saved to {filename}.")

    def display_attendance(self):
        for name, student in self.students.items():
            print(f"\nAttendance for {name}:")
            for record in student.attendance:
                status = "Present" if record["present"] else "Absent"
                print(f"Date: {record['date']}, Status: {status}")

def main():
    attendance_system = AttendanceSystem()

    while True:
        print("\n1. Add Students")
        print("2. Save Attendance")
        print("3. Display Attendance")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            names_input = input("Enter student names separated by commas: ")
            names = names_input.split(',')
            attendance_system.add_students(names)
        elif choice == '2':
            filename = input("Enter filename to save attendance (e.g., attendance.json): ")
            attendance_system.save_attendance(filename)
        elif choice == '3':
            attendance_system.display_attendance()
        elif choice == '4':
            print("Exiting the system.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()