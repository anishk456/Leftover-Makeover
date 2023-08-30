import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
import pickle 
import config

# load in parsed recipe dataset 
df_recipes = pd.read_csv('/Users/anish/Documents/ML/honestcooking_all_recipes_parsed.csv')
df_recipes['ingredients_parsed'] = df_recipes.ingredients_parsed.values.astype('U')

# TF-IDF feature extractor 
tfidf = TfidfVectorizer()
tfidf.fit(df_recipes['ingredients_parsed'])
tfidf_recipe = tfidf.transform(df_recipes['ingredients_parsed'])

# save the tfidf model and encodings 
with open('/Users/anish/Documents/ML/tfidf_model.pkl', "wb") as f:
    pickle.dump(tfidf, f)

with open('/Users/anish/Documents/ML/tfidf_encode.pkl', "wb") as f:
    pickle.dump(tfidf_recipe, f)
