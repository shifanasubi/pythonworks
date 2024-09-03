def is_amstrong(num):
 num=int(input("enter number"))
 org=num
 total=0
 digit_count=len(str(num))
 while(num!=0):
    digit=num%10
    exponent=digit**digit_count
    total=total+exponent
    num=num//10
 print(total)
 print("amstrng number" if total==org else "not a amstrng number")