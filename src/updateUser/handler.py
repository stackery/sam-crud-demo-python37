import boto3
import os
import json

def handler(message, context):
  print(message)

  if 'body' not in message:
    return {}

  user = json.loads(message['body'])
  userId = message['pathParameters']['id']

  params = {
    'id': {'S': userId},
    'FirstName': {'S': user['firstName']},
    'LastName': {'S': user['lastName']},
    'FavoriteColor': {'S': user['color']}
  }

  print('Updating user %s from table %s' % (userId, os.environ['TABLE_NAME']))
  client = boto3.client('dynamodb')
  response = client.put_item(TableName = os.environ['TABLE_NAME'], Item=params)
  print('Done')

  return {
    'statusCode': 204,
    'headers': {},
    'body': ''
  }