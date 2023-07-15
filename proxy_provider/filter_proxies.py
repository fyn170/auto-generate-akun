import yaml
from urllib.parse import urlparse
import random
import string

with open('free-akun-sg.yaml', 'r') as file:
    data = yaml.safe_load(file)

proxies = data.get('proxies', [])

filtered_proxies = []
bug_servers = [
    '104.17.3.81',
    'quiz.vidio.com',
    'zendesk1.grab.com',
    'cdn.appsflyer.com',
    'www.noice.id',
    'cdn.noice.id',
    'sogood.linefriends.com',
    'poe.garena.com'
]

for proxy in proxies:
    if (
        proxy.get('network') == 'ws' and
        proxy.get('port') == 80 and
        'ws-opts' in proxy and
        'path' in proxy['ws-opts'] and
        'headers' in proxy['ws-opts']
    ):
        url_parts = urlparse(proxy['server'])
        host = url_parts.netloc.split(':')[0]
        random_name = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
        proxy['name'] = f"\U0001F1F8\U0001F1EC {random_name}"
        proxy['server'] = random.choice(bug_servers)
        filtered_proxies.append(proxy)

data['proxies'] = filtered_proxies

with open('free-akun-sg.yaml', 'w') as file:
    yaml.dump(data, file, sort_keys=False, default_flow_style=False, allow_unicode=True)
