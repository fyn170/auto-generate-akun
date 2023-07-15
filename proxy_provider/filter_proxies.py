import yaml
from urllib.parse import urlparse

with open('free-akun-id.yaml', 'r') as file:
    data = yaml.safe_load(file)

proxies = data.get('proxies', [])

filtered_proxies = []
for proxy in proxies:
    if (
        (proxy.get('type') == 'vmess' and proxy.get('network') == 'ws') or
        (proxy.get('type') == 'trojan' and proxy.get('network') == 'ws')
    ):
        url_parts = urlparse(proxy['server'])
        proxy['server'] = url_parts.netloc
        filtered_proxies.append(proxy)

data['proxies'] = filtered_proxies

with open('free-akun-id.yaml', 'w') as file:
    yaml.dump(data, file, sort_keys=False, default_flow_style=False, allow_unicode=True)
