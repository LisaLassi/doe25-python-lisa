# CLASSES
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self): #Behöver inte kalla på just denna metod då denna string metod "letas" efter i klassen gällande print fuktionen pga string (str)
        return f"Name: {self.name} | Age: {self.age}"

    def greet(self, name_to_greet=None):
        if name_to_greet:
            print(f"Hello {name_to_greet}! My name is {self.name}, I'm {self.age} years old!")
        else:
            print(f"Hello! My name is {self.name}, I'm {self.age} years old!")

    def change_name(self, new_name):
        self.name = new_name

    def get_name(self):
        return self.name

p1 = Person("Lisa", 27)
p2 = Person("Ior", 22)
p3 = Person("Tove", 27)
p4 = Person("Patrik", 28)

p1.greet()
p2.greet("Helene")
p3.greet("Erik")
p4.greet()

'''
new_name = input(f"Set new name for {p1.name}: ")
p1.name = new_name
print("New name is", p1.name)
'''
#Better approach:
new_name = input(f"Set new name for {p1.get_name()}: ")
p1.change_name(new_name)
print("New name is", p1.get_name())

#Hur kan jag printa p1's namn?
print(p1)

print()
#---------------------------------------------------------------------------------------------------------
'''
class Car:
    def __init__(self, brand, speed=0): #Får vi ingen speed så sätts värdet till 0
        self.brand = brand
        self.speed = speed

    def __str__(self):
        return f"Brand: {self.brand} | Speed: {self.speed}" 

    def accelerate(self):
        self.speed += 10

    def brake (self):
        if (self.speed <= 0):
            return 0
        else:
            self.speed -= 10
            return self.speed
        
def change_speed(car_obj, should_accelerate):
    if should_accelerate:
        new_speed = car_obj.accelerate()
    else:
        if car_obj.speed <=0:
            new_speed = 0
            print("Car speed is already 0, can't brake.")
        else:
            new_speed = car_obj.brake()
            print(f"New speed for {car_obj.brand} is {new_speed}")
    print(new_speed) #se kod på github för att dessa ska funka

car1 = Car("Jeep", 150)
car2 = Car("Mercedes", 200)
car3 = Car("Volvo") 

car1.accelerate()
print(car1.speed)
car1.brake()
print(car1.speed)
car2.accelerate()
print(car2.speed)
car2.brake()
print(car2.speed)

print(car1)
print(car2)
print(car3)

print()
'''
#--------------------------------------------------------------------------------------------------------

class Student:
    def __init__(self, name, points):
        self.name = name
        self.points = points

    def add_points(self, x):
        self.points += x

    def has_passed(self):
        if self.points >=50:
            print(f"{self.name} has passed! {self.points}/50 points.")
            return True
        else:
            print(f"{self.name} has not passed, {self.points}/50 points.")
            return False

student1 = Student("Lisa", 40)
student2 = Student("Ior", 50)
student3 = Student("Tove", 20)

student1.has_passed()
student2.has_passed()
student3.has_passed()

print()

student1.add_points(10)
student1.has_passed()
student2.add_points(5)
student2.has_passed()
student3.add_points(30)
student3.has_passed()

print("-----------------------------------------------------")

#Another solution
class Student:
    def __init__(self, name, points):
        self.name = name
        self.points = points

    def add_points(self, x):
        self.points += x

    def has_passed(self):
        if self.points >=50:
            print(f"{self.name} has passed!")
            return True
        else:
            print(f"{self.name} has not passed")
            return False

student1 = Student("Lisa", 40)
student2 = Student("Ior", 50)
student3 = Student("Tove", 20)

student1.has_passed()
student2.has_passed()
student3.has_passed()

print()


