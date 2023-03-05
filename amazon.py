from selenium import webdriver
from bs4 import BeautifulSoup as Bs
import pandas as pd
import time
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(r"C:\Users\Hitesh\Downloads\chromedriver_win32\chromedriver.exe")


products = []
prices = []
ratings = []

# driver.get("https://www.flipkart.com/search?q=lap&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as"
#            "=off")
driver.get('https:/www.amazon.com')
search_box = driver.find_element_by_xpath('//*[@id="twotabsearchtextbox"]')
search_box.send_keys("laptop")
search_box.send_keys(Keys.ENTER)
time.sleep(5)
content = driver.page_source
soup = Bs(content, features="html.parser")
for a in soup.findAll('div', href=True, attrs={'class': 'a-section a-spacing-none aok-relative'}):
    name = a.find('span', attrs={'class': 'a-size-medium a-color-base a-text-normal'})
    price = a.find('span', attrs={'class': 'a-price-whole'})
    rating = a.find('span', attrs={'class': 'a-icon-alt'})
    products.append(name.text)
    prices.append(str(price.text[1:]).replace(",", ""))
    if rating is None:
        ratings.append("N/A")
    else:
        ratings.append(rating.text)
# next_btn = driver.find_element_by_class_name('a-class')
# next_btn.click()
# time.sleep(5)
# while True:
#     # noinspection PyBroadException
#     try:
#         for a in soup.findAll('div', href=True, attrs={'class': 'sg-col-inner'}):
#             name = a.find('span', attrs={'class': 'a-size-medium a-color-base a-text-normal'})
#             price = a.find('span', attrs={'class': 'a-price-whole'})
#             rating = a.find('span', attrs={'class': 'a-icon-alt'})
#             products.append(name.text)
#             prices.append(str(price.text[1:]).replace(",", ""))
#             if rating is None:
#                 ratings.append("N/A")
#             else:
#                 ratings.append(rating.text)
#         next_btn = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div[1]/div/span[3]/div[2]/div[31]/span/div/div/ul/li[8]/a')
#         next_btn.click()
#         time.sleep(1)
#     except:
#         break
df = pd.DataFrame({'Product Name': products, 'Price': prices, 'Rating': ratings})
df.to_csv('a.csv', index=False, encoding='utf-8')
