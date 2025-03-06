import time
import random
import json
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_options = Options()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(options=chrome_options)

block_full = []
counter = 0

for p in range(1, 6):
    url = f"https://www.cian.ru/cat.php?deal_type=rent&engine_version=2&offer_type=flat&p={p}&region=1&type=4"
    print(f"Парсинг страницы: {url}")
    
    try:
        driver.get(url)
        wait = WebDriverWait(driver, 10)
        listings = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "_93444fe79c--card--ibP42")))
        
        for listing in listings:
            try:
                title = listing.find_element(By.CSS_SELECTOR, "span[data-mark='OfferTitle']").text
                price = listing.find_element(By.CSS_SELECTOR, "span[data-mark='MainPrice']").text
                address_elements = listing.find_elements(By.CLASS_NAME, "_93444fe79c--address-link--OG8w1")
                address = ", ".join([elem.text for elem in address_elements])
                description = listing.find_element(By.CLASS_NAME, "_93444fe79c--description--fP5dP").text if listing.find_elements(By.CLASS_NAME, "_93444fe79c--description--fP5dP") else "Нет описания"
                link = listing.find_element(By.TAG_NAME, "a").get_attribute("href")
                
                block_full.append({
                    "title": title,
                    "price": price,
                    "address": address,
                    "description": description,
                    "link": link
                })
                counter += 1
                print(f"Обработано объявлений: {counter}")
            except Exception as e:
                print(f"Ошибка в карточке: {e}")
        
        time.sleep(random.uniform(2, 5))
    except Exception as e:
        print(f"Ошибка на странице {p}: {e}")
        break

with open("cian_data.json", "w", encoding="utf-8") as f:
    json.dump(block_full, f, ensure_ascii=False, indent=4)

print(f"Всего собрано: {counter} объявлений")
driver.quit()
