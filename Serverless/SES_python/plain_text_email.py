#We will be using the send_email method from the Boto3 library to send an email. 
#The key parameters for this method are:
#Source: Email address to send the email from.
#This email address should be verified with SES before it can be used.
#Destination: The destination for the email.
#Message: The actual message we want to send. The message can include both plain-text as well as HTML.

import boto3

def send_plain_email():
    ses_client = boto3.client("ses", region_name="us-west-2")
    CHARSET = "UTF-8"

    response = ses_client.send_email(
        Destination={
            "ToAddresses": [
                "putreal@mail.com',
            ],
        },
        Message={
            "Body": {
                "Text": {
                    "Charset": CHARSET,
                    "Data": "Hello, world!",
                }
            },
            "Subject": {
                "Charset": CHARSET,
                "Data": "Amazing Email Tutorial",
            },
        },
        Source="putreal@mail.com",
    )
