import boto3

resource = boto3.resource('dynamodb', endpoint_url='http://localhost:8000')

mytable = resource.create_table(
    TableName='mytable',
    KeySchema=[{ 'AttributeName': 'name', 'KeyType': 'HASH' }],
    AttributeDefinitions=[{ 'AttributeName': 'name', 'AttributeType': 'S' }],
    ProvisionedThroughput={ 'ReadCapacityUnits': 5, 'WriteCapacityUnits': 5 }
)

try:
    resource.batch_write_item(RequestItems={
        'mytable': [{ 'PutRequest': { 'Item': {
            'name': { 'S': 'myname' },
            'value': { 'S': 'myvalue' }
        }}}]
    })
    print(f'resource, specify all types : write succeeded.')
except Exception as e:
    print(f'resource, specify all types : write failed: {e}')

try:
    resource.batch_write_item(RequestItems={
        'mytable': [{ 'PutRequest': { 'Item': {
            'name': 'myname',
            'value': { 'S': 'myvalue' }
        }}}]
    })
    print(f'resource, specify value only: write succeeded.')
except Exception as e:
    print(f'resource, specify value only: write failed: {e}')

try:
    resource.batch_write_item(RequestItems={
        'mytable': [{ 'PutRequest': { 'Item': {
            'name': 'myname',
            'value': 'myvalue'
        }}}]
    })
    print(f'resource, specify none      : write succeeded.')
except Exception as e:
    print(f'resource, specify none      : write failed: {e}')