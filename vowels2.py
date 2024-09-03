text="ahello"
vowels="aeious"
v_count=0
consnce=0
c_count=0
for ch in vowels:
   if vowels.count(ch)==0:
      v_count+=1
   else:
      c_count+=1

print(f"vowels={v_count}")
print(f"consnce={c_count}")

