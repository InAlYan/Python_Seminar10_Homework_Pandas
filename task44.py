# Задача 44: В ячейке ниже представлен код генерирующий DataFrame, которая состоит всего из 1 столбца.
# Ваша задача перевести его в one hot вид. Сможете ли вы это сделать без get_dummies?
# Статья про one hot вид

import pandas as pd
import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})

data.loc[data['whoAmI'] == 'human', "whoAmI"] = 1
data.loc[data['whoAmI'] == 'robot', "whoAmI"] = 0
