# Задача 44: В ячейке ниже представлен код генерирующий DataFrame, которая состоит всего из 1 столбца.
# Ваша задача перевести его в one hot вид. Сможете ли вы это сделать без get_dummies?
# Статья про one hot вид

import pandas as pd
import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})

data_variant2 = data.copy()  # Для варианта 2

print("Начальный датафрейм:")
print(data)
print("-----------------------------------------------------------------------------------")

# Вариант 1
data.loc[data['whoAmI'] == 'human', "whoAmI"] = 1  # Меняем в one hot
data.loc[data['whoAmI'] == 'robot', "whoAmI"] = 0  # Меняем в one hot

print("Датафрейм в виде one hot:")
print(data)
print("-----------------------------------------------------------------------------------")

data.to_csv("whoAmI_one_hot.csv", index=False)  # Выгрузка в csv

# Вариант  2:
new_cols = ["Human", "Robot"]

data_variant2.loc[data_variant2['whoAmI'] == 'human', new_cols] = (1, 0)
data_variant2.loc[data_variant2['whoAmI'] == 'robot', new_cols] = (0, 1)

data_variant2 = data_variant2.drop('whoAmI', axis=1)

data_variant2 = data_variant2[new_cols].astype(int)

print("Датафрейм (вариант 2):")
print(data_variant2)

data_variant2.to_csv("human_robot.csv", index=False)  # Выгрузка в csv