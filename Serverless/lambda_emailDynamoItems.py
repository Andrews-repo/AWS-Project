import boto3
import json
import decimal
from boto3.dynamodb.conditions import Key, Attr

def lambda_handler(event, context):
    # TODO implement
    class DecimalEncoder(json.JSONEncoder):
        def default(self, o):
            if isinstance(o, decimal.Decimal):
                if o % 1 > 0:
                    return float(o)
                else:
                    return int(o)
            return super(DecimalEncoder, self).default(o)
        
    dynamodb = boto3.resource('dynamodb', region_name='us-east-2')
    
    table = dynamodb.Table('Fortunes')
    
    pe = "fortuneID, fortune"

    response = table.scan(
        ProjectionExpression=pe
        )
    
    while 'LastEvaluatedKey' in response:
        response = table.scan(
            ProjectionExpression=pe,
            ExclusiveStartKey=response['LastEvaluatedKey']
            )
    def listfortune():
        for i in response['Items']:
            yield i
            #print(json.dumps(i, cls=DecimalEncoder))
            #return(json.dumps(i, cls=DecimalEncoder))
            #print(i['fortuneID'], ":", i['fortune'])
    
    generator = listfortune()
    
    def a():
        output=[]
        for item in generator:
                output.append(json.dumps(item, cls=DecimalEncoder))
                #print(json.dumps(item, cls=DecimalEncoder))
        return output
    
    ses_client = boto3.client("ses", region_name="us-east-2")
    CHARSET = "UTF-8"
    response = ses_client.send_email(
        Destination={
            "ToAddresses": [
                "andrewpatty3@gmail.com",
            ],
        },
        Message={
            "Body": {
                "Text": {
                    "Charset": CHARSET,
                    "Data": '\n'.join(a()),
                }
            },
            "Subject": {
                "Charset": CHARSET,
                "Data": "Amazing Email Tutorial",
            },
        },
        Source="andrewpatty3@gmail.com",
    )

    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
