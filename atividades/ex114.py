import urllib
import urllib.request

try:
    site = urllib.request.urlopen('https://www.twitch.tv')
except:
    print('deu erro')
else:
    print('Acessado com sucesso')
    print(site.read)
