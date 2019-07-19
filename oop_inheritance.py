class Person:
    def __init__(self, give_name):
        self.name = give_name

    def greeting(self):
        return f"Hi my name is {self.name}"

class Student(Person):
    def learn(self):
        return "I get it!"

class Instructor(Person):
    def teach(self):
        return "An object is an instance of a class"

nadia = Instructor("Nadia")
print(nadia.greeting())

chris = Student("Chris")
print(chris.greeting())

print(nadia.teach())
print(chris.learn())

# This will not work because the learn function only pertains to the student class but not the instructor class and vice versa.
# It is not a inherited function between the two
print(nadia.learn())
print(chris.teach())