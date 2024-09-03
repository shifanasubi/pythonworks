f_read=open("C:\\Users\\USER\\Desktop\\PythonJuneWorks\\fileprograms\\years.txt","r")
f_century=open("C:\\Users\\USER\\Desktop\\PythonJuneWorks\\fileprograms\\century.txt","w")
f_noncentury=open("C:\\Users\\USER\\Desktop\\PythonJuneWorks\\fileprograms\\non_century.txt","w")
for year in f_read:
    y=int(year.rstrip("\n"))
    if y%100==0:
        f_century.write(str(y)+"\n")
    else:
        f_noncentury.write(str(y)+"\n")