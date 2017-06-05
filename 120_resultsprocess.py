import csv
import boto3

def lambda_handler(event, context):
    s3 = boto3.resource('s3')
    obj = s3.Object('20170602whichdog','110_resultsraw.csv')
    response = obj.get()
    lines = response[u'Body'].read()
    # lines = response[u'Body'].read().split()
    # a1 = [row['dogyes'] for row in csv.DictReader(lines, delimiter='|',fieldnames=['date','dogyes','dogno'])]
    # a1 = [row['dogyes'] for row in csv.DictReader(lines, delimiter='|',fieldnames=['date','dogyes','dogno'])]
    # for row in csv.DictReader(response['Body'], delimiter='|',fieldnames=['date','dogyes','dogno']):
        # a1 = row['dogyes']
        # a1 = 'yes'
    return str(lines)
    # return a1
    # return str(response['Body'])
    # return str(response)
