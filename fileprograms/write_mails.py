email_ids=["sam@gmail.com","smith@gmail.com","jhon@gmail.com","james@gmail.com"]
f=open("C:\\Users\\USER\\Desktop\\PythonJuneWorks\\fileprograms\\emails.txt","w")
for email in email_ids:
    f.write(email+"\n")