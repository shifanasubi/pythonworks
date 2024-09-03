def is_fibnocci(num):
current=1
previous=0
print(f"{previous},{current}",end=",")
for i in range(1,11):
    next=previous+current
    print(f"{next}",end=",")
    previous=current
    current=next

