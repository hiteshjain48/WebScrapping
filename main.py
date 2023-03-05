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
driver.get('https:/www.flipkart.com')
search_box = driver.find_element_by_xpath('//*[@id="container"]/div/div[1]/div[1]/div[2]/div[2]/form/div/div/input')
search_box.send_keys("laptop")
search_box.send_keys(Keys.ENTER)
time.sleep(5)
content = driver.page_source
soup = Bs(content, features="html.parser")
for a in soup.findAll('a', href=True, attrs={'class': '_1fQZEK'}):
    name = a.find('div', attrs={'class': '_4rR01T'})
    price = a.find('div', attrs={'class': '_30jeq3'})
    rating = a.find('div', attrs={'class': '_3LWZlK'})
    products.append(name.text)
    prices.append(str(price.text[1:]).replace(",", ""))
    if rating is None:
        ratings.append("N/A")
    else:
        ratings.append(rating.text)
next_btn = driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div[1]/div[2]/div[26]/div/div/nav/a[11]')
next_btn.click()
time.sleep(5)
while True:
    # noinspection PyBroadException
    try:
        for a in soup.findAll('a', href=True, attrs={'class': '_1fQZEK'}):
            name = a.find('div', attrs={'class': '_4rR01T'})
            price = a.find('div', attrs={'class': '_30jeq3'})
            rating = a.find('div', attrs={'class': '_3LWZlK'})
            products.append(name.text)
            prices.append(str(price.text[1:]).replace(",", ""))
            if rating is None:
                ratings.append("N/A")
            else:
                ratings.append(rating.text)
        next_btn = driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div[1]/div[2]/div[26]/div/div/nav/a['
                                                '12]')
        next_btn.click()
        time.sleep(1)
    except:
        break
df = pd.DataFrame({'Product Name': products, 'Price': prices, 'Rating': ratings})
df.to_csv('products1.csv', index=False, encoding='utf-8')
