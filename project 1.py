import requests
from bs4 import BeautifulSoup


link = "https://www.cian.ru/snyat-kvartiru/"
responce = requests.get(link).text
soup = BeautifulSoup(responce, 'lxml')
price_and_name_elements = soup.find_all("span")
address_elements = soup.find_all("div", class_="_93444fe79c--labels--L8WyJ")
block_div = soup.find_all('div')

block_description = []
block_price = []
block_name = []
block_address = []
block_full = []

for price in price_and_name_elements:
    if price.get("data-mark") == "MainPrice":
        block_price.append(f'Цена: {price.text}')

for name in price_and_name_elements:
    if name.get("data-mark") == "OfferTitle":
        block_name.append(f'Объявление: {name.text}')

for address in address_elements:
    links = address.find_all("a")
    address_parts = [link.text.strip() for link in links]
    full_address = ", ".join(address_parts)
    block_address.append(f'Адрес: {full_address}')

for i in range(len(block_name)):
  block_full_dop = []
  block_full_dop.append(block_name[i])
  block_full_dop.append(block_price[i])
  block_full_dop.append(block_address[i])
  block_full.append(block_full_dop)
