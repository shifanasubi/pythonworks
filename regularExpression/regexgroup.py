from re import finditer
text="aAbGc123 ,@k#7medef"
#pattern="[abf]"  ##for check a b or f in text
#pattern="[a-k]" #for check alphabets a to k
#pattern="[A-K]" #for check uppercase in a-k
#pattern="[a-z A-Z]"#for check capital&small a-z
#pattern="[0-9]" #for ckeck numbers
#pattern="[a-zA-z0-9]"#for check all alphanumeric
#pattern="[^0-9]"#for check without numbers(^ oposit or exclude)
#pattern="[\s]" #for space
pattern="[^a-zA-Z0-9\s]"
matcher=finditer(pattern,text)
for m in matcher:
    print(m.start(),"=",m.group())
