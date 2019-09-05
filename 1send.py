import smtplib
from email.mime.text import MIMEText
from email.header    import Header
import pandas as pd

ini = pd.read_excel('3ini.xlsx')
il = ini[0].values.tolist()
gmail_user      = il[0]
gmail_password  = il[1]
subject         = il[2]
body            = il[3]

df = pd.read_excel('2send.xlsx').iloc[:,0:1]
tl = df['Mail'].values.tolist()
    
msg = MIMEText(body, 'plain', 'utf-8')
msg['From'] = gmail_user
msg['Subject'] = Header(subject, 'utf-8')
    
for to in tl:
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(gmail_user, gmail_password)
    server.sendmail(gmail_user, to,  msg.as_string())
    server.close()
    print('Email sent!')