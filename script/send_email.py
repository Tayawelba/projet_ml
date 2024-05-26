# script/send_email.py
import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.mime.text import MIMEText

def send_email():
    user = os.getenv('EMAIL_USER')
    password = os.getenv('EMAIL_PASS')
    recipients = ['hesedtayawelba@gmail.com', 'hesestayawelba@live.com']

    msg = MIMEMultipart()
    msg['From'] = user
    msg['To'] = ', '.join(recipients)
    msg['Subject'] = 'Modèle Entraîné et Documentation'

    body = 'Veuillez trouver ci-joint le modèle entraîné et la documentation générée.'
    msg.attach(MIMEText(body, 'plain'))

    # Attach model and doc
    filenames = ['model/model_final.h5', 'doc/train_evaluate_model.html']
    for filename in filenames:
        with open(filename, 'rb') as attachment:
            part = MIMEApplication(attachment.read(), Name=os.path.basename(filename))
            part['Content-Disposition'] = f'attachment; filename="{os.path.basename(filename)}"'
            msg.attach(part)

    # Send email
    with smtplib.SMTP('smtp.gmail.com', 465) as server:
        server.starttls()
        server.login(user, password)
        server.sendmail(user, recipients, msg.as_string())

if __name__ == '__main__':
    send_email()
