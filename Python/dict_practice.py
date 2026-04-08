#1. Write a program that iterates through the dictionary person = {"name": "John", "age": 25, "city": "New York"} and prints both the keys and values.
#person={"name": "John", "age": 25, "city": "New York"}
person=dict(name="John", age=25, city="New York")

#2. Write a program that merges two dictionaries dict1 = {"name": "John", "age": 25} and dict2 = {"city": "New York", "country": "USA"}.
car={"model":"tata","Price":500000,"color":"red"}
person=dict(name="John", age=25, city="New York")
#print(car | person)

#3. Write a program that creates a dictionary from a list of numbers, where the keys are the numbers, and the values are their squares.
numbers=[1,2,3,4,5]
new_dict={num : num**2 for num in numbers}
#print(new_dict)

#4. Write a program that updates a dictionary person = {"name": "John", "age": 25} with another dictionary new_info = {"age": 26, "city": "New York"}.
person = {"name": "John", "age": 25}
new_info = {"age": 26, "city": "New York"}
person.update(new_info)
#print("Updated Dictionary:", person)

#5. Write a Python program that finds the key with the maximum value in a dictionary.
numbers={1:1,2:4,3:9,4:16,5:25}
key=max(numbers,key=numbers.get)
#print("key:",key, "Value:",numbers[key])


#6. Write a Python program that inverts a dictionary, i.e., swaps keys with values.
person = {"name": "John", "age": 25}
person={value:key for key,value in person.items()}
#print(person)


# Take sides as input
a = float(input("Enter side a: "))
b = float(input("Enter side b: "))
c = float(input("Enter side c: "))

# Check triangle validity
if a + b > c and a + c > b and b + c > a:
    print("It is a valid triangle")
else:
    print("Not a triangle")
