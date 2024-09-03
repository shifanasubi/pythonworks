#validate mobile number
# country code 91
# then first number 6-9

from re import fullmatch
ph_number=input("enter number")
pattern="(91)\\s?[6-9]\\d{9}"
matcher=fullmatch(pattern,ph_number)
print("invalid" if matcher==None else "valid")