year=(int(input("enter year")))
if (year%100==0 and year%400==0) or (year%100!=0 and year%4==0):
    print(f"{year} leap year")
else:
    print(f"{year} not leap year")