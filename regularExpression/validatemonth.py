#01,02,.......12
from re import fullmatch
month=input("enter month")
pattern="(0?[1-9]|0[0-2])"
matcher=fullmatch(pattern,month)
print("invalid" if matcher==None else "valid")