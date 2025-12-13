#create string using single quote,double and triple n print
str='Hello'
str1="Hello World"
str2="""Hello World"""
print(str)
print(str1)
print(str2)

#2. Count the number of occurrences of a specific character in a string.  
str="Hefshine Class"
print("Count of e:",str.count('e'))

str=input("Enter string")
ch=input("Enter char to count:")
result=str.count(ch)
print(f"the occurence of {ch} in {str} is:",result)

#3. Write a program to count the number of words in a string.
str10=input("Enter string")
str_split=str10.split()
final_str=len(str_split)
str10.split()

splt_str=str.split()
fnl_str=len(splt_str)
print(fnl_str)


#4. Write a program to check if a string contains only digits. 
str="12357"
print("String contains digits:",str.isdigit())
print(str.isnumeric())

# How can you sort the characters of a string alphabetically.
str12="Hefshine Softwares"
print("Alphabetically:",str12.isalpha())
#srtd_str=sorted(str14)
#jnd_str="".join(srtd_str)
#print(jnd_str)

#Write a program to find whether a given string is a palindrome
str=input("Enter string")
if str==str[::-1]:
    print("String is Palindrome")
else:
    print("String is not Palindrome")

#Write a Python code to reverse the words in a sentence.
str13="Python is high level language"
splt_str=str.split()
rev_str=split

# Accept comma separated sequence of words as input and print the words in sorted form (alphanumerically) 
#Sample Words : orange, red, white, black, green  
#Expected Result : black, green, orange, red, white 
str15=str(input("Enter string",))





#Write a program to swap comma and dot in a string.                 Sample string: "47,89,56.3"  Expected Output: "47.89.56,3" 
str14="47,89,56.3"
print(str14.replace(",","."))
#str14="47,89,56.3"
#str14=str14.replace(",","#")
#str14=str14.replace("."," ,")
#str14=str14.replace("#",".")
#print(str14)


#1. Replace all occurrences of a substring with another substring.
str1="This is incorrect Please try again till it is correct"
print(str1.replace("is","was"))

#2. Check if the string starts with a given prefix or ends with a given suffix
str2="Good Morning Have a Good Day"
print("Starts with:",str2.startswith("G"))
print("Ends With:",str2.endswith("Day"))

#3. Remove all whitespace from a string
str3="Hefshine Classes Pune     "
print(str3.strip())
print(str3.replace("",))

#4. Read a string. Exchange first and last character of a string. Display it.
str4="ABC DEF"
str4=f"XBC DEZ"
print(str4)

str5="John Cena is wrestler"
str5="{} cena is {}".format("Roman","superstar")
print(str5)


#5. Write a program to remove all spaces from a string in Python.
str6="Hefshine Classes    BALAJINAGAR     PUNE"
str6=f"Hefshine Classes"" BALAJINAGAR PUNE"  #replace(" ","")
print(str6)

#6. Read a line from user. Print three strings using odd  indexed characters, even indexed characters and every third character.
str7="Hefshine classes Pune"
list1=list(str7)
print("Odd Indexed characters are:",list1[1:len(list1):2])
print("Even Indexed characters are:",list1[:len(list1):2])
print("Every 3rd character is:",list1[2::3])

#7. Write a Python program to check if a substring exists in a given string.
str8="Hefshine Softwares"
if "Softwares" in str8:
   print("Substring exists")
else: 
   print("Substring not exists")



#8. Write a Python program to check if two strings are anagrams.
#use sorted function
