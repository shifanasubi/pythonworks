f=open("C:\\Users\\USER\\Desktop\\PythonJuneWorks\\fileprograms\\land_slide.txt","r")
data=[]
for line in f:
    lst=line.rstrip("\n").split(" ")
    dic={"state":lst[0],"year":[1],"deaths_count":int(lst[2])}
    data.append(dic)
# print(data)
state_summary={}
for dic in data:
    state=dic.get("state")
    deaths_count=dic.get("deaths_count")
    if state in state_summary:
        state_summary[state]+=deaths_count
    else:
        state_summary[state]=deaths_count
print(state_summary)
                  
