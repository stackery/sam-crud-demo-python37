import boto3
import os
import json

def handler(message, context):
  print(message)

  if 'body' not in message:
    return {}

  user = json.loads(message['body'])
  params = {
    'id': {'S': user['id']},
    'FirstName': {'S': user['firstName']},
    'LastName': {'S': user['lastName']},
    'FavoriteColor': {'S': user['color']}
  }

  print('Adding user to table %s' % os.environ['TABLE_NAME'])
  client = boto3.client('dynamodb')
  response = client.put_item(TableName = os.environ['TABLE_NAME'], Item = params)
  print('User added to table, done')

  return {
    'statusCode': 204,
    'headers': {},
    'body': ''
  }