start_limit=int(input("start_limit"))
end_limit=int(input("end_limit"))
while(start_limit<=end_limit):
    if(start_limit%2!=0):
        print(start_limit)
    start_limit=start_limit+1