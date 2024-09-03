# #print odd numbers
# num=[1,2,3,4,5,6,7,8]
# odd_num=[]
# for i in num:
#     if i%2!=0:
#          odd_num.append(i)
# print(odd_num)
# #remove even numbers from the list
num=[1,2,3,4,5,6,7,8]
even_num=[]
for i in num:
    if i%2==0:
        num.remove(i)
print(num)
