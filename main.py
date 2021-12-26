import yagmail
import os
import time

sender="webhrss@gmail.com"
receiver="fsufsbzc@yomail.info"
subject="This is subject of email"
contents=("""
Here is the content of email
""")
x=1
while x<=5:
  yag = yagmail.SMTP(user=sender, password=os.getenv('Passgm'))
  subject = subject + str(x)
  yag.send(to=receiver, subject= subject, contents = contents)
  print('Email Sent!!')
  x = x+1
  time.sleep(60)

