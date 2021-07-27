#Before we can send an email using SES,
#we need to verify the email address using
#the verify_email_identity method.



def verify_email_identity():
    ses_client = boto3.client("ses", region_name="us-west-2")
    response = ses_client.verify_email_identity(
        EmailAddress="putvalid@email.com"
    )
    print(response)
