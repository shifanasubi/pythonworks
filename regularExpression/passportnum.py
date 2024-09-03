from re import fullmatch 

passport_num=input("enter passport number:")

pattern="[A-Z][1-9][0-9][0\\s][0-9]{4}[1-9]"
matcher=fullmatch(pattern,passport_num)
print("invalid" if matcher==None else "valid")

# S71 19937