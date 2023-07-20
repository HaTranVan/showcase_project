import smtplib, ssl


def send_email(message_arg):
    host = 'smtp.gmail.com'
    port = 465

    username = '1472003h@gmail.com'
    password = 'aqobsfdyfpjxfnuf'
    receiver = '1472003h@gmail.com'

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(host, port, context=context) as sever:
        sever.login(username, password)
        sever.sendmail(username, receiver, message_arg)
