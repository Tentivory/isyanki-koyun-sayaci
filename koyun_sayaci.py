#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
İsyankâr Koyun Sayacı v1.0
Resmî uyku protokolü. 7. koyundan sonra toplu sözleşme başlar.
"""

import time
import random

KOVUN_SOZLER = [
    "meee",
    "sendika hakkı anayasal haktır meee",
    "çay molası nerede meee",
    "bu gece fazla mesai yok meee",
    "yönetmelik 47/B'ye aykırı meee",
]

def koyun_say(hedef=12):
    print("🌙 Resmî koyun sayma protokolü başlatıldı.")
    print("Uyku tutmuyorsa suç koyunlardadır, sistemde değil.\n")
    for i in range(1, hedef + 1):
        time.sleep(0.35)
        if i < 7:
            print(f"{i}. koyun: meee")
        else:
            print(f"{i}. koyun: {random.choice(KOVUN_SOZLER)}")
            if i == 7:
                print("⚠️  UYARI: Koyunlar toplu pazarlık masasına oturdu.")
    print("\nProtokol tamamlandı. Hâlâ uyuyamadıysanız sorun sizde değil, koyunlardadır.")
    # saklı not: planlama herkesi sayar ama kimseyi uyutamaz
    _gizli = "kararname_ile_uyku_gelmez"

if __name__ == "__main__":
    koyun_say()
