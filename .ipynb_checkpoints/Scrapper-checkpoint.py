from selenium import webdriver
from bs4 import BeautifulSoup as Bs
import pandas as pd
import time
from selenium.webdriver.common.keys import Keys


class WebScrapper:
    def __init__(self, search):
        self.search = search
        self.driver = webdriver.Chrome(r"C:\Users\Hitesh\Downloads\chromedriver_win32\chromedriver.exe")
        self.products = []
        self.prices = []
        self.ratings = []

    def getInfo(self, url):
        search_xpath = input("Enter the xpath of search box:")
        nxt_btn1_xpath = input("Enter the xpath of the next button on the first page:")
        nxt_btn_xpath = input("Enter the xpath of the next button on the second page:")
        a_class = input("Enter:")
        name_class = input("Enter the class of div containing name:")
        price_class = input("Enter the class of div containing price:")
        rating_class = input("Enter the class of div containing rating:")

        self.driver.get(url)
        search_box = self.driver.find_element_by_xpath(search_xpath)
        search_box.send_keys(self.search)
        search_box.send_keys(Keys.ENTER)
        time.sleep(5)
        content = self.driver.page_source
        soup = Bs(content, features="html.parser")
        for a in soup.findAll('a', href=True, attrs={'class': a_class}):
            name = a.find('div', attrs={'class': name_class})
            price = a.find('div', attrs={'class': price_class})
            rating = a.find('div', attrs={'class': rating_class})
            self.products.append(name.text)
            self.prices.append(str(price.text[1:]).replace(",", ""))
            if rating is None:
                self.ratings.append("N/A")
            else:
                self.ratings.append(rating.text)
        next_btn = self.driver.find_element_by_xpath(nxt_btn1_xpath)
        next_btn.click()
        time.sleep(5)
        while True:
            # noinspection PyBroadException
            try:
                for a in soup.findAll('a', href=True, attrs={'class': '_1fQZEK'}):
                    name = a.find('div', attrs={'class': name_class})
                    price = a.find('div', attrs={'class': price_class})
                    rating = a.find('div', attrs={'class': rating_class})
                    self.products.append(name.text)
                    self.prices.append(str(price.text[1:]).replace(",", ""))
                    if rating is None:
                        self.ratings.append("N/A")
                    else:
                        self.ratings.append(rating.text)
                next_btn = self.driver.find_element_by_xpath(nxt_btn_xpath)
                next_btn.click()
                time.sleep(1)
            except:
                break

    def data(self, filename):
        df = pd.DataFrame({'Product Name': self.products, 'Price': self.prices, 'Rating': self.ratings})
        df.to_csv(filename, index=False, encoding='utf-8')


flipkart = WebScrapper("laptop")
flipkart.getInfo('https:/amazon.com')
flipkart.data("amazon.csv")
