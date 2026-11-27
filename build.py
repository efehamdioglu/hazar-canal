# -*- coding: utf-8 -*-
"""Hazar Canal: çok dilli statik site üretici.
Çalıştır:  python build.py   →  site/ (Türkçe) ve site/<dil>/ klasörlerine HTML yazar.
Metinler i18n/<dil>.json dosyalarındadır; kaynak i18n/tr.json (hazarcanal.com içeriği)."""
import json, os, html

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "site")
MEDIA = "https://static.wixstatic.com/media/"
VIDEO = "https://video.wixstatic.com/video/"
AUDIO = "https://music.wixstatic.com/mp3/584124_a6968e2524b84530b68977e4395fe0bd-320.mp3"
# Sitenin yayınlandığı adres (paylaşım önizlemesi ve dil bağlantıları için).
SITE_URL = "https://efehamdioglu.com/hazar-canal/"
# Önizleme sürümü arama motorlarında asıl siteyle yarışmasın. Asıl siteye dönüşünce False yapın.
NOINDEX = True
EMAIL = "hazarcanal@icloud.com"
INSTAGRAM = "https://www.instagram.com/hazarcanalperfumes/"
TIKTOK = "https://www.tiktok.com/@hazarcanalparfum"
TESTER_URL = "https://www.shopier.com/Hazarcanal/44750828"

# (dil kodu, klasör, dilin kendi adı, bayrak dosyası). Türkçe kökte durur ve Türkiye mağazasını
# (iyzico, Shopier) gösterir; diğer diller Etsy'ye yönlendirir.
LANGS = [
    ("tr", "", "Türkçe", "tr"),
    ("en", "en/", "English (UK)", "gb"),
    ("en", "en/", "English (US)", "us"),
    ("it", "it/", "Italiano", "it"),
    ("fr", "fr/", "Français", "fr"),
    ("es", "es/", "Español", "es"),
    ("de", "de/", "Deutsch", "de"),
    ("ar", "ar/", "العربية", "sa"),
    ("ja", "ja/", "日本語", "jp"),
]
RTL = {"ar"}
EXTRA_FONTS = {
    "ar": "&family=Amiri&family=IBM+Plex+Sans+Arabic:wght@400;500",
    "ja": "&family=Shippori+Mincho&family=Zen+Kaku+Gothic+New:wght@400;500",
}

e = html.escape


def load(code):
    with open(os.path.join(HERE, "i18n", code + ".json"), encoding="utf-8") as f:
        return json.load(f)


TR = load("tr")
LANG, DIR, PRE, T = "tr", "", "", TR  # derleme sırasında dile göre değişir


def t(key, **kw):
    v = T.get(key, TR[key])
    return v.format(**kw) if kw else v


def has(key):
    return key in TR


# fetch_media.py çalıştırıldıysa uzak Wix adresleri yerel dosyalarla değiştirilir.
_MAP_FILE = os.path.join(HERE, "media_map.json")


def localize(doc):
    if not os.path.exists(_MAP_FILE):
        return doc
    mp = json.load(open(_MAP_FILE, encoding="utf-8"))
    for u in sorted(mp, key=len, reverse=True):
        doc = doc.replace(u, PRE + mp[u])
    doc = doc.replace(f'property="og:image" content="{PRE}media/', f'property="og:image" content="{SITE_URL}media/')
    if "wixstatic.com/" not in doc.replace('href="https://static.wixstatic.com"', ""):
        doc = doc.replace('<link rel="preconnect" href="https://static.wixstatic.com">' + chr(10), "")
    return doc


def im(i, w=1200):
    ext_ = "png" if i.endswith("1ab5b23b7d5743d997bc1f10f3cb0c17~mv2.png") else "jpg"
    return f"{MEDIA}{i}/v1/fit/w_{w},h_{w},q_85/hc.{ext_}"


def vid(i):
    return f"{VIDEO}{i}/720p/mp4/file.mp4"


def poster(i):
    return f"{MEDIA}{i}f000.jpg"


LOGO = "584124_1ab5b23b7d5743d997bc1f10f3cb0c17~mv2.png"
SKETCH = "584124_7e40977f842d4157abb6a4359ce6632b~mv2.jpeg"
LINEUP = "584124_c4d28bc2867945f284ddc85d30bae62e~mv2.jpg"
X, E = "Extrait de Parfum", "Eau de Parfum"

