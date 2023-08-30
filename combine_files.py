import pandas as pd

files = ['/Users/anish/Documents/ML/honestcooking_full_recipes.csv', '/Users/anish/Documents/ML/honestcooking_full_recipes1.csv', '/Users/anish/Documents/ML/honestcooking_full_recipes2.csv', '/Users/anish/Documents/ML/honestcooking_full_recipes3.csv', '/Users/anish/Documents/ML/honestcooking_full_recipes4.csv']
df = pd.DataFrame()
for file in files:
    food = pd.read_csv(file)
    df = pd.concat([df, food], axis=0)
df.to_csv('/Users/anish/Documents/ML/honestcooking_all_recipes.csv', index=False)