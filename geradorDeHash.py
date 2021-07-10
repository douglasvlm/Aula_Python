import hashlib

#
# resultado = hashlib.md5(b'Python Security')
# string =  hashlib.md5(string.encode('utf-8'))
#
# print('O hash da string é: ', resultado.hexdigest())
# print('O hash da string digita é : ', string.hexdigest())

string = input('Digite o texto a ser gerado a hash: ')

menu = int(input('''### Menu - Escolha o tipo de hash
                1) MD5
                2) SHA1
                3)SHA256
                4)SHA512
                Digite o número: '''))
if menu == 1:
    resultado = hashlib.md5(string.encode('utf-8'))
    print('A hash MD5 da string : ', string, ' é: ', resultado.hexdigest())
elif menu == 2:
    resultado = hashlib.sha1(string.encode('utf-8'))
    print('A hash sha1 da string : ', string, ' é ', resultado.hexdigest())
elif menu == 3:
    resultado = hashlib.sha256(string.encode('utf-8'))
    print('A hash sha256 da string : ', string, ' é ', resultado.hexdigest())
elif menu == 4:
    rresultado = hashlib.sha512(string.encode('utf-8'))
    print('A hash sha512 da string : ', string, ' é ', resultado.hexdigest())
else:
    print('Algo não deu certo!')