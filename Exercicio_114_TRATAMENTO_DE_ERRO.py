import urllib
import urllib.request
try:
    site = urllib.request.urlopen('http://www.youtube.com')
except (urllib.error.URLError):
    print('O youtube não está acessivel no memento')
else:
    print('consegui acessar o site do youtube com sucesso')