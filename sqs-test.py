import boto3

# from boto3.session import Session

# Create the Boto3 Session
session = boto3.Session(profile_name='brano')
client = session.client('sqs')

# Get the Queue URL
response = client.get_queue_url(
    QueueName='awseb-e-8ugv4byjnp-stack-AWSEBWorkerQueue-T6ANROMR84J6' # Or the name of your SQS queue
)
url = response['QueueUrl']

print(url)
