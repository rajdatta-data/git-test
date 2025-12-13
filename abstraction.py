# from abc import ABC ,abstractmethod
# class Animal(ABC):
#     @abstractmethod
#     def speak(self):
#         pass
#     @abstractmethod
#     def movement(self):
#         pass
#     def breed(self):
#         return "The breed is German Shephard"
# class Dog(Animal):
#     def speak(self):
#         return "Bark!!!"
#     def movement(self):
#         return "Running..."
# dog=Dog()
# print(dog.speak())
# print(dog.movement())
# print(dog.breed())

'''Error'''
# from abc import ABC, abstractmethod
# class Shape(ABC):
#     @abstractmethod
#     def area(self):
#         pass

#     @abstractmethod
#     def perimter(self):
#         pass

# class Rectangle(Shape):
#     def __init__(self,length,breadth):
#         self.length=length
#         self.breadth=breadth
#     def area(self):
#         return f"Area is: {self.length * self.breadth}"

#     def perimeter(self):
#         return f"Perimeter: {2*(self.length + self.breadth)}"
# rect=Rectangle(12,2)
# print(rect.area())
# print(rect.perimeter())

'''3.abs class vehicle and two method start(), stop() subclass is Car'''
# from abc import ABC,abstractmethod
# class Vehicle(ABC):
#     @abstractmethod
#     def start():
#         pass
#     @abstractmethod
#     def stop():
#         pass

# class Car(Vehicle):
#     # def __init__(self,start,stop):
#     #     self.start=start
#     #     self.stop=stop
#     def start(self):
#         return "Car started"
#     def stop(self):
#         return "Car stopped"
# car=Car()
# print(car.start())
# print(car.stop())

# from abc import ABC, abstractmethod

# # Abstract Class
# class BankAccount(ABC):
#     def _init_(self, balance=0):
#         self.balance = balance

#     @abstractmethod
#     def deposit(self, amount):
#         pass

#     @abstractmethod
#     def withdraw(self, amount):
#         pass


# # Savings Account with withdrawal limit
# class SavingsAccount(BankAccount):
#     def deposit(self, amount):
#         self.balance += amount
#         print(f"Deposited {amount}, New Balance: {self.balance}")

#     def withdraw(self, amount):
#         if amount > self.balance:
#             print("Insufficient balance in Savings Account")
#         elif amount > 10000:  # Example rule: max withdrawal limit
#             print("Savings Account withdrawal limit is 10000")
#         else:
#             self.balance -= amount
#             print(f"Withdrew {amount}, Remaining Balance: {self.balance}")


# # Current Account with overdraft allowed
# class CurrentAccount(BankAccount):
#     def deposit(self, amount):
#         self.balance += amount
#         print(f"Deposited {amount}, New Balance: {self.balance}")

#     def withdraw(self, amount):
#         overdraft_limit = -5000  # Allow negative balance up to -5000
#         if self.balance - amount < overdraft_limit:
#             print("Overdraft limit exceeded in Current Account")
#         else:
#             self.balance -= amount
#             print(f"Withdrew {amount}, Remaining Balance: {self.balance}")


# # Example usage
# savings = SavingsAccount(20000)
# savings.deposit(5000)
# savings.withdraw(15000)
# savings.withdraw(8000)

# print()

# current = CurrentAccount(5000)
# current.deposit(2000)
# current.withdraw(10000)
# current.withdraw(8000)

# from abc import ABC, abstractmethod
# class BankAccount(ABC):
#     def __init__(self,balance=0):
#         self.balance=balance
#     @abstractmethod
#     def deposit(self):
#         pass
#     @abstractmethod
#     def withdraw(self):
#         pass

# class SavingAccount(BankAccount):
#     def deposit(self, amount):
#         self.balanace+=amount
#         print(f"Depsoited amoubt is:{amount} and total balance is :{self.balanace}")

#     def withdraw(self, amount):
        
#         if self.balance >= amount:
#             self.balance-=amount
#             print(f"Total Balance is:{self.balance}")
#         else:
#             print("Enter valid amount")

# class CureentAccount(BankAccount):
#     def deposit(self, amount):
#         self.balance+=amount
#         print(f"Total Balance is:{self.balance}")

#     def withdraw(self, amount):
#         if amount >=-10000:
#             self.balance-=amount
#             print(f"Total Balance is:{self.balance}")
#         else:
#             print("Enter valid amount")


from abc import ABC, abstractmethod

class BankAccount(ABC):
    def __init__(self, balance=0):
        self.balance = balance

    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass


class SavingAccount(BankAccount):
    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited amount: {amount}, Total balance: {self.balance}")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"Withdrawn: {amount}, Total Balance: {self.balance}")
        else:
            print("Insufficient balance!")


class CurrentAccount(BankAccount):
    overdraft_limit = -10000  

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited amount: {amount}, Total balance: {self.balance}")

    def withdraw(self, amount):
        if self.balance - amount >= self.overdraft_limit:
            self.balance -= amount
            print(f"Withdrawn: {amount}, Total Balance: {self.balance}")
        else:
            print("Overdraft limit exceeded!")



s_acc = SavingAccount(5000)
s_acc.deposit(2000)
s_acc.withdraw(3000)
s_acc.withdraw(5000) 

print("-" * 40)

c_acc = CurrentAccount(2000)
c_acc.deposit(8000)
c_acc.withdraw(20000)  
c_acc.withdraw(2000)  



# 1. How do you create an abstract class in Python using the abc module? Provide 
# an example. 
# 2. Can an abstract class have concrete methods (methods with implementation)? 
# Demonstrate this with a Python example. 
# 3. Write a Python program with an abstract class Vehicle that has two abstract 
# methods: start() and stop(). Create a subclass Car that implements both methods. 
# 4. Write an abstract class Shape with an abstract method draw(), which accepts 
# arguments for color and size. Implement this method in a subclass Circle. 
#     5. Write a Python program to calculate the area of different shapes using 
# abstraction. 
# What to do: 
# 1. Create an abstract class called Shape with a method area(). 
# 2. Make two classes that inherit from Shape: 
# o Circle: takes a radius and calculates area using 3.14 * radius * radius. 
# o Square: takes a side length and calculates area using side * side. 
# 3. Create one object of each class and print their areas
# 6. Write an abstract class Employee with abstract method calculate_salary(). 
# Create subclasses FullTimeEmployee  and PartTimeEmployee that implement 
# salary calculation differently. 
# 7. Create an abstract class BankAccount with methods deposit() and 
# withdraw(). 
# Implement it in SavingsAccount and CurrentAccount with different withdrawal 
# rules. 
# 8.Create an abstract class Database with methods connect(), disconnect(), and 
# execute_query(query). 
# Implement it for MySQLDatabase and MongoDBDatabase.