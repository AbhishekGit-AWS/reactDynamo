from pprint import pprint
import boto3
from botocore.exceptions import ClientError


def delete_course(id, dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb')

    table = dynamodb.Table('courses')

    try:
        response = table.delete_item(
            Key={'id': id}
        )
    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        return response


def lambda_handler(event, context):
    id = event["id"]
    print("Deleting: ",id)
    delete_response = delete_course(id)
    if delete_response:
        print("Delete course succeeded:")
        pprint(delete_response, sort_dicts=False)
