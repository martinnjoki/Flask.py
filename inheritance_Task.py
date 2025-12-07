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
Student1.display_info()

Teacher1 = teacher("Pauline Waithera", 45, "Health Information System", 76000) 
Teacher1.display_info()

