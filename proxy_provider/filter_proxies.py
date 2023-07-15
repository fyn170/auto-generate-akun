import yaml

with open('free-akun-id.yaml', 'r') as file:
    data = yaml.safe_load(file)

proxies = data['proxies']

filtered_proxies = []
for proxy in proxies:
    if proxy.get('type') == 'vmess' and proxy.get('network') == 'ws':
        filtered_proxy = {
            'name': proxy['name'],
            'server': proxy['server'],
            'port': proxy['port'],
            'type': proxy['type'],
            'uuid': proxy['uuid'],
            'alterId': proxy.get('alterId', 0),
            'cipher': proxy.get('cipher', 'auto'),
            'tls': proxy.get('tls', False),
            'skip-cert-verify': proxy.get('skip-cert-verify', False),
            'servername': proxy.get('servername', ''),
            'network': proxy['network'],
            'ws-opts': {
                'path': proxy['ws-opts']['path'],
                'headers': proxy['ws-opts'].get('headers', {})
            },
            'udp': proxy.get('udp', False)
        }
        filtered_proxies.append(filtered_proxy)

data['proxies'] = filtered_proxies

with open('free-akun-id.yaml', 'w') as file:
    yaml.dump(data, file)
