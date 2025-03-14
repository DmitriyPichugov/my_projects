import time
import random
import json
import re
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


chrome_options = Options()
chrome_options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36")
chrome_options.add_argument("accept-language=en-US,en;q=0.9")
chrome_options.add_argument("--disable-blink-features=AutomationControlled")
driver = webdriver.Chrome(options=chrome_options)

block_full = []
counter = 0

for p in range(53, 55):
    url = f"https://www.cian.ru/cat.php?deal_type=rent&engine_version=2&offer_type=flat&p={p}&region=1&type=4"
    
    print(f"Парсинг страницы: {url}")
    
    try:
        driver.get(url)
        wait = WebDriverWait(driver, 30)
        listings = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "_93444fe79c--card--ibP42")))
        
        print(f"Найдено {len(listings)} объявлений на странице {p}")
        
        for listing in listings:
            try:
                title_element = listing.find_element(By.CSS_SELECTOR, "span[data-mark='OfferTitle']")
                title = title_element.text
                
                rooms_match = re.search(r'(\d+)-комн\.', title)
                rooms = rooms_match.group(1) if rooms_match else None
                
                if not rooms:
                    try:
                        subtitle_element = listing.find_element(By.CSS_SELECTOR, "span[data-mark='OfferSubtitle']")
                        subtitle_text = subtitle_element.text
                        rooms_match = re.search(r'(\d+)-комн\.', subtitle_text)
                        rooms = rooms_match.group(1) if rooms_match else "Не указано"
                    except:
                        rooms = "Не указано"
                
                square_match = re.search(r'(\d+(?:\.\d+)?)\s*м²', title)
                square = square_match.group(1) if square_match else None
                
                if not square:
                    try:
                        subtitle_element = listing.find_element(By.CSS_SELECTOR, "span[data-mark='OfferSubtitle']")
                        subtitle_text = subtitle_element.text
                        square_match = re.search(r'(\d+(?:\.\d+)?)\s*м²', subtitle_text)
                        square = square_match.group(1) if square_match else "Не указано"
                    except:
                        square = "Не указано"
                
                price = listing.find_element(By.CSS_SELECTOR, "span[data-mark='MainPrice']").text
                
                address_container = listing.find_element(By.CSS_SELECTOR, "div._93444fe79c--labels--L8WyJ")
                address_elements = address_container.find_elements(By.TAG_NAME, "a")
                address = ", ".join([elem.text for elem in address_elements]) if address_elements else "Адрес не найден"
                
                district_elements = address_container.find_elements(By.CSS_SELECTOR, "a[data-name='GeoLabel']")
                district = district_elements[3].text if "м." in district_elements[3].text else district_elements[2].text
                
                try:
                    price_info_element = listing.find_element(By.CSS_SELECTOR, "p[data-mark='PriceInfo']")
                    price_info_text = price_info_element.text
                except:
                    price_info_text = ""
                
                commission_match = re.search(r'комиссия\s+(\d+)%', price_info_text)
                commission = commission_match.group(1) if commission_match else "Без комиссии"
                
                deposit_match = re.search(r'залог\s+([\d\s]+)\s*₽', price_info_text)
                deposit = deposit_match.group(1).replace(' ', '') if deposit_match else "Без залога"
                
                link = listing.find_element(By.TAG_NAME, "a").get_attribute("href")
                
                block_full.append({
                    "title": title,
                    "rooms": rooms,
                    "square": square,
                    "price": price,
                    "address": address,
                    "district": district,
                    "commission": commission,
                    "deposit": deposit,
                    "link": link
                })
                
                counter += 1
                
                print(f"Обработано объявлений: {counter}")
                
            except Exception as e:
                print(f"Ошибка в карточке: {e}")
        
        time.sleep(random.uniform(5, 10))
        
    except Exception as e:
        print(f"Ошибка на странице {p}: {e}")
        
        with open(f"page_{p}.html", "w", encoding="utf-8") as f:
            f.write(driver.page_source)
        break

with open("cian_data.json", "w", encoding="utf-8") as f:
    json.dump(block_full, f, ensure_ascii=False, indent=4)

print(f"Всего собрано: {counter} объявлений")
driver.quit()