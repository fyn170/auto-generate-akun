import yaml

with open('free-akun-id.yaml', 'r') as file:
    data = yaml.safe_load(file)

proxies = data['proxies']

filtered_proxies = []
for proxy in proxies:
    if proxy.get('type') in ['trojan', 'vmess'] and proxy.get('network') == 'ws':
        filtered_proxy = {
            'name': proxy['name'],
            'type': proxy['type'],
            'server': proxy['server'],
            'port': proxy['port'],
            'cipher': proxy.get('cipher', 'auto'),
            'uuid': proxy.get('uuid', ''),
            'alterId': proxy.get('alterId', 0),
            'network': proxy['network'],
            'ws-opts': {
                'path': proxy.get('ws-opts', {}).get('path', ''),
            }
        }
        filtered_proxies.append(filtered_proxy)

data['proxies'] = filtered_proxies

with open('free-akun-id.yaml', 'w') as file:
    yaml.dump(data, file)
