import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

plt.style.use('dark_background') 

np.random.seed(99)
zaman_dakika = np.arange(0, 1440) 

trafik_mb = 50 + 20 * np.sin(zaman_dakika / 60) + np.random.normal(0, 5, 1440) 

trafik_mb[500:510] += 150 
trafik_mb[1200:1220] += 200 

df_network = pd.DataFrame({'Dakika': zaman_dakika, 'Trafik_MB': trafik_mb})

esik_degeri = df_network['Trafik_MB'].mean() + (df_network['Trafik_MB'].std() * 3)
anomaliler = df_network[df_network['Trafik_MB'] > esik_degeri] 

plt.figure(figsize=(14, 5))

plt.plot(df_network['Dakika'], df_network['Trafik_MB'], 
         color='cyan', alpha=0.7, label='Sistem Trafiği')

plt.scatter(anomaliler['Dakika'], anomaliler['Trafik_MB'], 
            color='red', s=45, label='Tespit Edilen Anomali', zorder=5) 

plt.axhline(esik_degeri, color='yellow', linestyle=':', linewidth=2, label='Tehlike Eşiği')

plt.annotate('Kritik Yüklenme Tespiti', xy=(1210, 260), xytext=(900, 280),
             arrowprops=dict(facecolor='yellow', shrink=0.05), color='yellow', fontsize=11)

plt.title("24 Saatlik Ağ Trafiği Monitörü ve Anomali Logları")
plt.xlabel("Günün Dakikaları (0 - 1440)")
plt.ylabel("Veri Transferi (MB)")
plt.legend(loc='upper left')

plt.tight_layout()
plt.savefig('siber_guvenlik_log_analizi.png', dpi=300)
plt.show()
