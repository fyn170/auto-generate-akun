import yaml

with open('free-akun-id.yaml', 'r') as file:
    data = yaml.safe_load(file)

proxies = data['proxies']

filtered_proxies = []
for proxy in proxies:
    if proxy.get('type') in ['trojan', 'vmess'] and proxy.get('network') == 'ws':
        filtered_proxies.append(proxy)

data['proxies'] = filtered_proxies

with open('free-akun-id.yaml', 'w') as file:
    yaml.dump(data, file)
