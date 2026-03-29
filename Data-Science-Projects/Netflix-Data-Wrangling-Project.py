import pandas as pd
import numpy as np

# Veriyi yükleme
df = pd.read_csv("../data/netflix_titles.csv")

# Tarih Dönüşümü
df["date_added"] = pd.to_datetime(df["date_added"].str.strip())

# Yeni sütun oluşturma
df["release_year_added"] = df["date_added"].dt.year
df["month_added"] = df["date_added"].dt.month_name()

print(
    "Tarih dönüşümü tamamlandı. İlk 5 satır yıl bilgisi:\n",
    df[["title", "release_year_added"]].head(),
)

# Eksik değer doldurma
df["director"] = df["director"].fillna("Unknown")
df["cast"] = df["cast"].fillna("No Data")
df["country"] = df["country"].fillna(df["country"].mode()[0])

# 2. Süre (Duration) Parçalama: '90 min' -> 90 (int)
# 'min' ve 'Seasons' kelimelerin ayırıp sayı ve birim olarak iki yeni sütun oluşturma
df["duration_num"] = df["duration"].str.split(" ").str[0].fillna(0).astype(int)
df["duration_unit"] = df["duration"].str.split(" ").str[1]

print(
    "\nTemizlenmiş süre bilgileri:\n",
    df[["title", "duration_num", "duration_unit"]].head(),
)

movies = df[df["type"] == "Movie"]

# NumPy ile süre analizi
movie_durations = movies["duration_num"].values

avg_duration = np.mean(movie_durations)
median_duration = np.median(movie_durations)
std_duration = np.std(movie_durations)

print(f"\nNetflix Film İstatistikleri:")
print(f"Ortalama Süre: {avg_duration:.2f} dk")
print(f"Medyan Süre: {median_duration} dk")
print(f"Standart Sapma: {std_duration:.2f}")

# 4. En Çok İçerik Üreten İlk 5 Ülke
top_countries = df.assign(country=df["country"].str.split(", ")).explode("country")
top_5_countries = top_countries["country"].value_counts().head(5)

print("\nEn çok içerik üreten ilk 5 ülke:\n", top_5_countries)

# 5. Tür Analizi
pivot_table = df.pivot_table(
    index="release_year_added", columns="type", values="show_id", aggfunc="count"
).tail(10)
print("\nSon 10 yılda eklenen içerik türü dağılımı:\n", pivot_table)
