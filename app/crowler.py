from urllib.request import urlopen
from bs4 import BeautifulSoup


def get_data(content):
    page = urlopen(f'https://michaelis.uol.com.br/moderno-portugues/busca/portugues-brasileiro/{content}/')
    soup = BeautifulSoup(page, 'html.parser')  
    
    sp = soup.find('div', id='main-container').find('div', class_='verbete bs-component')
    
    text = sp.get_text()
    
    point = text.find('2')
    if point > 0:
        pass
    else:
        point = text.find('EXPRESSÕES')
    text = text[:point]

    new = text.split(' ')
    new = " ".join(new[2:])
    
    return new 