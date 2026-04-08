#write program to check if number is within range[10,50]
#num=int(input("Enter the number:"))
#if num>=10 and num<=50:
    #print(f"{num} is within range [10,50]")
#else:
    #print(f"{num} is not within range[10,50]")
    
#write program to check no  is divisible by both 3 and 5

#if num%3==0 and num%5==0:
 #   print(f"{num} is divisible by both 3 and 5")
#else:
 #   print(f"{num} is not divisible by both 3 and 5")

 #write program to validate password
#password=input("Enter password:")


#write program to print Fizz if number is divisble 3 Buzz if divisible by 5 and FizzBuzz if divisible by both 3 and 5
#num=int(input("Enter number"))
#if num % 3==0 and num%5==0:
 #       print("FizzBuzz")
#elif num%3==0:
#        print("Fizz")
#elif num%5==0:
 #   print("Buzz")
#lse:
#    print(num)

#temp=int(input("Enter temperature"))
#if temp < 0:
   # print("Wear heavy jacket")
#elif 0 <= temp <=15:
 #   print("Wear a jacket")
#elif 16 <= temp <= 25:
 #   print("Wear a t-shirt")
#elif temp >= 25:
 #   print("Wear something light!!")
#else:
 #   print("Enter valid temperature")  


#6.discount
#quantity=int(input("Enter quantity"))
#price=float(input("Enter price"))
#total_cost=quantity * price
#discount=total_cost * 0.1
#final_cost=total_cost - discount
#if total_cost > 1000:

 #  print("Discounted price:",final_cost)
#else:
 #   print("No discount")

#7.
items=int(input("Enter number of items"))
price=int(input("Enter price"))
total_price=items * price
if total_price >= 500:
    discounted=total_price*0.15
    final_price=total_price-discounted
    print("Discounted price:",final_price)
elif 200 <= total_price <= 500:
    discounted=total_price*0.1
    final_price=total_price-discounted
    print("Discounted price:",final_price)
else:
    print("Total is less than $200")