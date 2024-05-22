import os
import mysql.connector
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.mime.text import MIMEText

#configuration

# Define the path to the PDF folder as one directory above the current script location
current_dir = os.path.dirname(os.path.abspath(__file__))
PDF_FOLDER = os.path.join(current_dir, '..', 'PDFs')

DB_HOST = "localhost"
DB_PORT = 3306
DB_USER = "root"
DB_PASSWORD = "silindana05100%"
DB_NAME = "psg_client_db"
EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = 587
EMAIL_USER = "clifford.silindana@gmail.com"
EMAIL_PASSWORD = "zgkj asxa hlgp gtmf"

def get_client_email(client_number):
    conn = mysql.connector.connect(
        host = DB_HOST,
        user = DB_USER,
        password = DB_PASSWORD,
        database = DB_NAME,
    )

    cursor = conn.cursor()
    cursor.execute("SELECT email FROM clients WHERE client_number = %s", (client_number,))
    result = cursor.fetchone()
    conn.close()

    return result[0] if result else None

def send_email(to_address, subject, body, attachment_path):
    email_message = MIMEMultipart()
    email_message["From"] = EMAIL_USER
    email_message["To"] = to_address
    email_message["Subject"] = subject

    email_message.attach(MIMEText(body, "plain"))

    with open(attachment_path, "rb") as attachment:
        part = MIMEApplication(attachment.read(), Name = os.path.basename(attachment_path))
        part['Content-Disposition'] = f'attachment; filename="{os.path.basename(attachment_path)}"'
        email_message.attach(part)

    with smtplib.SMTP(EMAIL_HOST, EMAIL_PORT) as server:
        server.starttls()
        server.login(EMAIL_USER, EMAIL_PASSWORD)
        server.sendmail(EMAIL_USER, to_address, email_message.as_string())


def main():
    for filename in os.listdir(PDF_FOLDER):
        if filename.endswith(".pdf"):
            client_number = filename.split(".")[0] # Assuming the client number is the part before the first dot
            client_email = get_client_email(client_number)

            if client_email:
                attachment_path = os.path.join(PDF_FOLDER, filename)
                send_email(
                    to_address = client_email,
                    subject = "Your PDF document",
                    body = "Good day. Please find your PDF document attached.",
                    attachment_path = attachment_path
                )

                print(f'Sent {filename} to {client_email}')
            else:
                print(f'No email found for client number {client_number}')

if __name__ == "__main__":
    main()






