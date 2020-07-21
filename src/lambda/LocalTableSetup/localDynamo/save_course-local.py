# Add one item to the table
from pprint import pprint
import boto3
from botocore.exceptions import ClientError


def save_course(course, dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource(
            'dynamodb', endpoint_url="http://localhost:8000")

    table = dynamodb.Table('courses')

    try:
        response = table.put_item(Item=course)
    except ClientError as e:
        # print(e.response['Error']['Message'])
        return e.response['Error']['Message']
    else:
        return response


if __name__ == '__main__':
    event = {
        "title": "Web Component Fundamentals",
        "authorId": "cory-house",
        "length": "5:10",
        "category": "HTML5"
    }

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
    pprint(course_resp)
