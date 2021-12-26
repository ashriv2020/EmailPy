import yagmail
import os
import time
import pandas

sender="webhrsss@gmail.com"
#receiver="fsufsbzc@yomail.info"
subject="This is subject of email"
contents="""
Here is the content of email
"""

#configure email
yag = yagmail.SMTP(user=sender, password=os.getenv('Passgm'))

#read csv file for email receiver contacts
df = pandas.read_csv('contacts.csv')
#print(df)

#iterate through csv file rows
for index, row in df.iterrows():
  yag.send(to=row['email'], subject= subject, contents = contents)
  print('Email Sent!!')


