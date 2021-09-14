import pandas as pd

dictionary = pd.read_csv("dictionary.csv")

for word in dictionary['単語']:
    print(word)