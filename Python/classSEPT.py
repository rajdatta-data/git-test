# class Bank:
#     name="SBI"     #class attribute
#     def __init__(self,role,EMP):
#         self.role=role       #instance attributes
#         self.EMP=EMP         #instance attributes
# emp1=Bank("Manager",1275)
# print(emp1.name)
# print(emp1.role)
# print(emp1.EMP)

# class Person:

#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
# p1=Person("Vinit",23)
# print(p1.name)
# print(p1.age)

# class car:
#     def __init__(self,make,model):
#         self.make=make
#         self.model=model
        
#     def displayinfo(self):
#         return f"Make:{self.make} and Model:{self.model}"


# c1=car("Tata","Punch")
# c2=car("BMW","SUV")
# print(c1.make,c1.model)
# print(c2.displayinfo())

# class Book:
#     def __init__(self,title="Unknown",author="Unknown"):
#         self.title=title
#         self.author=author
# book1=Book()
# print(book1.title)
# print(book1.author)
    
# class Book:
#     def __init__(self,title="Unknown",author="Unknown"):
#         self.title=title
#         self.author=author
# book1=Book("wing of fire","APJ Abdul kalam")
# print(book1.title)
# print(book1.author)


# class rect:
#     def __init__(self,len,wid):
#         self.len=len
#         self.wid=wid
#     def area(self):
#         return self.len*self.wid
# r=rect(12,5)
# print(r.area())

'''3. Write a Python program that defines a class Person with a constructor that 
initializes role and salary. Instantiate an object and print the values of role and 
salary.'''
# class Person:
#     def __init__(self,role,salary):
#         self.role=role
#         self.salary=salary
# p=Person("Manager",120000)
# print(p.role)
# print(p.salary)
 

'''4. Write a Python class Book with a default constructor. If no arguments are 
provided, set title and author to default values ("Unknown" and "Unknown").'''
# class Book:
#     def __init__(self,title="Unknown",author="Unknown"):
#         self.title=title
#         self.author=author
# b=Book("Wings of Fire","APJ Abdul Kalam")
# print(b.title)
# print(b.author)


'''5. Write a Python program that creates a Rectangle class with a constructor that 
takes width and height as arguments. The constructor should initialize these 
attributes and calculate the area.'''
# class Rectangle:
#     def __init__(self,l,b):
#         self.l=l
#         self.b=b
#     def area(self):
#         return f"The length of rectangle is {self.l} and breadth is {self.b} and area is {self.l*self.b}"
# rect=Rectangle(10,5)
# print(rect.area())


'''6. Define a simple Person class with a destructor _del_(). Print a message 
when an object of the Person class is deleted. '''
class Person:
    def __init__(self,name):
        self.name=name
        print(f"{self.name} is created")
    def __del__(self):
        print (f"{self.name} is deleted")
p=Person("Sujal")  
print(p.name)
del p 


'''7. Write a Python program that defines a Car class with two constructors: one 
for setting make and model, and another for setting make, model, and year.'''
# class car:
#     def __init__(self,make,model,year=None):
#         self.make=make
#         self.model=model
#         self.year=year
#     def display(self):
#         if self.year:
#             return f"The make is {self.make} and model is {self.model} and year is {self.year}"
#         else:
#             return f"The make is {self.make} and model is {self.model}"
# c=car("tata","punch",2022)
# print(c.display())
# d=car("BMW","x5")
# print(d.display())

 

'''8. Write a Python program that defines a Person class with a constructor that 
takes age as an argument. If the age is less than 18, assign the person to a 
"minor" group; otherwise, assign them to an "adult" group.'''
# class person:
#     def __init__(self,age):
#         self.age=age
#     def display(self):
#         if self.age <18:
#             return f"The {self.age} is minor group"
#         else:
#             return f"The {self.age} is an adult group"      
# p=person(23)
# print(p.display())
      

