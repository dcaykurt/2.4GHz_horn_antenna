"""
Dikdörtgen (piramidal) boynuz anten boyut hesabı.

Verilen frekans, hedef kazanç ve besleme dalga kılavuzu ölçülerinden
optimum kazançlı boynuz antenin ağız ve uzunluk ölçülerini hesaplar.

Yöntem: optimum piramidal boynuz tasarım bağıntıları
(C. A. Balanis, Antenna Theory, piramidal boynuz tasarımı). Tasarım
parametresi χ için ilk yaklaşım χ ≈ G / (2π·√(2π)) kullanılır.

Kullanım:
    python horn_tasarim.py                     # 2.4 GHz ve 5 GHz tablosu
    python horn_tasarim.py -f 2.4e9 -g 15 -a 104.775 -b 49.0625
"""
import argparse
import math

C = 3e8  # ışık hızı [m/s]


def boynuz_olcu(f_hz, g_dbi, a, b):
    """Ölçüler metre cinsinden döner.

    a, b   : dalga kılavuzu iç ölçüleri (geniş / dar kenar)
    rho_e  : E düzleminde tepe noktasından ağıza eğik uzunluk
    rho_h  : H düzleminde tepe noktasından ağıza eğik uzunluk
    a1, b1 : ağız ölçüleri (H / E düzlemi)
    p_e    : E düzleminde boynuz (konik kısım) eksenel uzunluğu
    p_h    : H düzleminde boynuz eksenel uzunluğu
    wg_h   : p_e ve p_h ortalaması (çizimde kullanılan boynuz yüksekliği)
    """
    lam = C / f_hz
    g = 10 ** (g_dbi / 10)
    chi = g / (2 * math.pi * math.sqrt(2 * math.pi))

    rho_e = chi * lam
    rho_h = g ** 2 * lam / (8 * math.pi ** 3 * chi)
    a1 = math.sqrt(3 * lam * rho_h)
    b1 = math.sqrt(2 * lam * rho_e)

    def eksenel(aciklik, kenar, rho):
        k = (rho / aciklik) ** 2 - 0.25
        return (aciklik - kenar) * math.sqrt(k) if k > 0 and aciklik > kenar else float("nan")

    p_e = eksenel(b1, b, rho_e)
    p_h = eksenel(a1, a, rho_h)
    return dict(lam=lam, rho_e=rho_e, rho_h=rho_h, a1=a1, b1=b1,
                p_e=p_e, p_h=p_h, wg_h=(p_e + p_h) / 2)


def yazdir(f_hz, g_dbi, a, b):
    r = boynuz_olcu(f_hz, g_dbi, a, b)
    cm = lambda x: "  -  " if math.isnan(x) else f"{x * 100:6.2f}"
    print(f"{f_hz / 1e9:4.1f} GHz {g_dbi:3.0f} dBi | a={a*100:5.2f} b={b*100:5.2f} | "
          f"ρe={cm(r['rho_e'])} ρh={cm(r['rho_h'])} a1={cm(r['a1'])} b1={cm(r['b1'])} "
          f"pe={cm(r['p_e'])} ph={cm(r['p_h'])} [cm]")


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description="Piramidal boynuz anten boyut hesabı")
    ap.add_argument("-f", "--frekans", type=float, help="frekans [Hz]")
    ap.add_argument("-g", "--kazanc", type=float, help="hedef kazanç [dBi]")
    ap.add_argument("-a", type=float, help="dalga kılavuzu geniş kenarı [mm]")
    ap.add_argument("-b", type=float, help="dalga kılavuzu dar kenarı [mm]")
    arg = ap.parse_args()

    if arg.frekans:
        yazdir(arg.frekans, arg.kazanc, arg.a / 1000, arg.b / 1000)
    else:
        # Projede kullanılan dalga kılavuzları
        for f, a, b in [(2.4e9, 0.104775, 0.0490625), (5e9, 0.050292, 0.02355)]:
            for g in (8, 12, 15, 18):
                yazdir(f, g, a, b)
            print()
