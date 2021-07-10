import ipaddress

ip = '192.168.0.1'
rede = "192.168.0.0/24"

endereco = ipaddress.ip_address(ip)
rede = ipaddress.ip_network(rede)
print(endereco)
print(endereco+ 2000)
print(rede)

for ip in rede:
    print(ip)