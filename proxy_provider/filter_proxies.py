import yaml
from urllib.parse import urlparse
import random
import string

files = ['free-akun-id.yaml', 'free-akun-sg.yaml']

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

random.shuffle(bug_servers)

for file_name in files:
    with open(file_name, 'r') as file:
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
            random_name = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
            proxy['name'] = f"\U0001F1EE\U0001F1E9 {random_name}"
            proxy['server'] = bug_servers.pop(0)
            filtered_proxies.append(proxy)

    data['proxies'] = filtered_proxies

    with open(file_name, 'w') as file:
        yaml.dump(data, file, sort_keys=False, default_flow_style=False, allow_unicode=True)
