num=int(input("enter number"))
sum=0
while(num!=0):
    digit=num%10
    exponent=digit**3
    sum=sum+exponent
    num=num/10
print(sum)