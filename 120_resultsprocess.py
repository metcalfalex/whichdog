import csv
import boto3
import json

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
    lists = [dogall,dogyes_count,dogall_count,score]
    keys = ['dogall','dogyes_count','dogall_count','score']
    dctlst = []
    for i,n in enumerate(dogall):
        lst2 = [item[i] for item in lists]
        dctlst.append(dict(zip(keys,lst2)))
    with open("/tmp/130_resultsprocessed.json","w") as outfile:
        json.dump(dctlst, outfile)
    s3.meta.client.upload_file('/tmp/130_resultsprocessed.json', '20170602whichdog', '130_resultsprocessed.json')
    # js json to table: http://jsfiddle.net/URU5G/1/
    return None