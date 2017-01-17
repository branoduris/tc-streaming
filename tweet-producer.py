import boto3
import json
import tweepy

import default_config

# Create the Boto3 Session
session = boto3.Session(profile_name=default_config.AWS_DEFAULT_PROFILE)
sqs_client = session.client('sqs')


## twitter credentials

consumer_key = default_config.consumer_key
consumer_secret = default_config.consumer_secret
access_token_key = default_config.access_token_key
access_token_secret = default_config.access_token_secret

# Set the Queue URL
queue_url = default_config.SQS_QUEUE_URL


class TwitterStreamListener(tweepy.StreamListener):
    """ A listener handles tweets are the received from the stream. """

    def on_status(self, status):
        json_str = json.dumps(status._json)
        print(json_str)
        response = sqs_client.send_message(
            QueueUrl=queue_url,
            MessageBody=json_str
        )
        print(response)
        return True

    def on_error(self, status_code):
        if status_code == 403:
            print("The request is understood, but it has been refused or access is not allowed. Limit is maybe reached")
            return False
        else:
            # TODO maybe add some log?
            print(status_code)


if __name__ == '__main__':

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.secure = True
    auth.set_access_token(access_token_key, access_token_secret)

    api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True, retry_count=10, retry_delay=5, retry_errors=5)

    streamListener = TwitterStreamListener()

    myStream = tweepy.Stream(auth=api.auth, listener=streamListener)
    myStream.userstream()

