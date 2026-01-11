# Analisis Data Zomato Menggunakan Python

# Langkah 1: Mengimpor pustaka Python yang diperlukan
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Langkah 2: Membaca data
dataframe = pd.read_csv("Zomato-data-.csv")
print("=== 5 Baris Pertama Data ===")
print(dataframe.head())
print("\n")

# Langkah 3: Pembersihan dan Persiapan Data

# 3.1 Konversi kolom rate menjadi float
def handleRate(value):
    value = str(value).split('/')
    value = value[0]
    return float(value)

dataframe['rate'] = dataframe['rate'].apply(handleRate)
print("=== Data Setelah Konversi Rate ===")
print(dataframe.head())
print("\n")

# 3.2 Informasi dataframe
print("=== Informasi Dataframe ===")
dataframe.info()
print("\n")

# 3.3 Cek nilai null
print("=== Nilai Null ===")
print(dataframe.isnull().sum())
print("\n")

# Langkah 4: Menjelajahi Jenis Restoran

# 4.1 Countplot tipe restoran
plt.figure(figsize=(10, 6))
sns.countplot(x=dataframe['listed_in(type)'])
plt.xlabel("Type of restaurant")
plt.title("Jumlah Restoran per Tipe")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('1_tipe_restoran.png')
plt.show()

# 4.2 Votes berdasarkan tipe restoran
grouped_data = dataframe.groupby('listed_in(type)')['votes'].sum()
result = pd.DataFrame({'votes': grouped_data})
plt.figure(figsize=(10, 6))
plt.plot(result, c='green', marker='o', linewidth=2, markersize=8)
plt.xlabel('Type of restaurant', fontsize=12)
plt.ylabel('Votes', fontsize=12)
plt.title('Total Votes per Tipe Restoran')
plt.xticks(rotation=45)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('2_votes_per_tipe.png')
plt.show()

# Langkah 5: Restoran dengan Votes Tertinggi
max_votes = dataframe['votes'].max()
restaurant_with_max_votes = dataframe.loc[dataframe['votes'] == max_votes, 'name']
print('=== Restaurant(s) with the maximum votes ===')
print(restaurant_with_max_votes)
print(f"Jumlah votes: {max_votes}")
print("\n")

# Langkah 6: Ketersediaan Pesanan Online
plt.figure(figsize=(8, 6))
sns.countplot(x=dataframe['online_order'])
dataframe['online_order'].value_counts()
plt.xlabel("Online Order")
plt.ylabel("Jumlah Restoran")
plt.title("Ketersediaan Pesanan Online")
plt.tight_layout()
plt.savefig('3_online_order.png')
plt.show()

# Statistik online order
print("=== Statistik Online Order ===")
print(dataframe['online_order'].value_counts())
print("\n")

# Langkah 7: Analisis Peringkat (Rating)
plt.figure(figsize=(10, 6))
plt.hist(dataframe['rate'], bins=5, color='skyblue', edgecolor='black')
plt.title('Distribusi Ratings')
plt.xlabel('Rating')
plt.ylabel('Jumlah Restoran')
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('4_rating_distribution.png')
plt.show()

# Langkah 8: Perkiraan Biaya untuk Pasangan
couple_data = dataframe['approx_cost(for two people)']
plt.figure(figsize=(12, 6))
sns.countplot(x=couple_data)
plt.xlabel("Approximate Cost (for two people)")
plt.ylabel("Jumlah Restoran")
plt.title("Distribusi Biaya untuk 2 Orang")
plt.xticks(rotation=90)
plt.tight_layout()
plt.savefig('5_cost_distribution.png')
plt.show()

# Langkah 9: Perbandingan Rating - Online vs Offline
plt.figure(figsize=(8, 6))
sns.boxplot(x='online_order', y='rate', data=dataframe)
plt.xlabel("Online Order")
plt.ylabel("Rating")
plt.title("Perbandingan Rating: Online vs Offline")
plt.tight_layout()
plt.savefig('6_rating_comparison.png')
plt.show()

# Statistik rating
print("=== Statistik Rating berdasarkan Online Order ===")
print(dataframe.groupby('online_order')['rate'].describe())
print("\n")

# Langkah 10: Preferensi Mode Pesanan berdasarkan Tipe Restoran
pivot_table = dataframe.pivot_table(
    index='listed_in(type)', 
    columns='online_order', 
    aggfunc='size', 
    fill_value=0
)

plt.figure(figsize=(10, 6))
sns.heatmap(pivot_table, annot=True, cmap='YlGnBu', fmt='d', cbar_kws={'label': 'Jumlah Restoran'})
plt.title('Heatmap: Tipe Restoran vs Online Order')
plt.xlabel('Online Order')
plt.ylabel('Listed In (Type)')
plt.tight_layout()
plt.savefig('7_heatmap.png')
plt.show()

print("=== Pivot Table: Tipe Restoran vs Online Order ===")
print(pivot_table)
print("\n")

# KESIMPULAN
print("="*60)
print("KESIMPULAN ANALISIS")
print("="*60)
print(f"1. Total restoran dalam dataset: {len(dataframe)}")
print(f"2. Restoran dengan online order: {len(dataframe[dataframe['online_order'] == 'Yes'])}")
print(f"3. Restoran tanpa online order: {len(dataframe[dataframe['online_order'] == 'No'])}")
print(f"4. Tipe restoran paling banyak: {dataframe['listed_in(type)'].value_counts().index[0]}")
print(f"5. Rating rata-rata: {dataframe['rate'].mean():.2f}")
print(f"6. Restoran dengan votes tertinggi: {restaurant_with_max_votes.values[0]}")
print("\nDari heatmap dapat dilihat bahwa:")
print("- Restoran makan (Dining) terutama menerima pesanan offline")
print("- Kafe terutama menerima pesanan online")
print("- Ini menunjukkan klien lebih suka memesan langsung di restoran")
print("  tetapi lebih suka memesan online di kafe")
print("="*60)