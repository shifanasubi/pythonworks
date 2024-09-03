#recursive-repeated
text="CABCADD"
word_count={}
#print first recursive character
for char in text:
    if char in word_count:
        print(char,"first recursive character")
        break
    else:
        word_count[char]=1

