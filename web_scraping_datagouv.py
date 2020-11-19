# -*- coding: utf-8 -*-
"""
Created on Sun Nov 15 11:51:12 2020

@author: Bast
"""

from bs4 import BeautifulSoup
import requests

url = ("https://www.gouvernement.fr/info-coronavirus/carte-et-donnees")

html = requests.get(url).text
soup = BeautifulSoup(html, "html5lib")

# On veut récupérer les valeurs issues du dashboard du gouv tous les jours par régions&



div_list = [div for div in soup("div")]
div = [p.text for p in soup("div") if p.get("class") == "jsx-3447427165 value"]

important_paragraphs = soup("div", {'class' : 'jsx-3447427165 value'})

print(div)
print(important_paragraphs)
#div class="jsx-792689997 value


paragraph_with_ids = [p["class"] for p in soup("div") if p.has_attr("class")]#print(paragraph_with_ids)

print(paragraph_with_ids)
print("----------------")
paragraph_with_ids = [p["id"] for p in soup("div") if p.has_attr("id")]
print(paragraph_with_ids)

print(soup.find_all("div"))

t=[sub_div for div in soup("div")
     for sub_div in div]
for i in soup("body"):
    print(i)


div_block_system=soup.find_all("div", class_="block block-system block-odd")
t = [div for div in div_block_system if div.has_attr("class")]
print(t)

for div in t:
    if div.get("class") == "content":
        print(div.text)