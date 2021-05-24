from peewee import Model, ForeignKeyField, ManyToManyField, SqliteDatabase, CharField, IntegerField, BooleanField, DecimalField
db = SqliteDatabase('cafedra_journal2.db')

class BaseModel(Model):
    class Meta:
        database = db

class Course(BaseModel):
    name = CharField()
    number = IntegerField()

class Teacher(BaseModel):
    name = CharField()
    course = ForeignKeyField(Course, backref='teachers')


def cafedra_test_data():
    db.create_tables([Course, Teacher])

    data_course = (
        ('math', 11),
        ('english', 22),
        ('physic', 5)
    )
    data_teacher = (
        ('Christopher Nolan'),
        ('Ketty Perry'),
        ('Jesus')
    )
    for coursname, coursnumber in data_course:
        course = Course.create(name=coursname, number=coursnumber)
        for name in data_teacher:
            Teacher.create(course=course, name=name)

def main():
    cafedra_test_data()

if __name__ == '__main__':
    main()