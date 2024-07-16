

def send_info_to_user(msg_body="test", subject_component=""):
    import smtplib
    from email.mime.text import MIMEText
    from email.header import Header
    from config import receivers, mail_host, mail_user, sender, user_pass163, subject
    # from weather_detail_getter import get_weather_detail

    mail_pass = user_pass163

    # Create the email message
    msg = MIMEText(msg_body, 'plain', 'utf-8')
    msg['From'] = mail_user
    msg['To'] = receivers
    subject = subject + subject_component

    msg['Subject'] = Header(subject, 'utf-8')

    # Send the email
    try:
        smtpObj = smtplib.SMTP()
        smtpObj.connect(mail_host, 25)
        smtpObj.login(mail_user, mail_pass)
        smtpObj.sendmail(sender, receivers, msg.as_string())
    except Exception as e:
        print(f"Failed to send email: {e}")

