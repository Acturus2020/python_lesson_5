import os
from peewee import Model, ForeignKeyField, ManyToManyField, SqliteDatabase, CharField, IntegerField
db = database = SqliteDatabase('cafedra_journal.db')


class BaseModel(Model):
    class Meta:
        database = db


class Student(BaseModel):
    name = CharField()
    age = IntegerField()


class Course(BaseModel):
    name = CharField()
    number = IntegerField()
    students = ManyToManyField(Student, backref='courses')


class Teacher(BaseModel):
    name = CharField()
    discipline = CharField()
    course = ForeignKeyField(Course, backref='teachers')


def setup():
    Course.create_table()
    Teacher.create_table()
    Student.create_table()
    StudentCourse = Student.courses.get_through_model()
    StudentCourse.create_table()


def main():
    setup()
    print('---Cafedra-Journal---')
    base_commands = [' 1 - Add Teacher', ' 2 - Add Student', '3 - Add Course', ' 4 - Show Students', '5 - Show Teachers', '6 - Show course', ' 7 - Complete course', ' 9 - Exit']
    while True:
        os.system('clear')
        for command in base_commands:
            print('Please write number:', command)
        user_command = int(input())
        if user_command == 1:
            print('=====Add Teacher=====')
            name = input('Please write name: ')
            discipline = input('Please write discipline: ')
            course = input('Write course:')
            Teacher.create(name=name, discipline=discipline, course=course)
        if user_command == 2:
            print('=====Add Student=====')
            name = input('Please write name: ')
            age = input('Please write age: ')
            Student.create(name=name, age=age)
        if user_command == 3:
            print('=====Create course=====')
            name = input('Please write name of course: ')
            number = input('Number of course:')
            course = Course.create(name=name, number=number)
            students = Student.select()
            for student in students:
                print('{0} Student: {1}'.format(student.id, student.name))
            print('0 - Continue create course!')
            while True:
                student_id = int(input('Please select student: '))
                if student_id == 0:
                    break
                student = Student.get(id=student_id)
                course.students.add(student)
                print('Student {} added to course.'.format(student.name))
            print('Created course id: ', course.id)
            for student in course.students:
                print('Student: ', student.name, student.age)
            input('Continue')
        if user_command == 4:
            print('=====Show students=====')
            students = Student.select()
            for student in students:
                print('Student N {}, {}, age={}'.format(student.id, student.name, student.age))
            input('Continue')
        if user_command == 5:
            print('=====Show teachers=====')
            teachers = Teacher.select()
            for teacher in teachers:
                print('Teacher: ', teacher.name, teacher.discipline)
            input('Continue')
        if user_command == 6:
            print('=====Show courses=====')
            courses = Course.select()
            for course in courses:
                print('Course N {}, {}, {}'.format(course.id, course.name, course.number))
                for student in course.students:
                    print('Students in ithis course: ', student.name)
                print('\n')
            input('Continue')
        if user_command == 9:
            break


if __name__ == '__main__':
    main()
