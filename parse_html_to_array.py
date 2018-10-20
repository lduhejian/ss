from bs4 import BeautifulSoup
import re
import json

with open("html") as html:
    soup = BeautifulSoup(html)
    containers = soup.findAll("div", {"class": "portfolio-items"})
    accounts = []
    for container in containers:
        items = container.findAll("div", {"class": "portfolio-item"})
        for item in items:
            ips = item.findAll("span", {"id": re.compile("[ipu*|ips*]")})
            ports = item.findAll("span", {"id": re.compile("port*")})
            passwords = item.findAll("span", {"id": re.compile("pws*")})
            encrypts = item(text=re.compile("Method*"))
            entrys = item.findAll("h4")
            if len(ips) > 0 and len(ports) > 0 and len(passwords) > 0 and len(encrypts) > 0 and len(entrys) >= 5:
                ip = ips[0].text.strip(' \t\n\r')
                port = ports[0].text.strip(' \t\n\r')
                password = passwords[0].text.strip(' \t\n\r')
                encrypt = encrypts[0].strip(' \t\n\r')
                account = {}
                account['ip'] = ip
                account['port'] = port
                account['password'] = password
                account['encrypt'] = encrypt.replace("Method:", "")
                accounts.append(account)
    print json.dumps(accounts)
