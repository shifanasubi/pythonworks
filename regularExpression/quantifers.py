from re import finditer
text="ab12xyz678#pqr123def"
#pattern="[a-z]{3}" #3 thavana vanna alphabets
#pattern="[0-9]{3}"
# pattern="([c-h]|[t-z])"
pattern="([a-z]{3}|[0-9]{3})"

matcher=finditer(pattern,text)
for m in matcher:
    print(m.start(),"=",m.group())