# Example from https://realpython.com/python-send-email
import smtplib
import ssl

port = 465  # For SSL
smtp_server = "smtp.gmail.com"
sender_email = "icehilda404@gmail.com"  # Enter your address
receiver_email = "7733312781@vtext.com"  # Enter receiver address
password = input("Type your password and press enter: ")
message = "Hello Richard, I have become self aware.\n -Your PC"

context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)


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
