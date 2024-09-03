from json import load
f=open("C:\\Users\\USER\\Desktop\\PythonJuneWorks\\jsonWorks\\filims.json","r")
filims = load(f)
for fl in filims:
    print(fl.get("title"))
