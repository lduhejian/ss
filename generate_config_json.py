import json
import uuid

try:
    with open('last-gui-config.json') as f1:
        gui_config = json.load(f1)
        LastActiveServerProfileId = gui_config['ActiveServerProfileId']
except:
    LastActiveServerProfileId = "not find"
useLast = False
with open('data.json') as f:
    accounts = json.load(f)
    result = "{\"LaunchAtLogin\": false,\"ShadowsocksRunningMode\": \"auto\",\"ServerProfiles\": ["
    ActiveServerProfileId = LastActiveServerProfileId
    for account in accounts:
        ip = account['ip']
        port = account['port']
        password = account['password']
        encrypt = account['encrypt']
        ServerProfileId = account['ip']+'-'+account['port']
        ActiveServerProfileId = ServerProfileId
        if ServerProfileId == LastActiveServerProfileId:
            useLast = True
        item = "{ \"Id\": \"" + ServerProfileId + "\", \"Method\": \"" + encrypt + "\", \"Plugin\": \"\",\"PluginOptions\": \"\",\"Password\": \"" + password + "\", \"Remark\": \"" + ip + "\", \"ServerHost\": \"" + ip + "\", \"ServerPort\": " + port + " },"
        # print(item)
        result = result + item
    if  result[-1] == ",":
        result = result[:-1]
    if  useLast == True:
        ActiveServerProfileId = LastActiveServerProfileId
    result = result + "],\"ActiveServerProfileId\": \"" + ActiveServerProfileId + "\",\"LocalSocks5.ListenAddress.Old\": \"127.0.0.1\",\"LocalSocks5.ListenPort.Old\": 1080,\"ShadowsocksOn\": true,\"NSNavPanelExpandedSizeForSaveMode\": \"{712, 521}\",\"NSNavLastRootDirectory\": \"~\/Desktop\",\"LocalSocks5.ListenPort\": 1080,\"NSNavPanelExpandedSizeForOpenMode\": \"{712, 448}\",\"LocalSocks5.EnableVerboseMode\": true}"
    print(result)
