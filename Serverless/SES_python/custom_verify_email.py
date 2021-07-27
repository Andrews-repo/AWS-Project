#SES can also be used to send custom verification emails to users. 
#This is useful if an application uses SES to send verification emails to their users.

#First, we will create a custom verification email template that will be used in the email.

import boto3

def create_custom_verification_email_template():
    ses_client = boto3.client('ses')
    response = ses_client.create_custom_verification_email_template(
        TemplateName= "CustomVerificationTemplate",
        FromEmailAddress= "abhishek@learnaws.org",
        TemplateSubject= "Please confirm your email address",
        TemplateContent= """
            <html>
            <head></head>
            <h1 style='text-align:center'>Please verify your account</h1>
            <p>Before we can let you access our product, please verify your email</p>
            </body>
            </html>
        """,
        SuccessRedirectionURL= "https://yourdomain.com/success",
        FailureRedirectionURL= "https://yourdomain.com/fail"
    )
    print(response)



#We can send a custom verification email using the template we created above.

def send_custom_verification_email():
    ses_client = boto3.client("ses")
    response = ses_client.send_custom_verification_email(
        EmailAddress= "receipientemail@gmail.com",
        TemplateName= "CustomVerificationTemplate"
    )
    print(response)