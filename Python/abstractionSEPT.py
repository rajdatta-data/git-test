# abstract method is method without implementation
# abstract class contains 1 or more abstract methods
# concrete method contains full implementation in abstract class
# from abc import ABC, abstractmethod
# class animal(ABC):
#     @abstractmethod
#     def speak(self):
#         pass

#     @abstractmethod
#     def move(self):
#         pass

# class dog(animal):
#     def speak(self):
#         return "Bark!!!!"
#     def move(self):
#         return "run!!!"

# class fish(animal):
#     def speak(self):
#         return "Blubb!!!"
#     def move(self):
#         return "swim!!!"
# d=dog()
# print(d.speak())
# print(d.move())

# f=fish()
# print(f.speak())
# print(f.move())

'''How do you create abstract class in python using abc module'''
# from abc import ABC,abstractmethod
# class car(ABC):
#     @abstractmethod
#     def speed(self):
#         pass
#     def company(self):
#         return f"The company of car is TATA"
    
# class bike(car):
#     def speed(self):
#         return f"The speed is High"
# c=bike()
# print(c.company())
# print(c.speed())

'''Can abstract class have conecrete methods(methods with implementation)'''
# from abc import ABC,abstractmethod
# class hefshine(ABC):
#     @abstractmethod
#     def language(self):
#         pass
#     def job(self):
#         return f"Python"
# class student(hefshine):
#     def language(self):
#         return f"Java and python are courses"
# s=student()
# print(s.job())
# print(s.language())

'''WAP with abstract class vehicle that has two abstract methods: start() and stop(). 
Create subclass Car that implements both'''
# from abc import ABC,abstractmethod
# class vehicle(ABC):
#     @abstractmethod
#     def start(self):
#         pass
#     @abstractmethod
#     def stop(self):
#         pass
# class car(vehicle):
#     def start(self):
#         return "The car has started"
#     def stop(self):
#         return "The car has stopped"
# c=car()
# print(c.start())

'''abstract method which accepts arguments colors and size '''
# from abc import ABC,abstractmethod
# class shape(ABC):
#     @abstractmethod
#     def draw(self,color,size):
#         pass
# class circle(shape):
#     def draw(self,color,size):
#         return f"The size of circle is {size} and color is {color}"
# c=circle()
# print(c.draw("Red",20))

# from abc import ABC,abstractmethod
# class shape(ABC):
#      @abstractmethod
#      def area(self):
#           pass  
# class circle(shape):
#      def area(self,r):
#           return f"The area of circle is {3.14*r*r}"
# class square(shape):
#      def area(self,side):
#           return f"The area of square is {side*side} "
# c=circle()
# print(c.area(5))
# c=square()
# print(c.area(4))

# from abc import ABC,abstractmethod
# class Employee(ABC):
#     @abstractmethod
#     def salary(self):
#         pass
# class FullTimeEmployee(Employee):
#     def salary(self,salary,hr):
#         return f"The salary of full time employee is {hr*salary}"
# class PartTimeEmployee(Employee):
#     def salary(self,salary):
#         return f"The salary of part time employee is {salary}"
# a=FullTimeEmployee()
# print(a.salary(12000,10))
# b=PartTimeEmployee()
# print(b.salary(40000))
       
from abc import ABC,abstractmethod
class BankAccount(ABC):
    def __init__(self,initial_balance):
        self.initial_balance=initial_balance
        print(f"Initial Balance:{self.initial_balance}")
        
    @abstractmethod
    def deposit(self):
        pass
    @abstractmethod
    def withdraw(self):
        pass
class Savings(BankAccount):
    def deposit(self,amount):
        self.initial_balance+=amount
        return f"Total Balance:{self.initial_balance}"
    def withdraw(self,amount):
        if self.initial_balance>amount:
            self.initial_balance-=amount
            return f"Balance after withdraw:{self.initial_balance}"
        else:
            return "Low Balance"
class Current(BankAccount):
    def deposit(self,amount):
        self.initial_balance+=amount
        return f"Total Balance:{self.initial_balance}"
    
    def withdraw(self,amount):
        if amount>=-10000:
            self.initial_balance-=amount
            return f"Balance After Withdraw:{self.initial_balance}"
        else:
            return "Low Balance"
        
# save=Savings(1000)
# print(save.deposit(2000))
# print(save.withdraw(1500))

curr=Current(2000)
print(curr.deposit(3000))
print(curr.withdraw(15000))
            
        
    
        
