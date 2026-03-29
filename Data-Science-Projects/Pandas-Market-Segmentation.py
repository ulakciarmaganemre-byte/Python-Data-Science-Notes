import pandas as pd
import numpy as np

np.random.seed(42)

musteri_sayisi = 500

df = pd.DataFrame(
    {
        "Musteri_ID": range(1001, 1001 + musteri_sayisi),
        "Uyelik_Tarihi": pd.to_datetime(
            np.random.choice(pd.date_range("2020-01-01", "2025-12-31"), musteri_sayisi)
        ),
        "Harcama_TL": np.random.uniform(100, 15000, musteri_sayisi).round(2),
        "Bolge": np.random.choice(
            ["Marmara", "Ege", "İç Anadolu", "Akdeniz", "Karadeniz"], musteri_sayisi
        ),
        "Son_Yorum": np.random.choice(
            [
                "Harika bir hizmet, çok memnunum.",
                "Fiyatlar çok pahalı iptal edeceğim!",
                "Kargo çok hızlı geldi, teşekkürler.",
                "Destek ekibi çok yavaş, üyeliği İPTAL etmeyi düşünüyorum.",
                "Normal bir deneyim, fena değil.",
                "Uygulama sürekli çöküyor, kesinlikle Iptal!",
                "Ürün defolu geldi ama iade süreci kolaydı.",
            ],
            musteri_sayisi,
        ),
    }
)

gunumuz = "2026-03-26"

# Görev 1: Üyelik Süresini Hesapla
df["Uyelik_Gunu"] = (pd.to_datetime(gunumuz) - df["Uyelik_Tarihi"]).dt.days

# Görev 2: Müşterileri Harcamalarına Göre Segmentlere Ayır
df["Harcama_Skoru"] = pd.qcut(
    df["Harcama_TL"], q=4, labels=["Düşük", "Orta", "Yüksek", "Premium"]
)

# Görev 3: İptal Riski Taşıyanları Tespit Et
df["Güvenlik_Durumu"] = np.where(
    df["Son_Yorum"].str.contains("iptal|ıptal", case=False, na=False),
    "riskli",
    "güvenli",
)
riskli_df = df[df["Güvenlik_Durumu"] == "riskli"]

# Görev 4: Çapraz Tablo (Crosstab) ile Özet Rapor Çıkar
ozet_tablo = pd.crosstab(df["Güvenlik_Durumu"], df["Harcama_Skoru"], margins=True)

# Sonuçlar
print("--- Özet Tablo ---")
print(ozet_tablo)
print("\n--- İlk 5 Müşteri Kaydı ---")
print(df.head())
