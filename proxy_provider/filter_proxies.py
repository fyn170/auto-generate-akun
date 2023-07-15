import yaml
from itertools import cycle
from urllib.parse import urlparse

# Daftar host yang ingin ditambahkan pada entri server
additional_hosts = [
    "sogood.linefriends.com",
    "104.17.3.81",
    "quiz.vidio.com",
    "cdn.noice.id",
    "cdn.appsflyer.com"
]

# Mengatur rotasi pada daftar host
rotating_hosts = cycle(additional_hosts)

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
        rotating_host = next(rotating_hosts)
        if proxy['server'].endswith('/'):
            proxy['server'] = proxy['server'][:-1]  # Menghapus spasi di akhir URL
        proxy['server'] = f"{proxy['server']}{rotating_host}"
        filtered_proxies.append(proxy)

data['proxies'] = filtered_proxies

with open('free-akun-id.yaml', 'w') as file:
    yaml.dump(data, file, sort_keys=False, default_flow_style=False, allow_unicode=True)
