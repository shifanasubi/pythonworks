from re import fullmatch
date=input("enter a date")
pattern="(0[0-9]|1[0-9]|2[0-9]|3[0-1])"
matcher=fullmatch(pattern,date)
print("invalid" if matcher==None else "valid")