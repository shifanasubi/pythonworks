# print unique numbers from the list 
num=[1,2,2,3,4,5,3,6,7]
list=[]
for i in num:
    if num.count(i)==1:
     list.append(i)
print(list)
