class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)


s1 = Student("Gayatri", 22)
s1.display()



class employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    def display(self):
        print("name:", self.name)
        print("salary:", self.salary)

emp1= employee("Sanvi", 13000)
emp1.display()
