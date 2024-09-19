class Person:
    def __init__(self,name:str,age:int):
        self.__name:str=name
        self.__age:int=age
    def displayInfo(self):
        return f"Name:{self.__name}, Age:{self.__age}"
#displayInfo in the Student and Teacher,override the displayInfo in the Person
class Student(Person):
    def __init__(self, name, age, studentId):
        super().__init__(name, age)
        self.studentId = studentId     
    def displayInfo(self):
        return f"StudentID:{self.studentId},{super().displayInfo()}"
        #super() call Person's displayInfo
        
class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age) 
        self.subject = subject
    def displayInfo(self):
        return f"{super().displayInfo()}, Subject:{self.subject}"
    #super() call Person's displayInfo

if __name__ == "__main__":
    student = Student(name="Tony", age=43, studentId="S1983")
    teacher = Teacher(name="Elvira", age=25, subject="Chemistry")

    print(student.displayInfo())
    print(teacher.displayInfo())  