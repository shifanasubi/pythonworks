source_word="CHICKEN"
target_word="HEN"
word_count={}
for ch in source_word:
    if ch in word_count:
        word_count[ch]+=1
    else:
        word_count[ch]=1
print(word_count)
is_kangaroo_word=True
for ch in target_word:
    if ch in word_count and word_count.get(ch)>0:
        word_count[ch]-=1
    else:
        word_count[ch]=1
        is_kangaroo_word=False
        break  
print(is_kangaroo_word)


