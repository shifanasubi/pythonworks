names={"hari","hello","chennai","hari","kollam"}
new_names=["hp","del","lenovo"]
# names.update(new_names)  #add elements from any collections to the set
# print(names)

# names.union(new_names) # return the combined elements from two sets and return as a new set
#new_set=names.intersection(new_names)#return common elements from 2 set objects as a new set
# new_set=names.difference(new_names) #return elements from set names which is not in set new_names as new set
new_set=names.symmetric_difference(new_names)#combine all elements from 2 set and remove common elements
print(new_set)
#difference()