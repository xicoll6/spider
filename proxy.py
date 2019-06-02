import requests
import threading
import time

def WhatIsmyIp(proxies):
    url = "http://ip.chinaz.com/getip.aspx"
    req_head = {'Host': 'ip.chinaz.com', 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
     'Accept-Encoding': 'gzip, deflate, sdch', 'Upgrade-Insecure-Requests': '1',
     'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36',
     'Connection': 'keep-alive', 'Accept-Language': 'zh-TW,zh;q=0.8,en-US;q=0.6,en;q=0.4,zh-CN;q=0.2'}
    try:
        r = requests.get(url, headers=req_head, proxies=proxies, timeout=5).text
    except requests.Timeout:
        return None
    except:
        return None
    try:
        # 判断是否可用
        r_ip = r.strip()
    except:
        print(r)
        return None
    return r_ip


def is_valid(ip_port):
    proxies = {
        "http": "http://" + ip_port
    }
    t_ip = WhatIsmyIp(proxies)
    if t_ip == ip_port.split(":")[0]:
        with open("v_record.txt","a") as f:
            f.write(ip_port+"\n")
        return True
    else:
        return False

with open("record.txt","r") as f:
    ip_list = f.readlines()

for ip in ip_list:
    ip = ip.strip()
    t = threading.Thread(target=is_valid, args=(ip,))
    t.setDaemon(True)
    t.start()

while not threading.activeCount() == 1:
    time.sleep(2)
    print(threading.activeCount())
    #print(is_valid("27.159.124.80:8118"))


