import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

email = "your email"
password = "your password"

sms_gateway = '17733312781@vtext.com'
smtp = "smtp.gmail.com"
port = 587
server = smtplib.SMTP(smtp, port)
server.startls()
server.login(email, password)

msg = MIMEMultipart()
msg['From'] = email
msg['To'] = sms_gateway

msg['Subject'] = "blah\n"

body = "insert message here\n"

msg.attach(MIMEText(body, 'plain'))

sms = msg.as_string()

server.sendmail(email, sms_gateway, sms)

server.quit()

#AT&T: [number]@txt.att.net
    #Sprint: [number]@messaging.sprintpcs.com or [number]@pm.sprint.com
    #T-Mobile: [number]@tmomail.net
    #Verizon: [number]@vtext.com
    #Boost Mobile: [number]@myboostmobile.com
    #Cricket: [number]@sms.mycricket.com
    #Metro PCS: [number]@mymetropcs.com
    #Tracfone: [number]@mmst5.tracfone.com
    #U.S. Cellular: [number]@email.uscc.net
    #Virgin Mobile: [number]@vmobl.com
