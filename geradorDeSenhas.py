import random, string

tamanho = int(input('Digite o tamanho da senha: '))#16
chars = string.ascii_letters + string.digits + 'ç!@#$%¨&*()_+'

rnd = random.SystemRandom() #os.urandom
print(''.join(rnd.choice(chars) for i in range(tamanho)))
