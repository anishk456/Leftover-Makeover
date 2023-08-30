import pandas as pd 
import requests
import time
from bs4 import BeautifulSoup
import numpy as np
from scrape_food_class import Recipe

# Reads in the csv containing each recipes url
recipe_df = pd.read_csv("/Users/anish/Documents/ML/honestcooking_urls.csv")
# The list of recipe attributes we want to scrape
attribs = ['recipe_name', 'ingredients']

# For each url (i) we add the attribute data to the i-th row
temp = pd.DataFrame(columns=attribs)
print("2601 to end")
for i in range(2601,len(recipe_df['recipe_urls'])):
    url = recipe_df['recipe_urls'][i]
    recipe_scraper = Recipe(url)

    temp.loc[i] = [getattr(recipe_scraper, attrib)() for attrib in attribs]
    if i % 25 == 0:
        print(f'Step {i} completed')
    time.sleep(2) #np.random.randint(5,7)

# Put all the data into the same dataframe
temp['recipe_urls'] = recipe_df['recipe_urls']
columns = ['recipe_urls'] + attribs
temp = temp[columns]

full_recipe_df = temp

full_recipe_df.to_csv(r"/Users/anish/Documents/ML/honestcooking_full_recipes4.csv", index=False)
