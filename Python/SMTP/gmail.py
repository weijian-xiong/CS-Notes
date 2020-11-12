import smtplib

sender_email = 'SenderEmail@gmail.com'  
sender_password = 'SenderPassword'

receiver = ['ReceiverEmail@gmail.com']  
subject = 'Email subject'  
body = 'How are you?'

email_content = \
"""From: %s
To: %s
Subject: %s

%s
""" % (sender_email, ", ".join(receiver), subject, body)

server = smtplib.SMTP("smtp.gmail.com", 587)
server.ehlo()
server.starttls()
server.login(sender_email, sender_password)
server.sendmail(sender_email, receiver, email_content)
server.quit()

print('Email: \n', email_content)