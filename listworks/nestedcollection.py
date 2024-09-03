# arr=[
# [10,20],
# [21,30],
# [40,53]
# ]
# evens=[num for lst in arr for num in lst if num%2==0]
# print(evens)

arr=[
    [10,14],
    [21,30],
    [40,53]
]
grtst=[num for lst in arr for num in lst if num>15]
print(grtst)