class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def display_info(self):
        print(f"Name:{self.name}, Age:{self.age}")

class student(Person):
    def __init__(self, name, age, student_id, course):
        super().__init__(name, age)
        self.student_id = student_id
        self.course = course
    def display_info(self):
        super().display_info()
        print(f"Student Id: {self.student_id}, Course: {self.course}") 

class teacher(Person):
    def __init__(self, name, age, subject, salary):
        super().__init__(name, age,)
        self.subject = subject
        self.salary = salary

    def display_info(self):
        super().display_info()
        print(f"SUBJECT: {self.subject}, SALARY: {self.salary}")
Student1 = student("Martin Mbungu", 34, "DHR094", "Health Records& IT")
print(Student1.name)
print(Student1.age)
print(Student1.student_id)
print(Student1.course)
Teacher1 = teacher("Pauline Waithera", 45, "Health Information System", 76000) 
print(Teacher1.name)
print(Teacher1.age)
print(Teacher1.subject)
print(Teacher1.salary)        

