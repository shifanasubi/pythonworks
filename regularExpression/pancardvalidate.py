#validate pancard
#first 3 chrctrs are alphabets
#4th place alphabet PCAFHT
# 5th place alphabet
# 4digit
# 1alphabet

from re import fullmatch

pancard_number=input("enter number:")
pattern="[A-Z]{3}[PCAFHT][A-Z][0-9]{4}[A-Z]{1}"
matcher=fullmatch(pattern,pancard_number)
print("invalid" if matcher==None else "valid")
