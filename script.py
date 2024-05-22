import os
import mysql.connector
import logging
import configparser
from mysql.connector import Error
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.mime.text import MIMEText
from email_utilities import get_client_email, send_email

#configuration

# Define the path to the PDF folder as one directory above the current script location
# current_dir = os.path.dirname(os.path.abspath(__file__))
# PDF_FOLDER = os.path.join(current_dir, '..', 'PDFs')

# DB_HOST = "localhost"
# DB_PORT = 3306
# DB_USER = "root"
# DB_PASSWORD = "silindana05100%"
# DB_NAME = "psg_client_db"
# EMAIL_HOST = "smtp.gmail.com"
# EMAIL_PORT = 587
# EMAIL_USER = "clifford.silindana@gmail.com"
# EMAIL_PASSWORD = "zgkj asxa hlgp gtmf"

# Load configuration
config = configparser.ConfigParser()
config.read(os.path.join(os.path.dirname(__file__), 'config.ini'))

# Configuration
DB_HOST = config['database']['host']
DB_PORT = int(config['database']['port'])
DB_USER = config['database']['user']
DB_PASSWORD = config['database']['password']
DB_NAME = config['database']['name']

EMAIL_HOST = config['email']['host']
EMAIL_PORT = int(config['email']['port'])
EMAIL_USER = config['email']['user']
EMAIL_PASSWORD = config['email']['password']

PDF_FOLDER = os.path.abspath(os.path.join(os.path.dirname(__file__), config['paths']['pdf_folder']))
LOG_FILE = os.path.join(os.path.dirname(__file__), config['paths']['log_file'])

# Setup logging
logging.basicConfig(filename='logs/script.log', level=logging.DEBUG, 
                    format='%(asctime)s %(levelname)s:%(message)s')

# def get_client_email(client_number):
#     conn = mysql.connector.connect(
#         host = DB_HOST,
#         user = DB_USER,
#         password = DB_PASSWORD,
#         database = DB_NAME,
#     )

#     cursor = conn.cursor()
#     cursor.execute("SELECT email FROM clients WHERE client_number = %s", (client_number,))
#     result = cursor.fetchone()
#     conn.close()

#     return result[0] if result else None

# def get_client_email(client_number):
#     try:
#         conn = mysql.connector.connect(
#             host=DB_HOST,
#             port=DB_PORT,
#             user=DB_USER,
#             password=DB_PASSWORD,
#             database=DB_NAME
#         )
#         if conn.is_connected():
#             cursor = conn.cursor()
#             cursor.execute("SELECT email FROM clients WHERE client_number = %s", (client_number,))
#             result = cursor.fetchone()
#             cursor.close()
#             conn.close()
#             logging.debug(f"Email for client {client_number}: {result[0] if result else 'None'}")
#             return result[0] if result else None
#     except Error as e:
#         logging.error(f"Error: {e}")
#         return None

# def send_email(to_address, subject, body, attachment_path):
#     email_message = MIMEMultipart()
#     email_message["From"] = EMAIL_USER
#     email_message["To"] = to_address
#     email_message["Subject"] = subject

#     email_message.attach(MIMEText(body, "plain"))

#     with open(attachment_path, "rb") as attachment:
#         part = MIMEApplication(attachment.read(), Name = os.path.basename(attachment_path))
#         part['Content-Disposition'] = f'attachment; filename="{os.path.basename(attachment_path)}"'
#         email_message.attach(part)

#     with smtplib.SMTP(EMAIL_HOST, EMAIL_PORT) as server:
#         server.starttls()
#         server.login(EMAIL_USER, EMAIL_PASSWORD)
#         server.sendmail(EMAIL_USER, to_address, email_message.as_string())

# def send_email(to_address, subject, body, attachment_path):
#     try:
#         email_message = MIMEMultipart()
#         email_message['From'] = EMAIL_USER
#         email_message['To'] = to_address
#         email_message['Subject'] = subject

#         # Attach the body with email_message
#         email_message.attach(MIMEText(body, 'plain'))

#         # Attach the PDF file
#         with open(attachment_path, 'rb') as attachment:
#             part = MIMEApplication(attachment.read(), Name=os.path.basename(attachment_path))
#             part['Content-Disposition'] = f'attachment; filename="{os.path.basename(attachment_path)}"'
#             email_message.attach(part)

#         # Connect to the server and send the email
#         with smtplib.SMTP(EMAIL_HOST, EMAIL_PORT) as server:
#             server.starttls()
#             server.login(EMAIL_USER, EMAIL_PASSWORD)
#             server.sendmail(EMAIL_USER, to_address, email_message.as_string())

#         logging.debug(f"Email sent to {to_address} with attachment {attachment_path}")

#     except Exception as e:
#         logging.error(f"Failed to send email to {to_address}: {e}")


def main():
    for filename in os.listdir(PDF_FOLDER):
        if filename.endswith(".pdf"):
            client_number = filename.split(".")[0] # Assuming the client number is the part before the first dot
            client_email = get_client_email(client_number, DB_HOST, DB_PORT, DB_USER, DB_PASSWORD, DB_NAME)

            if client_email:
                attachment_path = os.path.join(PDF_FOLDER, filename)
                send_email(
                    to_address = client_email,
                    subject = "Your PDF document",
                    body = "Good day. Please find your PDF document attached.",
                    attachment_path = attachment_path,
                    EMAIL_USER = EMAIL_USER, 
                    EMAIL_HOST = EMAIL_HOST, 
                    EMAIL_PORT = EMAIL_PORT, 
                    EMAIL_PASSWORD = EMAIL_PASSWORD
                )

                print(f'Sent {filename} to {client_email}')
            else:
                print(f'No email found for client number {client_number}')

if __name__ == "__main__":
    main()






