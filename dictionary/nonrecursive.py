text="AAFCDDSSEE"
word_count={}
for char in text:
    if char in word_count:
     word_count[char]+=1
    else:
     word_count[char]=1
for k,v in word_count.items():
    if v==1:
     print(k)


    

    