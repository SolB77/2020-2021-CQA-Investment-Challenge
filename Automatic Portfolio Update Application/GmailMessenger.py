#Import required libraries and modules
import config
from NonJupyterPCS import portfolioupdate
import smtplib


#Define function to send email
def send_email(subject, msg):
    try:
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()
        server.login(config.EMAIL_ADDRESS, config.PASSWORD)
        message = 'Subject: {}\n\n{}'.format(subject, msg)
        server.sendmail(config.EMAIL_ADDRESS, config.GROUP_EMAILS, message)
        server.quit()
        print('Success!')
    except:
        raise Exception('Email failed to send!')

#Send email
send_email('Dutchmen Alpha Fund Portfolio Update', portfolioupdate)


