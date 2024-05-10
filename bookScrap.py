from bs4 import BeautifulSoup
import pandas as pd
import requests


datas = []

request = requests.get('https://books.toscrape.com/')

html_code = request.text

soup = BeautifulSoup(html_code, 'lxml')

productPrices = soup.find_all('p', class_='price_color')

titles_scrap = soup.find_all('h3')

ratings = soup.find_all('p', class_='star-rating')

images = soup.find_all('img', class_='thumbnail')


for i in range(0, len(titles_scrap)):
    rating = ratings[i]['class'][1]

    if rating == 'One':
        datas.append([titles_scrap[i].text, productPrices[i].text,1, images[i]['src']])
    elif rating == 'Two':
        datas.append([titles_scrap[i].text, productPrices[i].text,2, images[i]['src']])
    elif rating == 'Three':
        datas.append([titles_scrap[i].text, productPrices[i].text,3, images[i]['src']])
    elif rating == 'Four':
        datas.append([titles_scrap[i].text, productPrices[i].text,4, images[i]['src']])
    else:
        datas.append([titles_scrap[i].text, productPrices[i].text,5, images[i]['src']])

df = pd.DataFrame(datas, columns=['Title', 'Price', 'rating', 'image'])
df.to_csv('datas.csv', index=False)



