import json
import os

file_list = os.listdir('.')
resultlist = []
with open('accounts.json', 'w') as result_file:
    for file in file_list:
        if '.maFile' in file:
            with open(file, 'r') as f:
                account = json.loads(f.readline())
                result = {
                    'name': account['account_name'],
                    'shared': account['shared_secret']
                }
                resultlist.append(result)
    print(json.dump(resultlist, result_file, indent = 2, ensure_ascii = False))
