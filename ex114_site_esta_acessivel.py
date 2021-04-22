"EX113 Site está acessível?"

import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except urllib.error.URLError:
    print('O site pudm não está acessível no momento!')
else:
    print('O site pudim está acessível!')
    print(site.read())
