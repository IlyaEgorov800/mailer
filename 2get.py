#Step 2 check feedback
import imaplib, email, smtplib, datetime
from email.mime.text import MIMEText
from email.header    import Header
import pandas as pd

cd = datetime.datetime.combine(datetime.datetime.now().date(),datetime.time(00, 00))
c = cd + datetime.timedelta(days=-cd.weekday(), weeks=0) #current week monday

ini = pd.read_excel('3ini.xlsx')
il = ini[0].values.tolist()
gmail_user      = il[0]
gmail_password  = il[1]
toto            = il[4].split(';')
subject         = il[5]
body            = il[6]

df = pd.read_excel('2send.xlsx')
to = df['Mail'].values.tolist()
mapping = df['Mapping'].values.tolist()

conn = imaplib.IMAP4_SSL("imap.gmail.com", 993)
conn.login(gmail_user, gmail_password)
conn.select("inbox")
typ, data = conn.search(None, 'ALL')

prlist = []
for num in data[0].split():
    typ, msg_data = conn.fetch(num, '(RFC822)')
    for response_part in msg_data:
        if isinstance(response_part, tuple):
            msg = email.message_from_bytes(response_part[1])
            ttt =  datetime.datetime.strptime(msg['Date'], "%a, %d %b %Y %H:%M:%S %z").replace(tzinfo=None)         
            if ttt > c:
                mail = msg['From']
                mail = mail[0:-1].partition('<')
                mail = mail[2]
                try:
                    nu = to.index(mail)
                    mm = mapping[nu]
                    prlist.append(mm)
                except:
                    prlist.append(mail)
           
conn.close()
conn.logout()

#Step 3 Got feedback and send to manager
for line in prlist:
    body = body + line + ", "

msg = MIMEText(body, 'plain', 'utf-8')
msg['From'] = gmail_user
msg['Subject'] = Header(subject, 'utf-8')

server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.ehlo()
server.login(gmail_user, gmail_password)
server.sendmail(gmail_user, toto,  msg.as_string())
server.close()
print('Email sent!')