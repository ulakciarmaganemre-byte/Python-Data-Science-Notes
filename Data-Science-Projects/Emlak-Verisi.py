import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme(style="ticks")
np.random.seed(77)

m2 = np.random.uniform(60, 250, 300)
uzaklik_km = np.random.uniform(1, 40, 300)
yas = np.random.randint(0, 40, 300)
fiyat_bin_tl = (m2 * 20) - (uzaklik_km * 50) - (yas * 30) + np.random.normal(0, 500, 300) + 5000
mahalle = np.where(uzaklik_km < 10, 'Merkez', np.where(uzaklik_km < 25, 'Banliyö', 'Kırsal'))
df_emlak = pd.DataFrame({'Fiyat_BinTL': fiyat_bin_tl, 'Metrekare': m2, 'Uzaklik_Km': uzaklik_km, 'Yas': yas, 'Bolge': mahalle})

plt.figure(figsize=(10,6))
sns.scatterplot(data=df_emlak,x='Uzaklik_Km',y='Fiyat_BinTL',hue='Bolge',size=m2,sizes=(20,200),palette='viridis',alpha=0.7)
plt.xlabel('Uzaklık')
plt.ylabel('Fiyat')
plt.legend(bbox_to_anchor=(1, 1), loc='upper left')
plt.annotate('En pahallı malikane', xy=(5, 9500), xytext=(5, 9000), arrowprops=dict(facecolor='red', shrink=0.05), fontsize=9, color='black', fontweight='bold')
plt.grid(True, linestyle='--', alpha=0.5)
plt.title('Emlak Fiyatları ve Uzaklık İlişkisi')
plt.show()
