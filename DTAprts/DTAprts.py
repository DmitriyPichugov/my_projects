import requests
import matplotlib.pyplot as plt
import re
from bs4 import BeautifulSoup


block_price = []
block_name = []
block_address = []
block_description = []
block_full = []
counter = 0
for p in range(1, 55):
  link = f"https://www.cian.ru/cat.php?deal_type=rent&engine_version=2&offer_type=flat&p={p}&region=1&type=4"
  print(link)
  
  responce = requests.get(link).text
  soup = BeautifulSoup(responce, 'lxml')
  price_and_name_elements = soup.find_all("span")
  address_elements = soup.find_all("div", class_="_93444fe79c--labels--L8WyJ")
  block_div = soup.find_all('div')
  
  
  for price in price_and_name_elements:
      if price.get("data-mark") == "MainPrice":
          block_price.append(price.text)

  for name in price_and_name_elements:
      if name.get("data-mark") == "OfferTitle":
          block_name.append(name.text)

  for address in address_elements:
      links = address.find_all("a")
      address_parts = [link.text.strip() for link in links]
      full_address = ", ".join(address_parts)
      block_address.append(full_address)

  for description in block_div:
    if description.get("data-name") == "Description":
      block_description.append(description)
      counter += 1
      print(counter)

  for i in range(len(block_name)):
    block_full_dop = []
    block_full_dop.append(block_name[i])
    block_full_dop.append(block_price[i])
    block_full_dop.append(block_address[i])
    block_full.append(block_full_dop)



print(counter)


