import os
import logging
import configparser
from email_utilities import get_client_email, send_email

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