# Parfümlerin yapısal verisi. Metinler i18n dosyalarında "p.<slug>.*" anahtarlarındadır.
P = [
    dict(slug="atlas", name="Atlas", kind=X, unisex=True,
         video="584124_b9ed81cf9ab044d896630c9f70f290ed", badges=["Alcohol Free"],
         love_img=(SKETCH, True),
         tr=["https://iyzi.link/AKkeWw", "https://www.shopier.com/parfumhazarcanal/47835192"],
         etsy="https://www.etsy.com/listing/4545928847/atlas-extrait-de-parfum"),
    dict(slug="devil", name="Devil", kind=X, unisex=True,
         video="584124_6efa45b7936e45d29223df2e728ca78f", portrait=True,
         love_img=("584124_94d42ff273a840619b9cb458160116e7~mv2.jpeg", False),
         gallery=[("584124_5e094f2d4d1d4b6b8590f4dafebfd3be~mv2.png", "g-6"), ("584124_d23c884e2d85441d9eb22edcfd2fae03~mv2.png", "g-6")],
         tr=["https://iyzi.link/AKkfbQ", "https://www.shopier.com/parfumhazarcanal/47835281"],
         etsy="https://www.etsy.com/listing/4521422161/devil-extrait-de-parfum", sister="devil-edp"),
    dict(slug="barbaros", name="Barbaros", kind=X, unisex=True,
         video="584124_af0c4b3c6ab749e79e698fbb8844c2d1",
         love_img=("584124_ca554a37e23640d8a3d6d1849b6815e6~mv2.jpeg", False),
         gallery=[("584124_c8e6abd3b64a45d989984574ac77efef~mv2.jpg", "g-5"), ("quote", "g-7")],
         tr=["https://iyzi.link/AKkfaA", "https://www.shopier.com/parfumhazarcanal/47835262"],
         etsy="https://www.etsy.com/listing/4382986168/barbaros-extrait-de-parfum", sister="barbaros-edp"),
    dict(slug="sahmaran", name="Şahmaran", kind=X, unisex=True,
         video="584124_f9e4eec8e0344e80aa53e43267249f10",
         love_img=("584124_9ef16b85bf184800b7b3f5e228a0f976~mv2.jpg", False),
         gallery=[("quote", "g-5"), ("584124_b6287ad7c5fc4ff9a0f2bcc1fe37497e~mv2.jpg", "g-7")],
         tr=["https://www.shopier.com/hcperfumes/40982052"],
         etsy="https://www.etsy.com/listing/4545948890/ahmaran-extrait-de-parfum", sister="sahmaran-edp"),
    dict(slug="arora", name="Arora", kind=E,
         video="584124_72f9a994597048f589043799ba6cf9d2",
         image="584124_828f6621be0a4d0baadb3b9c59bea8b2~mv2.jpg",
         badges=["Fragrantica Awards, 68th Best Bottle Design"],
         tr=["https://iyzi.link/AKkfbg", "https://www.shopier.com/parfumhazarcanal/47835208"],
         etsy="https://www.etsy.com/listing/4545935651/arora-eau-de-parfum"),
    dict(slug="devil-edp", name="Devil", kind=E, base="devil",
         image="584124_8fdc6a94281242ce939edc150d1ec214~mv2.png",
         tr=["https://www.shopier.com/37210655"], sister="devil"),
    dict(slug="barbaros-edp", name="Barbaros", kind=E, base="barbaros",
         image="584124_d8a3ea6910854837a7f56cd2b8518904~mv2.png",
         gallery=[("584124_c8e6abd3b64a45d989984574ac77efef~mv2.jpg", "g-5"), ("quote", "g-7")],
         tr=["https://www.shopier.com/37210668"], sister="barbaros"),
    dict(slug="sahmaran-edp", name="Şahmaran", kind=E, base="sahmaran",
         image="584124_5c3ff7c2bf894b9f901fb016bdb5ebb4~mv2.png",
         gallery=[("quote", "g-5"), ("584124_b6287ad7c5fc4ff9a0f2bcc1fe37497e~mv2.jpg", "g-7")],
         tr=["https://www.shopier.com/37210691"], sister="sahmaran"),
]
BY = {p["slug"]: p for p in P}
EXTRAIT = [p for p in P if p["kind"] == X]
EDP = [p for p in P if p["kind"] == E]


