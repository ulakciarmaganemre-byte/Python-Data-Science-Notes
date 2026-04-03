import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

np.random.seed(10)

yillar = np.repeat(np.arange(1970, 2021), 12)
ay_isimleri = ['Oca', 'Şub', 'Mar', 'Nis', 'May', 'Haz', 'Tem', 'Ağu', 'Eyl', 'Eki', 'Kas', 'Ara']
aylar = np.tile(ay_isimleri, 51)

trend = np.repeat(np.linspace(-0.2, 1.2, 51), 12) 
sicaklik_farki = trend + np.random.normal(0, 0.2, len(yillar))

df_iklim = pd.DataFrame({'Yil': yillar, 'Ay': aylar, 'Fark_Derece': sicaklik_farki})

df_yillik = df_iklim.groupby('Yil')['Fark_Derece'].mean().reset_index()

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))

ax1.plot(df_yillik['Yil'], df_yillik['Fark_Derece'], color='crimson', linewidth=2)


ax1.fill_between(df_yillik['Yil'], 0, df_yillik['Fark_Derece'], 
                 where=(df_yillik['Fark_Derece'] > 0), color='red', alpha=0.3)
ax1.fill_between(df_yillik['Yil'], 0, df_yillik['Fark_Derece'], 
                 where=(df_yillik['Fark_Derece'] <= 0), color='blue', alpha=0.3)

ax1.axhline(0, color='black', linestyle='--') 
ax1.set_title("Küresel Sıcaklık Anomalisi (1970-2020)")
ax1.set_xlabel("Yıl")
ax1.set_ylabel("Referans Sıcaklıktan Fark (°C)")

iklim_matris = df_iklim.pivot(index='Yil', columns='Ay', values='Fark_Derece')
iklim_matris = iklim_matris[ay_isimleri] 


sns.heatmap(iklim_matris, cmap='coolwarm', center=0, ax=ax2,
            cbar_kws={'label': 'Sıcaklık Farkı (°C)'}) 

ax2.set_title("Aylık İklim Anomalisi Isı Haritası")
ax2.set_xlabel("Aylar")
ax2.set_ylabel("Yıllar")

plt.tight_layout()
plt.savefig('iklim_trend_analizi.png', dpi=300)
plt.show()
