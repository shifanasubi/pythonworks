# student={"name":"sukumar","course":"fullstack","course":"datascience"}
# print(student)
# print(student["name"])
# print(student.keys()) #return the keys in the dictionry

# #overwrite(update) the value if the key is present else add as a new pair
# student["name"]="hari" #update the value
# student['place']="chennai"# add as a new pair 

# new=student.items()
# print(new) #dictnryitems([('names','hari'),('course','fullstack'),('place','chennai')]) # key value oru tuplente ullilum ellam koode or listilum aayit represent cheyyunnu


student={"name":"sukumar","course":"datascience","place":"chennai"}
# for i in student:
#     print(f"{i} = {student[i]}") #return key,values
  
#update
# for i in student:
    # if i=="course":
    #   student["course"]="fullstack"#update
# print(student)
    #remove the key: value from the dictionry if its present (1 method)
# student.pop("place")
# print(student)
#another method
for key,value in student.items:
   if key=="place":
     del student[key]
print(student)




