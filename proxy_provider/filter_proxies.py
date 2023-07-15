import yaml
from itertools import cycle
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

# Mengatur rotasi pada daftar host
rotating_flex_hosts = cycle(flex_hosts)
rotating_game_hosts = cycle(game_hosts)
rotating_edukasi_hosts = cycle(edukasi_hosts)

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
        proxy['server'] = url_parts.netloc
        if proxy['server'].endswith('/'):
            proxy['server'] = proxy['server'][:-1]  # Menghapus spasi di akhir URL
        if proxy['server'] in flex_hosts:
            rotating_host = next(rotating_flex_hosts)
        elif proxy['server'] in game_hosts:
            rotating_host = next(rotating_game_hosts)
        elif proxy['server'] in edukasi_hosts:
            rotating_host = next(rotating_edukasi_hosts)
        else:
            continue
        proxy['server'] = f"{proxy['server']}{rotating_host}"
        filtered_proxies.append(proxy)

data['proxies'] = filtered_proxies

with open('free-akun-id.yaml', 'w') as file:
    yaml.dump(data, file, sort_keys=False, default_flow_style=False, allow_unicode=True)
