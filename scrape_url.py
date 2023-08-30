import requests
from bs4 import BeautifulSoup
import pandas as pd


#############################
# recipe_url_df = pd.DataFrame() 
# # Gordon Ramsey recipe website
# url = "https://www.gordonramsay.com/gr/recipes/getRecipes?start="
# for i in range(0, 161, 16):  
    
#     p = requests.get(url + str(i))

#     # BeautifulSoup enables to find the elements/tags in a webpage
#     soup = BeautifulSoup(p.text, "html.parser")

#     # Selecting all the 'a' tags (URLs) present in the webpage and extracting 
#     # their 'href' attribute
#     recipe_urls = pd.Series([a.get("href") for a in soup.find_all("a")])

#     recipe_urls = recipe_urls[(recipe_urls.str.count("/")>3)
#                           & (recipe_urls.str.contains("/recipes/")==True)
#                           & (recipe_urls.str.contains("/category/")==False)
#                          ].unique()
    
#     # DataFrame to store the scraped URLs
#     df = pd.DataFrame({"recipe_urls":recipe_urls})
#     df['recipe_urls'] = "https://www.gordonramsay.com" + df['recipe_urls'].astype('str')
#     #Appending 'df' to a main DataFrame 'init_urls_df'
#     recipe_url_df = pd.concat([df, recipe_url_df], ignore_index=True)
    

# recipe_url_df.to_csv(r"/Users/anish/Documents/ML/foodrecipe_urls.csv", sep="\t", index=False)


##############################
recipe_url_df = pd.DataFrame() 
# Honest Cooking recipe website
url = "https://honestcooking.com/category/recipes/main-courses-2/page/"
for i in range(1, 54):  
    
    p = requests.get(url + str(i) + "/")

    # BeautifulSoup enables to find the elements/tags in a webpage
    soup = BeautifulSoup(p.text, "html.parser")

    # Selecting all the 'a' tags (URLs) present in the webpage and extracting 
    # their 'href' attribute
    recipe_urls = pd.Series([a.get("href") for a in soup.find_all("a")])

    recipe_urls = recipe_urls[(recipe_urls.str.count("/")>3)
                            & (recipe_urls.str.count("-")>0)
                          & (recipe_urls.str.contains("/recipes/")==False)
                          & (recipe_urls.str.contains("/category/")==False)
                          & (recipe_urls.str.contains("/author/")==False)
                          & (recipe_urls.str.contains("/culinary-travel/")==False)
                         ].unique()
    
    # DataFrame to store the scraped URLs
    df = pd.DataFrame({"recipe_urls":recipe_urls})
    df['recipe_urls'] = "" + df['recipe_urls'].astype('str')
    #Appending 'df' to a main DataFrame 'init_urls_df'
    recipe_url_df = pd.concat([df, recipe_url_df], ignore_index=True)

recipe_url_df.to_csv(r"/Users/anish/Documents/ML/honestcooking_urls.csv", sep="\t", index=False)