import json
print('=' * 97)
print('DN'.ljust(50), 'Description'.ljust(20), 'Speed'.ljust(10), 'MTU'.ljust(10))
print('-' * 50, '-' * 20, '-' * 10, '-' * 10)


json_input = open('sample-data.json', encoding='utf8')
answer = json.load(json_input)
data = answer["imdata"]

for i in data:
    abc = i['l1PhysIf']["attributes"]
    print(abc["dn"].ljust(50), abc["speed"].ljust(20), abc["descr"].ljust(10), abc["mtu"].ljust(10))