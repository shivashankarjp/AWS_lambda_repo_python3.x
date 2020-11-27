import boto3
client = boto3.client('sns')

def lambda_handler(event, context):
	topic_arn='arn:aws:sns:us-east-1:12345678912:example'
	message='please look into your ec2 console some event is happening ......'
	client.publish(TopicArn=topic_arn,Message=message)