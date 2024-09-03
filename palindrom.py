num=int(input("enter number"))
result=0
original=0
while(num!=0):
    digits=num%10
    result=result*10+digits
    num=num//10
print(f"palindrom" if result==original else "not palindrom")