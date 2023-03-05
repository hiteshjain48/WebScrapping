from cgitb import html
from lib2to3.pgen2 import driver
import requests
from bs4 import BeautifulSoup
word = "logic"
url1 = f"https://www.google.com/search?query={word} meaning"
r1 = requests.get(url1)
data1 = BeautifulSoup(r1.text, "html.parser")
word1 = data1.find("div", class_="BNeawe" ).text
meaning = data1.find("div", class_="BNeawe s3v9rd AP7Wnd").text
print(meaning.partition(".")[0] + " this is meaning")
print(word1[1::] + " This is on google")
print(word + " this is ours")
print(type(word))
print(type(word1))
word2 = word1[1::]
if word2 is word:
    meaning = data1.find("div", class_="BNeawe s3v9rd AP7Wnd").text
# speak(f"The meaning of {word} is {meaning}")
# print(f"The meaning of {word} is {meaning}")
# print(data1.prettify())
    print(word1)
    print(meaning.partition(".")[0])
else:
    print("Invalid word")
# print(type(meaning))
# search = "my location"
# url1 = f"https://www.google.com/search?query={search}"
# r1 = requests.get(url1)
# data1 = BeautifulSoup(r1.text, "html.parser")
# location = data1.find("div", class_="BNeawe").text
# search_temp = "temperature in " + location
# url2 = f"https://www.google.com/search?query={search_temp}"
# r2 = requests.get(url2)
# data2 = BeautifulSoup(r2.text, "html.parser")
# temp = data2.find("div", class_="BNeawe").text
# # speak(f"current temperature of {location} is {temp}")
# print(f"current temperature of {location} is {temp}")