def tagline(p):
    return t(f'p.{p.get("base", p["slug"])}.tagline')


def kind(p_or_str):
    k = p_or_str if isinstance(p_or_str, str) else p_or_str["kind"]
    return f'<span lang="fr">{k}</span>'


def ext(href, label, cls="btn"):
    return f'<a class="{cls}" href="{e(href)}" target="_blank" rel="noopener">{e(label)}<span class="sr"> {e(t("ui.new_tab"))}</span></a>'


def buy_links(p):
    """(etiket, adres) listesi. Türkçe sayfa Türkiye mağazasını, diğer diller varsa Etsy'yi gösterir."""
    if LANG != "tr" and p.get("etsy"):
        return [(t("buy.etsy"), p["etsy"])]
    many = len(p["tr"]) > 1
    return [((t("buy.iyzico") if "iyzi" in u else t("buy.shopier")) if many else t("buy.buy"), u) for u in p["tr"]]


def buy(p, mode="full"):
    """mode: full (düğme + ikinci bağlantı), one (tek düğme), row (koleksiyon dizini satırı)."""
    first_cls = "row__buy" if mode == "row" else "btn btn--solid"
    rest_cls = "row__buy" if mode == "row" else "link"
    links = buy_links(p)[:1] if mode == "one" else buy_links(p)
    out = "".join(ext(u, l, first_cls if k == 0 else rest_cls) for k, (l, u) in enumerate(links))
    return f'<div class="row__buys">{out}</div>' if mode == "row" else out


def preview(p):
    """Parfümün atmosferik görseli: sahne fotoğrafı varsa o, yoksa film karesi."""
    return im(p["image"], 1200) if p.get("image") else poster(p["video"])


def video(vid_id, label=None, hero=False):
    a11y = f'aria-label="{e(label)}"' if label else 'aria-hidden="true"'
    return f'<video muted loop playsinline{" autoplay" if hero else ""} preload="none" poster="{poster(vid_id)}" data-src="{vid(vid_id)}" {a11y}></video>'


def lang_menu(fname):
    cur = next(l for l in LANGS if l[0] == LANG)
    items = "".join(
        f'<li><a href="{PRE}{d}{fname}" lang="{c}" hreflang="{c}" data-flag="{f}"{" aria-current=" + chr(34) + "true" + chr(34) if c == LANG else ""}>'
        f'<img class="flag" src="{PRE}assets/flags/{f}.svg" alt="" width="20" height="15">{e(n)}</a></li>'
        for c, d, n, f in LANGS)
    return (f'<details class="lang"><summary aria-label="{e(t("ui.language"))}: {e(cur[2])}">'
            f'<img class="flag" src="{PRE}assets/flags/{cur[3]}.svg" alt="" width="20" height="15"><span>{LANG.upper()}</span></summary>'
            f'<ul>{items}</ul></details>')


def header(cur, fname):
    def a(href, label):
        c = ' aria-current="page"' if href == cur else ""
        return f'<a href="{href}"{c}>{e(label)}</a>'

    def col(title_html, items):
        lis = "".join(f'<li data-p="{p["slug"]}"><a href="{p["slug"]}.html">{e(p["name"])}</a></li>' for p in items)
        return f'<div><h3 class="cap">{title_html}</h3><ul>{lis}</ul></div>'

    sound = (f'<button type="button" class="sound" aria-pressed="false" title="Şahmaran, Hazar Canal">'
             f'<i aria-hidden="true"><span></span><span></span><span></span></i>{e(t("ui.sound"))}</button>')
    menu = lang_menu(fname)
    return f'''<a class="skip" href="#icerik">{e(t("ui.skip"))}</a>
<header class="top">
  <div class="wrap top__in">
    <a class="brand" href="index.html" aria-label="{e(t("ui.home_aria"))}" lang="tr" dir="ltr">Hazar Canal</a>
    <nav class="nav" aria-label="{e(t("ui.nav_aria"))}">
      <button type="button" class="nav__btn" aria-expanded="false" aria-controls="mega">{e(t("nav.collection"))}</button>
      {a("test.html", t("nav.quiz"))}
      <a href="index.html#deneme-seti">{e(t("nav.tester"))}</a>
      <a href="index.html#atolye">{e(t("nav.atelier"))}</a>
    </nav>
    <div class="tools">
      {menu}{sound}
      <button type="button" class="burger" aria-expanded="false" aria-controls="mega" aria-label="{e(t("ui.menu"))}"><span></span><span></span></button>
    </div>
  </div>
</header>
<div class="mega" id="mega" hidden>
  <div class="wrap mega__in">
    {col(kind(X), EXTRAIT)}
    {col(kind(E), EDP)}
    <div>
      <h3 class="cap">{e(t("nav.discover"))}</h3>
      <ul>
        <li><a href="test.html">{e(t("nav.quiz"))}</a></li>
        <li><a href="index.html#deneme-seti">{e(t("nav.tester"))}</a></li>
        <li><a href="index.html#atolye">{e(t("nav.atelier"))}</a></li>
      </ul>
      <div class="mega__tools">{menu}{sound}</div>
    </div>
  </div>
</div>'''


