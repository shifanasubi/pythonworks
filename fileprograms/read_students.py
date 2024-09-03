f=open("C:\\Users\\USER\\Desktop\\PythonJuneWorks\\fileprograms\\studnts.txt","r")
students=[]
for stud in f:
    students.append(stud.rstrip("\n"))
print(students)