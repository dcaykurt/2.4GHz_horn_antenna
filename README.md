# 2.4 GHz Dikdörtgen Boynuz Anten Tasarımı

<p align="center"><img src="gorseller/sonuclar/15dbi_isima_3b.png" width="420" alt="Boynuz anten 3B ışıma örüntüsü"></p>

## Proje Hakkında

Bu çalışmada 2.4 GHz bandında çalışan, 15 dBi hedef kazançlı bir dikdörtgen (piramidal) boynuz anten tasarlanmış, Altair FEKO ile elektromanyetik benzetimi yapılmış, üretilmiş ve sahada test edilmiştir. Çalışma Haziran 2022'de gerçekleştirilmiştir.

Tasarım sürecinde anten boyutları analitik bağıntılarla hesaplanmış, farklı kazanç ve frekans değerleri için modeller oluşturulmuştur. Dalga kılavuzu ve ağız boyutlarındaki değişimlerin kazanç ve hüzme genişliğine etkisi parametrik olarak incelenmiştir. Üretilen anten, NRF24L01 haberleşme modülleriyle açık alanda denenmiştir.

## Öne Çıkan Sonuçlar

| Parametre | Değer |
|---|---|
| Çalışma frekansı | 2.4 GHz |
| Benzetim kazancı (eksen yönünde) | **15.11 dBi** |
| Yarı güç hüzme genişliği (φ = 0° / φ = 90°) | 31.4° / 27.2° |
| Ağız ölçüleri (a₁ × b₁) | 30.7 cm × 25.0 cm |
| Benzetim aracı | Altair FEKO 2022 (MoM) |
| Saha testi | 300 m'de başarılı haberleşme; öngörülen pratik menzil 600–900 m |

## Tasarım

<p align="center"><img src="gorseller/diyagram/boynuz_geometri.svg" width="820" alt="Boynuz anten geometrisi"></p>

Anten ölçüleri, optimum kazançlı piramidal boynuz anten tasarım bağıntıları ile belirlenmiştir. G hedef kazancı (doğrusal) ve λ dalga boyu olmak üzere:

| Büyüklük | Bağıntı |
|---|---|
| Tasarım parametresi | χ ≈ G / (2π·√(2π)) |
| E düzlemi eğik uzunluk | ρₑ = χ·λ |
| H düzlemi eğik uzunluk | ρₕ = G²·λ / (8π³·χ) |
| Ağız ölçüleri | a₁ = √(3λρₕ),  b₁ = √(2λρₑ) |
| Boynuz uzunlukları | pₑ = (b₁ − b)·√((ρₑ/b₁)² − ¼),  pₕ = (a₁ − a)·√((ρₕ/a₁)² − ¼) |

Bu bağıntılarla 2.4 GHz ve 5 GHz için 12, 15 ve 18 dBi kazançlı tasarımlar hesaplanmıştır:

| Frekans | Kazanç | a × b (dalga kılavuzu) | a₁ × b₁ (ağız) | pₑ / pₕ |
|---|---|---|---|---|
| 2.4 GHz | 12 dBi | 10.48 × 4.91 cm | 21.72 × 17.73 cm | 6.45 / 3.29 cm |
| 2.4 GHz | **15 dBi** | 10.48 × 4.91 cm | **30.68 × 25.05 cm** | **17.49 / 13.08 cm** |
| 2.4 GHz | 18 dBi | 10.48 × 4.91 cm | 43.33 × 35.38 cm | 40.35 / 34.23 cm |
| 5 GHz | 12 dBi | 5.03 × 2.36 cm | 10.43 × 8.51 cm | 3.10 / 1.58 cm |
| 5 GHz | 15 dBi | 5.03 × 2.36 cm | 14.73 × 12.02 cm | 8.40 / 6.28 cm |
| 5 GHz | 18 dBi | 5.03 × 2.36 cm | 20.80 × 16.98 cm | 19.37 / 16.43 cm |

Hesaplamalar [`hesaplama/horn_tasarim.py`](hesaplama/horn_tasarim.py) ile farklı frekans ve kazanç değerleri için tekrarlanabilir:

```bash
python hesaplama/horn_tasarim.py                                   # tablo
python hesaplama/horn_tasarim.py -f 2.4e9 -g 15 -a 104.775 -b 49.0625
```

## Benzetim

Antenin dalga kılavuzu ve boynuz gövdesi CADFEKO'da modellenmiş, dalga kılavuzu portu ile beslenmiştir. Simetri düzlemleri tanımlanmış, ağ (mesh) oluşturulmuş ve model moment yöntemi (MoM) ile çözülmüştür. Sonuçlar POSTFEKO'da yakın alan ve uzak alan olarak incelenmiştir.

<p align="center">
  <img src="gorseller/sonuclar/15dbi_kazanc_kartezyen_hpbw.png" width="49%" alt="Kazanç - kartezyen">
  <img src="gorseller/sonuclar/15dbi_kazanc_polar_hpbw.png" width="40%" alt="Kazanç - polar">
</p>
<p align="center"><i>15 dBi tasarımın φ = 0° düzlemindeki kazancı: eksen yönünde 15.11 dBi, yarı güç hüzme genişliği 31.4°</i></p>

<p align="center">
  <img src="gorseller/sonuclar/15dbi_uzak_alan_2b.png" width="49%" alt="Uzak alan">
  <img src="gorseller/sonuclar/15dbi_yakin_alan_e.png" width="49%" alt="Yakın alan">
