from re import fullmatch
variable_name=input("enter a variable")
pattern="[a-zA-z][a-zA-z0-9_]*"
matcher=fullmatch(pattern,variable_name)
print("invalid" if matcher==None else "valid")