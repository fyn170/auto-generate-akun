import ruamel.yaml

with open('free-akun-id.yaml', 'r') as file:
    data = ruamel.yaml.round_trip_load(file)

proxies = data['proxies']

filtered_proxies = []
for proxy in proxies:
    if proxy.get('type') == 'vmess' and proxy.get('network') == 'ws':
        filtered_proxy = ruamel.yaml.comments.CommentedMap()
        filtered_proxy['name'] = proxy['name']
        filtered_proxy['server'] = proxy['server']
        filtered_proxy['port'] = proxy['port']
        filtered_proxy['type'] = proxy['type']
        filtered_proxy['uuid'] = proxy['uuid']
        filtered_proxy['alterId'] = proxy.get('alterId', 0)
        filtered_proxy['cipher'] = proxy.get('cipher', 'auto')
        filtered_proxy['tls'] = proxy.get('tls', False)
        filtered_proxy['skip-cert-verify'] = proxy.get('skip-cert-verify', False)
        filtered_proxy['servername'] = proxy.get('servername', '')
        filtered_proxy['network'] = proxy['network']
        filtered_proxy['ws-opts'] = ruamel.yaml.comments.CommentedMap()
        filtered_proxy['ws-opts']['path'] = proxy['ws-opts']['path']
        filtered_proxy['ws-opts']['headers'] = proxy['ws-opts'].get('headers', ruamel.yaml.comments.CommentedMap())
        filtered_proxy['udp'] = proxy.get('udp', False)
        filtered_proxies.append(filtered_proxy)

data['proxies'] = filtered_proxies

with open('free-akun-id.yaml', 'w') as file:
    ruamel.yaml.round_trip_dump(data, file)
