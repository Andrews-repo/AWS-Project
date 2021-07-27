#SES also allows us to send emails formatted as HTML. It is important 
#to note that these emails can only be processed by email clients that support HTML.


import boto3

def send_html_email():
    ses_client = boto3.client("ses", region_name="us-east-2")
    CHARSET = "UTF-8"
    HTML_EMAIL_CONTENT = """
        <html>
            <head></head>
            <h1 style='text-align:center'>This is the heading</h1>
            <p>Hello, world</p>
            </body>
        </html>
    """

    response = ses_client.send_email(
        Destination={
            "ToAddresses": [
                "putworking@email.com",
            ],
        },
        Message={
            "Body": {
                "Html": {
                    "Charset": CHARSET,
                    "Data": HTML_EMAIL_CONTENT,
                }
            },
            "Subject": {
                "Charset": CHARSET,
                "Data": "Amazing Email Tutorial",
            },
        },
        Source="putworking@email.com",
    )