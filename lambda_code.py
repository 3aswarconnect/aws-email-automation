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
