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

for host in flex_hosts:
    proxy = {
        'name': f"vpn-{host}",
        'server': host,
        'port': 80,
        'type': 'vmess',
        'uuid': '',
        'alterId': 0,
        'cipher': 'auto',
        'tls': False,
        'skip-cert-verify': True,
        'servername': '',
        'network': 'ws',
        'ws-opts': {
            'path': '/vmess',
            'headers': {
                'Host': host
            }
        },
        'udp': True
    }
    proxies.append(proxy)

for host in game_hosts:
    proxy = {
        'name': f"vpn-{host}",
        'server': host,
        'port': 80,
        'type': 'trojan',
        'password': '',
        'skip-cert-verify': True,
        'sni': 'null',
        'network': 'ws',
        'ws-opts': {
            'path': '/trojan',
            'headers': {
                'Host': host
            }
        },
        'udp': True
    }
    proxies.append(proxy)

for host in edukasi_hosts:
    proxy = {
        'name': f"vpn-{host}",
        'server': host,
        'port': 80,
        'type': 'vmess',
        'uuid': '',
        'alterId': 0,
        'cipher': 'auto',
        'tls': False,
        'skip-cert-verify': True,
        'servername': '',
        'network': 'ws',
        'ws-opts': {
            'path': '/vmess',
            'headers': {
                'Host': host
            }
        },
        'udp': True
    }
    proxies.append(proxy)

data['proxies'] = proxies

with open('free-akun-id.yaml', 'w') as file:
    yaml.dump(data, file, sort_keys=False, default_flow_style=False, allow_unicode=True)
