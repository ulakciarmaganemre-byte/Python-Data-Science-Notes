import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

saatler = pd.date_range("2026-04-02 00:00", "2026-04-02 23:59", freq="min")
kalp_ritmi = np.random.normal(75, 5, len(saatler))
df_saglik = pd.DataFrame({'Zaman': saatler, 'BPM': kalp_ritmi})

df_saglik.loc[(df_saglik['Zaman'].dt.hour >= 2) & (df_saglik['Zaman'].dt.hour <= 7), 'BPM'] -= 20 #uyku sırasında kalp ritmi düşer
df_saglik.loc[(df_saglik['Zaman'].dt.hour == 18) | (df_saglik['Zaman'].dt.hour == 19), 'BPM'] += 60 #egzersiz sırasında kalp ritmi yükselir

plt.figure(figsize=(14, 6))
df_saglik['BPM_Yumusak'] = df_saglik['BPM'].rolling(window=10).mean()
plt.plot(df_saglik['Zaman'], df_saglik['BPM_Yumusak'], color='magenta', linewidth=2)
plt.xlabel('Zaman')
plt.ylabel('BPM')
plt.title('Zamana göre günlük BPM değişimi')
genel_ortalama = df_saglik['BPM'].mean()
plt.axhline(genel_ortalama,label=f'Günlük Ortalama ({int(genel_ortalama)} BPM)')
plt.title("24 Saatlik Akıllı Saat Kalp Ritmi Analizi")
plt.xlabel("Tarih-Saat")
plt.ylabel("Nabız (BPM)")
plt.axvspan('2026-04-02 02:00', '2026-04-02 08:00', color='navy', alpha=0.2, label='Uyku')
plt.axvspan('2026-04-02 09:00', '2026-04-02 17:00', color='gold', alpha=0.2, label='Mesai')
plt.axvspan('2026-04-02 18:00', '2026-04-02 20:00', color='red', alpha=0.2, label='Spor')
plt.legend()
plt.show()
