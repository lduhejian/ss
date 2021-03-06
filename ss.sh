#! /usr/bin/bash

# 获取服务器配置列表
curl -x socks5h://localhost:1080 "https://do.ishadowx.net/" -H 'User-Agent: Mozilla/5.0 (iPhone; CPU iPhone OS 10_2 like Mac OS X) AppleWebKit/602.3.12 (KHTML, like Gecko) Mobile/14C92'  -H 'Accept-Language: zh-cn'   > html
/usr/local/bin/python parse_html_to_array.py > data.json

if [ -s data.json ]
then
    # 首先将现有的配置导出
    defaults export com.qiuyuzhou.ShadowsocksX-NG last-gui-config.plist
    # 将 plist 二进制转成可读的 json 文件
    plutil -convert json -o last-gui-config.json last-gui-config.plist
    # 生成新的 gui-config.json
    /usr/local/bin/python generate_config_json.py > gui-config.json

    # 将服务器配置列表导入 ShadowsocksX-NG
    plutil -convert xml1 gui-config.json -o gui-config.plist
    defaults import com.qiuyuzhou.ShadowsocksX-NG gui-config.plist

    # 重启 ShadowsocksX-NG
    osascript -e 'quit app "ShadowsocksX-NG"'
    sleep 1
    open -a shadowsocksx-ng
    sleep 1
    osascript -e 'display notification "更新了 ss 账号"'
else
    osascript -e 'display notification "获取账号失败"'
fi
