# aws-email-automation

# EMAIL SENDING USING LAMBDA AND SES

## Project Title:
AWS Email Automation Project

## Description:
This project facilitates automated email sending using AWS Lambda and SES. It's designed to notify on S3 bucket events, providing a scalable solution for real-time email notifications.

## Setup:

### Step 1: Create S3 Bucket
- Create an S3 bucket named `testinglambdaandses`.

### Step 2: Create IAM Role
- Create an IAM role named `lambda_and_ses_role` with the following permissions:
  - AmazonS3FullAccess
  - AmazonSESFullAccess
  - CloudWatchFullAccess

### Step 3: Create Lambda Function
- Create a Lambda function named `emailtesting`.
- Use the following code snippet for the Lambda function:

```python
import json
import boto3

def lambda_handler(event, context):
    file_name = event['Records'][0]['s3']['object']['key']
    bucket_name = event['Records'][0]['s3']['bucket']['name']
    print("Event details: ", event)
    print("File Name: ", file_name)
    print("Bucket Name: ", bucket_name)

    subject = 'Event from ' + bucket_name
    client = boto3.client("ses")

    body = """
        <br>
        This is a notification mail to inform you regarding the S3 event.
        The file {} is inserted in the {} bucket.
    """.format(file_name, bucket_name)

    message = {"Subject": {"Data": subject}, "Body": {"Html": {"Data": body}}}
    response = client.send_email(
        Source="e6281937589@gmail.com",
        Destination={"ToAddresses": ["e6281937589@gmail.com"]},
        Message=message
    )

    print("The mail is sent successfully")

Step 4: Verify Email Address
Verify the email address (e6281937589@gmail.com) in Amazon SES.
Step 5: Deploy Lambda Function
Paste the provided code into the Lambda function and click deploy.
Usage:
Once the setup is complete, the Lambda function will automatically send an email notification whenever a new file is inserted into the S3 bucket.
Dependencies:
The project relies on the boto3 library for interacting with AWS services
