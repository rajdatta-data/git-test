# class Person:
#     def __init__(self,age):
#         self._age=age
# class Student(Person):
#     def __init__(self, name,age):
#         super().__init__(age)  
#         self.name=name
#     def show(self):
#         return f"The name of person is {self.name} and age is {self.age}"



#3.Write python class Account with a private attribute balance and method deposit() that modifies
#the balanace.Show how a private attribute is not accessible from outside class



       

#4.Write a python class student with a private attribute age. Create getter and setter methods to
#access and modify the age attribute
# class Student:
#     def __init__(self, age):
#         self.__age = age 

#     def get_age(self):
#         return self.__age
   
#     def set_age(self, age):
#         if age > 0:  
#             self.__age = age
#         else:
#             print("Age must be a positive number.")

# s1 = Student(18)
# print("Initial Age:", s1.get_age())  
# s1.set_age(20) 
# print("Updated Age:", s1.get_age())
# s1.set_age(-5) 





# class student:
#     def __init__(self,age=0):
#         self.__age=age

#     #getter method
#     def get_age(self):
#         return f"Age is: {self.__age}"
#     #setter method
#     def set_age(self,age):
#         if age > 0:
#             self.__age=age
#         else:
#             print("Enter valid age")
# std=student(20)
# print(std.get_age())
# std.set_age(25)
# print(std.get_age())

#5. Use property decorators in python to implement getter and setter methods for a private attribute radius Create
#method to calculate the area of circle using radius.

