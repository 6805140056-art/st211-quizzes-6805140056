import  smtplib
def send_mail(to,subject):
    server = smtplib.SMTP("smtp.example.com")
    server.sendmail("noreply@app.com",to, subject)
    server,quit()
    return True
def notify_user(user_email):
    send_mail(user_email,"Welcome")
    return f"Notified{user_email}"