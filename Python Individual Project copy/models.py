# models.py
from database import Database

class Student:
    def __init__(self):
        self.db = Database()

    def create(self, data):
        query = """INSERT INTO Student (Enroll_No, Name, Dob, Gender, Address, Phone_No, Email, Enroll_Year, Course) 
                   VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"""
        params = (data['Enroll_No'], data['Name'], data['Dob'], data['Gender'], data['Address'],
                  data['Phone_No'], data['Email'], data['Enroll_Year'], data['Course'])
        return self.db.execute_query(query, params)

    def read(self, enroll_no):
        query = "SELECT * FROM Student WHERE Enroll_No = %s"
        print(f"Running query: {query} with params: {enroll_no}")
        result = self.db.execute_query(query, (enroll_no,))
        if result:
            row = result.fetchone()
            return row if row else None
        return None

    def update(self, data):
        query = """UPDATE Student SET Name = %s, Dob = %s, Gender = %s, Address = %s, 
                   Phone_No = %s, Email = %s, Enroll_Year = %s, Course = %s 
                   WHERE Enroll_No = %s"""
        params = (data['Name'], data['Dob'], data['Gender'], data['Address'], data['Phone_No'],
                  data['Email'], data['Enroll_Year'], data['Course'], data['Enroll_No'])
        return self.db.execute_query(query, params)

    def delete(self, enroll_no):
        query = "DELETE FROM Student WHERE Enroll_No = %s"
        return self.db.execute_query(query, (enroll_no,))

class Course:
    def __init__(self):
        self.db = Database()

    def create(self, data):
        query = """INSERT INTO Courses (Course_Name, Course_Duration, Course_Fee, Dept_Name, HOD) 
                   VALUES (%s, %s, %s, %s, %s)"""
        params = (data['Course_Name'], data['Course_Duration'], data['Course_Fee'],
                  data['Dept_Name'], data['HOD'])
        return self.db.execute_query(query, params)

    def read(self, course_id):
        query = "SELECT * FROM Courses WHERE Course_Id = %s"
        result = self.db.execute_query(query, (course_id,))
        return result.fetchone() if result else None

    def update(self, data):
        query = """UPDATE Courses SET Course_Name = %s, Course_Duration = %s, Course_Fee = %s, 
                   Dept_Name = %s, HOD = %s WHERE Course_Id = %s"""
        params = (data['Course_Name'], data['Course_Duration'], data['Course_Fee'],
                  data['Dept_Name'], data['HOD'], data['Course_Id'])
        return self.db.execute_query(query, params)

    def delete(self, course_id):
        query = "DELETE FROM Courses WHERE Course_Id = %s"
        return self.db.execute_query(query, (course_id,))

class Faculty:
    def __init__(self):
        self.db = Database()

    def create(self, data):
        query = """INSERT INTO Faculty (Faculty_Name, Faculty_No, Course_Id) 
                   VALUES (%s, %s, %s)"""
        params = (data['Faculty_Name'], data['Faculty_No'], data['Course_Id'])
        return self.db.execute_query(query, params)

    def read(self, faculty_id):
        query = "SELECT * FROM Faculty WHERE Faculty_Id = %s"
        result = self.db.execute_query(query, (faculty_id,))
        return result.fetchone() if result else None

    def update(self, data):
        query = """UPDATE Faculty SET Faculty_Name = %s, Faculty_No = %s, Course_Id = %s 
                   WHERE Faculty_Id = %s"""
        params = (data['Faculty_Name'], data['Faculty_No'], data['Course_Id'], data['Faculty_Id'])
        return self.db.execute_query(query, params)

    def delete(self, faculty_id):
        query = "DELETE FROM Faculty WHERE Faculty_Id = %s"
        return self.db.execute_query(query, (faculty_id,))

class Event:
    def __init__(self):
        self.db = Database()

    def create(self, data):
        query = """INSERT INTO Events (Event_Name, Event_Type, Event_Duration, Event_Date) 
                   VALUES (%s, %s, %s, %s)"""
        params = (data['Event_Name'], data['Event_Type'], data['Event_Duration'], data['Event_Date'])
        return self.db.execute_query(query, params)

    def read(self, event_id):
        query = "SELECT * FROM Events WHERE Event_Id = %s"
        result = self.db.execute_query(query, (event_id,))
        return result.fetchone() if result else None

    def update(self, data):
        query = """UPDATE Events SET Event_Name = %s, Event_Type = %s, Event_Duration = %s, 
                   Event_Date = %s WHERE Event_Id = %s"""
        params = (data['Event_Name'], data['Event_Type'], data['Event_Duration'],
                  data['Event_Date'], data['Event_Id'])
        return self.db.execute_query(query, params)

    def delete(self, event_id):
        query = "DELETE FROM Events WHERE Event_Id = %s"
        return self.db.execute_query(query, (event_id,))