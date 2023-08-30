import requests
from bs4 import BeautifulSoup
import pandas as pd 
import numpy as np


headers = {'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36"}

class Recipe():
    #This class will give the details of the food recipe
    
    def __init__(self, url):
        self.url = url 
        self.soup = BeautifulSoup(requests.session().get(url, headers=headers, timeout=(6, 12)).text, 'html.parser')
        #requests.get(url, headers=headers, timeout=(8, 12)).content
    def recipe_name(self):
        """ Locates the recipe title """
        # Some of the urls are not recipe urls so to avoid errors we use try/except 
        try:
            return self.soup.find('h1').text.strip()
          
        except: 
            return np.nan
        

    def ingredients(self):
        """ Creating a vector containing the ingredients of the recipe """
        try:
            ingredients = []
            for i in self.soup.find_all(class_="tr-ingredient-checkbox-container"):
                item = i.contents[0]["aria-label"]
                ingredients.append(item)
            return ingredients
        except:
            return np.nan

# url = "https://honestcooking.com/chicken-chili-verde-with-beans/"

# soup = BeautifulSoup(requests.get(url).content, 'html.parser')
# #print(soup.find('h1').text.strip())

# # tag = soup.find_all(class_="tr-ingredient-checkbox-container")[0].contents[0]
# # print(tag["aria-label"])
# ingredients = []
# for i in soup.find_all(class_="tr-ingredient-checkbox-container"):
#     item = i.contents[0]["aria-label"]
#     ingredients.append(item)

# print(ingredients)
# # print(soup.find_all("ul")[5])
