from selenium import webdriver
from bs4 import BeautifulSoup as Bs
import pandas as pd
import time
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(r"C:\Users\Hitesh\Downloads\chromedriver_win32\chromedriver.exe")

driver.get('https://in.indeed.com/jobs?q=computer%20science%20engineering&start=10&vjk=b64e2da46b5a8d48')

content = driver.page_source

soup = Bs(content, features='html.parser')
# for a in soup.findAll('a', href=True, attrs)
# a = soup.findAll('span', href=True, attrs={'class': 'mosiac-zone'})

# print(a)
b=0
print("b before", b)
for a in soup.findAll(attrs={'class':'jobsearch-ResultsList'}):
    print(a)