def footer():
    def col(title_html, items):
        return f'<div><h3 class="cap">{title_html}</h3><ul>' + "".join(f'<li><a href="{h}"{x}>{e(l)}</a></li>' for l, h, x in items) + "</ul></div>"
    blank = ' target="_blank" rel="noopener"'
    return f'''<footer class="foot">
  <div class="wrap">
    <div class="foot__grid">
      <div><a class="brand" href="index.html" lang="tr" dir="ltr">Hazar Canal</a>
        <p class="it mute" style="margin-top:1.5rem">{e(t("outro.tag"))}</p></div>
      {col(kind(X), [(p["name"], p["slug"] + ".html", "") for p in EXTRAIT])}
      {col(kind(E), [(p["name"], p["slug"] + ".html", "") for p in EDP])}
      {col(e(t("nav.discover")), [(t("nav.quiz"), "test.html", ""), (t("nav.tester"), "index.html#deneme-seti", ""), (t("nav.atelier"), "index.html#atolye", "")])}
      {col(e(t("nav.contact")), [(EMAIL, "mailto:" + EMAIL, ""), ("Instagram", INSTAGRAM, blank), ("TikTok", TIKTOK, blank)])}
    </div>
    <div class="foot__base"><span>© Hazar Canal</span><span>{e(t("foot.base"))}</span></div>
  </div>
</footer>
<audio id="hc-audio" src="{AUDIO}" preload="none" loop></audio>
<script src="{PRE}assets/app.js" defer></script>'''


def page(fname, title, desc, body, accent="", cur="", ogimg=None):
    seen, alts = set(), ""
    for c, d, _, _ in LANGS:
        if c not in seen:
            seen.add(c)
            alts += f'<link rel="alternate" hreflang="{c}" href="{SITE_URL}{d}{fname}">\n'
    doc = f'''<!doctype html>
<html lang="{LANG}" dir="{"rtl" if LANG in RTL else "ltr"}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{e(title)}</title>
<meta name="description" content="{e(desc)}">
<meta name="theme-color" content="#0b0a09">
{'<meta name="robots" content="noindex">' if NOINDEX else ''}
<meta property="og:title" content="{e(title)}">
<meta property="og:description" content="{e(desc)}">
<meta property="og:type" content="website">
{f'<meta property="og:image" content="{ogimg}">' if ogimg else ''}
{alts}<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 64 64'%3E%3Crect width='64' height='64' fill='%230b0a09'/%3E%3Cpath d='M20 16v32M44 16v32M20 32h24M32 8v48' stroke='%23c9c2b2' stroke-width='3' fill='none'/%3E%3C/svg%3E">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="preconnect" href="https://static.wixstatic.com">
<link href="https://fonts.googleapis.com/css2?family=Jost:wght@400;500&family=Libre+Caslon+Display&family=Sorts+Mill+Goudy:ital@0;1{EXTRA_FONTS.get(LANG, "")}&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{PRE}assets/style.css">
</head>
<body{f' data-p="{accent}"' if accent else ''}>
{header(cur, fname)}
<main id="icerik">
{body}
</main>
{footer()}
</body>
</html>
'''
    with open(os.path.join(OUT, DIR, fname), "w", encoding="utf-8", newline="\n") as f:
        f.write(localize(doc))


def invite():
    return f'''<section class="invite" aria-labelledby="inv-h">
  <div class="wrap invite__in rv">
    <div><h2 class="head it" id="inv-h">{e(t("invite.title"))}</h2>
      <p>{e(t("invite.text"))}</p></div>
    <a class="btn btn--solid" href="test.html">{e(t("nav.quiz"))}</a>
  </div>
</section>'''


