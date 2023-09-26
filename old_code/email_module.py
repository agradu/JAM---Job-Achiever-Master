from smtplib import SMTP
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.mime.text import MIMEText


class Email:
    # Standard secure SMTP port (at the day of today)
    SMTP_PORT = 587

    def __init__(
        self,
        sender: str,
        password: str,
        receivers: list,
        subject: str,
        email_server: str = "smtp.gmail.com",
    ):
        self.sender = sender
        self._password = password
        self.receivers = receivers
        self.subject = subject
        self.email_server = email_server

    @property
    def password(self):
        # App's password
        return self._password

    @password.setter
    def password(self, string):
        self._password = string

    @staticmethod
    def attachments(documents: list):
        # Build the object rapresenting the attachment(s)
        for document in documents.copy():
            with open(document, "rb") as file:
                attachment = MIMEApplication(file.read())
                attachment.add_header(
                    "Content-Disposition", "attachment", filename=document
                )
                documents.remove(document)
                documents.append(attachment)
        return documents

    def send(self, password, body, attachments):
        # Connect to the SMTP server
        print("Connecting to server...")
        with SMTP(self.email_server, self.SMTP_PORT) as smtp:
            # Encript the connection with SMTP "starttls" method
            smtp.starttls()
            # Login into email account
            smtp.login(self.sender, password)
            print("Successfully connected to server.")
            print()

            # Loop through the list of receivers
            for receiver in self.receivers:
                print(f"Sending email to: {receiver}...")
                # Create the message container (outer email message)
                msg = MIMEMultipart()
                msg["From"] = self.sender
                msg["To"] = receiver
                msg["Subject"] = self.subject

            # Add the message body to the container
            msg.attach(MIMEText(body, "plain"))

            # Add the attachment(s) to the container
            for attachment in attachments:
                msg.attach(attachment)

            # Send the email
            smtp.send_message(msg)
            print(f"Email sent to: {receiver}.")
            print()
