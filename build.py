# -*- coding: utf-8 -*-
"""Hazar Canal — statik site üretici.
Çalıştır:  python build.py   →  site/ klasörüne HTML sayfalarını yazar.
Tüm metinler hazarcanal.com'daki mevcut içerikten alınmıştır."""
import json, os, html

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "site")
MEDIA = "https://static.wixstatic.com/media/"
VIDEO = "https://video.wixstatic.com/video/"
AUDIO = "https://music.wixstatic.com/mp3/584124_a6968e2524b84530b68977e4395fe0bd-320.mp3"
# Sitenin yayınlandığı adres (paylaşım önizleme görseli için). Kendi alan adına taşınınca değiştirin.
SITE_URL = "https://efehamdioglu.com/hazar-canal/"
# Önizleme sürümü arama motorlarında asıl siteyle yarışmasın. Asıl siteye dönüşünce False yapın.
NOINDEX = True
EMAIL = "hazarcanal@icloud.com"
INSTAGRAM = "https://www.instagram.com/hazarcanalperfumes/"
TIKTOK = "https://www.tiktok.com/@hazarcanalparfum"
TESTER_URL = "https://www.shopier.com/Hazarcanal/44750828"

e = html.escape

# fetch_media.py çalıştırıldıysa uzak Wix adresleri yerel dosyalarla değiştirilir.
_MAP_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "media_map.json")


def localize(doc):
    if not os.path.exists(_MAP_FILE):
        return doc
    mp = json.load(open(_MAP_FILE, encoding="utf-8"))
    for u in sorted(mp, key=len, reverse=True):
        doc = doc.replace(u, mp[u])
    doc = doc.replace('property="og:image" content="media/', f'property="og:image" content="{SITE_URL}media/')
    if "wixstatic.com/" not in doc.replace('href="https://static.wixstatic.com"', ""):
        doc = doc.replace('<link rel="preconnect" href="https://static.wixstatic.com">' + chr(10), "")
    return doc

# Türkçe sayfada (lang="tr") büyük harfe çevrilen yabancı sözcükler "İ" almasın diye lang="en" ile sarılır.
EN_WORDS = {"Devil", "Extrait de Parfum", "Eau de Parfum", "Unisex", "Alcohol Free", "Ambergris", "Litchi",
            "Fragrantica Awards — 68th Best Bottle Design", "Cherry", "White Chocolate", "Passion Flower", "Vanilla",
            "Pineapple", "Seaweed", "Frangipani", "Sandalwood", "Vanilla Absolute", "Blueberry", "Musc", "Patchouli",
            "Pink Pepper", "Hibiscus", "Apricot", "Coconut", "Lily of the Valley", "Cocoa Absolute", "Iris", "Cedarwood"}


def tx(x):
    return f'<span lang="en">{e(x)}</span>' if x in EN_WORDS else e(x)


def brandfix(x):
    for w in ("Shopier", "Instagram", "TikTok", "Get it on Etsy"):
        x = x.replace(w, f'<span lang="en">{w}</span>')
    return x


def im(i, w=1200):
    ext = "png" if i.endswith("1ab5b23b7d5743d997bc1f10f3cb0c17~mv2.png") else "jpg"
    return f"{MEDIA}{i}/v1/fit/w_{w},h_{w},q_85/hc.{ext}"


def vid(i):
    return f"{VIDEO}{i}/720p/mp4/file.mp4"


def poster(i):
    return f"{MEDIA}{i}f000.jpg"


LOGO = "584124_1ab5b23b7d5743d997bc1f10f3cb0c17~mv2.png"
SKETCH = "584124_7e40977f842d4157abb6a4359ce6632b~mv2.jpeg"
LINEUP = "584124_c4d28bc2867945f284ddc85d30bae62e~mv2.jpg"

CRAFT = [
    ("El Yapımı Tasarım",
     "Her Hazar Canal şişesi ve mızrak kapağı, özgün tasarım sürecinin ardından el işçiliğiyle üretilir ve boyanır. Her parça küçük farklılıklar taşıyarak onu benzersiz kılar."),
    ("Doğal Yağlar",
     "Formüllerimizde yüksek kaliteli doğal yağlar ve özenle seçilmiş aromatik hammaddeler kullanılır."),
]
TICKS = ["Uzun kalıcılık", "Niş kalite esans", "Güvenli ödeme"]

