import boto3

def delete_table(table_to_delete, dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb', endpoint_url="http://localhost:8000")

    table = dynamodb.Table(table_to_delete)
    table.delete()


if __name__ == '__main__':
    table_to_delete ='authors'
    delete_table(table_to_delete)
    print(table_to_delete ,"table deleted.")
