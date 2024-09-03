words=["hello","hai","hello","hai","hai","hi"]
# print word count
# hello:2,hai:3,hi:1
word_set=set(words)
for w in word_set:
    print(w,words.count(w))