import csv
import boto3

def lambda_handler(event, context):
    s3 = boto3.resource('s3')
    obj = s3.Object('20170602whichdog','110_resultsraw.csv')
    response = obj.get()
    lines = response[u'Body'].read().decode('utf-8').split('\n')
    csvfile = csv.DictReader(lines, delimiter='|',fieldnames=['date','dogyes','dogno'])
    dogyes = [int(row['dogyes']) for row in csvfile]
    csvfile = csv.DictReader(lines, delimiter='|',fieldnames=['date','dogyes','dogno'])
    dogno = [int(row['dogno']) for row in csvfile]
    dogall = sorted(set(dogyes + dogno))
    dogyes_count = [dogyes.count(n) for n in dogall]
    dogall_count = [dogyes.count(n) + dogno.count(n) for n in dogall]
    score = [(dogyes_count[i] - dogall_count[i]/2 + 5)/10 if dogall_count[i] < 10 else dogyes_count[i] / dogall_count[i] for i, n in enumerate(dogall)]
    # output to json and save to s3: dogall | dogyes_count | dogall_count | score
    # js json to table: http://jsfiddle.net/URU5G/1/
    return score