</p>
<p align="center"><i>Uzak alan toplam kazanç haritası (solda) ve ağız önündeki yakın alan elektrik alan dağılımı (sağda)</i></p>

<details>
<summary><b>FEKO'da tasarım adımları</b></summary>

| | |
|---|---|
| <img src="gorseller/tasarim_adimlari/02_dalga_kilavuzu_cizim.png" width="400"><br>Dalga kılavuzunun çizimi | <img src="gorseller/tasarim_adimlari/03_boynuz_cizim.png" width="400"><br>Boynuz gövdesinin çizimi |
| <img src="gorseller/tasarim_adimlari/04_birlestirme.png" width="400"><br>Parçaların birleştirilmesi (union) | <img src="gorseller/tasarim_adimlari/05_port.png" width="400"><br>Dalga kılavuzu portunun eklenmesi |
| <img src="gorseller/tasarim_adimlari/06_kaynak.png" width="400"><br>Kaynak tanımı | <img src="gorseller/tasarim_adimlari/07_frekans.png" width="400"><br>Frekansın belirlenmesi |
| <img src="gorseller/tasarim_adimlari/08_yakin_alan.png" width="400"><br>Yakın alan isteği | <img src="gorseller/tasarim_adimlari/09_uzak_alan.png" width="400"><br>Uzak alan isteği |
| <img src="gorseller/tasarim_adimlari/10_simetri.png" width="400"><br>Simetri düzlemleri | <img src="gorseller/tasarim_adimlari/11_mesh.png" width="400"><br>Ağ (mesh) oluşturma |
| <img src="gorseller/tasarim_adimlari/12_cozumleme.png" width="400"><br>Çözümleme | <img src="gorseller/tasarim_adimlari/13_postfeko.png" width="400"><br>Sonuçların incelenmesi |

</details>

## Boyutsal Değişimlerin Etkisi

Tasarlanan antenler üzerinde dalga kılavuzu ve ağız ölçüleri değiştirilerek kazanç ve hüzme genişliğine etkileri incelenmiştir.

| Model | Değişiklik | Eksen yönü kazancı | Hüzme genişliği (φ = 0° / 90°) |
|---|---|---|---|
| 12 dBi optimum | — | 11.92 dBi | 45.5° / 40.4° |
| 12 dBi | Dalga kılavuzu %30 küçültülmüş | 11.34 dBi | 49.3° / 42.7° |
| **15 dBi optimum** | — | **15.11 dBi** | **31.4° / 27.2°** |
| 15 dBi | Dalga kılavuzu %50 büyütülmüş | 15.43 dBi | 30.1° / 25.4° |
| 15 dBi | Ağız %50 küçültülmüş | 11.78 dBi | 40.7° / 53.2° |
| 15 dBi optimum, 5 GHz | — | 15.12 dBi | 31.4° / 27.2° |

Dalga kılavuzunun büyütülmesi kazancı az miktarda artırmış, ağzın küçültülmesi ise kazançta belirgin bir düşüşe ve hüzme genişliğinde artışa yol açmıştır. Ağzı küçültülmüş modelde ana hüzme bozulmakta ve en yüksek kazanç (13.54 dBi) eksen dışında, θ = 15° yönünde oluşmaktadır.

<p align="center">
  <img src="gorseller/sonuclar/dalga_kilavuzu_50_buyuk_kazanc.png" width="49%" alt="Dalga kılavuzu büyütülmüş">
  <img src="gorseller/sonuclar/agiz_50_kucuk_kazanc.png" width="49%" alt="Ağız küçültülmüş">
</p>
<p align="center"><i>Dalga kılavuzu %50 büyütülmüş model (solda) ve ağzı %50 küçültülmüş model (sağda)</i></p>

## Üretim ve Test

<p align="center"><img src="gorseller/uretim/uretilen_antenler.jpg" width="520" alt="Üretilen boynuz antenler"></p>

Anten, mukavva karton gövde üzerine alüminyum folyo kaplanarak üretilmiştir. Besleme SMA konektör ile yapılmıştır. Üretilen 2.4 GHz, 14 dBi'lik anten NRF24L01 haberleşme modülleriyle test edilmiştir. Hesaplanan açık alan menzili 950 m'dir. Test alanının izin verdiği en uzak mesafe olan 300 m'de haberleşme başarıyla sağlanmış; sonuçlara göre antenin pratikte 600–900 m menzile ulaşabileceği öngörülmüştür.

## Repo Yapısı

```
hesaplama/
├── horn_tasarim.py            Boyut hesaplama aracı
└── tasarlanan_antenler.xlsx   Tasarım tablosu
feko/
├── 2.4GHz/
│   ├── 12dBi_optimum/
│   ├── 12dBi_dalga_kilavuzu_30_kucuk/
│   ├── 15dBi_optimum/
│   ├── 15dBi_dalga_kilavuzu_50_buyuk/
│   └── 15dBi_agiz_50_kucuk/
└── 5GHz/
    └── 15dBi_optimum/
gorseller/                     Diyagramlar, benzetim sonuçları, tasarım adımları, üretim
```

FEKO klasörlerinde her model için CADFEKO modeli (`.cfx`), çözücü girdisi (`.pre`), POSTFEKO oturumu (`.pfs`), sonuç dosyaları (`.bof`, `.out`) bulunmaktadır. Modeller Altair FEKO 2022 Student Edition ile oluşturulmuştur.

## Lisans

Bu proje [MIT Lisansı](LICENSE) ile yayımlanmıştır.

---

**Deniz Can Aykurt** · Elektrik Elektronik Mühendisi
