import pandas as pd
import smtplib
import xlrd

file_path = 
email = 
password = 

emails = pd.read_excel(file_path)

server = smtplib.SMTP("smtp.gmail.com",587)
server.starttls()
server.login(email,password)

message =
subject = 
body = "Subject : {}\n\n{}".format(subject,message)

for i in emails['Address']:
    server.sendmail(email,i,body)
server.quit()
