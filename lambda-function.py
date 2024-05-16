import json
import boto3 
import logging
from botocore.exceptions import ClientError
from boto3.dynamodb.conditions import Attr

# Configure logging
logger = logging.getLogger(__name__)

def lambda_handler(event, context):
    # Retrieve the input from the query parameters
    params = event
    string = params.get('string', '').lower()
    
    
    # Check if string is empty, return bad request if either is empty
    if not string.strip():
        return {
            'statusCode': 400,
            'body': json.dumps("string cannot be empty.")
        }
    
    # Initialize the DynamoDB resource
    dynamodb = boto3.resource('dynamodb', region_name='eu-north-1') 
    
    # Select the DynamoDB table
    table = dynamodb.Table('YorubaAPI') 
    
    # Initialize HTTP headers
    status_code = 200
    item = None
    
    # Query the database based on the provided language and string
    try:
        response = table.scan(
            FilterExpression=Attr('english').eq(string)
        )
        items = response['Items']
        # Assuming only one item is returned, retrieve the first item
        if items:
            item = items[0]
        else:
            logger.info("No items found for the provided key.")
    except ClientError as err:
        # Log an error if there's an issue fetching the item
        logger.error(
            "Couldn't fetch item. Here's why: %s: %s",
            err.response["Error"]["Code"],
            err.response["Error"]["Message"]
        )
        raise

    # Prepare the response
    response = {
        'statusCode': status_code,
        'body': item
    }
   

    return response
