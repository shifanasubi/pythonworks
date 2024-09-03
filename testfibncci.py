num=int(input("enter a number:"))
previous=0
current=1
next=previous+current
is_fibo=False
while(next<=num):
    next=previous+current
    previous=current
    current=next
    if num==next:
        is_fibo=True
        break
print(is_fibo)