P = [
    dict(
        slug="atlas", name="Atlas", kind="Extrait de Parfum", gender="Unisex",
        tagline="Sessiz lüksün zirvesi.", chips=["Odunsu", "Derin", "Tanrısal"],
        video="584124_b9ed81cf9ab044d896630c9f70f290ed",
        card_notes=[], badges=["Alcohol Free"],
        story=[
            "Efsaneler, göğü omuzlarında taşıyan bir varlıktan bahseder. Yük onun için ağırlık değil, kaderdir.",
            "İlk dokunuşta kayısının altın ışığı yükselir. Güneşin batmadan önce bıraktığı sıcak iz gibi. Hindistan cevizi kremsi bir katman örer;",
            "Kalbinde müge çiçeği gizlidir. Tanrısal bir saflık, görünmeyen bir zarafet.",
            "Sonra karanlık derinleşir. Kakao sahneye iner; yoğun, koyu, neredeyse kadim. Amber Xtreme gücü büyütür, aurayı genişletir, etrafında görünmez bir hâle oluşturur.",
            "Ve sandal ağacı… Toprağın hafızası gibi. Zamansız. Sarsılmaz. Sonsuz.",
        ],
        story_big="Bu bir mit.",
        love_title="“Bunları seviyorsan, Atlas sana göre.”",
        love=["İnsanların kokunu merak etmesini seviyorsan.",
              "Tehlikeli bir aura taşımanın kötü bir şey olmadığını düşünüyorsan.",
              "Odunsu, iddialı ama boğucu olmayan kokuları seviyorsan."],
        love_end="Atlas sana göre.",
        love_img=(SKETCH, True),
        pyramid=[("Üst notalar", ["Hibiscus", "Apricot", "Coconut"]),
                 ("Kalp notaları", ["Lily of the Valley", "Cocoa Absolute"]),
                 ("Dip notaları", ["Iris", "Sandalwood", "Cedarwood", "Vanilla"])],
        tr=[("Satın Al", "https://iyzi.link/AKkeWw"), ("Shopier ile Satın Al", "https://www.shopier.com/parfumhazarcanal/47835192")],
        etsy="https://www.etsy.com/listing/4545928847/atlas-extrait-de-parfum",
    ),
    dict(
        slug="devil", name="Devil", kind="Extrait de Parfum", gender="Unisex",
        tagline="Şeytani içgüdülerinizi ortaya çıkarın.", chips=["İddialı", "Yoğun", "Baştan Çıkarıcı"],
        character="Sıcak • Meyveli • Vanilya • Yoğun",
        video="584124_6efa45b7936e45d29223df2e728ca78f", portrait=True,
        bottle="584124_94d42ff273a840619b9cb458160116e7~mv2.jpeg",
        card_notes=["Cherry", "Litchi", "White Chocolate", "Passion Flower", "Vanilla"],
        gallery=[("584124_5e094f2d4d1d4b6b8590f4dafebfd3be~mv2.png", "g-6"), ("584124_d23c884e2d85441d9eb22edcfd2fae03~mv2.png", "g-6")],
        love_img=("584124_94d42ff273a840619b9cb458160116e7~mv2.jpeg", False),
        pyramid=[("Notaları", ["Vişne", "Litchi", "Pasiflora", "Vanilya"])],
        tr=[("Satın Al", "https://iyzi.link/AKkfbQ"), ("Shopier ile Satın Al", "https://www.shopier.com/parfumhazarcanal/47835281")],
        etsy="https://www.etsy.com/listing/4521422161/devil-extrait-de-parfum",
        sister="devil-edp",
    ),
    dict(
        slug="barbaros", name="Barbaros", kind="Extrait de Parfum", gender="Unisex",
        tagline="Denizlerin hakimi", chips=["Aromatik Marine", "Güçlü", "Karizmatik"],
        video="584124_af0c4b3c6ab749e79e698fbb8844c2d1",
        bottle="584124_ca554a37e23640d8a3d6d1849b6815e6~mv2.jpeg",
        card_notes=["Pineapple", "Seaweed", "Ambergris", "Vanilla"],
        story=["Tuzlu rüzgarlar, savaşçı bir zarafet. Barbaros, denizin derinliğinden gelen karizmatik bir imza."],
        love_title="Bunu seversin eğer",
        love=["Deniz esintili kokular seviyorsan.",
              "Maskülen karakterli ve vanilyalı parfümler hoşuna gidiyorsa.",
              "Fresh + odunsu dengesi arıyorsan.",
              "Karizmatik imza kokusu istiyorsan."],
        love_img=("584124_ca554a37e23640d8a3d6d1849b6815e6~mv2.jpeg", False),
        gallery=[("584124_c8e6abd3b64a45d989984574ac77efef~mv2.jpg", "g-5"), ("quote", "g-7")],
        pyramid=[("Notaları", ["Ananas", "Deniz Yosunu", "Vanilya", "Ambergris"])],
        tr=[("Satın Al", "https://iyzi.link/AKkfaA"), ("Shopier ile Satın Al", "https://www.shopier.com/parfumhazarcanal/47835262")],
        etsy="https://www.etsy.com/listing/4382986168/barbaros-extrait-de-parfum",
        sister="barbaros-edp",
    ),
    dict(
        slug="sahmaran", name="Şahmaran", kind="Extrait de Parfum", gender="Unisex",
        tagline="Zehirli bir çekicilik, efsanevi bir gizem", chips=["Floral Amber", "Gizemli", "Sensual"],
        video="584124_f9e4eec8e0344e80aa53e43267249f10",
        bottle="584124_9ef16b85bf184800b7b3f5e228a0f976~mv2.jpg",
        card_notes=["Frangipani", "Sandalwood", "Ambergris", "Vanilla Absolute"],
        story=["İhanet ve arzunun iç içe geçtiği karanlık bir floral amber. Baştan çıkarıcı, sıcak ve unutulmaz."],
        love_title="Bunu seversin eğer",
        love=["Sıcak amber ve vanilyalı parfümler seviyorsan.",
              "İmza kokusu arıyorsan.",
              "Gizemli ve dikkat çekici kokular hoşuna gidiyorsa.",
              "Niş parfüm karakterini seviyorsan."],
        love_img=("584124_9ef16b85bf184800b7b3f5e228a0f976~mv2.jpg", False),
        gallery=[("quote", "g-5"), ("584124_b6287ad7c5fc4ff9a0f2bcc1fe37497e~mv2.jpg", "g-7")],
        pyramid=[("Notaları", ["Frangipani Çiçeği", "Vanilya", "Ambergris", "Sandal Ağacı"])],
        tr=[("Satın Al", "https://www.shopier.com/hcperfumes/40982052")],
        etsy="https://www.etsy.com/listing/4545948890/ahmaran-extrait-de-parfum",
        sister="sahmaran-edp",
    ),
    dict(
        slug="arora", name="Arora", kind="Eau de Parfum",
        tagline="Doğanın uyanışını teninizde hissettirecek benzersiz bir esans", chips=[],
        video="584124_72f9a994597048f589043799ba6cf9d2",
        image="584124_828f6621be0a4d0baadb3b9c59bea8b2~mv2.jpg",
        card_notes=["Blueberry", "Musc", "Vanilla", "Patchouli"],
        badges=["Fragrantica Awards — 68th Best Bottle Design"],
        story=["Kuzey ışıklarının gökyüzünde sergilediği o büyülü dans şimdi teninde parlıyor. ARORA, doğanın en görkemli gösterisinden ilham alarak tasarlandı."],
        story_big="Işığın tenle buluştuğu an…",
        pyramid=[("Notaları", ["Patchouli", "Blueberry", "Vanilla"])],
        tr=[("Satın Al", "https://iyzi.link/AKkfbg"), ("Shopier ile Satın Al", "https://www.shopier.com/parfumhazarcanal/47835208")],
        etsy="https://www.etsy.com/listing/4545935651/arora-eau-de-parfum",
    ),
    dict(
        slug="devil-edp", name="Devil", kind="Eau de Parfum",
        tagline="Şeytani içgüdülerinizi ortaya çıkarın.", chips=[],
        image="584124_8fdc6a94281242ce939edc150d1ec214~mv2.png",
        card_notes=["Cherry", "Pink Pepper", "Passion Flower", "Vanilla"],
        pyramid=[("Notaları", ["Vişne", "Pasiflora", "Vanilya"])],
        tr=[("Satın Al", "https://www.shopier.com/37210655")], sister="devil",
    ),
    dict(
        slug="barbaros-edp", name="Barbaros", kind="Eau de Parfum",
        tagline="Denizlerin hakimi", chips=[],
        image="584124_d8a3ea6910854837a7f56cd2b8518904~mv2.png",
        card_notes=["Pineapple", "Seaweed", "Ambergris", "Vanilla"],
        gallery=[("584124_c8e6abd3b64a45d989984574ac77efef~mv2.jpg", "g-5"), ("quote", "g-7")],
        pyramid=[("Notaları", ["Ananas", "Deniz Yosunu", "Vanilya", "Ambergris"])],
        tr=[("Satın Al", "https://www.shopier.com/37210668")], sister="barbaros",
    ),
    dict(
        slug="sahmaran-edp", name="Şahmaran", kind="Eau de Parfum",
        tagline="Zehirli bir çekicilik, efsanevi bir gizem", chips=[],
        image="584124_5c3ff7c2bf894b9f901fb016bdb5ebb4~mv2.png",
        card_notes=["Frangipani", "Sandalwood", "Ambergris", "Vanilla"],
        gallery=[("quote", "g-5"), ("584124_b6287ad7c5fc4ff9a0f2bcc1fe37497e~mv2.jpg", "g-7")],
        pyramid=[("Notaları", ["Frangipani Çiçeği", "Vanilya", "Ambergris"])],
        tr=[("Satın Al", "https://www.shopier.com/37210691")], sister="sahmaran",
    ),
]
BY = {p["slug"]: p for p in P}
EXTRAIT = [p for p in P if p["kind"].startswith("Extrait")]
EDP = [p for p in P if p["kind"].startswith("Eau")]


