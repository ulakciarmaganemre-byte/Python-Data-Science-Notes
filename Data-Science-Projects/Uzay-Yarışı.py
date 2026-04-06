from matplotlib.pylab import f
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

ajanslar = ['SpaceX', 'NASA', 'ESA', 'Roscosmos', 'ISRO']
df_uzay = pd.DataFrame({
    'Ajans': ajanslar, 
    'Firlatma_Sayisi': [120, 85, 40, 60, 30], 
    'Ucus_Maliyeti_M$': [50, 150, 120, 70, 35], 
    'Basari_Orani_%': [98.5, 95.0, 92.5, 90.0, 94.0]
})

fig, (ax1,ax2) = plt.subplots(1,2,figsize=(12,6))
ax1.plot(df_uzay['Ajans'],df_uzay['Ucus_Maliyeti_M$'])
ax1.set_xlabel('Ajans İsimleri')
ax1.set_ylabel('Maliyetleri')
ax1.set_title('Ajanslar ve Maliyetleri')

ax2.bar(df_uzay['Ajans'],df_uzay['Firlatma_Sayisi'])
ax2.tick_params(axis='both', labelcolor='blue')
ax2.set_xlabel('Ajans İsimler')
ax2.set_ylabel('Fırlatma Sayısı')
ax2.set_title('Ajanslar ve Fırlatma Sayıları')

ax3 = ax2.twinx()
ax3.plot(df_uzay['Ajans'], df_uzay['Basari_Orani_%'], color='gold', marker='*', markersize=12, linewidth=2)
ax3.tick_params(axis='y', labelcolor='gold')
ax3.set_ylabel('Başarı Oranı',c='gold')
plt.show()
