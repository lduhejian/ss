#! /usr/bin/fish

curl -x socks5h://localhost:1080 "https://do.ishadowx.net/" -H 'User-Agent: Mozilla/5.0 (iPhone; CPU iPhone OS 10_2 like Mac OS X) AppleWebKit/602.3.12 (KHTML, like Gecko) Mobile/14C92'  -H 'Accept-Language: zh-cn'   > html
python parse_html_to_array.py > data.json
python generate_config_json.py > gui-config.json
