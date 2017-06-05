import csv
import boto3
# import json

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
        # for lst in lists:
        lst2 = [item[i] for item in lists]
        dctlst.append(dict(zip(keys,lst2)))
    # for i in enumerate(dogall):
        # lst2 = [lst[i] for lst in lists]
        # dctlst.append(dict(zip(keys,lst2)))
        # for lst in lists:
            # x = dict(zip(keys,lst))
            # dctlst.append(dict(zip(keys,lst)))
        # lst2 = [lst[i] for lst in lists]
        # dctlst.append(dict(zip(keys,lst2)))
    # lst2 = [lst[item] for lst in lists for item in enumerate(dogall)]
    # output to json and save to s3: dogall | dogyes_count | dogall_count | score
    # d = {}
    # d['dogyes']=n for n in dogall
    # dogall_json = json.dumps(dogall)
    # dogall_json = dict(zip('dogall',dogall))
    # dogall_dict = {'dogall': value for value in dogall}
    # d = {k:v for k, v in dogall}
    # dogall_dict_list = [dict(str(value)) for value in dogall]
    # js json to table: http://jsfiddle.net/URU5G/1/
    # return x
    return dctlst
    # return lst2
    # return lists[0]
