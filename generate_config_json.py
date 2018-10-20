import json

with open('data.json') as f:
    accounts = json.load(f)["data"]

    result = "{\"configs\": ["
    for account in accounts:
        ip = account[1]
        port = account[2]
        encrypt = account[3]
        password = account[4]
        item = "{ \"method\": " + encrypt + ", \"password\": " + password + ", \"remarks\": \"shadowsocks\", \"server\": " + ip + ", \"server_port\": " + port + " },"
        # print(item)
        result = result + item
    result += "],\"localPort\": 1080, \"shareOverLan\": false }"
    print(result)
