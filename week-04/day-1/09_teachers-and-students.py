# Teacher Student
#
# Create Student and Teacher classes
# Student
    # learn()
    # question(teacher) -> calls the teachers answer method
# Teacher
    # teach(student) -> calls the students learn method
    # answer()

class Teacher:

    def answer(self):
        print("new things to learn")

    def teach(self, student):
        print("Ulj le, eggyes")
        student.learn()


class Student:

    def learn(self):
        print("new stuff")

    def question(self, teacher):
        print("Milyen messsze van a Fold a Holdtol?")
        teacher.answer()


pisti = Student()
sensei = Teacher()

pisti.question(sensei)
