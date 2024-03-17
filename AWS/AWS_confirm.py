import boto3

# Create an SNS client
sns = boto3.client('sns','eu-central-1')

# Replace 'YOUR_SUBSCRIPTION_ARN' with the actual ARN of the subscription you want to confirm
subscription_arn = 'arn:aws:sns:eu-central-1:266061335929:development-topic'

# Replace 'YOUR_TOKEN' with the actual token received in the subscription confirmation message
token = 'fcf0bf57-07c9-4c8f-be63-990faaae8d3c'

# Call the `confirm_subscription` method to confirm the subscription
# Confirmation
response = sns.confirm_subscription(
  TopicArn=subscription_arn, 
  Token=token, 
  AuthenticateOnUnsubscribe='true'
)

# Print the response to confirm if the subscription was successful
print(response)
