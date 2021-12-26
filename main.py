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

#iterate through csv file rows
for index, row in df.iterrows():
  toEmailAddress = row['email']
  #attach from csv file path
  contents_dynamic=[f"""Hi {row['name']},
  You have billed amount {row['amount']}.   
  Please see attached file for details. Thanks.""",  row['filepath']]
  # print(contents_dynamic)
  yag.send(to=toEmailAddress, subject= subject, contents = contents_dynamic)
  print(f"Email Sent to {row['email']}!!")


