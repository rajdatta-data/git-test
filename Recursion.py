'''Q Write a recursive function factorial(n) that return the factorial of a number n '''

# def factorial(n):
#     if n==0:
#         return 1
#     else:
#         return n * factorial(n - 1)
# print("Factorial = ",factorial(5))

'''Q  Write a recursive function fibonacci(n) that return the nth number in the fibonacci sequence'''

# def fib(n):
#     if n<=0:
#         return 0
#     elif n==1:
#         return 1
#     else:
#         return fib(n-1) + fib(n-2)
# print(fib(6))

'''Q '''

def sum_list(lst):
    if len(lst)<=0:
        return 0
    else:
        return lst[0] + sum_list(lst[1:])
lst=[1,2,3,4,5]
print(sum_list(lst))

'''Q '''

# s="racecar"

# def is_palindrome(s):
#     if len(s) <=1 :
#         return True
#     elif s[0] != s[-1]:
#         return False
#     else:
#         return is_palindrome(s[1:-1])
    
# print(is_palindrome(s))



