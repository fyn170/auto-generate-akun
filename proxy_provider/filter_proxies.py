import yaml
from urllib.parse import urlparse

with open('free-akun-id.yaml', 'r') as file:
    data = yaml.safe_load(file)

proxies = data.get('proxies', [])

filtered_proxies = []
for proxy in proxies:
    if (
        proxy.get('network') == 'ws' and
        proxy.get('port') == 80
    ):
        url_parts = urlparse(proxy['server'])
        host = url_parts.netloc.split(':')[0]
        proxy['server'] = host
        filtered_proxies.append(proxy)

data['proxies'] = filtered_proxies

with open('free-akun-id.yaml', 'w') as file:
    yaml.dump(data, file, sort_keys=False, default_flow_style=False, allow_unicode=True)
