import json
import uuid

with open('data.json') as f:
    accounts = json.load(f)

    result = "{\"LaunchAtLogin\": false,\"ShadowsocksRunningMode\": \"auto\",\"ServerProfiles\": ["
    for account in accounts:
        ip = account['ip']
        port = account['port']
        password = account['password']
        encrypt = account['encrypt']
        item = "{ \"Id\": \"" + str(uuid.uuid1()).upper() + "\", \"Method\": \"" + encrypt + "\", \"Plugin\": \"\",\"PluginOptions\": \"\",\"Password\": \"" + password + "\", \"Remark\": \"" + ip + "\", \"ServerHost\": \"" + ip + "\", \"ServerPort\": " + port + " },"
        # print(item)
        result = result + item
    if  result[-1] == ",":
        result = result[:-1]
    result += "],\"ActiveServerProfileId\": \"7402A647-7042-45F3-AA47-3C0492F883E9\",\"LocalSocks5.ListenAddress.Old\": \"127.0.0.1\",\"LocalSocks5.ListenPort.Old\": 1080,\"ShadowsocksOn\": true,\"NSNavPanelExpandedSizeForSaveMode\": \"{712, 521}\",\"NSNavLastRootDirectory\": \"~\/Desktop\",\"LocalSocks5.ListenPort\": 1080,\"NSNavPanelExpandedSizeForOpenMode\": \"{712, 448}\",\"LocalSocks5.EnableVerboseMode\": true}"
    print(result)
