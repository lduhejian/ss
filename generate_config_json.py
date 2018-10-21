import json

with open('data.json') as f:
    accounts = json.load(f)

    result = "{\"LaunchAtLogin\": false,\"ShadowsocksRunningMode\": \"auto\",\"ServerProfiles\": ["
    for account in accounts:
        ip = account['ip']
        port = account['port']
        password = account['password']
        encrypt = account['encrypt']
        item = "{ \"Id\": " + random.randrange(1,99999999999,1) + ", \"Method\": \"" + encrypt + "\", \"Plugin\": \"\",\"PluginOptions\": \"\",\"Password\": \"" + password + "\", \"remarks\": \"" + ip + "\", \"ServerHost\": \"" + ip + "\", \"ServerPort\": \"" + port + "\" },"
        # print(item)
        result = result + item

    result += "],\"ActiveServerProfileId\": \"7402A647-7042-45F3-AA47-3C0492F883E9\",\"LocalSocks5.ListenAddress.Old\": \"127.0.0.1\",\"LocalSocks5.ListenPort.Old\": 1080,\"ShadowsocksOn\": true,\"NSNavPanelExpandedSizeForSaveMode\": \"{712, 521}\",\"NSNavLastRootDirectory\": \"~\/Desktop\",\"LocalSocks5.ListenPort\": 1080,\"NSNavPanelExpandedSizeForOpenMode\": \"{712, 448}\",\"LocalSocks5.EnableVerboseMode\": true}"
    print(result)
