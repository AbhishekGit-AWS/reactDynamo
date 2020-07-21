import boto3
from pprint import pprint

def scan_authors(dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb')

    table = dynamodb.Table('authors')
    response = table.scan()
    
    return response['Items']


def lambda_handler(event, context):
    print("All authors: ")
    authors = scan_authors()
    pprint(authors, sort_dicts=False)