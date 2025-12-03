class Animal:
    def __init__(self, name):
        self.name = name
    def speak(self):
        return "General Sound" 
    
class Dog(Animal):
    def speak(self):
        return "Barks" 
dog1 = Dog("Max")    
