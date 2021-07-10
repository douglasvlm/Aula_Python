import os #importa recursos do SO
import time

with open('host.txt') as file:
    dump = file.read()
    dump = dump.splitlines()
    for ip in dump:
        print('Verificando ip: ', ip)
        print("-" * 60)
        #print(ip)
        os.system('ping -n 2 {}'.format(ip))
        print("-" * 60)
        time.sleep(5)

