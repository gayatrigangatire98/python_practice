class parent:
    def show(self):
        print("parent self")

class child(parent):
    pass

c1=child()
c1.show()

class animal:
    def eat(self):
        print("animal is eating")

class dog (animal):
    pass
d1=dog()
d1.eat()

class person:
    def __init__(self , name ,age):
        self.name =  name
        self.age = age

class student (person):
    pass
s1=student("Gayatri" ,  23)
print(s1.name)
print(s1.age)
    

class employee:
    def __init__(self , name):
        self.name=name
    def display_name(self):
        print("Employee name is:", self.name)

class manager(employee):
    pass
m1=manager("Rahul")
m1.display_name()