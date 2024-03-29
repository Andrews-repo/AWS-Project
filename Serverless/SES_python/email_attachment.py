from email import encoders
from email.mime.base import MIMEBase
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import boto3

def send_email_with_attachment():
    msg = MIMEMultipart()
    msg["Subject"] = "This is an email with an attachment!"
    msg["From"] = "putworking@email.com"
    msg["To"] = "putworking@email.com"

    # Set message body
    body = MIMEText("Hello, world!", "plain")
    msg.attach(body)

    filename = "document.pdf"  # In same directory as script

    with open(filename, "rb") as attachment:
        part = MIMEApplication(attachment.read())
        part.add_header("Content-Disposition",
                        "attachment",
                        filename=filename)
    msg.attach(part)

    # Convert message to string and send
    ses_client = boto3.client("ses", region_name="us-west-2")
    response = ses_client.send_raw_email(
        Source="putworking@email.com",
        Destinations=["putworking@email.com"],
        RawMessage={"Data": msg.as_string()}
    )
    print(response)