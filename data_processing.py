import pandas as pd

# Assuming you have three CSV files: daily_sales_data_0.csv.csv, file2.csv, file3.csv

daily_sales_data_0.csv = pd.read_csv('daily_sales_data_0.csv.csv')
file2 = pd.read_csv('file2.csv')
file3 = pd.read_csv('file3.csv')

daily_sales_data_0.csv_pink_morsels = daily_sales_data_0.csv[daily_sales_data_0.csv['product'] == 'Pink Morsels']
file2_pink_morsels = file2[file2['product'] == 'Pink Morsels']
file3_pink_morsels = file3[file3['product'] == 'Pink Morsels']

daily_sales_data_0.csv_pink_morsels.to_csv('daily_sales_data_0.csv_pink_morsels.csv', index=False)
file2_pink_morsels.to_csv('file2_pink_morsels.csv', index=False)
file3_pink_morsels.to_csv('file3_pink_morsels.csv', index=False)
