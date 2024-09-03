#print words starting with vowels
words=["hello","hai","python","apple","eagle"]
vowels="aeiou"
for i in range(0,len(words)):
    first_letter=words[i][0]
    if vowels.count(first_letter)!=0:
        print(words[i])