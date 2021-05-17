# Mateush Vilen Serializer lesson

import sqlite3


class StudentDatabaseMixin:
    @staticmethod
    def __run_sql_command(command):
        conn = sqlite3.connect("db_for_serializer_pizzeria.db")
        cursor = conn.cursor()
        cursor.execute(command)
        conn.close()

    def update_student_first_name(self, first_name):
        command = "UPDATE STUDENTS SET FIRST_NAME = '{0}' WHERE ID = {1};".format(first_name, self.id)
        Student.__run_sql_command(command)
        self.first_name = first_name

    @staticmethod
    def get_students_from_database():
        conn = sqlite3.connect("db_for_serializer_pizzeria.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM students")
        raw_students = cursor.fetchall()
        conn.close()
        students = []
        for raw in raw_students:
            student = Student(*raw)
            students.append(student)
        return students

    @staticmethod
    def create_table():
        pass

    @staticmethod
    def add_student_to_database():
        pass


class Student(StudentDatabaseMixin):
    id = None
    first_name = ''
    last_name = ''
    address = ''

    def __init__(self, id, first_name, last_name, address):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.address = address

    def __getattr__(self, attr):
        return self.first_name.upper()

    @property
    def full_name(self):
        return '{} {}'.format(self.first_name, self.last_name)

    def __str__(self):
        return 'Student: {}'.format(self.full_name)

    @staticmethod
    def get_fields():
        return ['id', 'first_name', 'last_name', 'address']


students = Student.get_students_from_database()
print(students.aroofoor)
for student in students:
    updated_first_name = student.first_name + " UPDATED"
    # student.update_student_first_name(updated_first_name)
    print(student.full_name)