def ext(href, label, cls="btn"):
    return f'<a class="{cls}" href="{e(href)}" target="_blank" rel="noopener">{brandfix(e(label))}<span class="sr"> (yeni sekmede açılır)</span></a>'


def buy(p, first_solid=True, only_first=False):
    """Mağazaya göre satın alma düğmeleri. Etsy bağlantısı olanlarda TR / International ayrışır."""
    links = p["tr"][:1] if only_first else p["tr"]
    tr = "".join(ext(u, l, "btn btn--solid" if (k == 0 and first_solid) else "btn") for k, (l, u) in enumerate(links))
    if p.get("etsy"):
        return (f'<span data-store="tr">{tr}</span>'
                f'<span data-store="int">{ext(p["etsy"], "Get it on Etsy", "btn btn--solid" if first_solid else "btn")}</span>')
    return tr


def notes_inline(ns):
    return '<p class="notes-inline">' + " ".join(f"<span>{tx(n)}</span>" for n in ns) + "</p>"


def header(cur):
    def a(href, label):
        c = ' aria-current="page"' if href == cur else ""
        return f'<a href="{href}"{c}>{label}</a>'

    def col(title, items):
        lis = "".join(
            f'<li data-p="{p["slug"]}"><a href="{p["slug"]}.html">{tx(p["name"])}<small>{tx(p["kind"])}</small></a></li>' for p in items)
        return f'<div><h3 class="label">{tx(title)}</h3><ul>{lis}</ul></div>'

    seg = ('<div class="seg" role="group" aria-label="Mağaza seçimi">'
           '<button type="button" data-set-store="tr" aria-pressed="true" title="Türkiye mağazası">TR</button>'
           '<button type="button" data-set-store="int" aria-pressed="false" title="International store" lang="en">INT</button></div>')
    sound = ('<button type="button" class="sound" aria-pressed="false" title="Şahmaran — Hazar Canal">'
             '<i aria-hidden="true"><span></span><span></span><span></span></i>Ses</button>')
    return f'''<a class="skip" href="#icerik">İçeriğe geç</a>
<header class="top">
  <div class="wrap top__in">
    <a class="brand" href="index.html" aria-label="Hazar Canal — ana sayfa">Hazar Canal<small lang="en">Perfumes</small></a>
    <nav class="nav" aria-label="Ana menü">
      <button type="button" class="nav__btn" aria-expanded="false" aria-controls="mega">Koleksiyon</button>
      {a("test.html", "Kişilik Testi")}
      <a href="index.html#deneme-seti">Deneme Seti</a>
      <a href="index.html#atolye">Atölye</a>
    </nav>
    <div class="tools">
      {seg}{sound}
      <button type="button" class="burger" aria-expanded="false" aria-controls="mega" aria-label="Menü"><span></span><span></span></button>
    </div>
  </div>
</header>
<div class="mega" id="mega" hidden>
  <div class="wrap mega__in">
    {col("Extrait de Parfum", EXTRAIT)}
    {col("Eau de Parfum", EDP)}
    <div>
      <h3 class="label">Keşfet</h3>
      <ul>
        <li><a href="test.html">Kişilik Testi<small>12 soru</small></a></li>
        <li><a href="index.html#deneme-seti">Deneme Seti<small>5 × 5 ml</small></a></li>
        <li><a href="index.html#atolye">Atölye<small>El yapımı</small></a></li>
      </ul>
      <div class="mega__tools">{seg}{sound}</div>
    </div>
  </div>
</div>'''


