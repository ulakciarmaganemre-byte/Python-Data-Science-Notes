import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme(style="white")
np.random.seed(42)

grup = np.random.choice(['A (Eski Tasarım)', 'B (Yeni Tasarım)'], 500)
yas = np.random.randint(18, 65, 500)

harcama = np.where(grup == 'B (Yeni Tasarım)', 
                   np.random.normal(500, 150, 500), 
                   np.random.normal(420, 120, 500))
harcama += np.where((yas > 30) & (yas < 40), 100, 0)

df_ecom = pd.DataFrame({'Test_Grubu': grup, 'Yas': yas, 'Harcama_TL': harcama})

# Analiz derinliğini artırmak için yaş verisini kategorik segmentlere ayırma
df_ecom['Yas_Grubu'] = pd.cut(df_ecom['Yas'], 
                              bins=[17, 25, 35, 50, 65], 
                              labels=['18-25', '26-35', '36-50', '50+'])

fig = plt.figure(figsize=(15, 6))

ax1 = plt.subplot(1, 2, 1)
sns.kdeplot(data=df_ecom, x="Harcama_TL", hue="Test_Grubu", 
            fill=True, common_norm=False, palette="crest", alpha=0.5, ax=ax1)

ax1.set_title("A/B Testi: Tasarımın Satışlara Etkisi")
ax1.set_xlabel("Harcama (TL)")
ax1.set_ylabel("Yoğunluk")

ax2 = plt.subplot(1, 2, 2)
sns.boxplot(x="Yas_Grubu", y="Harcama_TL", hue="Test_Grubu", 
            data=df_ecom, palette="Set2", ax=ax2)

ax2.set_title("Yaş Gruplarına Göre Harcama Dağılımı")
ax2.set_xlabel("Yaş Segmenti")
ax2.set_ylabel("Harcama (TL)")

plt.tight_layout()
plt.savefig('ab_testi_sonuclari.png', dpi=300)
plt.show()
