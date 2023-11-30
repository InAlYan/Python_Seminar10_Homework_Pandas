# Задача 44: В ячейке ниже представлен код генерирующий DataFrame, которая состоит всего из 1 столбца.
# Ваша задача перевести его в one hot вид. Сможете ли вы это сделать без get_dummies?
# Статья про one hot вид

import pandas as pd
import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})

print("Начальный датафрейм:")
print(data)
print("-----------------------------------------------------------------------------------")

data.loc[data['whoAmI'] == 'human', "whoAmI"] = 1
data.loc[data['whoAmI'] == 'robot', "whoAmI"] = 0

print("Датафрейм в виде one hot:")
print(data)

data.to_csv("whoAmI_one_hot.csv", index=False) # Выгрузка в csv
