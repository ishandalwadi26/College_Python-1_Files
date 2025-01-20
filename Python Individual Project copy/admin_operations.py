# admin_operations.py
from models import Student, Course, Faculty, Event

class AdminOperations:
    def __init__(self):
        self.student = Student()
        self.course = Course()
        self.faculty = Faculty()
        self.event = Event()

    def student_operations(self):
        while True:
            print("\nStudent Operations:")
            print("1. Add Student")
            print("2. View Student")
            print("3. Update Student")
            print("4. Delete Student")
            print("5. Back to Main Menu")

            choice = input("Enter your choice: ")

            if choice == '1':
                data = {
                    'Enroll_No': input("Enter Enrollment Number: "),
                    'Name': input("Enter Name: "),
                    'Dob': input("Enter Date of Birth (YYYY-MM-DD): "),
                    'Gender': input("Enter Gender: "),
                    'Address': input("Enter Address: "),
                    'Phone_No': input("Enter Phone Number: "),
                    'Email': input("Enter Email: "),
                    'Enroll_Year': int(input("Enter Enrollment Year: ")),
                    'Course': input("Enter Course: ")
                }
                self.student.create(data)
                print("Student added successfully!")

            elif choice == '2':
                enroll_no = int(input("Enter Enrollment Number: "))
                student_data = self.student.read(enroll_no)
                if student_data:
                    print(student_data)
                else:
                    print("Student not found!")

            elif choice == '3':
                data = {
                    'Enroll_No': input("Enter Enrollment Number: "),
                    'Name': input("Enter Name: "),
                    'Dob': input("Enter Date of Birth (YYYY-MM-DD): "),
                    'Gender': input("Enter Gender: "),
                    'Address': input("Enter Address: "),
                    'Phone_No': input("Enter Phone Number: "),
                    'Email': input("Enter Email: "),
                    'Enroll_Year': int(input("Enter Enrollment Year: ")),
                    'Course': input("Enter Course: ")
                }
                self.student.update(data)
                print("Student updated successfully!")

            elif choice == '4':
                enroll_no = input("Enter Enrollment Number: ")
                self.student.delete(enroll_no)
                print("Student deleted successfully!")

            elif choice == '5':
                break

            else:
                print("Invalid choice. Please try again.")

    def course_operations(self):
        while True:
            print("\nCourse Operations:")
            print("1. Add Course")
            print("2. View Course")
            print("3. Update Course")
            print("4. Delete Course")
            print("5. Back to Main Menu")

            choice = input("Enter your choice: ")

            if choice == '1':
                data = {
                    'Course_Name': input("Enter Course Name: "),
                    'Course_Duration': int(input("Enter Course Duration (in months): ")),
                    'Course_Fee': int(input("Enter Course Fee: ")),
                    'Dept_Name': input("Enter Department Name: "),
                    'HOD': input("Enter HOD Name: ")
                }
                self.course.create(data)
                print("Course added successfully!")

            elif choice == '2':
                course_id = int(input("Enter Course ID: "))
                course_data = self.course.read(course_id)
                if course_data:
                    print(course_data)
                else:
                    print("Course not found!")

            elif choice == '3':
                data = {
                    'Course_Id': int(input("Enter Course ID: ")),
                    'Course_Name': input("Enter Course Name: "),
                    'Course_Duration': int(input("Enter Course Duration (in months): ")),
                    'Course_Fee': int(input("Enter Course Fee: ")),
                    'Dept_Name': input("Enter Department Name: "),
                    'HOD': input("Enter HOD Name: ")
                }
                self.course.update(data)
                print("Course updated successfully!")

            elif choice == '4':
                course_id = int(input("Enter Course ID: "))
                self.course.delete(course_id)
                print("Course deleted successfully!")

            elif choice == '5':
                break

            else:
                print("Invalid choice. Please try again.")

    def faculty_operations(self):
        while True:
            print("\nFaculty Operations:")
            print("1. Add Faculty")
            print("2. View Faculty")
            print("3. Update Faculty")
            print("4. Delete Faculty")
            print("5. Back to Main Menu")

            choice = input("Enter your choice: ")

            if choice == '1':
                data = {
                    'Faculty_Name': input("Enter Faculty Name: "),
                    'Faculty_No': input("Enter Faculty Number: "),
                    'Course_Id': int(input("Enter Course ID: "))
                }
                self.faculty.create(data)
                print("Faculty added successfully!")

            elif choice == '2':
                faculty_id = int(input("Enter Faculty ID: "))
                faculty_data = self.faculty.read(faculty_id)
                if faculty_data:
                    print(faculty_data)
                else:
                    print("Faculty not found!")

            elif choice == '3':
                data = {
                    'Faculty_Id': int(input("Enter Faculty ID: ")),
                    'Faculty_Name': input("Enter Faculty Name: "),
                    'Faculty_No': input("Enter Faculty Number: "),
                    'Course_Id': int(input("Enter Course ID: "))
                }
                self.faculty.update(data)
                print("Faculty updated successfully!")

            elif choice == '4':
                faculty_id = int(input("Enter Faculty ID: "))
                self.faculty.delete(faculty_id)
                print("Faculty deleted successfully!")

            elif choice == '5':
                break

            else:
                print("Invalid choice. Please try again.")

    def event_operations(self):
        while True:
            print("\nEvent Operations:")
            print("1. Add Event")
            print("2. View Event")
            print("3. Update Event")
            print("4. Delete Event")
            print("5. Back to Main Menu")

            choice = input("Enter your choice: ")

            if choice == '1':
                data = {
                    'Event_Name': input("Enter Event Name: "),
                    'Event_Type': input("Enter Event Type: "),
                    'Event_Duration': int(input("Enter Event Duration (in hours): ")),
                    'Event_Date': input("Enter Event Date (YYYY-MM-DD): ")
                }
                self.event.create(data)
                print("Event added successfully!")

            elif choice == '2':
                event_id = int(input("Enter Event ID: "))
                event_data = self.event.read(event_id)
                if event_data:
                    print(event_data)
                else:
                    print("Event not found!")

            elif choice == '3':
                data = {
                    'Event_Id': int(input("Enter Event ID: ")),
                    'Event_Name': input("Enter Event Name: "),
                    'Event_Type': input("Enter Event Type: "),
                    'Event_Duration': int(input("Enter Event Duration (in hours): ")),
                    'Event_Date': input("Enter Event Date (YYYY-MM-DD): ")
                }
                self.event.update(data)
                print("Event updated successfully!")

            elif choice == '4':
                event_id = int(input("Enter Event ID: "))
                self.event.delete(event_id)
                print("Event deleted successfully!")

            elif choice == '5':
                break

            else:
                print("Invalid choice. Please try again.")