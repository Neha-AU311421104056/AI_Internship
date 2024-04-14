






# Example usage with multiple recipients
'''sender_email = 'neha.bio2004@gmail.com'
sender_password = 'zqgg kcaj khor hcts'
receiver_emails = ['neha.llsacc123@gmail.com,leelavathi.devi123@gmail.com']
subject = 'Test Email '
message = 'This is a test email sent using Python to multiple recievers.'

send_email(sender_email, sender_password, receiver_emails, subject, message)'''




import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import ssl

def send_email(sender_email, sender_password, receiver_emails, subject, message):
    # Set up the MIME
    email = MIMEMultipart()
    email['From'] = sender_email
    email['To'] = ', '.join(receiver_emails)  # Join multiple emails with comma and space
    email['Subject'] = subject

    # Attach the message to the email
    email.attach(MIMEText(message, 'plain'))

    # Connect to the SMTP server with SSL and disable certificate verification
    context = ssl.create_default_context()
    context.check_hostname = False
    context.verify_mode = ssl.CERT_NONE
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context)

    try:
        # Login to the sender's email account
        server.login(sender_email, sender_password)
        # Send the email to each recipient
        for receiver_email in receiver_emails:
            server.sendmail(sender_email, receiver_email, email.as_string())
        print("Emails sent successfully!")
    except Exception as e:
        print(f"Failed to send email. Error: {e}")
    finally:
        # Close the connection
        server.quit()

# Get input from the user
sender_email = input("Enter your email address: ")
sender_password = input("Enter your email password: ")
receiver_emails = input("Enter recipient email addresses separated by commas: ").split(',')
subject = input("Enter the subject of the email: ")
message = input("Enter the message you want to send: ")

# Example usage with multiple recipients
send_email(sender_email, sender_password, receiver_emails, subject, message)
