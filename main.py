import yagmail
import os
import time
import pandas

sender="webhrsss@gmail.com"
#receiver="fsufsbzc@yomail.info"
subject="invoice attached"
#attach a txt file as content
contents=["""
Here is the content of email
""", 'bill1.txt']

#configure email
yag = yagmail.SMTP(user=sender, password=os.getenv('Passgm'))

#read csv file for email receiver contacts
df = pandas.read_csv('contacts.csv')
#print(df)

#modularize the code
def send_email(name, toEmailAddress, amount, filepath):
  #attach from csv file path, generate dynamic contents
  contents_dynamic=[f"""Hi {name}, You have to pay {amount}.   
  Please see attached file for details. Thanks.""",  filepath]
  yag.send(to=toEmailAddress, subject= subject, contents = contents_dynamic)
  # print(contents_dynamic)
  print(f"Email Sent to {toEmailAddress}!!")

#iterate through csv file rows
for index, row in df.iterrows():
  toEmailAddress = row['email']
  name = row['name']
  amount = row['amount']  
  filepath= row['filepath']
  send_email(name, toEmailAddress, amount, filepath)


