# Yoruba to English Translator Lambda Function

This Lambda function serves as a Yoruba to English translation service. It fetches data from DynamoDB and provides translations via a GET API endpoint.

## Functionality

- Fetches Yoruba to English translations from DynamoDB.
- Provides translations via a GET API endpoint.
- Serverless architecture using AWS Lambda and DynamoDB.

## Usage

To use the translation service:

1. Invoke the Lambda function to fetch translations from DynamoDB.
2. Access the GET API endpoint to request translations.

## Deployment

Deploy the Lambda function using the AWS Lambda console or the AWS CLI. Ensure that the necessary permissions are set up for accessing DynamoDB.

## Technologies Used

- **AWS Lambda**: Serverless compute service for running the translation function.
- **DynamoDB**: NoSQL database for storing translation data.
- **AWS API Gateway**: Provides a RESTful API endpoint for accessing translations.

## Example

To fetch a translation for a Yoruba word:


The response will contain the English translation of the Yoruba word.

## License

This project is licensed under the [MIT License](LICENSE).
