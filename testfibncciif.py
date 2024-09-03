num=int(input("enter number"))
current=1
next=1
previous=0
is_fibo=False
if num==0 or num==1:
    is_fibo=True
else:
    next=previous+current
    while(next<=num):
       next=previous+current
       previous=current
       current=next
       if next==num:
          is_fibo=True
          break
print(is_fibo)
