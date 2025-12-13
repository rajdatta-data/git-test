#basics
#1 Match a word that starts with "a" and ends with "z" (like "apple" or "amazing").
import re
pattern = r'\ba\w*z\b'   #\w*: Matches zero or more word characters (letters, digits, or underscores).
text = "applez amazing az amazingz"
matches = re.findall(pattern, text)
print(matches)


#2 Extract all numbers from a string.
import re
pattern = r'\d+'
text = "I have 2 apples and 10 bananas. I paid 5 rs."
matches = re.findall(pattern, text)
print(matches)


#3 Check if a string contains only alphabetic characters.
import re
pattern = r'^[a-zA-Z]+$'
print(re.match(pattern, "Hello"))
print(re.match(pattern, "Hello123"))
print(re.match(pattern, "123"))


#4 Replace multiple consecutive spaces in a string with a 
# single space.
import re
pattern = r'\s+'
text = "This   is    a    sentence  with   multiple   spaces."
result = re.sub(pattern, ' ', text)
print(result)


#5 Extract all email addresses from a text.
#mrvishaldahibhate441@gmail.com
import re
pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$'
text = "Contact us at support@example.com or hefshine@company.org."
emails = re.findall(pattern, text)

print(emails)
 

#6 Check if the string contains the word "Python".
import re
pattern = r'\bPython\b'
text1 = "I love Python programming!"
text2 = "I love programming!"
text3 = "Learn Python at https://www.python.org"

print(re.search(pattern, text1))
print(re.search(pattern, text2))
print(re.search(pattern, text3))


#7 Extract dates that match the format DD-MM-YYYY.
import re
pattern = r'\b\d{2}-\d{2}-\d{4}\b'
text = "The important dates are 01-01-2022, 2023-12-34, and 25-12-2021."
dates = re.findall(pattern, text)
print(dates)


#8 Match all words that start with the letter "a".
import re
pattern = r'\ba\w*\b'
text = "apple is amazing and awesome."
matches = re.findall(pattern, text)

print(matches)


#advanced 
#1. Write a regular expression to validate an email address. A valid email 
# follows the pattern:
# •	Starts with alphanumeric characters.
# •	Contains a @ symbol.
# •	After the @, there is a domain name with at least one period (.).
# •	Domain extension should be 2-4 letters long.
import re

def validate_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$'
    return bool(re.match(pattern, email))

print(validate_email("example@example.com"))  # True
print(validate_email("invalid-email.com"))   # False


#2.Extract Dates from a Text
# Write a regular expression to extract all dates in the format DD/MM/YYYY from a given text.
# Example:
# Input: "The meeting is scheduled for 15/03/2025 and the follow-up will be on 18/04/2025."
# Output: ['15/03/2025', '18/04/2025']
import re

def extract_dates(text):
    pattern = r'\b\d{2}/\d{2}/\d{4}\b'
    return re.findall(pattern, text)

text = "The meeting is scheduled for 15/03/2025 and the follow-up will be on 18/04/2025."
print(extract_dates(text))

#3.Check for Palindrome Using Regex
# Write a regular expression to check whether a given string is a palindrome 
# (it reads the same backward as forward).
import re

def is_palindrome(text):
    cleaned_text = re.sub(r'[^a-zA-Z0-9]', '', text).lower()
    return cleaned_text == cleaned_text[::-1]

print(is_palindrome("A man, a plan, a canal: Panama"))  
print(is_palindrome("race a car"))  

#4.Match Phone Number Format
# Write a regular expression to match phone numbers in the following formats:
# •	(123) 456-7890
# •	123-456-7890
# •	123.456.7890
# •	123 456 7890
import re

def validate_phone_number(phone_number):
    pattern = r'^\(?\d{3}\)?[\s.-]?\d{3}[\s.-]?\d{4}$'
    return bool(re.match(pattern, phone_number))

print(validate_phone_number("(123) 456-7890"))
print(validate_phone_number("123-456-7890")) 
print(validate_phone_number("123.456.7890"))   
print(validate_phone_number("123 456 7890"))
print(validate_phone_number("1234567890"))   



#5. Count Occurrences of a Word in a Text
# Write a regular expression to count the occurrences of a word "apple" in a given text, irrespective of case.
import re

def count_word_occurrences(text, word):
    pattern = r'\b' + re.escape(word) + r'\b'
    return len(re.findall(pattern, text, re.IGNORECASE))

text = "Apple is a fruit. I love apple pie. An apple a day keeps the doctor away."
print(count_word_occurrences(text, "apple"))




#6. Remove All Non-Alphanumeric Characters
# Write a regular expression to remove all non-alphanumeric characters from a 
# string (only letters and numbers should remain).
import re

def remove_non_alphanumeric(text):
    pattern = r'[^a-zA-Z0-9]'
    return re.sub(pattern, '', text)

text = "Hello, world! 1234."
print(remove_non_alphanumeric(text))  # "Helloworld1234"

#7.Match a URL
# Write a regular expression to match URLs that start with http:// or https://, 
# followed by a domain name and optional path/query parameters.
import re

def validate_url(url):
    pattern = r'^(http|https)://[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}(?:/[a-zA-Z0-9&%_./-]*)?$'
    return bool(re.match(pattern, url))

print(validate_url("https://www.example.com"))  # True
print(validate_url("http://example.com/path/to/page?name=value"))  # True
print(validate_url("ftp://example.com"))  # False

#8. Replace Multiple Spaces with a Single Space
# Write a regular expression to replace all sequences of multiple spaces with a single space in a string.
import re

def replace_multiple_spaces(text):
    pattern = r'\s+'
    return re.sub(pattern, ' ', text)

text = "This   is   a   sentence     with   extra    spaces."
print(replace_multiple_spaces(text))  # "This is a sentence with extra spaces."

#9.Check if String Contains Only Digits
# Write a regular expression to check if a string contains only digits.
import re

def is_only_digits(text):
    pattern = r'^\d+$'
    return bool(re.match(pattern, text))

print(is_only_digits("12345"))
print(is_only_digits("123a45"))