def kind_line(p):
    if p.get("unisex"):
        return e(t("ui.kind_unisex")).replace("{kind}", kind(p))
    return kind(p)


# ------------------------------------------------------------------ ANA SAYFA
def home():
    atlas = BY["atlas"]

    def row(k, p):
        badge = "".join(f'<span class="row__badge" lang="en" dir="ltr">{e(b)}</span>' for b in p.get("badges", []))
        return f'''<article class="row rv" data-p="{p["slug"]}" data-i="{k}" data-tag="{e(tagline(p))}" data-kind="{e(p["kind"])}">
        <img class="row__thumb" src="{preview(p)}" alt="" loading="lazy">
        <span class="row__no" aria-hidden="true">{k + 1:02d}</span>
        <div class="row__main">
          <h3 class="name row__name"><a href="{p["slug"]}.html">{e(p["name"])}<span class="sr"> {e(p["kind"])}</span></a></h3>
          <p class="row__notes">{e(t(f'p.{p["slug"]}.notes_card'))}</p>{badge}
        </div>
        {buy(p, "row")}
      </article>'''

    rows_x = "".join(row(P.index(p), p) for p in EXTRAIT)
    rows_e = "".join(row(P.index(p), p) for p in EDP)
    stage = "".join(f'<img src="{preview(p)}" alt="" loading="lazy">' for p in P)

    def film(p, vid_id, key, cls):
        return f'''<article class="film {cls} rv" data-p="{p["slug"]}">
        {video(vid_id, t("alt.film", name=p["name"]))}
        <div class="film__cap">
          <h3 class="name">{e(p["name"])}</h3>
          <p>{e(t(key))}</p>
          <a class="link" href="{p["slug"]}.html">{e(t("ui.explore_scent"))}</a>
        </div>
      </article>'''

    body = f'''<section class="hero" data-p="atlas" aria-labelledby="hero-h">
  <div class="hero__media">{video(atlas["video"], hero=True)}</div>
  <div class="wrap hero__in">
    <div>
      <p class="hero__kind">{kind_line(atlas)}</p>
      <h1 class="hero-name" id="hero-h">Atlas</h1>
      <p class="hero__tag">{e(tagline(atlas))}</p>
    </div>
    <div class="hero__side"><div class="acts">{buy(atlas)}<a class="link" href="atlas.html">{e(t("ui.view"))}</a></div></div>
  </div>
</section>

<section class="sec" id="atolye" aria-labelledby="at-h">
  <div class="wrap house">
    <div class="house__text rv">
      <span class="spear" aria-hidden="true"></span>
      <h2 class="cap" id="at-h">{e(t("craft.1.title"))}</h2>
      <p class="lead">{e(t("craft.1.text"))}</p>
      <h3 class="cap" style="margin-top:1rem">{e(t("craft.2.title"))}</h3>
      <p class="mute" style="max-width:40ch">{e(t("craft.2.text"))}</p>
    </div>
    <figure class="house__fig rv" style="--d:.15s"><img src="{im(SKETCH, 1200)}" alt="{e(t("home.sketch_alt"))}" loading="lazy"><figcaption>{e(t("home.sketch_cap"))}</figcaption></figure>
    <ul class="claims rv">
      <li>{e(t("claim.1"))}</li>
      <li>{e(t("claim.2"))}</li>
      <li>{e(t("claim.3"))}<span>{e(t("claim.4"))}</span></li>
      <li>{e(t("claim.5"))}<span>{e(t("claim.6"))}</span></li>
    </ul>
  </div>
</section>

<section class="sec sec--tight" id="koleksiyon" aria-labelledby="kol-h">
  <div class="wrap">
    <div class="sec__head rv"><h2 class="head" id="kol-h">{e(t("home.collection"))}</h2></div>
    <div class="index">
      <div class="index__list">
        <p class="cap index__group">{kind(X)}</p>
        {rows_x}
        <p class="cap index__group">{kind(E)}</p>
        {rows_e}
      </div>
      <aside class="index__stage" aria-hidden="true">
        <div class="stage__frame">{stage}</div>
        <p class="stage__cap"><i id="stage-tag"></i><span id="stage-kind" lang="fr"></span></p>
      </aside>
    </div>
  </div>
</section>

<section class="sec sec--tight" aria-label="{e(t("home.films"))}">
  <div class="wrap films">
    {film(BY["sahmaran"], "584124_cb121a7fabad49c7ac3f78723b2dfa23", "film.sahmaran", "film--wide")}
    <div class="films__row">
      {film(BY["barbaros"], "584124_af0c4b3c6ab749e79e698fbb8844c2d1", "film.barbaros", "film--land")}
      {film(BY["devil"], "584124_b8ebb1c3a80e4214bb80f9cceade2a4e", "film.devil", "film--port")}
    </div>
  </div>
</section>

{invite()}

<section class="sec sec--bone on-bone" id="deneme-seti" aria-labelledby="ds-h">
  <div class="wrap split">
    <figure class="split__img rv"><img src="{im(LINEUP, 1400)}" alt="{e(t("tester.alt"))}" loading="lazy"></figure>
    <div class="split__body rv" style="--d:.15s">
      <h2 class="head" id="ds-h">{e(t("tester.title"))}</h2>
      <p>{e(t("tester.text"))}</p>
      <p class="small">{e(t("tester.contents"))}</p>
      {ext(TESTER_URL, t("buy.buy"), "btn btn--solid")}
    </div>
  </div>
</section>

<section class="outro" aria-labelledby="out-h">
  <div class="wrap rv">
    <span class="spear" aria-hidden="true"></span>
    <h2 class="sr" id="out-h">Hazar Canal</h2>
    <img class="mark" src="{im(LOGO, 500)}" alt="Hazar Canal" loading="lazy">
    <p class="lead">{e(t("outro.tag"))}</p>
    <p class="cap" style="margin-top:4rem">{e(t("outro.follow"))}</p>
    <div class="follow" style="margin-top:1rem">{ext(INSTAGRAM, "Instagram", "link")}{ext(TIKTOK, "TikTok", "link")}</div>
  </div>
</section>'''
    page("index.html", t("home.title"), t("home.desc"), body, cur="index.html", ogimg=poster(atlas["video"]))


