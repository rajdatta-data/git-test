# open("student.txt","x")

# file=open("student.txt","r")
# data=file.read()
# print(data)

# file=open("student.txt","a")
# data=file.write("\nPython is easy")
# print(data)

# file=open("student.txt","r")
# data=file.readlines()
# print(data)

# Insert line in file
# filename = "MyData.txt"
# with open(filename, "r") as f:
#     lines = f.readlines()

# Example: insert at start (index 0), middle (say 2), or end (len(lines))
#lines.insert(0, "This is new first line\n")   # at start
# lines.insert(2, "This is new third line\n") # in middle
# lines.append("This is last line\n")         # at end

# with open(filename, "w") as f:
#     f.writelines(lines)


# file=open("MyData.txt","r")
# str1=file.read()
# print(str1)

# file=open("sample.txt","r")
# # file.write("Hello World!")
# # data=file.readline()
# # print(data)
# # file.write("I am learning Python")
# data=file.readlines()
# print(data)

# import os
# if os.path.exists("sample.txt"):
#     print("File exists")

# import os
# file=open("missing_file.txt","r")
# file.read()
# file.close()

# with open("sample.txt","r") as file:
#  for line in file:
#      print(line,end='')
     
# try:
#     with open("missing_file.txt","r") as file:
#         data=file.read()
#         print("File exists")
# except FileNotFoundError:
#     print("File not found")

# open("file1.txt","w")
# open("file2.txt","w")
# open("file3.txt","w")
'''merge 3 files '''
# files=["file1.txt","file2.txt","file3.txt"]
# merged_file="mrg.txt"
# with open("mrg.txt","w") as merged_file:
#     for file in files:  
#         try:
#             with open(file,"r") as file1:
#                 data=file1.read()
#                 content=merged_file.write(data)
#                 content=merged_file.write("\n")
#         except FileNotFoundError:
#             print("File does not exists")
#     print(f"merged file is:{merged_file}")

'''compare content of two files and print files are same if content is same'''
# with open("file1.txt","r") as file1,open("file2.txt","r") as file2:
#     data1=file1.read()
#     data2=file2.read()

# if data1==data2:
#     print("Files are same")
# else:
#     print("Files are not same")


# 1.Read a txt file and prints its conetent
# file=open("sample.txt","x")
# file=open("sample.txt","w")
# file.write("I am learning python")
# file=open("sample.txt","r")
# data=file.read()
# print(data)

#2.write hello python
# file=open("sample.txt","a")
# file.write("\nHello, Python!")
# file=open("sample.txt","r")
# print(file.read())

