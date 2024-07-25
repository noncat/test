import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

csv_path = "/home/noncat/Документы/DO/int_cert/contracts_by_region_export_postgresql.csv"

if os.path.isfile(csv_path):
     
    data = pd.read_csv(csv_path)

    data.columns = [col.lower() for col in data.columns]

    top_10_regions = data.sort_values(by='contract_count', ascending=False).head(10)

    sns.set(style="whitegrid")

    plt.figure(figsize=(12, 8))
    bar_plot = sns.barplot(x='region_code', y='contract_count', data=top_10_regions, palette='coolwarm')

    bar_plot.set_xlabel('Region Code', fontsize=14)
    bar_plot.set_ylabel('Contract Count', fontsize=14)
    bar_plot.set_title('Top 10 Regions by Contract Count for Physical Persons', fontsize=16)

    for index, row in top_10_regions.iterrows():
        bar_plot.text(index, row.contract_count, round(row.contract_count, 2), color='black', ha="center", va="bottom")

    plt.ylim(0, top_10_regions['contract_count'].max() * 1.1)

    plt.xticks(rotation=45)

    plt.show()
