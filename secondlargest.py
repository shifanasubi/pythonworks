num1=int(input("enter num1:"))
num2=int(input("enter num2:"))
num3=int(input("enter num3:"))
if num1>num2 and num1>num3:
    if num2>num3:
        print(f"second largest number is num2={num2}")
    else:
        print(f"second largest number is num3={num3}")
elif num2>num1 and num2>num3:
    if num1>num3:
        print(f"second largest number is num1={num1}")
    else:
        print("second largest number is num3={num3}")
elif num3>num1 and num3>num2:
    if num2>num1:
        print(f"second largest number is num2={num2}")
    else:
        print(f"second largest number is num1={num1}")