def footer():
    def col(title, items):
        return f'<div><h3 class="label">{tx(title)}</h3><ul>' + "".join(f'<li><a href="{h}"{x}>{e(l)}</a></li>' for l, h, x in items) + "</ul></div>"
    blank = ' target="_blank" rel="noopener"'
    return f'''<footer class="foot">
  <div class="wrap">
    <div class="foot__grid">
      <div><a class="brand" href="index.html">Hazar Canal<small lang="en">Perfumes</small></a>
        <p class="mute" style="margin-top:1.25rem;max-width:26ch">Parfüm Dünyasına Adım Atın</p></div>
      {col("Extrait de Parfum", [(p["name"], p["slug"] + ".html", "") for p in EXTRAIT])}
      {col("Eau de Parfum", [(p["name"], p["slug"] + ".html", "") for p in EDP])}
      {col("Keşfet", [("Kişilik Testi", "test.html", ""), ("Deneme Seti", "index.html#deneme-seti", ""), ("Atölye", "index.html#atolye", "")])}
      {col("İletişim", [(EMAIL, "mailto:" + EMAIL, ""), ("Instagram", INSTAGRAM, blank), ("TikTok", TIKTOK, blank)])}
    </div>
    <div class="foot__base label"><span>© Hazar Canal</span><span>Niş kalite esans · El yapımı tasarım</span></div>
  </div>
</footer>
<audio id="hc-audio" src="{AUDIO}" preload="none" loop></audio>
<script src="assets/app.js" defer></script>'''


def page(fname, title, desc, body, accent="", cur="", ogimg=None):
    doc = f'''<!doctype html>
<html lang="tr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{e(title)}</title>
<meta name="description" content="{e(desc)}">
<meta name="theme-color" content="#0a0908">
{'<meta name="robots" content="noindex">' if NOINDEX else ''}
<meta property="og:title" content="{e(title)}">
<meta property="og:description" content="{e(desc)}">
<meta property="og:type" content="website">
{f'<meta property="og:image" content="{ogimg}">' if ogimg else ''}
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 64 64'%3E%3Crect width='64' height='64' fill='%230a0908'/%3E%3Cpath d='M18 14v36M46 14v36M18 32h28M32 8v48' stroke='%23c9c2b2' stroke-width='4' fill='none'/%3E%3C/svg%3E">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="preconnect" href="https://static.wixstatic.com">
<link href="https://fonts.googleapis.com/css2?family=Bodoni+Moda:ital,opsz,wght@0,6..96,400..600;1,6..96,400..500&family=EB+Garamond:ital,wght@0,400;0,500;1,400&family=Jost:wght@400;500&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/style.css">
<style>.sr{{position:absolute;width:1px;height:1px;overflow:hidden;clip-path:inset(50%);white-space:nowrap}}</style>
<script>try{{if(localStorage.getItem('hc-store')==='int')document.documentElement.dataset.store='int'}}catch(e){{}}</script>
</head>
<body{f' data-p="{accent}"' if accent else ''}>
{header(cur)}
<main id="icerik">
{body}
</main>
{footer()}
</body>
</html>
'''
    with open(os.path.join(OUT, fname), "w", encoding="utf-8", newline="\n") as f:
        f.write(localize(doc))


def invite():
    return '''<section class="invite" aria-labelledby="inv-h">
  <div class="wrap invite__in rv">
    <div><h2 class="display h-md" id="inv-h">Hangi parfüm senin için?</h2>
      <p class="mute">Kişilik testini cevaplayın, size uygun parfümü bulalım.</p></div>
    <a class="btn" href="test.html">Kişilik Testi</a>
  </div>
</section>'''


