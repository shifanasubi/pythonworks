from re import finditer
text="subisgqguisubigtsubidgdrsubi"
matche_subi=finditer("subi",text)
count=0
for m in matche_subi:
    print(m.start(),"=",m.group())
    count=count+1
print("no.of subi",count)