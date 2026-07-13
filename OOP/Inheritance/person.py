class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def showPerson(self):
        print(f"name is {self.name},Age is {self.age}")

class Student(Person):
            def __init(self,student_id):
               super().__init__(name,age)
               self.student_id=student_id
            def showInfo(self):
             print(f"student id is {student_id}")

name=input("enter name ")
age=int(input("enter age"))
student_id=int(input("Enter student id "))
s=Student(name,age)
s.showPerson()
s.showInfo()



