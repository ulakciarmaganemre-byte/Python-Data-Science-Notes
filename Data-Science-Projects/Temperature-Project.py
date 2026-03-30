import numpy as np

sıcaklık = np.random.randint(low=-5, high=40, size=(364))
düzenli_sıcaklık = np.reshape(sıcaklık,(52,7))
sıralı_düzenli_sıcaklık = np.sort(düzenli_sıcaklık,axis=1)
en_düşük_sıcaklık = (sıralı_düzenli_sıcaklık.min(axis=1))
en_yüksek_sıcaklık = (sıralı_düzenli_sıcaklık.max(axis=1))
haftalar = list(range(1,53))

print(f"{en_düşük_sıcaklık,en_yüksek_sıcaklık}")

for i in range (52):
    print(f"Hafta {haftalar[i]}'en soğuk:{en_düşük_sıcaklık[i]}")
    print(f"Hafta {haftalar[i]}'en sıcak:{en_yüksek_sıcaklık[i]}\n")

koşul = sıcaklık > 30 
koşullu_sıcaklık = sıcaklık[koşul]
print(koşullu_sıcaklık)
print(len(koşullu_sıcaklık))

print(sıralı_düzenli_sıcaklık*1.8 + 32)