# ------------------------------------------------------------------ ANA SAYFA
def home():
    atlas = BY["atlas"]
    relics = ""
    for k, p in enumerate([BY["devil"], BY["barbaros"], BY["sahmaran"]]):
        relics += f'''<article class="relic rv" data-p="{p["slug"]}" style="--d:{k * .12}s">
      <div class="relic__img"><img src="{im(p["bottle"], 900)}" alt="{e(p["name"])} Extrait de Parfum şişesi" loading="lazy"></div>
      <div class="relic__body">
        <h3 class="display h-md"><a class="cover" href="{p["slug"]}.html">{tx(p["name"])}</a></h3>
        {notes_inline(p["card_notes"])}
        <div class="btn-row">{buy(p, first_solid=True, only_first=True)}<a class="btn" href="{p["slug"]}.html" tabindex="-1" aria-hidden="true">İncele</a></div>
      </div>
    </article>'''

    edps = ""
    for k, p in enumerate(EDP):
        badge = "".join(f'<span class="badge">{tx(b)}</span>' for b in p.get("badges", []))
        edps += f'''<article class="edp rv" data-p="{p["slug"]}" style="--d:{(k % 2) * .12}s">
      <img src="{im(p["image"], 1400)}" alt="{e(p["name"])} Eau de Parfum" loading="lazy">
      <div class="edp__body">
        {f'<div>{badge}</div>' if badge else ''}
        <h3 class="display h-lg"><a class="cover" href="{p["slug"]}.html">{tx(p["name"])}</a></h3>
        <div class="edp__foot">{notes_inline(p["card_notes"])}<div class="btn-row">{buy(p, first_solid=False, only_first=True)}</div></div>
      </div>
    </article>'''

    def film(p, vid_id, tag, cls, label):
        return f'''<article class="film {cls} rv" data-p="{p["slug"]}">
        <video muted loop playsinline preload="none" poster="{poster(vid_id)}" data-src="{vid(vid_id)}" aria-label="{e(p["name"])} filmi"></video>
        <div class="film__cap">
          <p class="label"><b>{label}</b></p>
          <h3 class="display h-lg">{tx(p["name"])}</h3>
          <p class="italic">{e(tag)}</p>
          <a class="tlink" href="{p["slug"]}.html">Kokuyu keşfet</a>
        </div>
      </article>'''

    body = f'''<section class="hero" data-p="atlas" aria-labelledby="hero-h">
  <div class="hero__media"><video muted loop playsinline autoplay poster="{poster(atlas["video"])}" data-src="{vid(atlas["video"])}" aria-hidden="true"></video></div>
  <div class="wrap hero__in">
    <p class="label"><b lang="en">Extrait de Parfum</b> &nbsp;·&nbsp; <span lang="en">Unisex</span></p>
    <h1 class="display h-xl hero__name" id="hero-h">Atlas</h1>
    <div class="hero__row">
      <p class="lede italic">Sessiz lüksün zirvesi.</p>
      <div class="btn-row"><a class="btn" href="atlas.html">İncele</a>{buy(atlas)}</div>
    </div>
  </div>
</section>

{invite()}

<section class="sec sec--bone on-bone" id="extrait" aria-labelledby="ex-h">
  <div class="wrap">
    <div class="sec__head rv">
      <div><p class="label">Koleksiyon · I</p><h2 class="display h-lg" id="ex-h" lang="en">Extrait de Parfum</h2></div>
      <p class="label" lang="en">Unisex</p>
    </div>
    <div class="relics">{relics}</div>
  </div>
</section>

<section class="sec" id="edp" aria-labelledby="edp-h">
  <div class="wrap">
    <div class="sec__head rv">
      <div><p class="label">Koleksiyon · II</p><h2 class="display h-lg" id="edp-h" lang="en">Eau de Parfum</h2></div>
    </div>
    <div class="edps">{edps}</div>
  </div>
</section>

<section class="sec" style="padding-top:0" aria-label="Filmler">
  <div class="wrap films">
    {film(BY["sahmaran"], "584124_cb121a7fabad49c7ac3f78723b2dfa23", "Zehirli bir çekicilik, efsanevi bir gizem", "film--wide", "Film · I")}
    <div class="films__row">
      {film(BY["barbaros"], "584124_af0c4b3c6ab749e79e698fbb8844c2d1", "Denizlerin hakimi Barbaros", "film--land", "Film · II")}
      {film(BY["devil"], "584124_b8ebb1c3a80e4214bb80f9cceade2a4e", "Şeytani içgüdülerinizi ortaya çıkarın.", "film--port", "Film · III")}
    </div>
  </div>
</section>

<section class="sec sec--bone on-bone" id="deneme-seti" aria-labelledby="ds-h">
  <div class="wrap split">
    <figure class="split__img rv"><img src="{im(LINEUP, 1400)}" alt="Beş Hazar Canal şişesi yan yana: Devil, Şahmaran, Atlas, Barbaros ve Arora" loading="lazy"></figure>
    <div class="split__body rv" style="--d:.12s">
      <p class="label">Tester</p>
      <h2 class="display h-lg" id="ds-h">Deneme Seti</h2>
      <p class="lede">Bu tester, deneme seti, imza kokunu bulman için tasarlandı. Koleksiyonun her karakterini deneyimle.</p>
      <ul class="ml-list" aria-label="Set içeriği">
        <li><a href="devil.html">Devil 5ml</a></li><li><a href="sahmaran.html">Şahmaran 5ml</a></li><li><a href="barbaros.html">Barbaros 5ml</a></li><li><a href="arora.html">Arora 5ml</a></li><li><a href="atlas.html">Atlas 5ml</a></li>
      </ul>
      {ext(TESTER_URL, "Satın Al", "btn btn--solid")}
    </div>
  </div>
</section>

<section class="sec" id="atolye" aria-labelledby="at-h">
  <div class="wrap">
    <div class="sec__head rv"><div><p class="label">Atölye</p><h2 class="display h-lg" id="at-h" lang="en">Ultraniche<br>Design</h2></div></div>
    <div class="craft">
      <figure class="craft__img rv"><img src="{im(SKETCH, 1200)}" alt="Şişe ve kapak tasarımlarının kurşun kalem eskizleriyle dolu bir defter" loading="lazy"><figcaption class="label">Eskiz defterinden</figcaption></figure>
      <div class="craft__items">
        {"".join(f'<div class="craft__item rv"><h3 class="display h-md">{e(t)}</h3><p>{e(d)}</p></div>' for t, d in CRAFT)}
        <ul class="claims rv">
          <li>Niş Kalite Esans<br><span class="mute" lang="en">Niche Quality</span></li>
          <li>Uzun Süre Kalıcılık<br><span class="mute" lang="en">Long-Lasting</span></li>
          <li lang="en">Ultraniche Design</li>
          <li lang="en">Handmade Design</li>
        </ul>
        <div class="seals rv"><span class="seal" lang="en">Cruelty Free</span><span class="seal">Vegan</span></div>
      </div>
    </div>
  </div>
</section>

<hr class="rule">
<section class="outro" aria-labelledby="out-h">
  <div class="wrap rv">
    <img class="mark" src="{im(LOGO, 500)}" alt="" loading="lazy">
    <h2 class="display h-lg" id="out-h">Hazar Canal</h2>
    <p class="italic">Parfüm Dünyasına Adım Atın</p>
    <p class="label" style="margin-top:3.5rem">Bizi takip edin</p>
    <div class="follow" style="margin-top:1rem">{ext(INSTAGRAM, "Instagram", "tlink")}{ext(TIKTOK, "TikTok", "tlink")}</div>
  </div>
</section>'''
    page("index.html", "Hazar Canal Parfum — Niş, el yapımı parfümler",
         "Hazar Canal: el yapımı şişeler, niş kalite esanslar. Atlas, Devil, Barbaros, Şahmaran ve Arora.",
         body, cur="index.html", ogimg=poster(atlas["video"]))


