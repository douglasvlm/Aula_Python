from bs4 import BeautifulSoup
import requests

site = requests.get('https://climatempo.com.br/').content

soup = BeautifulSoup(site, 'html.parser')

#print(soup.prettify())

temperatura = soup.find("h3", class_="title -gray-dark-2 _margin-b-10")
print(temperatura.string)

print(soup.title.string) #<title>
print(soup.a) #tag a
print(soup.p) #tag p
print(soup.find('admin'))
procurar = input('Qual TAG deseja encontrar na pagina : ')
print(soup.find(procurar))