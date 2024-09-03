from re import fullmatch
email_id=input("enter mail")
pattern="\w[\w\._]*@gmail.com"
matcher=fullmatch(email_id,pattern)
print("invalid" if matcher==None else "valid")

# +match one or more
# ? optional
# * zero or more