# Daily PDF Email Sender

This Python script reads PDF files from a specified folder and extracts client numbers from the file names. These client numbers are primary keys for clients in a MySQL database, so it proceeds to look up corresponding email addresses and then sends the PDFs to the respective client via email. The script is designed to run daily as a cron job.

## Requirements

- Python 3.x
- MySQL database with a "clients" table containing "client_number" and "email" columns
- SMTP server for sending emails
- Access to an SMTP server (e.g., Gmail) for sending emails

## Features

- Automatically sends PDF files to customers via email.
- Retrieves customer email addresses from a MySQL database.
- Configurable settings via a `config.ini` file.
- Logging of script execution for debugging purposes.

## Installation

1. **Clone the repository**:
   git clone https://github.com/clifford-silindana/PDFCronJob.git
   cd PDFCronJob

2. **Install Python packages**:
   pip install mysql-connector-python

3. Configure your email settings and database connection details in the config.ini file.

4. Place your PDF files in the designated folder, default is pdfs in project root.

## Usage

To run the script, navigate into the project folder and execute the following command:
python script.py

## Logging

The script logs its execution to a log file, the default is logs/script.log. Review of the log file helps with troubleshooting any issues encountered during email sending.
