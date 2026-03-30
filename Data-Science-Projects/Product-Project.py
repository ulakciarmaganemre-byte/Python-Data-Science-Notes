import pandas as pd
import numpy as np

np.random.seed(101)

df_urunler = pd.DataFrame({
    'Urun_ID': ['U101', 'U102', 'U103', 'U104', 'U105'],
    'Maliyet': [50, 120, 30, 80, 200],
    'Satis_Fiyati': [80, 180, 50, 130, 320],
    'Teslimat_Suresi_Gun': [3, 5, 2, 4, 7] 
})

tarihler = pd.date_range(start='2024-01-01', periods=180, freq='D')
magazalar = ['Magaza_A', 'Magaza_B', 'Magaza_C']
urunler = df_urunler['Urun_ID'].tolist()

index = pd.MultiIndex.from_product([tarihler, magazalar, urunler], names=['Tarih', 'Magaza', 'Urun_ID'])
df_talep = pd.DataFrame(index=index).reset_index()

df_talep['Musteri_Talebi'] = np.random.poisson(lam=15, size=len(df_talep))

df_talep['Gunluk_Stok'] = 20

print("--- Ürün Kataloğu ---")
print(df_urunler)
print("\n--- Talep Logları (İlk 5 Satır) ---")
print(df_talep.head())


df_birleş = pd.merge(df_urunler,df_talep,on="Urun_ID") 

df_birleş["Gerçekleşen_Satış"] = np.where(df_birleş['Musteri_Talebi']<20,df_birleş['Musteri_Talebi'],np.nan)  
df_birleş["Kayıp_Satış"] = np.where(df_birleş['Musteri_Talebi']>20,df_birleş['Musteri_Talebi']-20,np.nan)    
