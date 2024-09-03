word1="PQRS"
word2="ABCDEFG"
#PAQBRCSDEFG
smallest_word=word1 if len(word1)<len(word2) else word2
merged_str=""
for i in range(0,len(smallest_word)):
    merged_str=merged_str+word1[i]+word2[i]
if len(word1)>len(word2):
    balance=word1[len(smallest_word)]
else:
    balance=word2[len(smallest_word)]
merged_str=

