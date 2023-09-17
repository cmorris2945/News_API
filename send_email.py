import smtplib, ssl

def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    username = "youremail@gmail.com"
    password = "your password for the email account here."

    receiver = "whoisreceiing@gmail.com"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host,port,context=context) as server:
        server.login(username, password)
        server.sendmail(username,receiver,message)





