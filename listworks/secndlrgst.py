number=[1,8,3,10,9,21,11]
largest=0
second_largest=0
for i in number:
    if i >second_largest and i >largest:
        second_largest=largest
        largest=i

    elif i > second_largest and i < largest:

        second_largest = i
print(f"second_largest largest is {second_largest}")