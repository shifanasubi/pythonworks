# secondsmallest number
numbers=[10,2,3,5,7,1,9,4]
# numbers.sort()  #print(number(1)) inghne koduthal sorted aavumbo ascending orderil aavumallo apo index koduthal simple aayi kittum


smallest_num = numbers[-1]
second_smallest=numbers[0]

for i in numbers:
    if i <second_smallest and i< smallest_num:
        second_smallest=smallest_num
        smallest_num=i
    elif i<second_smallest and i> smallest_num:
        second_smallest=i
print(second_smallest)
print(smallest_num)
