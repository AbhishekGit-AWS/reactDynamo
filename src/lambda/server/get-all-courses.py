import boto3
from pprint import pprint


def scan_courses(dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb')

    table = dynamodb.Table('courses')
    response = table.scan()
    
    return response['Items']


def lambda_handler(event, context):
    print("All Courses: ")
    courses = scan_courses()
    pprint(courses, sort_dicts=False)