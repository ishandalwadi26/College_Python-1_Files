# main.py
from admin_operations import AdminOperations
from performance_report import PerformanceReport

def main():
    admin_ops = AdminOperations()
    performance_report = PerformanceReport()

    while True:
        print("\nCollege Management System - Admin Panel")
        print("1. Student Operations")
        print("2. Course Operations")
        print("3. Faculty Operations")
        print("4. Event Operations")
        print("5. Generate Overall Performance Report")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            admin_ops.student_operations()
        elif choice == '2':
            admin_ops.course_operations()
        elif choice == '3':
            admin_ops.faculty_operations()
        elif choice == '4':
            admin_ops.event_operations()
        elif choice == '5':
            data = performance_report.get_overall_performance()
            performance_report.visualize_performance(data)
        elif choice == '6':
            print("Thank you for using the College Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()