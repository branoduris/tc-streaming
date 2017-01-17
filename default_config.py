import os

# Default app config
AWS_REGION = 'us-west-2'

consumer_key = os.environ['tc_twitter_consumer_key'] # 'OsQA2BjCokitlGmPgZ5Vxjygk'
consumer_secret = os.environ['tc_twitter_consumer_secret'] # 'ZIqZHvYNffPbkSA2zTbj63rVIn7Y7vljtAoGR6c9IjogDnZKgZ'
access_token_key = os.environ['tc_twitter_access_token_key'] # '702797682335731712-HLOGL4Xjz9SuUzOGCSwaVhvTGeIqSHK'
access_token_secret = os.environ['tc_twitter_access_token_secret'] # 'mzie5dju8Crd4JFNaPPmcXHrQWgBid5seRrwoxv9dnr76'

SQS_QUEUE_URL = os.environ['sqs_worker_queue_url'] #'https://us-west-2.queue.amazonaws.com/545157427766/awseb-e-8ugv4byjnp-stack-AWSEBWorkerQueue-T6ANROMR84J6'