from pprint import pprint
import boto3
from botocore.exceptions import ClientError


def get_course(id, dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource(
            'dynamodb', endpoint_url="http://localhost:8000")

    table = dynamodb.Table('courses')

    try:
        response = table.get_item(Key={'id': id})
    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        return response['Item']


if __name__ == '__main__':
    event = {
        "id": "web-component-fundamentals"
    }

    id = event["id"]
    course = get_course(id,)
    if course:
        print("Get course succeeded:")
        pprint(course, sort_dicts=False)