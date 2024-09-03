# number=[1,2,[3,(100,200,300),4,5,6]] >>> [1,2,[3,4,(100,150,200,300)],5,6]
number=[1,2,[3,(100,200,300),4],5,6]
num=number[2][1]
new_num=list(num)
new_num.insert(1,150)
print(tuple(new_num))
number[2][1]=tuple(new_num)

pop_num=number[2]
pop_num.pop()
print(pop_num)
pop_num.insert(1,4)
print(pop_num)
print(number)