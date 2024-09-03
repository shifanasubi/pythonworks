f=open("C:\\Users\\USER\\Desktop\\PythonJuneWorks\\fileprograms\\news.txt","r")
# word_list=[]
# for line in f:
#     words=line.rstrip("\n").split(" ")
#     for w in words:
#         word_list.append(w)
# print(word_list)


word_list=[w for line in f for w in line.rstrip("\n").split(" ") if w!=""]
wc={w:word_list.count(w) for w in word_list}
# print(wc)
 
def get_value(key):
    return wc.get(key)
srt=sorted(wc,key=get_value,reverse=True)
print(srt)