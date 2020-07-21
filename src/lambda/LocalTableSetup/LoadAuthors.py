## Import JSON to put the entire JSON to the the table: Loop through the JSON object and use put_item()
from decimal import Decimal
import json
import boto3
import os

def load_movies(json_to_load, target_table, dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb', endpoint_url="http://localhost:8000")
    
    table = dynamodb.Table(target_table)
    for obj in json_to_load:
        # print("Adding", obj[0])
        table.put_item(Item=obj)

if __name__ == '__main__':
    source_json='dummyAuthors.json'
    target_table='authors'
    with open(source_json) as json_file:
        data = json.load(json_file, parse_float=Decimal)
    load_movies(data, target_table)