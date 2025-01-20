# performance_report.py
import matplotlib.pyplot as plt
from database import Database

class PerformanceReport:
    def __init__(self):
        self.db = Database()

    def get_overall_performance(self):
        query = """
        SELECT s.Name, AVG(m.SPI) as AverageSPI 
        FROM Student s 
        JOIN Marks m ON s.Enroll_No = m.Enroll_No
        GROUP BY s.Enroll_No
        """
        result = self.db.execute_query(query)
        return result.fetchall() if result else None

    def visualize_performance(self, data):
        if not data:
            print("No performance data available.")
            return

        names = [student['Name'] for student in data]
        spis = [float(student['AverageSPI']) for student in data]

        plt.figure(figsize=(12, 6))
        plt.bar(names, spis)
        plt.title('Overall Student Performance')
        plt.xlabel('Student Names')
        plt.ylabel('Average SPI')
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        plt.savefig('performance_report.png')
        plt.close()
        print("Performance report generated and saved as 'performance_report.png'")
