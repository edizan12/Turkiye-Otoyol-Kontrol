import datetime

# Otoyol veri tabanı
otoyollar = {
    "O-1": {"isim": "İstanbul 1. Çevreyolu", "ucretli": False, "yid": False},
    "O-2": {"isim": "İstanbul 2. Çevreyolu (TEM)", "ucretli": True, "yid": False},
    "O-3": {"isim": "Avrupa Otoyolu", "ucretli": True, "yid": False},
    "O-4": {"isim": "Anadolu Otoyolu", "ucretli": True, "yid": False},
    "O-5": {"isim": "İstanbul–İzmir Otoyolu + Osmangazi", "ucretli": True, "yid": True},
    "O-6": {"isim": "Kuzey Marmara Otoyolu", "ucretli": True, "yid": True},
    "O-20": {"isim": "Ankara Çevreyolu", "ucretli": False, "yid": False},
    "O-30": {"isim": "İzmir Çevreyolu", "ucretli": False, "yid": False},
    "O-31": {"isim": "İzmir–Aydın Otoyolu", "ucretli": True, "yid": False},
    "O-32": {"isim": "İzmir–Çeşme Otoyolu", "ucretli": True, "yid": False},
    "YSS": {"isim": "Yavuz Sultan Selim Köprüsü", "ucretli": True, "yid": True},
    "FSM": {"isim": "Fatih Sultan Mehmet Köprüsü", "ucretli": True, "yid": False},
    "15TEM": {"isim": "15 Temmuz Şehitler Köprüsü", "ucretli": True, "yid": False},
    "AVRASYA": {"isim": "Avrasya Tüneli", "ucretli": True, "yid": True},
    "ÇANAKKALE": {"isim": "1915 Çanakkale Köprüsü", "ucretli": True, "yid": True},
}

# Bayram zamanları (örnek veri; gerçek sorgu için Resmî Gazete verileri kullanılabilir)
bayramlar = [
    (datetime.date(2025,6,5), datetime.date(2025,6,9))  # Kurban Bayramı 2025
]

def bayram_mi(tarih):
    return any(start <= tarih <= end for start, end in bayramlar)

def otoyol_durum(kod, tarih=None):
    tarih = tarih or datetime.date.today()
    bayram = bayram_mi(tarih)
    kod = kod.upper()
    if kod not in otoyollar:
        return f"{kod} adlı otoyol veya köprü bulunamadı."
    oto = otoyollar[kod]
    if bayram and not oto["yid"]:
        return f"{oto['isim']} — BAYRAM DÖNEMİ ÜCRETSİZ."
    return f"{oto['isim']} — {'ÜCRETLİ' if oto['ucretli'] else 'ÜCRETSİZ'}."

if __name__ == "__main__":
    print("Otoyol kodunu girin (örn: O-4, FSM, YSS). 'q' ile çıkış.")
    while True:
        giris = input("> ").strip()
        if giris.lower() == 'q':
            break
        print(otoyol_durum(giris))
