#1.Write lambda function that adds 10 to given number
# result=lambda x:x+10
# print(result(5))

#convert list of strings to uppercase using map
# list1=["harry","thor","thanos"]
# result=list(map(lambda x:x.upper(),list1))
# print(result)

#add corresponding elements of two lists using map
# list1=[1,2,3,4,5,6]
# list2=[10,20,30,40,50,60]
# result=list(map(lambda x,y:x+y,list1,list2))
# print(result)

#filter out names starts with a
# lst=["apple","banana","anar"]
# result=list(filter(lambda x:x.startswith("a"),lst))
# print(result)


#filter out number greater than 10
# list2=[10,20,30,40,50,60]
# result=list(filter(lambda x:x>10,list2))
# print(result)

#product of two numbers
# result=lambda x,y:x*y
# print(result(5,10))

#square each elemnet from list
# list1=[1,2,3,4]
# result=list(map(lambda x:x**2,list1))
# print(result)

#filter out even no from list
# lst=[1,2,3,4,5,6,7]
# result=list(filter(lambda x:x%2==0,lst))
# print(result)

#remove empty strings
# lst=[" ","abc","bcd"," "]
# result=list(filter(lambda x:x!=" ",lst))
# print(result)


#sort words by length
# lst=["abc","ab","xyza","rstuv","qwertr"]
# result=sorted(lst,key=lambda x:len(x))
# print(result)

#extract last digit from list
# lis=[12,34,67,89,26]
# result=list(map(lambda x:x%10,lis))
# print(result)

#max string by length
# lis=["harry","potter","captain","spiderman"]
# result=max(lis,key=lambda x:len(x))
# print(result)


