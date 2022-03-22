import requests
import json

def get_proxies():
    print("Downloading proxies...")
    save_path = 'pixivScrape/proxy_list.txt'
    url = 'https://proxylist.geonode.com/api/proxy-list?'
    gets = ['limit=200&page=1&filterUpTime=100&speed=medium&protocols=https%2Csocks4%2Csocks5&anonymityLevel=elite&anonymityLevel=anonymous',
            'limit=200&page=1&filterUpTime=100&speed=fast&protocols=https%2Csocks4%2Csocks5&anonymityLevel=elite&anonymityLevel=anonymous']

    proxyjsons = []
    for get in gets:
        proxy_json = requests.get(url + get).text
        proxy_json = json.loads(proxy_json)
        proxyjsons.extend(proxy_json["data"])

    # CREATING PROXY DICT
    prxy_list = []    
    for proxy in proxyjsons:
        protocol = proxy["protocols"][0]
        ip_ = proxy["ip"]
        port = proxy["port"]
        proxy_str = protocol + "://" + ip_ + ":" + port
        prxy_list.append(proxy_str)    
            
    with open(save_path, 'w') as f:
        for proxy_str in prxy_list:
            f.write(proxy_str + "\n")
            
    print('Saved {} proxies to {}'.format(len(prxy_list), save_path))
            
if __name__=="__main__":
    get_proxies()