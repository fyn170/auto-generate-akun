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
            'uuid': proxy.get('uuid', ''),
            'alterId': proxy.get('alterId', 0),
            'cipher': proxy.get('cipher', 'auto'),
            'tls': proxy.get('tls', False),
            'skip-cert-verify': proxy.get('skip-cert-verify', False),
            'network': proxy['network'],
            'ws-opts': {
                'path': proxy.get('ws-opts', {}).get('path', ''),
                'headers': proxy.get('ws-opts', {}).get('headers', {})
            },
            'udp': proxy.get('udp', False)
        }
        if proxy.get('type') == 'trojan':
            filtered_proxy['password'] = proxy.get('password', '')
            filtered_proxy['sni'] = proxy.get('sni', '')

        filtered_proxies.append(filtered_proxy)

data['proxies'] = filtered_proxies

with open('free-akun-id.yaml', 'w') as file:
    yaml.dump(data, file)
