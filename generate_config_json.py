import json
import uuid

with open('data.json') as f:
    accounts = json.load(f)
    result = "{\"LaunchAtLogin\": false,\"ShadowsocksRunningMode\": \"auto\",\"ServerProfiles\": ["
    ActiveServerProfileId = ""
    for account in accounts:
        ip = account['ip']
        port = account['port']
        password = account['password']
        encrypt = account['encrypt']
        ServerProfileId = str(uuid.uuid1()).upper()
        ActiveServerProfileId = ServerProfileId
        item = "{ \"Id\": \"" + ServerProfileId + "\", \"Method\": \"" + encrypt + "\", \"Plugin\": \"\",\"PluginOptions\": \"\",\"Password\": \"" + password + "\", \"Remark\": \"" + ip + "\", \"ServerHost\": \"" + ip + "\", \"ServerPort\": " + port + " },"
        # print(item)
        result = result + item
    if  result[-1] == ",":
        result = result[:-1]
    result = result + "],\"ActiveServerProfileId\": \"" + ActiveServerProfileId + "\",\"LocalSocks5.ListenAddress.Old\": \"127.0.0.1\",\"LocalSocks5.ListenPort.Old\": 1080,\"ShadowsocksOn\": true,\"NSNavPanelExpandedSizeForSaveMode\": \"{712, 521}\",\"NSNavLastRootDirectory\": \"~\/Desktop\",\"LocalSocks5.ListenPort\": 1080,\"NSNavPanelExpandedSizeForOpenMode\": \"{712, 448}\",\"LocalSocks5.EnableVerboseMode\": true}"
    print(result)
