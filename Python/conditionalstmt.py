# 1.Write a program to check if a number is within the range [10, 50].
# num=int(input("Enter the number: "))

# if 10 <=num <=50:
#     print(f"{num} is within the range of [10-50]")
# else:
#     print(f"{num} is not within the range of [10-50]")    


# 2.Write a program to check if a number is divisible by both 3 and 5.
# num=int(input("Enter the number: "))

# if num%3==0 and num%5==1:
#     print(f"{num} is divisible by both 3 and 5")
# else:
#     print(f"{num} is not divisible by both 3 and 5")

# 3.	Write a program to validate a password. The program should check 
# if the password meets the following conditions: 
# 	At least 8 characters long. 
# 	Contains both uppercase and lowercase letters. 
# 	Contains at least one digit. 
# Input: A string for the password. 
# Output: "Valid Password" or "Invalid Password". 

# password=input("Enter the password: ")

# if (len(password)>=8 and any(ch.isupper() for ch in password) 
#                     and any(ch.islower() for ch in password)
#                     and any(ch.isdigit() for ch in password)):
#     print("Valid password")
# else:
#     print("Invalid Password")    




# 4.	Write a program to print "Fizz" if a number is divisible by 3, "Buzz" if
# divisible by 5, and "FizzBuzz" if divisible by both 3 and 5.
#  Otherwise, print the number itself. 
# Input: A single integer.  
# Output: Fizz, Buzz, FizzBuzz, or the number.

# num=int(input("Enter the number: "))
# if num % 3 ==0 and num %5==0:
#     print("FizzBuzz")

# elif num %3 ==0:
#     print("Fizz")

# elif num % 5==0:
#     print("Buzz")

# else:
#     print(num)


# 5.	Write a code that takes the temperature in Celsius as input and 
# prints out what you should wear:
# •	Below 0°C: "Wear a heavy jacket!"
# •	0°C to 15°C: "Wear a jacket!"
# •	16°C to 25°C: "Wear a t-shirt!"
# •	Above 25°C: "Wear something light!"

# temp=int(input("Enter the temperature in celcius: "))
# if temp<0:
#     print("Wear a heavy jacket!")
# elif 0 <= temp <=15:
#     print("Wear a jacket!")
# elif 16 <= temp <=25:
#     print("Wear a t-shirt!")    
# elif temp >25:
#     print("Wear something light!")  
# else:
#     print("Enter valid input..")    

# 6.A shop gives a discount of 10% if the cost of purchased quantity is
#   more than $1000. 
# Take appropriate inputs and print total cost for user. 
# quantity=int(input("Enter the quantity: "))
# price=float(input("Enter the price: "))

# total_cost=quantity* price
# discount= total_cost * 0.1
# final_cost= total_cost - discount

# if total_cost>1000:
#     print("final amount is: ",  final_cost)
# else:
#     print("discount is not applicable")    

# 7.Write a Python function that calculates the total price of items in
# a shopping cart and applies a discount based on the total price:
# If the total is greater than $500, apply a 15% discount.
# If the total is between $200 and $500, apply a 10% discount.
# If the total is less than $200, apply no discount.
#quantity=int(input("Enter the quantity: "))
#rice=float(input("Enter the price: "))
#total_cost=quantity* price

#if total_cost > 500:
 #   discount=total_cost * 0.15
  #  final_cost=total_cost- discount
   # print("final cost is :",final_cost)

#elif  200<=total_cost<=500:
 #   discount=total_cost * 0.1
  #  final_cost=total_cost- discount
   # print("final cost is :",final_cost)

#else:
 #   print("No discount applicable")
#for i in range(1,11):
 #   print(i)
