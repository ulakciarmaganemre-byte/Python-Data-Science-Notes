import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme(style="whitegrid")
np.random.seed(42)

gunler = np.arange(1, 29)
haftalar = ['Hafta 1']*7 + ['Hafta 2']*7 + ['Hafta 3']*7 + ['Hafta 4']*7
uyku_saati = np.linspace(8, 4, 28) + np.random.normal(0, 0.5, 28)
yazilan_kod = np.linspace(100, 1000, 28) + np.random.normal(0, 100, 28)
sicrama_cm = np.linspace(30, 45, 28) + np.random.normal(0, 1.5, 28) 

df_performans = pd.DataFrame({
    'Gun': gunler, 'Hafta': haftalar, 'Uyku': uyku_saati, 
    'Kod_Satiri': yazilan_kod, 'Sicrama_Cm': sicrama_cm
})

fig , (ax1,ax2) = plt.subplots(1,2,figsize= (15,6))
sns.barplot(data=df_performans, x='Hafta',y='Kod_Satiri',capsize=0.1,palette='mako',ax=ax1)
ax2.plot(df_performans['Gun'],df_performans['Uyku'],color='red',marker='o',label='Uyku (Saat)')
ax2.set_xlabel('Günler',color='red')
ax2.set_ylabel('Uyku (Saat)',color='red')
ax2.tick_params(axis='y', labelcolor='red')
ax3 = ax2.twinx()
ax3.plot(df_performans['Gun'],df_performans['Sicrama_Cm'],color='green', marker='s', linestyle='--',label='Sıçrama (Cm)')
ax3.set_ylabel("Dikey Sıçrama (Cm)", color='green')
ax3.tick_params(axis='y', labelcolor='green')
plt.title('Uyku Yoksunluğu vs Fiziksel Gelişim')
ax2.legend(loc='best')
ax3.legend(loc='best')
plt.tight_layout()
plt.show()
