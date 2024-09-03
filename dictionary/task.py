numbers=[1000,2000,500,1000,2000,1000]
num_count={}
for n in numbers:
    if n in num_count:
        num_count[n]+=1
    else:
        num_count[n]=1
print(num_count)