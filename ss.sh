#! /usr/bin/fish


set timestamp (date +%s)
curl -x socks5h://localhost:1080 "https://free-ss.site/ss.json?_=$timestamp000" > data.json
set gui_json (python generate_config_json.py)
echo $gui_json > gui-config.json
