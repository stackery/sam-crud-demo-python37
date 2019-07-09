import boto3
import os
import json

def handler(message, context):
  print(message)

  print('Getting all users from table %s' % os.environ['TABLE_NAME'])
  client = boto3.client('dynamodb')
  response = client.scan(TableName = os.environ['TABLE_NAME'], Select='ALL_ATTRIBUTES')
  print('Done')

  return {
    'statusCode': 200,
    'headers': {},
    'body': json.dumps(response['Items'])
  }