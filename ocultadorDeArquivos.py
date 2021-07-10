import ctypes

atributo_ocultar = 0x02

pasta = input("Digite o caminho da pasta a ser ocultada ex(c:/pastas): ")

#retorno = ctypes.windll.kernel32.SetFileAttributesW('texteocultar.txt', atributo_ocultar)
retorno = ctypes.windll.kernel32.SetFileAttributesW(pasta, atributo_ocultar)

if retorno:
    print("Arquivo ocultado")
else:
    print("Arquivo não foi ocultado")