# ------------------------------------------------------------------ ÜRÜN SAYFASI
def product(p):
    i = P.index(p)
    prev, nxt = P[i - 1], P[(i + 1) % len(P)]
    full = f'{p["name"]} {p["kind"]}'
    if p.get("video"):
        media = f'<video muted loop playsinline autoplay poster="{poster(p["video"])}" data-src="{vid(p["video"])}" aria-hidden="true"></video>'
        og = poster(p["video"])
    else:
        media = f'<img src="{im(p["image"], 2000)}" alt="{e(full)}">'
        og = im(p["image"], 1200)
    chips = ('<ul class="chips">' + "".join(f"<li>{tx(c)}</li>" for c in p["chips"]) + "</ul>") if p["chips"] else ""
    badges = "".join(f'<span class="badge">{tx(b)}</span> ' for b in p.get("badges", []))
    split = " phero--split" if p.get("portrait") else ""
    hero = f'''<section class="phero{split}" aria-labelledby="p-h">
  <div class="phero__media">{media}</div>
  <div class="{'' if split else 'wrap '}phero__in">
    <p class="label"><b>{tx(p["kind"])}</b>{' &nbsp;·&nbsp; ' + e(p["gender"]) if p.get("gender") else ''}</p>
    <h1 class="display h-xl" id="p-h" style="margin-left:-.04em">{tx(p["name"])}</h1>
    <div class="phero__grid">
      <div style="display:grid;gap:1rem">
        <p class="lede italic">{e(p["tagline"])}</p>
        {chips}
        {f'<div>{badges}</div>' if badges else ''}
      </div>
      <div class="phero__buy">
        <div class="btn-row">{buy(p)}</div>
        <ul class="ticks">{"".join(f"<li>{e(t)}</li>" for t in TICKS)}</ul>
      </div>
    </div>
  </div>
</section>'''

    facts = [("Tür", e(p["kind"]))]
    if p.get("gender"): facts.append(("Cinsiyet", e(p["gender"])))
    if p.get("character"): facts.append(("Koku Karakteri", e(p["character"])))
    if p.get("sister"):
        s = BY[p["sister"]]
        facts.append(("Diğer yorumu", f'<a class="tlink" href="{s["slug"]}.html" style="font-size:.74rem">{tx(s["name"])} {tx(s["kind"])}</a>'))
    facts_html = '<dl class="facts rv">' + "".join(f"<div><dt>{k}</dt><dd>{v}</dd></div>" for k, v in facts) + "</dl>"
    story = p.get("story") or [p["tagline"]]
    story_html = "".join(f"<p>{e(s)}</p>" for s in story)
    if p.get("story_big"): story_html += f'<p class="big">{e(p["story_big"])}</p>'
    if p["slug"] == "atlas": story_html += '<p class="label" style="margin-top:.5rem">Odunsu. Derin. Tanrısal. — Sessiz lüksün zirvesi.</p>'
    body = hero + f'''
<section class="sec" aria-label="Hikâye">
  <div class="wrap story">
    {facts_html}
    <div class="story__text rv" style="--d:.1s">{story_html}</div>
  </div>
</section>'''

    if p.get("love"):
        img_id, cover = p["love_img"]
        alt = "Tasarım eskizleri" if cover else f'{p["name"]} şişesi'
        body += f'''
<section class="sec sec--bone on-bone" aria-labelledby="love-h">
  <div class="wrap love">
    <figure class="love__img{' love__img--cover' if cover else ''} rv"><img src="{im(img_id, 1100)}" alt="{e(alt)}" loading="lazy"></figure>
    <div class="rv" style="--d:.12s">
      <p class="label">Sana göre mi?</p>
      <h2 class="display h-md" id="love-h" style="margin-top:.75rem">{e(p["love_title"])}</h2>
      <ol>{"".join(f"<li><span>{e(x)}</span></li>" for x in p["love"])}</ol>
      {f'<p class="display h-sm italic love__end">{e(p["love_end"])}</p>' if p.get("love_end") else ''}
      <div class="btn-row" style="margin-top:2rem">{buy(p, only_first=True)}</div>
    </div>
  </div>
</section>'''
    elif p.get("love_img"):
        img_id, _ = p["love_img"]
        body += f'''
<section class="sec sec--bone on-bone" aria-label="Şişe">
  <div class="wrap love">
    <figure class="love__img rv"><img src="{im(img_id, 1100)}" alt="{e(p["name"])} şişesi" loading="lazy"></figure>
    <div class="rv" style="--d:.12s">
      <p class="label">Koku Karakteri</p>
      <h2 class="display h-lg" style="margin-top:.75rem">{"<br>".join(e(x.strip()) for x in p["character"].split("•"))}</h2>
      <div class="btn-row" style="margin-top:2rem">{buy(p, only_first=True)}</div>
    </div>
  </div>
</section>'''

    rows = "".join(
        f'<div class="pyramid__row rv{" pyramid__row--solo" if len(p["pyramid"]) == 1 else ""}">{"" if len(p["pyramid"]) == 1 else f"""<p class="label">{e(t)}</p>"""}<ul>{"".join(f"<li>{tx(n)}</li>" for n in ns)}</ul></div>'
        for t, ns in p["pyramid"])
    body += f'''
<section class="sec" aria-labelledby="n-h">
  <div class="wrap">
    <div class="sec__head rv"><div><p class="label">{tx(p["name"])}</p><h2 class="display h-lg" id="n-h">Notaları</h2></div></div>
    <div class="pyramid">{rows}</div>
  </div>
</section>'''

    if p.get("gallery"):
        figs = "".join(
            (f'<figure class="{c} g-quote rv"><p class="label">{tx(p["name"])}</p><blockquote>{e(p["tagline"])}</blockquote></figure>' if g == "quote" else
             f'<figure class="{c} rv"><img src="{im(g, 1800)}" alt="{e(p["name"])} — görsel dünya" loading="lazy"></figure>')
            for g, c in p["gallery"])
        body += f'<section class="sec" style="padding-top:0" aria-label="Görseller"><div class="wrap gallery">{figs}</div></section>'

    body += f'''
<section class="sec" style="padding-top:0" aria-label="Atölye">
  <div class="wrap"><div class="craft__items" style="grid-template-columns:repeat(auto-fit,minmax(min(100%,22rem),1fr))">
    {"".join(f'<div class="craft__item rv"><h2 class="display h-sm">{e(t)}</h2><p>{e(d)}</p></div>' for t, d in CRAFT)}
  </div></div>
</section>
{invite()}
<nav class="sister" aria-label="Diğer parfümler">
  <a href="{prev["slug"]}.html" data-p="{prev["slug"]}"><span class="label">← Önceki</span><span class="display h-md">{tx(prev["name"])}</span><span class="label">{tx(prev["kind"])}</span></a>
  <a href="{nxt["slug"]}.html" data-p="{nxt["slug"]}"><span class="label">Sonraki →</span><span class="display h-md">{tx(nxt["name"])}</span><span class="label">{tx(nxt["kind"])}</span></a>
</nav>
<div class="buybar"><strong>{tx(p["name"])}</strong>{buy(p, only_first=True)}</div>'''
    desc = f'{full} — {p["tagline"]} Notalar: {", ".join(n for _, ns in p["pyramid"] for n in ns)}.'
    page(p["slug"] + ".html", f"{full} | Hazar Canal", desc, body, accent=p["slug"], ogimg=og)


