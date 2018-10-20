import json

with open('data.json') as f:
    accounts = json.load(f)

    result = "{\"configs\": ["
    for account in accounts:
        ip = account['ip']
        port = account['port']
        password = account['password']
        encrypt = account['encrypt']
        item = "{ \"method\": \"" + encrypt + "\", \"password\": \"" + password + "\", \"remarks\": \"" + ip + "\", \"server\": \"" + ip + "\", \"server_port\": \"" + port + "\" },"
        # print(item)
        result = result + item
    result += "],\"localPort\": 1080, \"shareOverLan\": false }"
    print(result)
