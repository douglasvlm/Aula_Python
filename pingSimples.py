import os #importa recursos do SO
print("#" * 60)
#Variavel que recebe o ip
ip_ou_host = input('Digite o ip : ')
print("-" * 60)
#Chamada do SO system comando ping numero de pacotes 6
os.system('ping -n 6 {}' .format(ip_ou_host))
print("-" * 60)