import imaplib
import email
from email.header import decode_header
import schedule
import time
import smtplib
from email.mime.text import MIMEText

def process_email(msg):
    sender_email = msg.get("From")
    subject, encoding = decode_header(msg["Subject"])[0]
    subject = subject.decode(encoding) if encoding else subject

    # Add your logic to generate a response based on the email content
    
    reply_body = "Genrated replay from GPT"

    # Send the response
    send_email(sender_email, "Re: " + subject, reply_body)

def fetch_emails():
    try:
        # Connect to the IMAP server
        mail = imaplib.IMAP4_SSL('your_mail_server.com')
        mail.login('your_email@example.com', 'your_email_password')
        mail.select('inbox')

        # Search for new emails
        status, messages = mail.search(None, 'UNSEEN')
        messages = messages[0].split()

        for mail_id in messages:
            # Fetch the email by ID
            _, msg_data = mail.fetch(mail_id, '(RFC822)')
            msg = email.message_from_bytes(msg_data[0][1])

            # Process the email and send a response
            process_email(msg)

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        # Logout and close the connection
        mail.logout()

def send_email(to, subject, body):
    # Set up your email sending configuration (replace with your SMTP server details)
    smtp_server = 'smtp.example.com'
    smtp_port = 587
    smtp_username = 'your_username'
    smtp_password = 'your_password'

    # Create the email message
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = 'your_email@example.com'
    msg['To'] = to

    # Connect to the SMTP server and send the email
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(smtp_username, smtp_password)
        server.sendmail('your_email@example.com', [to], msg.as_string())

def job():
    print("Checking emails...")
    fetch_emails()

if __name__ == "__main__":
    # Schedule the job to run every 15 minutes
    schedule.every(15).minutes.do(job)

    while True:
        # Run any pending scheduled jobs
        schedule.run_pending()

        # Introduce a 1-second delay between iterations
        time.sleep(1)
