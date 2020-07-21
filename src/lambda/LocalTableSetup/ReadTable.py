import boto3

def scan_table(table_to_scan, dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb', endpoint_url="http://localhost:8000")

    table = dynamodb.Table(table_to_scan)
    response = table.scan()
    
    return response['Items']

if __name__ == '__main__':
    table_to_scan ='courses'
    records = scan_table(table_to_scan)

    for record in records:
        print(record)
    # for author in records:
    #     print("ID: ", author['id'], ", FirstName: ", author['firstName'], "LastName: ", author['lastName'])