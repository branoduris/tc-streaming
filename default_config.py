import os

# Default app config
AWS_REGION = os.environ['AWS_REGION']
AWS_DEFAULT_PROFILE = os.environ['AWS_DEFAULT_PROFILE']

consumer_key = os.environ['tc_twitter_consumer_key']
consumer_secret = os.environ['tc_twitter_consumer_secret']
access_token_key = os.environ['tc_twitter_access_token_key']
access_token_secret = os.environ['tc_twitter_access_token_secret']

SQS_QUEUE_URL = os.environ['sqs_worker_queue_url']