# Add one item to the table
from pprint import pprint
import boto3


def update_course(course, dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource(
            'dynamodb', endpoint_url="http://localhost:8000")

    table = dynamodb.Table('courses')
    response = table.put_item(Item=course)

    return response


if __name__ == '__main__':
    event = {
        "title": "Web Component Fundamentals",
        "authorId": "cory-house",
        "length": "5:3",
        "category": "HTML5"
    }
    id = event["title"].replace(" ", "-").lower()

    course = {
        "id": id,
        "title": event["title"],
        "authorId": event["authorId"],
        "length": event["length"],
        "category": event["category"]
    }

    course_resp = update_course(course)
    pprint(course_resp, sort_dicts=False)