import requests
from bs4 import BeautifulSoup
import urllib

def run():
    for i in range (50, 56):
        response = requests.get('https://xkcd.com/{}'.format(i))
        sopa = BeautifulSoup(response.content, 'html.parser')
        contenedor_imagen = sopa.find(id = 'comic')

        url_imagen = contenedor_imagen.find('img') ['src']
        nombre = url_imagen.split('/')[-1]
        print('Descangando la imagen {}'.format(nombre))
        urllib.urlretrieve('https:{}'.format(url_imagen), nombre)

if __name__ == "__main__":
    run()