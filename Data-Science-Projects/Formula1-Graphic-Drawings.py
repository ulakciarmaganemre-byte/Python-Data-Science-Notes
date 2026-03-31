import pandas as pd
import numpy as np

np.random.seed(42)
print("Formula 1 Veri Setleri Yükleniyor...\n")
# =========================================================
# VERİ 1: Şampiyona Puan Durumu (Lineplot ve Annotate için)
# =========================================================
yarislar = np.arange(1, 23)
df_sampiyona = pd.DataFrame({
    'Yaris_No': yarislar,
    'Verstappen': np.cumsum(np.random.randint(15, 26, size=22)), 
    'Hamilton': np.cumsum(np.random.randint(10, 25, size=22)),   
    'Leclerc': np.cumsum(np.random.randint(0, 20, size=22))     
})
df_sampiyona.loc[17, 'Hamilton'] = df_sampiyona.loc[16, 'Hamilton'] 

# =========================================================
# VERİ 2: Takımların Galibiyet Sayıları 
# =========================================================
df_takimlar = pd.DataFrame({
    'Takim': ['Red Bull', 'Mercedes', 'Ferrari', 'McLaren', 'Aston Martin'],
    'Galibiyet': [12, 6, 3, 1, 0]
})

# =========================================================
# VERİ 3: Pit Stop Süreleri ve Bitiş Pozisyonu 
# =========================================================

pit_sureleri = np.random.uniform(1.8, 5.0, 100)
bitis_pozisyonu = (pit_sureleri * 3) + np.random.normal(0, 3, 100)
bitis_pozisyonu = np.clip(bitis_pozisyonu, 1, 20) 

df_pitstop = pd.DataFrame({
    'Pit_Suresi_Sn': pit_sureleri,
    'Sira': np.round(bitis_pozisyonu).astype(int)
})

import matplotlib.pyplot as plt

plt.style.use('default')

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

ax1.plot(df_sampiyona['Yaris_No'],df_sampiyona['Verstappen'], color='blue', marker='o',label="Verstappen")
ax1.plot(df_sampiyona['Yaris_No'],df_sampiyona['Hamilton'], color='yellow', marker='o',label="Hamilton")
ax1.plot(df_sampiyona['Yaris_No'],df_sampiyona['Leclerc'], color='red', marker='o',label="Leclerc")
ax1.set_title("Puan Durumu")
ax1.set_xlabel("Yarışlar")
ax1.set_ylabel("Puanlar")
ax1.grid(True)
ax1.legend(loc='best')
ax1.annotate('Kritik Puan Kaybı!',xy=(18,307),xytext=(16,270),arrowprops=dict(facecolor='red',shrink=0.05),fontsize=8, fontweight='bold',color='red')

ax2.bar(df_takimlar['Takim'], df_takimlar['Galibiyet'], color='green')
ax2.set_title("Takım Galibiyetleri")
ax2.set_xlabel("Takımlar")
ax2.grid(True)

plt.tight_layout()
plt.show()

plt.figure(figsize=(6,6), dpi=100, facecolor='w', edgecolor='k')
plt.scatter(df_pitstop['Pit_Suresi_Sn'],df_pitstop['Sira'],c=df_pitstop['Pit_Suresi_Sn'],cmap='plasma',alpha=0.8)
plt.title("Pit Süresi ve Sıraları") 
plt.xlabel("Pit Süresi") 
plt.ylabel("Sıralar")
plt.colorbar(label="Pit Süresi")
plt.show()
