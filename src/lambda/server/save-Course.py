# Add one item to the table
from pprint import pprint
import boto3
from botocore.exceptions import ClientError


def save_course(course, dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb')

    table = dynamodb.Table('courses')

    try:
        response = table.put_item(Item=course)
    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        return response


def lambda_handler(event, context):

    id = event["title"].replace(" ", "-").lower()

    course = {
        "id": id,
        "title": event["title"],
        "authorId": event["authorId"],
        "length": event["length"],
        "category": event["category"],
        "watchHref": "http://www.pluralsight.com/courses/"+id
    }

    course_resp = save_course(course)
    return course_resp