# ------------------------------------------------------------------ ÜRÜN SAYFASI
def product(p):
    i = P.index(p)
    s = p["slug"]
    prev, nxt = P[i - 1], P[(i + 1) % len(P)]
    full = f'{p["name"]} {p["kind"]}'
    if p.get("video"):
        media = video(p["video"], hero=True)
        og = poster(p["video"])
    else:
        media = f'<img src="{im(p["image"], 2000)}" alt="{e(full)}">'
        og = im(p["image"], 1200)
    split = " hero--split" if p.get("portrait") else ""
    meta = f'<p class="hero__meta small">{e(t(f"p.{s}.chips"))}</p>' if has(f"p.{s}.chips") else ""
    badges = "".join(f'<p class="row__badge" lang="en" dir="ltr">{e(b)}</p>' for b in p.get("badges", []))
    body = f'''<section class="hero{split}" aria-labelledby="p-h">
  <div class="hero__media">{media}</div>
  <div class="{'' if split else 'wrap '}hero__in">
    <div>
      <p class="hero__kind">{kind_line(p)}</p>
      <h1 class="hero-name" id="p-h">{e(p["name"])}</h1>
      <p class="hero__tag">{e(tagline(p))}</p>
      {meta}{badges}
    </div>
    <div class="hero__side">
      <div class="acts">{buy(p)}</div>
      <p class="hero__ticks">{e(t("ticks"))}</p>
    </div>
  </div>
</section>'''

    facts = [(t("fact.kind"), kind(p))]
    if p.get("unisex"): facts.append((t("fact.gender"), e(t("ui.unisex"))))
    if has(f"p.{s}.character"): facts.append((t("fact.character"), e(t(f"p.{s}.character"))))
    if p.get("sister"):
        o = BY[p["sister"]]
        facts.append((t("fact.other"), f'<a class="link" href="{o["slug"]}.html">{e(o["name"])} {kind(o)}</a>'))
    facts_html = '<dl class="facts rv">' + "".join(f'<div><dt class="cap">{e(k)}</dt><dd>{v}</dd></div>' for k, v in facts) + "</dl>"
    story = t(f"p.{s}.story") if has(f"p.{s}.story") else [tagline(p)]
    story_html = "".join(f"<p>{e(x)}</p>" for x in story)
    if has(f"p.{s}.big"): story_html += f'<p class="big">{e(t(f"p.{s}.big"))}</p>'
    if has(f"p.{s}.closing"): story_html += '<p class="it mute">' + "<br>".join(e(x) for x in t(f"p.{s}.closing")) + "</p>"
    lead = " story__text--lead" if len(story) <= 2 else ""
    body += f'''
<section class="sec" aria-label="{e(t("aria.story"))}">
  <div class="wrap story">
    {facts_html}
    <div class="story__text{lead} rv" style="--d:.1s">{story_html}</div>
  </div>
</section>'''

    if has(f"p.{s}.love"):
        img_id, cover = p["love_img"]
        alt = t("alt.sketches") if cover else t("alt.bottle", name=p["name"])
        title = t(f"p.{s}.love_title") if has(f"p.{s}.love_title") else t("love.title")
        end = f'<p class="lead love__end">{e(t(f"p.{s}.love_end"))}</p>' if has(f"p.{s}.love_end") else ""
        body += f'''
<section class="sec sec--bone on-bone" aria-labelledby="love-h">
  <div class="wrap love">
    <figure class="love__img{' love__img--cover' if cover else ''} rv"><img src="{im(img_id, 1100)}" alt="{e(alt)}" loading="lazy"></figure>
    <div class="love__body rv" style="--d:.15s">
      <h2 class="head" id="love-h">{e(title)}</h2>
      <ul>{"".join(f"<li>{e(x)}</li>" for x in t(f"p.{s}.love"))}</ul>
      {end}
      <div class="acts">{buy(p, "one")}</div>
    </div>
  </div>
</section>'''
    elif p.get("love_img"):
        img_id, _ = p["love_img"]
        body += f'''
<section class="sec sec--bone on-bone" aria-labelledby="love-h">
  <div class="wrap love">
    <figure class="love__img rv"><img src="{im(img_id, 1100)}" alt="{e(t("alt.bottle", name=p["name"]))}" loading="lazy"></figure>
    <div class="love__body rv" style="--d:.15s">
      <h2 class="cap" id="love-h">{e(t("fact.character"))}</h2>
      <p class="head" style="margin-top:1rem">{e(t(f"p.{s}.character"))}</p>
      <div class="acts">{buy(p, "one")}</div>
    </div>
  </div>
</section>'''

    notes = t(f"p.{s}.notes")
    labels = [t("notes.top"), t("notes.heart"), t("notes.base")] if len(notes) == 3 else [None] * len(notes)
    rows = "".join(
        f'<div class="notes__row">{f"""<p class="cap">{e(l)}</p>""" if l else ""}<p>{e(n)}</p></div>'
        for l, n in zip(labels, notes))
    body += f'''
<section class="sec" aria-labelledby="n-h">
  <div class="wrap notes">
    <div class="notes__head rv"><h2 class="cap" id="n-h">{e(t("notes.title"))}</h2></div>
    <div class="notes__body rv" style="--d:.1s">{rows}</div>
  </div>
</section>'''

    if p.get("gallery"):
        figs = "".join(
            (f'<figure class="{c} g-quote rv"><blockquote>{e(tagline(p))}</blockquote></figure>' if g == "quote" else
             f'<figure class="{c} rv"><img src="{im(g, 1800)}" alt="{e(t("alt.world", name=p["name"]))}" loading="lazy"></figure>')
            for g, c in p["gallery"])
        body += f'<section class="sec sec--tight" aria-label="{e(t("aria.gallery"))}"><div class="wrap gallery">{figs}</div></section>'

    body += f'''
<section class="sec sec--tight" aria-label="{e(t("nav.atelier"))}">
  <div class="wrap"><div class="craft rv">
    <div><h2>{e(t("craft.1.title"))}</h2><p>{e(t("craft.1.text"))}</p></div>
    <div><h2>{e(t("craft.2.title"))}</h2><p>{e(t("craft.2.text"))}</p></div>
  </div></div>
</section>
{invite()}
<nav class="sister" aria-label="{e(t("ui.other_perfumes"))}">
  <a href="{prev["slug"]}.html" data-p="{prev["slug"]}"><em>{e(t("ui.prev"))}</em><span class="name">{e(prev["name"])}</span><em>{kind(prev)}</em></a>
  <a href="{nxt["slug"]}.html" data-p="{nxt["slug"]}"><em>{e(t("ui.next"))}</em><span class="name">{e(nxt["name"])}</span><em>{kind(nxt)}</em></a>
</nav>
<div class="buybar"><strong>{e(p["name"])}</strong>{buy(p, "one")}</div>'''
    desc = f'{full}. {tagline(p).rstrip(".。")}. {t("notes.desc_label")}: {"; ".join(notes)}.'
    page(s + ".html", f"{full} | Hazar Canal", desc, body, accent=s, ogimg=og)


