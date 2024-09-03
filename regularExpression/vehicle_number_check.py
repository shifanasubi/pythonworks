# starting with KL
# two digits
# alphabets(one or two)
# 4 digits

from re import fullmatch
vehicle_number=input("enter vehicle number")
pattern="(KL)[0-9]{2}[A-Z]{1,2}[0-9]{4}" # *means optional varam varathirikam ethrathavana venelum varam
matcher=fullmatch(pattern,vehicle_number)#?varam varathirikam but oru thavane varan padullu
print("invalid" if matcher==None else "valid")