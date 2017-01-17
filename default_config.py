import os

# Default app config
AWS_REGION = 'us-west-2'

consumer_key = os.environ['tc_twitter_consumer_key']
consumer_secret = os.environ['tc_twitter_consumer_secret']
access_token_key = os.environ['tc_twitter_access_token_key']
access_token_secret = os.environ['tc_twitter_access_token_secret']

SQS_QUEUE_URL = os.environ['sqs_worker_queue_url']