# ------------------------------------------------------------------ KİŞİLİK TESTİ
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
RESULT_KEYS = {"Devil": "devil", "Barbaros": "barbaros", "Sahmaran": "sahmaran", "Arora": "arora", "Atlas": "atlas"}


def quiz():
    questions = t("quiz.q")
    total = len(questions)
    qs = ""
    for n, (q, opts) in enumerate(questions, 1):
        o = "".join(
            f'<label class="opt"><input type="radio" name="q{n}" value="q{n}a{k}"><span class="k" aria-hidden="true">{chr(64 + k)}</span><span>{e(x)}</span></label>'
            for k, x in enumerate(opts, 1))
        qs += f'''<div class="q" hidden>
        <p class="cap" aria-hidden="true" dir="ltr">{n:02d} / {total}</p>
        <fieldset>
        <legend><span class="sr">{e(t("quiz.q_sr", n=n, total=total))} </span>{e(q)}</legend>
        <div class="opts">{o}</div></fieldset></div>'''
    perfumes = {}
    for k, s in RESULT_KEYS.items():
        label, url = buy_links(BY[s])[0]
        perfumes[k] = dict(slug=s, name=BY[s]["name"], desc=t(f"quiz.r.{s}"), url=url, buy=label)
    data = json.dumps({"weights": WEIGHTS, "perfumes": perfumes,
                       "strings": {"next": t("quiz.next"), "show": t("quiz.show")}}, ensure_ascii=False)
    body = f'''<section class="quiz" id="quiz" aria-labelledby="quiz-h">
  <div class="quiz__bar" aria-hidden="true"><i></i></div>
  <div class="quiz__stage"><div class="wrap"><div class="quiz__in">
    <div class="quiz__intro">
      <p class="cap">{e(t("quiz.count"))}</p>
      <h1 class="head" id="quiz-h">{e(t("quiz.title"))}</h1>
      <p class="lead">{e(t("quiz.intro"))}</p>
      <button type="button" class="btn btn--solid" id="q-start">{e(t("quiz.start"))}</button>
    </div>
    {qs}
    <div class="quiz__nav" hidden>
      <button type="button" class="link" id="q-back">{e(t("quiz.back"))}</button>
      <button type="button" class="btn btn--solid" id="q-next" disabled>{e(t("quiz.next"))}</button>
    </div>
    <div class="quiz__result" hidden aria-live="polite">
      <p class="cap">{e(t("quiz.result_cap"))}</p>
      <h2 class="hero-name" id="r-name" tabindex="-1"></h2>
      <p class="lead" id="r-desc"></p>
      <div class="acts">
        <a class="btn btn--solid" id="r-page" href="#">{e(t("quiz.view"))}</a>
        <a class="link" id="r-buy" href="#" target="_blank" rel="noopener"></a>
        <button type="button" class="link" id="r-again">{e(t("quiz.again"))}</button>
      </div>
      <ul class="scores" id="r-scores" aria-label="{e(t("quiz.scores_aria"))}"></ul>
    </div>
    <noscript><p>{e(t("quiz.noscript"))}</p></noscript>
  </div></div></div>
</section>
<script type="application/json" id="quiz-data">{data}</script>'''
    page("test.html", f'{t("quiz.page_title")} | Hazar Canal', t("quiz.desc"), body, cur="test.html")


def main():
    global LANG, DIR, PRE, T
    built = []
    for code, d, _, _ in LANGS:
        if code in built:
            continue
        path = os.path.join(HERE, "i18n", code + ".json")
        if not os.path.exists(path):
            print("Atlandı (çeviri dosyası yok):", code)
            continue
        LANG, DIR, PRE, T = code, d, ("../" if d else ""), load(code)
        os.makedirs(os.path.join(OUT, d), exist_ok=True)
        home()
        for p in P:
            product(p)
        quiz()
        built.append(code)
    print("Tamam:", ", ".join(built), "dilleri,", len(P) + 2, "sayfa her biri")


if __name__ == "__main__":
    main()
