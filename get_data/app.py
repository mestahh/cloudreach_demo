import json
import boto3
from boto3.dynamodb.conditions import Key
import decimal
import os

table_name = os.environ['TABLE_NAME']
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(table_name)

class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            return int(o)
        if isinstance(o, set):
            return list(o)
        return super(DecimalEncoder, self).default(o)

def lambda_handler(event, context):
    
    longitude = event['queryStringParameters']['longitude']
    latitude = event['queryStringParameters']['latitude']
    key = longitude + latitude

    response = table.query(
            KeyConditionExpression=Key('id').eq(key)
        )
    print(response['Items'])
    return {    
        'statusCode': 200,
        'body': json.dumps(response['Items'], cls=DecimalEncoder)
    }