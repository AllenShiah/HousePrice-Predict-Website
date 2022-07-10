import pandas as pd
import numpy as np
from sklearn.utils import shuffle



# 原本資料 289 MB 
compare_data = pd.read_csv('compare/compare_index.csv')

# 1. 去除用不到欄位 220 MB 
drop_columns = ['area_m2', 'manager', 'Total_price',
    'including_basement', 'including_arcade', 'Main_Usage_Walk',
   'Main_Usage_Living', 'Main_Usage_Selling', 'Main_Usage_Manufacturing',
   'Main_Usage_Parking', 'Main_Usage_SnE', 'Main_Usage_Farm',
   'Building_Material_stone',  'Non_City_Land_Usage',
   'Unit_Price_Ping']
compare_data = compare_data.drop(columns=drop_columns)


# 2. 將資料變45%，99.6MB
compare_data = shuffle(compare_data)
row_count = int(0.45 * len(compare_data))
compare_data_small = compare_data[:row_count]

compare_data_small.to_csv('compare/compare_index_small.csv',index=False)


check = compare_data['Parking_Area'].value_counts()



