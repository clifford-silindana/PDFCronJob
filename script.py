import os
import mysql.connector
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.mime.text import MIMEText

#configuration
PDF_FOLDER = ""
DB_HOST = "localhost"
DB_PORT = 3306
DB_USER = "root"
DB_PASSWORD = "silindana05100%"
DB_NAME = "psg_client_db"
EMAIL_HOST = ""
EMAIL_PORT = 587
EMAIL_USER = ""
EMAIL_PASSWORD = ""

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



