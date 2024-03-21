import ssl
import smtplib
from email.message import EmailMessage
sender="niharikagupta197@gmail.com"
password="ygjlsximhcniuoaj"
receiver="aakritimaurya91@gmail.com"

subject="subject hai yeh mail ka"
body="Ye body hai mail ki"

em=EmailMessage()
em['From']=sender
em['To']=receiver
em['Subject']=subject
em.set_content(body)

security=ssl.create_default_context()

server=smtplib.SMTP_SSL('smtp.gmail.com',465,context=security)
server.login(sender, password)
server.sendmail(sender,receiver,em.as_string())

print("email sent")