# ------------------------------------------------------------------ KİŞİLİK TESTİ
QUIZ = [
    ("Parfümü en çok ne zaman kullanacaksın?", ["Gündüz, günlük kullanım", "Gece dışarı / bar / club", "Özel günler"]),
    ("Kokun nasıl bir hava versin?", ["Ferah & temiz", "Seksi & iddialı", "Gizemli & mistik", "Güçlü & karizmatik", "Modern & yaratıcı"]),
    ("Koku yoğunluğun nasıl olsun?", ["Hafif", "Dengeli", "Güçlü"]),
    ("Hangi koku ailesine çekiliyorsun?", ["Tatlı", "Ferah – temiz", "Odunsu – baharatlı", "Çiçeksi", "Modern – hafif tatlı"]),
    ("Stilini en çok hangisi anlatıyor?", ["Streetwear / rahat ama havalı", "Klasik & şık", "Bohem / özgür ruh", "Minimal & clean"]),
    ("Sosyal ortamlarda hangi karakterdesin?", ["Eğlenceli & enerjik", "Sakin ama dikkat çekici", "Derin & anlamlı", "Sıcak & samimi"]),
    ("En çok hangi iltifatı duymak istersin?", ["“Çok temiz kokuyorsun.”", "“Aşırı seksi kokuyorsun.”", "“Kokun çok farklı, tam senin gibi.”", "“Çok şık kokuyor.”"]),
    ("Hangi estetik vibe seni anlatıyor?", ["Soft girl/boy", "Night luxe", "Scandi minimal", "Goddess / mystical", "Y2K modern"]),
    ("Günlük enerjin hangisi?", ["Chill", "Electric", "Confident", "Sweet & soft", "Mysterious"]),
    ("Signature scent’in nasıl olmalı?", ["Modern ama tanıdık", "Tamamen özgün", "Temiz & günlük", "Ağır & etkileyici", "Hafif tatlı & enerjik"]),
    ("Hayat mottosu?", ["Less is more", "If not now, when?", "Main character energy", "Go with the flow", "Nothing is random"]),
    ("Bu yılki enerjin ne?", ["Glow up ✨", "Kendim olma zamanı", "Quiet luxury", "Macera & spontanlık", "Enerji yükseltme"]),
]
WEIGHTS = {
    "q1a1": {"Barbaros": 2, "Arora": 1}, "q1a2": {"Devil": 2, "Atlas": 1}, "q1a3": {"Atlas": 2, "Sahmaran": 1},
    "q2a1": {"Barbaros": 2}, "q2a2": {"Devil": 3, "Atlas": 1}, "q2a3": {"Sahmaran": 3}, "q2a4": {"Atlas": 3}, "q2a5": {"Arora": 3, "Devil": 1},
    "q3a1": {"Barbaros": 2, "Arora": 1}, "q3a2": {"Sahmaran": 1, "Arora": 1, "Barbaros": 1}, "q3a3": {"Devil": 2, "Atlas": 2},
    "q4a1": {"Devil": 3}, "q4a2": {"Barbaros": 3}, "q4a3": {"Atlas": 3}, "q4a4": {"Sahmaran": 3}, "q4a5": {"Arora": 3},
    "q5a1": {"Arora": 3, "Devil": 1}, "q5a2": {"Atlas": 3, "Sahmaran": 1}, "q5a3": {"Sahmaran": 3}, "q5a4": {"Barbaros": 2, "Arora": 1},
    "q6a1": {"Devil": 2, "Arora": 1}, "q6a2": {"Atlas": 2}, "q6a3": {"Sahmaran": 2}, "q6a4": {"Barbaros": 2},
    "q7a1": {"Barbaros": 2}, "q7a2": {"Devil": 3}, "q7a3": {"Arora": 3}, "q7a4": {"Atlas": 3},
    "q8a1": {"Barbaros": 2, "Arora": 1}, "q8a2": {"Devil": 3, "Atlas": 1}, "q8a3": {"Barbaros": 2}, "q8a4": {"Sahmaran": 3}, "q8a5": {"Arora": 3},
    "q9a1": {"Barbaros": 2}, "q9a2": {"Devil": 2}, "q9a3": {"Atlas": 2}, "q9a4": {"Arora": 2}, "q9a5": {"Sahmaran": 2},
    "q10a1": {"Barbaros": 2}, "q10a2": {"Arora": 3}, "q10a3": {"Barbaros": 2}, "q10a4": {"Atlas": 3}, "q10a5": {"Devil": 2, "Arora": 1},
    "q11a1": {"Barbaros": 2}, "q11a2": {"Arora": 2}, "q11a3": {"Devil": 2}, "q11a4": {"Sahmaran": 2}, "q11a5": {"Atlas": 2},
    "q12a1": {"Arora": 3}, "q12a2": {"Sahmaran": 2}, "q12a3": {"Atlas": 3}, "q12a4": {"Devil": 2}, "q12a5": {"Barbaros": 2},
}
RESULTS = {
    "Devil": dict(slug="devil", name="DEVIL", url="https://iyzi.link/AKkfbQ",
                  desc="Gece enerjisi, seksi aura, tatlı-yoğun bir imza. Vişne, beyaz çikolata ve passionflower ile akılda kalıcı bir çekim gücü."),
    "Barbaros": dict(slug="barbaros", name="BARBAROS", url="https://iyzi.link/AKkfaA",
                     desc="Ferah, deniz esintili, temiz ve modern. Ananas, deniz tuzu ve ambergris ile gündüz ve yaz imzası."),
    "Sahmaran": dict(slug="sahmaran", name="ŞAHMARAN", url="https://www.shopier.com/hcperfumes/40982052",
                     desc="Mistik, egzotik, çiçeksi ama derin… Muz, frangipani, ambergris ve sandal ağacıyla gizemli bir aura."),
    "Arora": dict(slug="arora", name="ARORA", url="https://iyzi.link/AKkfbg",
                  desc="Işıltılı, modern, hafif tatlı-fresh. Y2K + glow-up vibe’ının parfüm hali."),
    "Atlas": dict(slug="atlas", name="ATLAS", url="https://iyzi.link/AKkeWw",
                  desc="Güçlü, odunsu, karizmatik. Sessiz lüksün kokusu."),
}


