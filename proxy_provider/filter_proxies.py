import yaml

with open('free-akun-id.yaml', 'r') as file:
    data = yaml.safe_load(file)

proxies = data.get('proxies', [])

filtered_proxies = []
for proxy in proxies:
    if proxy.get('network') == 'ws':
        filtered_proxies.append(proxy)

data['proxies'] = filtered_proxies

with open('free-akun-id.yaml', 'w') as file:
    yaml.dump(data, file)

with open('free-akun-id.yaml', 'w') as file:
    file.write("proxies:\n")
    for proxy in filtered_proxies:
        file.write(f"  - name: {proxy['name']}\n")
        file.write(f"    server: {proxy['server']}\n")
        file.write(f"    port: {proxy['port']}\n")
        file.write(f"    type: {proxy['type']}\n")
        file.write(f"    uuid: {proxy['uuid']}\n")
        file.write(f"    alterId: {proxy.get('alterId', 0)}\n")
        file.write(f"    cipher: {proxy.get('cipher', 'auto')}\n")
        file.write(f"    tls: {proxy.get('tls', False)}\n")
        file.write(f"    skip-cert-verify: {proxy.get('skip-cert-verify', False)}\n")
        file.write(f"    servername: {proxy.get('servername', '')}\n")
        file.write(f"    network: {proxy['network']}\n")
        file.write(f"    ws-opts:\n")
        file.write(f"      path: {proxy['ws-opts']['path']}\n")
        file.write("      headers:\n")
        for header, value in proxy['ws-opts'].get('headers', {}).items():
            file.write(f"        {header}: {value}\n")
        file.write(f"    udp: {proxy.get('udp', False)}\n")
        file.write("\n")
