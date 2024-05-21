# Daily PDF Email Sender

This Python script reads PDF files from a specified folder and extracts client numbers from the file names. These client numbers are primary keys for clients in a MySQL database, so it proceeds to look up corresponding email addresses and then sends the PDFs to the respective client via email. The script is designed to run daily as a cron job.

## Requirements

- Python 3.x
- MySQL database with a "clients table containing "client_number` and "email" columns
- SMTP server for sending emails

## Installation

1. **Clone the repository**:

   ```sh
   git clone https://github.com/clifford-silindana/PDFCronJob.git
   cd PDFCronJob
   ```

2. **Install Python packages**:
   ```sh
   pip install mysql-connector-python
   ```
