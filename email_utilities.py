import os
import logging
import mysql.connector
from mysql.connector import Error
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.mime.text import MIMEText

def get_client_email(client_number, DB_HOST, DB_PORT, DB_USER, DB_PASSWORD, DB_NAME):
    try:
        conn = mysql.connector.connect(
            host=DB_HOST,
            port=DB_PORT,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME
        )
        if conn.is_connected():
            cursor = conn.cursor()
            cursor.execute("SELECT email FROM clients WHERE client_number = %s", (client_number,))
            result = cursor.fetchone()
            cursor.close()
            conn.close()
            logging.debug(f"Email for client {client_number}: {result[0] if result else 'None'}")
            return result[0] if result else None
    except Error as e:
        logging.error(f"Error: {e}")
        return None
    

def send_email(to_address, subject, body, attachment_path, EMAIL_USER, EMAIL_HOST, EMAIL_PORT, EMAIL_PASSWORD):
    try:
        email_message = MIMEMultipart()
        email_message['From'] = EMAIL_USER
        email_message['To'] = to_address
        email_message['Subject'] = subject

        # Attach the body with email_message
        email_message.attach(MIMEText(body, 'plain'))

        # Attach the PDF file
        with open(attachment_path, 'rb') as attachment:
            part = MIMEApplication(attachment.read(), Name=os.path.basename(attachment_path))
            part['Content-Disposition'] = f'attachment; filename="{os.path.basename(attachment_path)}"'
            email_message.attach(part)

        # Connect to the server and send the email
        with smtplib.SMTP(EMAIL_HOST, EMAIL_PORT) as server:
            server.starttls()
            server.login(EMAIL_USER, EMAIL_PASSWORD)
            server.sendmail(EMAIL_USER, to_address, email_message.as_string())

        logging.debug(f"Email sent to {to_address} with attachment {attachment_path}")

    except Exception as e:
        logging.error(f"Failed to send email to {to_address}: {e}")