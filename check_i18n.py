# -*- coding: utf-8 -*-
"""Çeviri dosyalarını kaynakla (i18n/tr.json) karşılaştırır: anahtarlar, dizi biçimleri, yer tutucular.
Çalıştır:  python check_i18n.py"""
import io, json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
I18N = os.path.join(HERE, "i18n")
src = json.load(io.open(os.path.join(I18N, "tr.json"), encoding="utf-8"))
KEEP = ["Hazar Canal", "Atlas", "Devil", "Barbaros", "Şahmaran", "Arora", "iyzico", "Shopier", "Etsy"]


def shape(v):
    if isinstance(v, list):
        return [shape(x) for x in v]
    return "s"


def strings(v):
    if isinstance(v, list):
        for x in v:
            yield from strings(x)
    else:
        yield v


bad = 0
for f in sorted(os.listdir(I18N)):
    if f == "tr.json" or not f.endswith(".json"):
        continue
    try:
        d = json.load(io.open(os.path.join(I18N, f), encoding="utf-8"))
    except Exception as ex:
        print(f, "JSON HATASI:", ex)
        bad += 1
        continue
    problems = []
    if set(d) != set(src):
        problems.append("anahtar farkı: eksik %s, fazla %s" % (sorted(set(src) - set(d)), sorted(set(d) - set(src))))
    for k in src:
        if k not in d:
            continue
        if shape(d[k]) != shape(src[k]):
            problems.append("biçim farkı: " + k)
            continue
        for a, b in zip(strings(src[k]), strings(d[k])):
            if sorted(re.findall(r"\{\w+\}", a)) != sorted(re.findall(r"\{\w+\}", b)):
                problems.append("yer tutucu farkı: " + k)
            for name in KEEP:
                if name in a and name not in b:
                    problems.append("ad korunmamış (%s): %s" % (name, k))
            if not b.strip():
                problems.append("boş değer: " + k)
            if "—" in b:
                problems.append("uzun çizgi: " + k)
    print(f, "tamam" if not problems else "\n  " + "\n  ".join(problems))
    bad += len(problems)
sys.exit(1 if bad else 0)
