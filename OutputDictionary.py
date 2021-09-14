import pandas as pd
import numpy as np

dictionary = pd.read_csv("dictionary.csv")

#単語idの追加
dictionary["ID"] = range(1,len(dictionary)+1)

for word_id in range(len(dictionary)):
    id = dictionary["ID"][word_id]
    word = dictionary["単語"][word_id]
    print(str(id)+":"+word)