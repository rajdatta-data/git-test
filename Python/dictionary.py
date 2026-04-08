# students={
#     "name":"Suryansh",
#     "Rollno":21,
#     "course":"Python",
#     "city":"Pune",
#     "city1":"Pune",
#     "mobno":9922,
#     "cgpa":9.28
# }

# students.pop("city")

# students.popitem()

# del students["name"]

# students.clear()

# students.copy()

# s=dict(students)

# print(s)

# students["grade"]="A"


# students.update({"gmail":"hefshinesoftwares@abc.org"})
# print(students)

# print(students.popitem())

# del students["Rollno"]

# students.clear()


# print(students.update({"name":"Kishor"}))

# students["age"]=23

# A=students["mobno"]

# print(A)

# B=students.get("city")

# print(B)

# a=students["city"]
# print(a)
# b=students.get("cgpa")
# print(b)

# print(students.keys())
# print(students.values())
# print(students.items())




# Car=dict(
#     Brand = "Tata",
#     model = "Punch",
#     color = ["black", "white", "red"],
#     price = 700000,
#     milage = "17kmpl"
# )


# newCar=Car.copy()
# print(newCar)

# newcar1=dict(Car)
# print(newcar1)


# print(Car)

# myfamily={
#     "child1":{
#         "name":"Pavan",
#         "age":23
#         },
#     "child2":{
#         "name":"Sakshi",
#         "age":{
#             "year":21,
#             "months":3
#         }
#     },
#     "child3": {
#         "name":"mrunali",
#         "age":21
#     }
# }
# print(myfamily["child2"]["age"]["year"])

# 1. Create a dictionary with the following keys and 
# values: "name": "John", "age": 25, "city": "New York". 
# Access and print the value of the "age" key.

# person={"name": "John", "age": 25, "city": "New York"}
# x=person.get("age")
# print(x)

# y=person["age"]
# print(y)

# 2. Write a program that adds a new key-value pair "country": "USA" 
# to the dictionary person = {"name": "John", "age": 25, "city": "New York"}

# person = {"name": "John", "age": 25, "city": "New York"}

# # person.update({"country":"USA"})

# person["addr"]="mumbai"
# print(person)

# Write a program to remove the "city" key from the dictionary 
# person = {"name": "John", "age": 25, "city": "New York"} and 
# print the resulting dictionary.

# person = {"name": "John", "age": 25, "city": "New York"}

# print(person.pop("city"))

# print(person)

# 4. Write a program to check if the key "age" exists in the dictionary 
# person = {"name": "John", "age": 25, "city": "New York"}.

# person = {"name": "John", "age": 25, "city": "New York"}

# print("age" in person)

# var =input("Enter the key to check: ")

# if var in person:
#     print(f"{var} exists")
# else:
#     print(f"{var} does not exists")    


# 5. Write a program that gets the value of the key "gender" in
# the dictionary person = {"name": "John", "age": 25, "city": "New York"}. 
# If the key doesn't exist, return "Not Available"

# person = {"name": "John", "age": 25, "city": "New York", "gender":"Male"}

# if "gender" in person:
#     print(person["gender"])

# else:
#     print("Not Available")  


# Write a Python program that inverts a dictionary, i.e., swaps keys with values.
# students={
#     "name":"Suryansh",
#     "Rollno":21,
#     "course":"Python",
#     "city":"Pune",
#     "mobno":9922,
#     "cgpa":9.28
# }

# students={value : key for key, value in students.items()}

# dict1 = {"name": "John", "age": 25}
# dict2 = {"city": "New York", "country": "USA"}

# mrg_dict={**dict1, **dict2, **students}

# print(mrg_dict)

# numbers=[1,2,3,4,5,6,7,8,9,10]
# new_dict={num : num**2 for num in numbers}
# print(new_dict)


# def swap_dict(input_dict):
#     swapped = {}                          # new dictionary
#     for k, v in input_dict.items():       # loop through key-value pairs
#         swapped[v] = k                    # swap key and value
#     return swapped
# input_dict = {'apple': 2, 'banana': 4, 'pear': 1}
# print(swap_dict(input_dict))
