import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import schedule
import time
from datetime import datetime, timedelta

def send_daily_email():
    # email details
    sender_email = "mycoworker@gmail.com"  # replace with your Gmail address
    receiver_email = "person@gmail.com"  # replace with the recipient's email address
    subject = "Daily Test"

    # calculate the date for one week from today
    today = datetime.now()
    one_week_later = today + timedelta(days=7)
    date = one_week_later.strftime("%Y-%m-%d")

    link = "https://www.uoregon.edu/"  # replace with the desired link

    # email content
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject

    # text content
    body = f"Date for one week from today: {date}\n\nCheck out this link: {link}"
    message.attach(MIMEText(body, "plain"))

    # embed the image in the email content
    image_path = "/Users/ovpri_student/Desktop/all/vscode/dog.jpeg"  # replace with the path to your image file
    with open(image_path, "rb") as f:
        image = MIMEImage(f.read(), name="image.jpg")
    image.add_header("Content-ID", "<image1>")
    message.attach(image)

    # connect to the SMTP server and send the email
    smtp_server = "smtp.gmail.com"  # gmail's SMTP server
    smtp_port = 587  # use 465 for SSL/TLS connection
    smtp_username = "mycoworker@gmail.com"  # replace with your Gmail address
    smtp_password = "password"  # replace with your Gmail password or an app-specific password

    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(smtp_username, smtp_password)
        server.sendmail(sender_email, receiver_email, message.as_string())

# schedule the email to be sent every day at a specific time (e.g., 11:35 AM)
schedule.every().day.at("10:10").do(send_daily_email)

while True:
    schedule.run_pending()
    time.sleep(1)
