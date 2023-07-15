import yaml
from urllib.parse import urlparse

# Daftar host untuk paket flex
flex_hosts = [
    "sogood.linefriends.com",
    "www.noice.id",
    "cdn.noice.id",
    "zendesk1.grab.com"
]

# Daftar host untuk paket game
game_hosts = [
    "cdn.appsflyer.com",
    "poe.garena.com"
]

# Daftar host untuk paket edukasi
edukasi_hosts = [
    "104.17.3.81",
    "104.18.3.2",
    "104.18.2.2"
]

with open('free-akun-id.yaml', 'r') as file:
    data = yaml.safe_load(file)

proxies = data.get('proxies', [])

filtered_proxies = []
for proxy in proxies:
    if (
        (proxy.get('type') == 'vmess' or proxy.get('type') == 'trojan') and
        proxy.get('network') == 'ws' and
        proxy.get('port') == 80
    ):
        url_parts = urlparse(proxy['server'])
        host = url_parts.netloc.split(':')[0]
        if host in flex_hosts:
            proxy['server'] = host
        elif host in game_hosts:
            proxy['server'] = host
        elif host in edukasi_hosts:
            proxy['server'] = host
        else:
            continue
        filtered_proxies.append(proxy)

data['proxies'] = filtered_proxies

with open('free-akun-id.yaml', 'w') as file:
    yaml.dump(data, file, sort_keys=False, default_flow_style=False, allow_unicode=True)
