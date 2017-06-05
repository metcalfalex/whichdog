import boto3

def lambda_handler(event, context):
	s3 = boto3.resource('s3')
	raw = s3.meta.client.get_object(Bucket='20170602whichdog',Key='110_resultsraw.csv')
	return raw.read(10)