def quiz():
    qs = ""
    for n, (q, opts) in enumerate(QUIZ, 1):
        o = "".join(
            f'<label class="opt"><input type="radio" name="q{n}" value="q{n}a{k}"><span class="k">{chr(64 + k)}</span><span>{e(t)}</span><span class="a" aria-hidden="true">→</span></label>'
            for k, t in enumerate(opts, 1))
        qs += f'''<div class="q" hidden>
        <p class="label" aria-hidden="true"><b>{n:02d}</b> / {len(QUIZ)}</p>
        <fieldset>
        <legend><span class="sr">Soru {n} / {len(QUIZ)}: </span>{e(q)}</legend>
        <div class="opts">{o}</div></fieldset></div>'''
    data = json.dumps({"weights": WEIGHTS, "perfumes": RESULTS}, ensure_ascii=False)
    body = f'''<section class="quiz" id="quiz" aria-labelledby="quiz-h">
  <div class="quiz__bar" aria-hidden="true"><i></i></div>
  <div class="quiz__stage"><div class="wrap"><div class="quiz__in">
    <div class="quiz__intro">
      <p class="label">12 soru · 2 dakika</p>
      <h1 class="display h-lg" id="quiz-h">Hazar Canal Parfüm Kişilik Testi</h1>
      <p class="lede">Soruları içinden geldiği gibi cevapla… Sana en uygun kokuyu bulalım.</p>
      <button type="button" class="btn btn--solid" id="q-start">Teste Başla</button>
    </div>
    {qs}
    <div class="quiz__nav" hidden>
      <button type="button" class="tlink tlink--back" id="q-back">Geri</button>
      <button type="button" class="btn btn--solid" id="q-next" disabled>Devam</button>
    </div>
    <div class="quiz__result" hidden aria-live="polite">
      <p class="label">Senin için en uygun parfüm</p>
      <h2 class="display h-xl" id="r-name" tabindex="-1" style="margin-left:-.04em"></h2>
      <p class="desc" id="r-desc"></p>
      <div class="btn-row">
        <a class="btn btn--solid" id="r-page" href="#">Parfümü İncele</a>
        <a class="btn" id="r-buy" href="#" target="_blank" rel="noopener">Satın Al</a>
        <button type="button" class="btn" id="r-again">Tekrar Dene</button>
      </div>
      <ul class="scores" id="r-scores" aria-label="Diğer kokularla uyumun"></ul>
    </div>
    <noscript><p>Test için tarayıcınızda JavaScript açık olmalı.</p></noscript>
  </div></div></div>
</section>
<script type="application/json" id="quiz-data">{data}</script>'''
    page("test.html", "Parfüm Kişilik Testi | Hazar Canal",
         "12 soruluk kişilik testini cevaplayın, size en uygun Hazar Canal parfümünü bulalım.", body, cur="test.html")


def main():
    os.makedirs(OUT, exist_ok=True)
    home()
    for p in P:
        product(p)
    quiz()
    print("Tamam:", ", ".join(sorted(f for f in os.listdir(OUT) if f.endswith(".html") and not f.startswith("_"))))


if __name__ == "__main__":
    main()
