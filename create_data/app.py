import json
import boto3
from boto3.dynamodb.conditions import Key
import os

table_name = os.environ['TABLE_NAME']
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(table_name)

def add_item(key, counter):
    response = table.put_item(
       Item={
            'id': key,
            'counter': counter
        }
    )
    return response

def get_items(key):
    response = table.query(
            KeyConditionExpression=Key('id').eq(key)
        )
    return response['Items']

# This is a fake get closes hotspot method
def get_closest_hotspot(longitude, latitude):
    if (int(longitude) > 100 and int(longitude) < 110) and (int(latitude) > 100 and int(latitude) < 110):
        return "100", "100"
    return None

def lambda_handler(event, context):
    body = json.loads(event['body'])
    longitude = body['longitude']
    latitude = body['latitude']

    closest_hotspot = get_closest_hotspot(longitude, latitude)

    if closest_hotspot:
        key = closest_hotspot[0] + closest_hotspot[1]
        existing_items = get_items(key)
        if (len(existing_items) == 0):
            add_item(key, 1)
        else:
            add_item(key, existing_items[0]['counter'] + 1)

    return {    
        'statusCode': 200,
        'body': json.dumps({"message": "Successful"})
    }