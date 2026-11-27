# -*- coding: utf-8 -*-
"""Sayfalardaki Wix medya adreslerini site/media/ klasörüne indirir ve media_map.json yazar.
build.py bu haritayı bulursa sayfaları yerel dosyalara bağlar.
Çalıştır:  python fetch_media.py  (ardından python build.py)"""
import glob, io, json, os, re, urllib.request

ROOT = os.path.dirname(os.path.abspath(__file__))
SITE = os.path.join(ROOT, "site")
MEDIA = os.path.join(SITE, "media")
MAP = os.path.join(ROOT, "media_map.json")
PAT = re.compile(r'https://(?:static|video|music)\.wixstatic\.com/[^"\s<>]+')


def local_name(u):
    m = re.search(r"/media/(?:584124_)?([0-9a-f]{8})[0-9a-f]*f000\.jpg$", u)
    if m: return f"poster-{m.group(1)}.jpg"
    m = re.search(r"/media/(?:584124_)?([0-9a-f]{8})[^/]*/v1/fit/w_(\d+)[^/]*/hc\.(\w+)$", u)
    if m: return f"img-{m.group(1)}-{m.group(2)}.{m.group(3)}"
    m = re.search(r"/video/(?:584124_)?([0-9a-f]{8})[^/]*/(\w+)/mp4/file\.mp4$", u)
    if m: return f"film-{m.group(1)}.mp4"
    if u.endswith(".mp3"): return "sahmaran.mp3"
    raise SystemExit("Tanınmayan adres: " + u)


if os.path.exists(MAP):
    os.remove(MAP)  # haritasız üret ki uzak adresler görünsün
import build  # noqa: E402
build.main()

urls = sorted({u for f in glob.glob(os.path.join(SITE, "*.html")) for u in PAT.findall(io.open(f, encoding="utf-8").read())})
os.makedirs(MEDIA, exist_ok=True)
mp, total = {}, 0
for u in urls:
    name = local_name(u)
    dst = os.path.join(MEDIA, name)
    if not os.path.exists(dst) or os.path.getsize(dst) == 0:
        req = urllib.request.Request(u, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=120) as r, open(dst, "wb") as o:
            o.write(r.read())
    total += os.path.getsize(dst)
    mp[u] = "media/" + name
    print(f"{os.path.getsize(dst) / 1024:8.0f} KB  {name}")
assert len(set(mp.values())) == len(mp), "ad çakışması"
json.dump(mp, io.open(MAP, "w", encoding="utf-8"), indent=1)
build.main()
print(f"{len(mp)} dosya, toplam {total / 1048576:.1f} MB")
