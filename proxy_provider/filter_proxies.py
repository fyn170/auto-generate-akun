import yaml

with open('free-akun-id.yaml', 'r') as file:
    data = yaml.safe_load(file)

proxies = data['proxies']

filtered_proxies = [proxy for proxy in proxies if (
    proxy.get('type') in ['vmess', 'trojan'] and
    proxy.get('network') == 'ws' and
    proxy.get('country') == '🇮🇩'
)]

data['proxies'] = filtered_proxies

with open('free-akun-id.yaml', 'w') as file:
    yaml.dump(data, file)
