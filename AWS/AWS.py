import boto3

sns = boto3.client('sns', region_name='eu-central-1')
topic_arn = "arn:aws:sns:eu-central-1:266061335929:development-topic"
token = "fcf0bf57-07c9-4c8f-be63-990faaae8d3c"

"""
response = sns.subscribe(
    TopicArn=topic_arn,
    Protocol='email',
    Endpoint='daniel@supracontrol.com'
)


response = sns.publish(
    TopicArn=topic_arn,
    Message='Hello from Amazon SNS!'
)
"""

response = sns.confirm_subscription(
    TopicArn=topic_arn,
    Token=token
    # AuthenticateOnUnsubscribe='string'
)

print("All is ok")