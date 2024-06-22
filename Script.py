import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score, classification_report
from sklearn.preprocessing import LabelEncoder
import matplotlib.pyplot as plt

file_path = 'C:\\Users\\lenov\\Documents\\Kuliah\\Semester6\\DATA-MINING\\Data-Mining_Naive-Bayes\\data\\PharmaDrugSales.xlsx'  
data = pd.read_excel(file_path)


data = data.dropna()
data = data[data['Year'] != '#VALUE!']
data['Year'] = data['Year'].astype(int)
data['Month'] = data['Month'].astype(int)
data['Date'] = data['Date'].astype(int)
data['Hour'] = data['Hour'].astype(int)


label_encoder = LabelEncoder()
data['Day'] = label_encoder.fit_transform(data['Day'])


target_columns = [
    'AceticAcidDerivatives', 'PropionicAcidDerivatives', 'SalicylicAcidDerivatives', 
    'PyrazolonesAndAnilides', 'AnxiolyticDrugs', 'HypnoticsSndSedativesDrugs', 
    'ObstructiveAirwayDrugs', 'Antihistamines'
]


features = ['Year', 'Month', 'Date', 'Hour', 'Day']
X = data[features]


total_sales_by_year = data.groupby('Year')[target_columns].sum()


for col in target_columns:
    if col in total_sales_by_year.columns:
        total_sales_by_year[f'Rank_{col}'] = total_sales_by_year[col].rank(ascending=False, method='min')


total_sales_by_year.to_excel('C:\\Users\\lenov\\Documents\\Kuliah\\Semester6\\DATA-MINING\\Data-Mining_Naive-Bayes\\data\\perbandingan\\total_sales_by_year.xlsx')

print("\nPerbandingan Penjualan Obat Berdasarkan Tahun:")
print(total_sales_by_year)


print("\nObat Paling Laris Berdasarkan Tahun:")
for year, row in total_sales_by_year.iterrows():
    print(f"Tahun {year}:")
    for col in target_columns:
        if col in row.index:
            rank_col = f'Rank_{col}'
            rank = row[rank_col]
            print(f"  {int(rank)}. {col}")
