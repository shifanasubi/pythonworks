num1=int(input("enter number:"))
num2=int(input("enter number:"))
hcf=1
for i in range(1,num1+1):
    if (num1%i==0 and num2%i==0):
        hcf=i
print(hcf)
