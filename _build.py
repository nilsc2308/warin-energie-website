# -*- coding: utf-8 -*-
"""Generator für die Website der Warin Energie GmbH: gemeinsamer Kopf/Fuß, alle Seiten, Sitemap.
Aufruf: python3 _build.py   (erzeugt die HTML-Dateien neben dieser Datei)"""
import json, os, html as H
OUT = os.path.dirname(os.path.abspath(__file__)) + '/'
DOMAIN = 'https://www.warin-energie.de'
TODAY = '2026-09-23'
VER = '20260923-8'
CO = dict(name='Warin Energie GmbH', brand='Warin Energie', street='Auf dem Hügel 21', zip='52249', city='Eschweiler',
          tel='0163 823 37 13', telh='+491638233713', mail='c.warin@warin-energie.de', office='office@warin-energie.de',
          person='Christoph Warin', lat='50.83367', lon='6.26860')

BOLT_PTS = '63,8 54,40.5 78.5,40.5 67.5,54.5 33,97 46.5,54.5 24,54.5'
MARK = f'<svg viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg" aria-hidden="true"><circle cx="50" cy="50" r="50" fill="#d00000"/><polygon points="{BOLT_PTS}" fill="#fff"/></svg>'
LOGO = f'<span class="mark">{MARK}</span><span class="wordmark"><b>WARIN</b><i>ENERGIE GMBH</i></span>'
ARROW = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12h14M13 6l6 6-6 6"/></svg>'
TEL = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1.9.4 1.8.7 2.7a2 2 0 0 1-.5 2.1L8 9.8a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.4c.9.3 1.8.6 2.7.7a2 2 0 0 1 1.9 2z"/></svg>'
MAIL = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="3" y="5" width="18" height="14" rx="2"/><path d="m3 7 9 6 9-6"/></svg>'
PIN = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 22s7-6.2 7-12a7 7 0 1 0-14 0c0 5.8 7 12 7 12z"/><circle cx="12" cy="10" r="2.5"/></svg>'
CHEV = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="m6 9 6 6 6-6"/></svg>'
BOLT = f'<svg class="bolt-ico" viewBox="20 5 62 95" aria-hidden="true"><polygon points="{BOLT_PTS}" fill="currentColor"/></svg>'

# Die drei Hebel und die acht Leistungen: Datei, Titel, Kurztitel, Hebel, Formel-Term, Einzeiler
LEVERS = [('preis', 'Einkauf & Preis'), ('kosten', 'Verträge & Kosten'), ('verbrauch', 'Verbrauch & Anlagen')]
SERVICES = [
    ('energiebeschaffung.html', 'Energiebeschaffung', 'Beschaffung', 'preis', 'preis', 'Strom und Erdgas zu bestmöglichen Marktpreisen, mit Marktbeobachtung und Ausschreibung.'),
    ('immobilienwirtschaft.html', 'Immobilienwirtschaft', 'Immobilien', 'preis', 'preis', 'Niedrige Nebenkosten für Mehrfamilienhäuser, Wohnanlagen und Eigentümergemeinschaften.'),
    ('mitarbeiter-tarife.html', 'Mitarbeiter-Tarife', 'Mitarbeiter-Tarife', 'preis', 'preis', 'Gute Energietarife für die Haushalte Ihrer Belegschaft, ohne Kosten für das Unternehmen.'),
    ('vertragsmanagement.html', 'Vertragsmanagement', 'Verträge', 'kosten', 'vertrag', 'Laufzeiten, Kündigungsfristen, Mengentoleranzen und Pönalen im Griff.'),
    ('rechnungspruefung.html', 'Rechnungsprüfung', 'Rechnungsprüfung', 'kosten', 'netz', 'Jede Abrechnung geprüft, das Clearing mit dem Versorger übernommen.'),
    ('antragsmanagement.html', 'Antragsmanagement', 'Anträge', 'kosten', 'steuern', 'Entlastung bei Strom- und Energiesteuer beantragen, Fristen einhalten.'),
    ('energieeffizienz.html', 'Energieeffizienz', 'Effizienz', 'verbrauch', 'menge', 'Energieaudit, ISO 50001, Netzwerke, Förderung und Energieausweise.'),
    ('anlagen-contracting.html', 'Anlagen-Contracting', 'Contracting', 'verbrauch', 'menge', 'Neue Heizung, BHKW oder Druckluft ohne eigene Investition.'),
]
TERMS = {'menge': 'Menge', 'preis': 'Energiepreis', 'netz': 'Netzentgelte', 'steuern': 'Steuern & Umlagen', 'vertrag': 'Vertragsrisiko'}
MAIN = [('referenzen.html', 'Referenzen'), ('unternehmen.html', 'Unternehmen'), ('ratgeber.html', 'Ratgeber')]
ALLNAV = [('index.html', 'Start')] + [(s[0], s[1]) for s in SERVICES] + [('referenzen.html', 'Referenzen'), ('unternehmen.html', 'Unternehmen'), ('partner.html', 'Partner'), ('ratgeber.html', 'Ratgeber'), ('faq.html', 'Häufige Fragen'), ('kontakt.html', 'Kontakt')]

# Echte Referenzlogos von der alten Website (Datei, Name, Breite, Höhe)
LOGOS = [('remondis', 'Remondis', 310, 102), ('hoermann', 'Hörmann', 361, 115), ('trilux', 'Trilux', 398, 137), ('alesco', 'alesco', 194, 72), ('caritas', 'Caritas Düren-Jülich', 144, 208),
         ('auto-conen', 'Auto Conen Gruppe', 208, 208), ('fbr', 'Fertigbeton Rheinland', 128, 126), ('richter', 'Richter', 176, 208), ('brueck', 'Brück Maschinenbau', 463, 119), ('emg-casting', 'EMG Casting AG', 488, 103),
         ('sarstedt', 'Sarstedt', 313, 66), ('queck', 'Stahlbau Queck', 244, 90), ('dreher', 'Dreher Granulators', 144, 112), ('st-antonius', 'St.-Antonius-Hospital Eschweiler', 158, 160), ('quickpack', 'quickpack', 160, 132),
         ('domini', 'Domini Hausverwaltungen', 472, 208), ('refood', 'ReFood', 406, 134), ('eigelshoven', 'Sägewerk Eigelshoven', 293, 100), ('autohaus-herten', 'Autohaus Herten', 329, 103), ('mohaba', 'Mohaba', 318, 171),
         ('guennewig', 'Günnewig Hotels & Restaurants', 228, 151), ('haku', 'HAKU CNC-Zerspanungstechnik', 250, 78), ('schloemer', 'Schloemer Gruppe', 243, 106), ('raiffeisen', 'Raiffeisen-Bank Eschweiler', 426, 91), ('marpa-jansen', 'Marpa Jansen', 351, 208),
         ('api', 'api Computerhandels GmbH', 376, 141), ('siemes-schuhcenter', 'Siemes Schuhcenter', 484, 114), ('barth', 'barth Metallwerke', 234, 97), ('mercedes-benz', 'Mercedes-Benz', 484, 106), ('plastics-recycling', 'plastics-recycling.eu', 283, 171), ('futterhaus', 'Das Futterhaus', 346, 103)]
PARTNERS = [('p-sempact', 'Sempact AG', 178, 51), ('p-wiro', 'WiRo Consulting GmbH', 488, 186), ('p-bdg', 'BDG Service GmbH', 182, 59), ('p-guido-schmitz', 'Immobiliensachverständiger Guido Schmitz', 488, 120), ('p-vgplan', 'VG-Plan Bauingenieur', 488, 159)]


def logo_img(k, n, w, h, lazy=True):
    lz = ' loading="lazy" decoding="async"' if lazy else ''
    return f'<img src="img/logos/{k}.webp" width="{w}" height="{h}" alt="Logo {H.escape(n)}"{lz}>'


def formula(active=None, cls=''):
    """Die Kostenformel als Zeile. Der Term der Seite wird rot und mit Blitz markiert."""
    def t(k):
        on = ' on' if k == active else ''
        return f'<span class="term t-{k}{on}">{BOLT if on else ""}{TERMS[k]}</span>'
    return (f'<span class="formula {cls}" role="img" aria-label="Energiekosten gleich Menge mal Klammer auf Energiepreis plus Netzentgelte plus Steuern und Umlagen Klammer zu plus Vertragsrisiko">'
            f'<span class="lhs">Energiekosten</span><span class="op">=</span>{t("menge")}<span class="op">×</span><span class="op br">(</span>{t("preis")}<span class="op">+</span>{t("netz")}<span class="op">+</span>{t("steuern")}<span class="op br">)</span><span class="op">+</span>{t("vertrag")}</span>')


def head(p):
    ld = [{
        "@context": "https://schema.org", "@type": "ProfessionalService", "@id": DOMAIN + "/#business", "name": "Warin Energie Consulting", "legalName": CO['name'],
        "description": "Energieberatung für Unternehmen aus Eschweiler: Energiebeschaffung, Vertragsmanagement, Rechnungsprüfung, Antragsmanagement, Energieeffizienz, Anlagen-Contracting, Immobilienwirtschaft und Mitarbeiter-Tarife.",
        "url": DOMAIN + "/", "telephone": "+49 163 8233713", "email": CO['mail'], "image": DOMAIN + "/img/og.jpg", "logo": DOMAIN + "/favicon.svg",
        "address": {"@type": "PostalAddress", "streetAddress": CO['street'], "postalCode": CO['zip'], "addressLocality": CO['city'], "addressRegion": "Nordrhein-Westfalen", "addressCountry": "DE"},
        "geo": {"@type": "GeoCoordinates", "latitude": float(CO['lat']), "longitude": float(CO['lon'])},
        "areaServed": ["Eschweiler", "Aachen", "Städteregion Aachen", "Düren", "Stolberg", "Jülich", "Köln", "Nordrhein-Westfalen", "Deutschland"],
        "founder": {"@type": "Person", "name": CO['person'], "jobTitle": "Geschäftsführender Gesellschafter, Energiemanager für die Industrie"},
        "vatID": "DE304182335"
    }]
    if p.get('ld'): ld.extend(p['ld'] if isinstance(p['ld'], list) else [p['ld']])
    url = DOMAIN + '/' + ('' if p['file'] == 'index.html' else p['file'])
    f = p['file']
    cur = lambda x: ' aria-current="page"' if f == x or p.get('parent') == x else ''
    svc_on = ' class="on"' if f in [s[0] for s in SERVICES] else ''
    groups = [('preis', 'Einkauf & Preis'), ('kosten', 'Verträge, Rechnungen, Anträge'), ('verbrauch', 'Verbrauch & Anlagen')]
    mega = ''.join(f'<div class="mg"><p class="mg-h">{n}</p><ul>' + ''.join(f'<li><a href="{s[0]}"{cur(s[0])}><b>{s[1]}</b><span>{s[5]}</span></a></li>' for s in SERVICES if s[3] == k) + '</ul></div>' for k, n in groups)
    mega += '<div class="mg mg-tools"><p class="mg-h">Selbst ausprobieren</p><ul>' + ''.join(f'<li><a href="{t[0]}#werkzeug">{tool_icon(t[3])}<b>{t[2]}</b></a></li>' for t in TOOLS) + '</ul></div>'
    return f'''<!DOCTYPE html>
<html lang="de">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{p['title']}</title>
<meta name="description" content="{p['desc']}">
<link rel="canonical" href="{url}">
{'<meta name="robots" content="noindex, follow">' if p.get('noindex') else ''}
<meta property="og:type" content="{'article' if p.get('article') else 'website'}">
<meta property="og:site_name" content="Warin Energie Consulting">
<meta property="og:locale" content="de_DE">
<meta property="og:title" content="{p['title']}">
<meta property="og:description" content="{p['desc']}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{DOMAIN}/img/og.jpg">
<meta property="og:image:width" content="1200"><meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#ffffff">
<link rel="icon" href="favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="apple-touch-icon.png">
<link rel="preload" href="fonts/ibm-plex-sans-latin-standard-normal.woff2" as="font" type="font/woff2" crossorigin>
{'<link rel="preload" as="image" href="img/industriehalle-l.webp" imagesrcset="img/industriehalle-m.webp 800w, img/industriehalle-l.webp 1400w, img/industriehalle.webp 2000w" imagesizes="100vw">' if f == 'index.html' else ''}
<link rel="stylesheet" href="styles.css?v={VER}">
<script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script>
</head>
<body class="{p.get('body', '')}">
<a class="skip" href="#main">Zum Inhalt springen</a>
<div class="curtain intro" aria-hidden="true"><div class="intro-mark">{MARK}</div></div>
<div class="curtain leave" aria-hidden="true"></div>
<div class="progress" id="progress" aria-hidden="true"></div>
<header class="head" id="head">
  <div class="head-in">
    <a class="logo" href="index.html" aria-label="Warin Energie GmbH – Startseite">{LOGO}</a>
    <nav class="nav" aria-label="Hauptnavigation"><ul>
      <li class="has-mega"><button type="button"{svc_on} aria-expanded="false" aria-controls="mega">Leistungen {CHEV}</button></li>
      <li><a href="referenzen.html"{cur('referenzen.html')}>Referenzen</a></li>
      <li><a href="unternehmen.html"{cur('unternehmen.html')}>Unternehmen</a></li>
      <li><a href="ratgeber.html"{cur('ratgeber.html')}>Ratgeber</a></li>
      <li><a href="kontakt.html"{cur('kontakt.html')}>Kontakt</a></li>
    </ul></nav>
    <div class="right"><a class="tel" href="tel:{CO['telh']}" aria-label="Anrufen: {CO['tel']}">{TEL}<span>{CO['tel']}</span></a><a class="btn red mag" href="kontakt.html?thema=rechnung">Rechnung prüfen lassen</a>
    <button class="menu-btn" type="button" aria-expanded="false" aria-controls="menu"><span class="lbl">Menü</span><span class="lines"><span></span><span></span></span></button></div>
  </div>
  <div class="mega" id="mega"><div class="mega-in">{mega}</div></div>
</header>
<div class="menu" id="menu">
  <div class="menu-in">
    <ul>{''.join(f'<li><a href="{a}"{cur(a)}>{t}</a></li>' for a, t in ALLNAV)}</ul>
    <div class="menu-foot"><b>{CO['name']}</b><span>{CO['street']}, {CO['zip']} {CO['city']}</span><a href="tel:{CO['telh']}">{CO['tel']}</a><a href="mailto:{CO['mail']}">{CO['mail']}</a></div>
  </div>
</div>
<main id="main">
'''


def foot(p):
    return f'''</main>
<div class="sticky-cta"><a class="btn red" href="kontakt.html?thema=rechnung">Rechnung prüfen lassen {ARROW}</a><a class="btn line" href="tel:{CO['telh']}" aria-label="Anrufen">{TEL}</a></div>
<footer class="footer">
  <div class="wrap">
    <div class="top">
      <div class="brand"><a class="logo" href="index.html" aria-label="Warin Energie GmbH – Startseite">{LOGO}</a><p>Energiekostenoptimierung für Unternehmen, von Anfang bis Ende durchdacht. Aus Eschweiler für die Region und ganz Deutschland.</p></div>
      {''.join(f'<div><h4>{n}</h4><ul>' + ''.join(f'<li><a href="{s[0]}">{s[1]}</a></li>' for s in SERVICES if s[3] == k) + '</ul></div>' for k, n in LEVERS)}
      <div><h4>Warin Energie</h4><ul><li><a href="referenzen.html">Referenzen</a></li><li><a href="unternehmen.html">Unternehmen</a></li><li><a href="partner.html">Partner</a></li><li><a href="ratgeber.html">Ratgeber</a></li><li><a href="faq.html">Häufige Fragen</a></li><li><a href="kontakt.html">Kontakt</a></li></ul></div>
      <div><h4>Kontakt</h4><ul><li>{CO['name']}</li><li>{CO['street']}</li><li>{CO['zip']} {CO['city']}</li><li><a href="tel:{CO['telh']}">{CO['tel']}</a></li><li><a href="mailto:{CO['mail']}">{CO['mail']}</a></li></ul></div>
    </div>
    <div class="bottom"><span>© 2026 {CO['name']}</span><span class="legal"><a href="impressum.html">Impressum</a><a href="datenschutz.html">Datenschutz</a></span><a class="totop" href="#">Nach oben</a></div>
  </div>
</footer>
<script src="https://cdn.jsdelivr.net/npm/gsap@3.13.0/dist/gsap.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/gsap@3.13.0/dist/ScrollTrigger.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/lenis@1.3.11/dist/lenis.min.js"></script>
<script src="main.js?v={VER}"></script>
</body>
</html>
'''


def ph(title, lead, term=None, facts=None, crumbs=None):
    """Formel-Kopf: Kostenformel als Zeile (Term der Seite rot), darunter Titel links, rechts Lead + Kurzfakten."""
    fx = ''.join(f'<li>{x}</li>' for x in (facts or []))
    tl = f'<p class="fh-term">{BOLT}Wirkt auf: <b>{TERMS[term]}</b></p>' if term else ''
    cr = f'<p class="crumb"><a href="index.html">Start</a> / {crumbs}</p>' if crumbs else ''
    return f'''<section class="fh{' has-term' if term else ''}"><div class="wrap">
  {f'<div class="fh-formula">{formula(term)}</div>' if term else ''}
  <div class="fh-grid">
    <div>{cr}<h1 class="split">{title}</h1></div>
    <div class="fh-side"><p class="lead reveal">{lead}</p>{tl}{f'<ul class="fh-facts reveal">{fx}</ul>' if fx else ''}</div>
  </div>
</div></section>'''


def cta(h, t, btn='Anfrage senden', href='kontakt.html'):
    return f'''<section class="sec tight"><div class="wrap"><div class="cta-band reveal"><div><h2>{h}</h2><p>{t}</p></div><div class="cta-act"><a class="btn red big mag" href="{href}">{btn} {ARROW}</a><a class="cta-tel" href="tel:{CO['telh']}">{TEL}{CO['tel']}</a></div></div></div></section>'''


def more(file):
    """Weiter zu den anderen Leistungen desselben Hebels."""
    s = next(x for x in SERVICES if x[0] == file)
    others = [x for x in SERVICES if x[0] != file]
    others.sort(key=lambda x: x[3] != s[3])
    return f'''<section class="sec tight more"><div class="wrap"><h2 class="h3">Weitere Hebel an Ihrer Energierechnung</h2><ul class="more-list">{''.join(f'<li class="reveal"><a href="{x[0]}"><span class="ml-t">{x[1]}</span><span class="ml-d">{x[5]}</span><span class="ml-k">{TERMS[x[4]]}</span>{ARROW}</a></li>' for x in others[:4])}</ul></div></section>'''


TOOLS = [  # Seite, Frage, Werkzeug, Symbol (SVG-Pfade 32x32)
    ('vertragsmanagement.html', 'Bis wann muss ich meinen Liefervertrag kündigen?', 'Fristen-Rechner', '<rect x="5" y="7" width="22" height="20" rx="3"/><path d="M5 13h22M11 4v6M21 4v6M12 19l3 3 6-6"/>'),
    ('rechnungspruefung.html', 'Was steht eigentlich alles auf meiner Stromrechnung?', 'Musterrechnung zum Anklicken', '<path d="M8 4h16v24l-4-2-4 2-4-2-4 2z"/><path d="M12 10h8M12 15h8M12 20h5"/>'),
    ('antragsmanagement.html', 'Welche Steuer kann ich mir zurückholen?', 'Antrags-Matrix', '<rect x="4" y="4" width="10" height="10" rx="2"/><rect x="18" y="4" width="10" height="10" rx="2"/><rect x="4" y="18" width="10" height="10" rx="2"/><path d="M20 23l3 3 5-6"/>'),
    ('energieeffizienz.html', 'Brauche ich ein Energieaudit oder ISO 50001?', 'Pflichten-Check', '<path d="M4 24a12 12 0 0 1 24 0"/><path d="M16 24l6-8"/><circle cx="16" cy="24" r="2"/>'),
    ('energiebeschaffung.html', 'Festpreis, Tranchen oder Spotmarkt?', 'Beschaffungsmodelle im Vergleich', '<path d="M3 24l6-8 5 4 6-10 4 5 5-7"/><circle cx="9" cy="16" r="2"/><circle cx="20" cy="10" r="2"/>'),
    ('anlagen-contracting.html', 'Neue Anlage kaufen oder mieten?', 'Contracting-Waage', '<path d="M16 5v22M9 27h14M5 10h22"/><path d="M5 10l-3 8h6zM27 10l-3 8h6z"/>'),
    ('immobilienwirtschaft.html', 'Wie viele Verträge spare ich mir bei mehreren Häusern?', 'Bündelungs-Baukasten', '<path d="M3 28V14l6-4 6 4v14zM17 28V10l6-5 6 5v18z"/><path d="M3 28h26"/>'),
    ('mitarbeiter-tarife.html', 'Was haben meine Mitarbeitenden davon?', 'Perspektiv-Wechsel', '<circle cx="11" cy="11" r="4"/><circle cx="22" cy="13" r="3"/><path d="M3 26c0-5 4-8 8-8s8 3 8 8M19 26c0-4 2-7 6-7 3 0 4 2 4 4"/>'),
]


def tool_icon(p):
    return f'<svg viewBox="0 0 32 32" aria-hidden="true">{p}</svg>'

# ============================ STARTSEITE ============================
CURVE = 'M0,300 C40,290 70,250 110,262 S170,330 210,300 S260,170 300,190 S360,260 400,230 S450,110 490,140 S560,220 600,180 S660,60 700,90 S760,170 800,150'


def photo(name, alt, w=2000, h=1333, lazy=True, late=False, sizes='100vw', cls=''):
    """Foto in drei Größen. late=True: erst nach dem load-Ereignis laden."""
    srcset = f'img/{name}-m.webp 800w, img/{name}-l.webp 1400w, img/{name}.webp {w}w'
    c = f' class="{cls}"' if cls else ''
    if late:
        return f'<img data-src="img/{name}-l.webp" data-srcset="{srcset}" sizes="{sizes}" width="{w}" height="{h}" alt="{alt}" data-late{c}>'
    load = ' loading="lazy" decoding="async"' if lazy else ' fetchpriority="high"'
    return f'<img src="img/{name}-l.webp" srcset="{srcset}" sizes="{sizes}" width="{w}" height="{h}" alt="{alt}"{load}{c}>'


def sphoto(nm, alt):
    """Foto der Ersatzfassung: wird nur per Skript geladen, wenn die Szene nicht läuft."""
    return photo(nm, alt, sizes='(max-width: 820px) 100vw, 50vw').replace(' src="', ' data-st-src="').replace(' srcset="', ' data-st-srcset="')


SCENE = [  # Foto, Alt-Text, Überschrift, Text
    ('industriehalle', 'Große Industriehalle mit Hallenkran und einfallendem Licht', 'Nach dem Personal kommt oft schon die Energie.', 'Warin Energie begleitet Unternehmen bei allem, was Energie kostet: Einkauf, Verträge, Rechnungen, Anträge und Effizienz.'),
    ('produktion', 'Arbeiter an einer Maschine, Funken fliegen', 'Sie kümmern sich um Ihre Produktion.', 'Wir kümmern uns um die Energiekosten dahinter – damit Ihre Zeit, Ihr Geld und Ihr Personal im Kerngeschäft bleiben.'),
    ('umspannwerk', 'Umspannwerk mit Leitungen unter blauem Himmel', 'Wir lesen Ihre Rechnung Zeile für Zeile.', 'Netzentgelte, Umlagen, Steuern, Messstellenbetrieb: Wir prüfen jede Position und übernehmen das Clearing mit dem Versorger.'),
    ('strommasten', 'Strommasten im Sonnenuntergang', 'Wir kaufen ein, wenn der Markt es hergibt.', 'Ausschreibung, Tranchen oder Festpreis – nur bei zuverlässigen Versorgern und mit laufender Marktbeobachtung.'),
    ('hochspannung', 'Hochspannungsleitung in der Abenddämmerung mit Lichtspuren', 'Ein Ansprechpartner für alles, was Energie kostet.', 'Unabhängig, aus Eschweiler, für Unternehmen aller Branchen.'),
]

LEVER_BLOCKS = [  # Formel-Term, Überschrift, Text, Leistungen
    ('menge', 'Weniger verbrauchen.', 'Die günstigste Kilowattstunde ist die, die Sie nicht brauchen. Wir untersuchen Beleuchtung, Druckluft, Pumpen, Lastspitzen, Wärme und Kälte, begleiten Energieaudit und ISO 50001 und nutzen Förderungen.', ['energieeffizienz.html', 'anlagen-contracting.html']),
    ('preis', 'Besser einkaufen.', 'Strom und Erdgas zu bestmöglichen Marktpreisen: Wir bündeln, schreiben aus, verhandeln und behalten den Markt im Blick. Auch für Wohnungsbestände und die Haushalte Ihrer Belegschaft.', ['energiebeschaffung.html', 'immobilienwirtschaft.html', 'mitarbeiter-tarife.html']),
    ('netz', 'Richtig abrechnen lassen.', 'Netzentgelte sind komplex und fehleranfällig. Wir prüfen jede Abrechnung gegen Vertrag und Preisblatt und klären Abweichungen direkt mit dem Versorger.', ['rechnungspruefung.html']),
    ('steuern', 'Zurückholen, was Ihnen zusteht.', 'Stromsteuer, Energiesteuer, Besondere Ausgleichsregelung: Wir prüfen die Voraussetzungen, stellen die Anträge und halten die Fristen ein.', ['antragsmanagement.html']),
    ('vertrag', 'Verträge, die zur Produktion passen.', 'Laufzeiten, Kündigungsfristen, Mengentoleranzen, Pönalen bei Kurzarbeit: Wir legen Verträge auf Ihren Verbrauch aus und behalten jede Frist im Blick.', ['vertragsmanagement.html']),
]


def index():
    n = len(SCENE)
    frames = ''.join(f'<div class="frame f{i + 1}">{photo(nm, alt, lazy=False) if i == 0 else photo(nm, alt, late=True)}</div>' for i, (nm, alt, _, _) in enumerate(SCENE))
    split = f'<div class="half a" aria-hidden="true"></div><div class="half b" aria-hidden="true"></div>'
    caps = ''
    for i, (_, _, h, t) in enumerate(SCENE):
        tag = 'h1' if i == 0 else 'p'
        role = '' if i == 0 else ' role="heading" aria-level="2"'
        extra = ''
        if i == n - 1:
            extra = f'''<div class="cap-person"><img src="img/christoph-warin.webp" width="292" height="350" alt="Christoph Warin" loading="lazy" decoding="async"><span><b>Christoph Warin</b>Geschäftsführer, Energiemanager für die Industrie</span></div>
          <div class="actions"><a class="btn red big mag" href="kontakt.html?thema=rechnung">Rechnung prüfen lassen {ARROW}</a><a class="btn ghost big" href="#hebel">Leistungen ansehen</a></div>'''
        caps += f'<div class="cap c{i + 1}"><{tag} class="cap-h"{role}>{h}</{tag}><p class="cap-t">{t}</p>{extra}</div>'
    scene = f'''
<section class="scene" aria-label="Einstieg">
  <div class="stage">
    {frames}
    {split}
    <div class="shade" aria-hidden="true"></div>
    <div class="caps">{caps}</div>
    <div class="s-prog" aria-hidden="true">{''.join('<span><i></i></span>' for _ in SCENE)}</div>
  </div>
</section>
<div class="scene-static">
  {''.join(f'<figure>{sphoto(nm, alt)}<figcaption>{"<h1>" + h + "</h1>" if i == 0 else "<b>" + h + "</b>"}<span>{t}</span></figcaption></figure>' for i, (nm, alt, h, t) in enumerate(SCENE))}
</div>'''

    svc = {s[0]: s for s in SERVICES}
    blocks = ''.join(f'''<article class="lv" data-term="{k}"><p class="lv-k">{BOLT}{TERMS[k]}</p><h3>{h}</h3><p>{t}</p><ul class="lv-links">{''.join(f'<li><a href="{f}">{svc[f][1]} {ARROW}</a></li>' for f in links)}</ul></article>''' for k, h, t, links in LEVER_BLOCKS)
    stack = ''.join(f'<li class="st-{k}"><span>{TERMS[k]}</span></li>' for k in ['menge', 'preis', 'netz', 'steuern', 'vertrag'])
    hebel = f'''
<section class="sec hebel" id="hebel" aria-labelledby="hebel-h">
  <div class="wrap">
    <div class="hebel-head"><h2 id="hebel-h" class="split">Ihre Energiekosten sind eine Rechnung. Wir arbeiten an jedem Faktor.</h2>
      <div class="formel-line reveal">{formula()}</div></div>
    <div class="hebel-grid">
      <div class="hebel-side" aria-hidden="true"><ol class="stack">{stack}</ol></div>
      <div class="hebel-list">{blocks}</div>
    </div>
  </div>
</section>'''

    calc = f'''
<section class="sec dark lift calc-sec" id="rechner" aria-labelledby="calc-h">
  <div class="wrap">
    <div class="calc-grid">
      <div class="calc-intro"><h2 id="calc-h" class="split">Was ein Cent pro Kilowattstunde wert ist.</h2><p class="reveal">Rechnen Sie selbst: Jahresverbrauch mal Preisunterschied. Welcher Unterschied bei Ihnen drin ist, zeigt der Vergleich Ihrer Rechnung mit dem Markt.</p></div>
      <div class="calc reveal" data-calc>
        <fieldset><legend>Jahresverbrauch Strom</legend><div class="chips" data-k="kwh">{''.join(f'<button type="button" class="chip{" on" if v == 500000 else ""}" data-v="{v}">{l}</button>' for v, l in [(100000, '100.000 kWh'), (500000, '500.000 kWh'), (2000000, '2 Mio. kWh'), (10000000, '10 Mio. kWh')])}</div>
          <label class="own">oder eigener Wert <input type="text" inputmode="numeric" name="kwh" placeholder="z. B. 750000" autocomplete="off"> kWh</label></fieldset>
        <fieldset><legend>Preisunterschied</legend><div class="chips" data-k="ct">{''.join(f'<button type="button" class="chip{" on" if v == 1 else ""}" data-v="{v}">{l}</button>' for v, l in [(0.5, '0,5 ct/kWh'), (1, '1 ct/kWh'), (2, '2 ct/kWh'), (3, '3 ct/kWh')])}</div></fieldset>
        <fieldset><legend>Vertragslaufzeit</legend><div class="chips" data-k="y">{''.join(f'<button type="button" class="chip{" on" if v == 2 else ""}" data-v="{v}">{l}</button>' for v, l in [(1, '1 Jahr'), (2, '2 Jahre'), (3, '3 Jahre')])}</div></fieldset>
        <output class="calc-out" aria-live="polite"><span class="co-row"><span>pro Jahr</span><b id="c-year">5.000 €</b></span><span class="co-row big"><span>über die Laufzeit</span><b id="c-total">10.000 €</b></span><span class="co-eq" id="c-eq">500.000 kWh × 1 ct = 5.000 € netto pro Jahr</span></output>
        <p class="note">Reine Rechnung ohne Einsparzusage, netto ohne Steuern und Umlagen.</p>
      </div>
    </div>
  </div>
</section>'''

    half = (len(LOGOS) + 1) // 2
    row = lambda items: ''.join(f'<li class="lr-i">{logo_img(k, nm, w, h)}</li>' for k, nm, w, h in items)
    refs = f'''
<section class="sec refs" aria-labelledby="refs-h">
  <div class="wrap refs-head"><h2 id="refs-h" class="split">Ein Auszug unserer Referenzen.</h2><p class="reveal">Von der Klinik bis zum Stahlbau: Unsere Erfahrung stammt aus Projekten in Automotive, CNC, Lebensmittel, Medizintechnik, Gesundheit, Gießereien, Papier, Verpackungen, Abfall- und Immobilienwirtschaft.</p></div>
  <div class="logo-rows"><ul class="lr r1">{row(LOGOS[:half])}</ul><ul class="lr r2">{row(LOGOS[half:])}</ul></div>
  <p class="wrap refs-foot"><a class="link" href="referenzen.html">Alle {len(LOGOS)} Referenzen ansehen {ARROW}</a></p>
</section>'''

    about = f'''
<section class="about" aria-labelledby="about-h">
  <div class="about-photo">{photo('leitstand', 'Leitstand eines Kraftwerks mit Schaltwand', sizes='(max-width: 1020px) 100vw, 50vw')}</div>
  <div class="about-txt">
    <h2 id="about-h" class="split">Unabhängig. Aus Eschweiler.</h2>
    <p class="reveal">Unser Know-how und die jahrelange Erfahrung in der Energiewirtschaft und in Unternehmen aller Branchen machen uns zu einem kompetenten Partner in allen energierelevanten Fragen. Dazu kommt ein Netzwerk aus Fachleuten für Effizienz und Technik.</p>
    <div class="about-person reveal"><img src="img/christoph-warin.webp" width="292" height="350" alt="Christoph Warin" loading="lazy" decoding="async"><span><b>Christoph Warin</b>Geschäftsführender Gesellschafter<br>Energiemanager für die Industrie<a href="tel:{CO['telh']}">{CO['tel']}</a></span></div>
    <a class="btn white mag reveal" href="unternehmen.html">Das Unternehmen {ARROW}</a>
  </div>
</section>'''

    tools = f'''
<section class="sec tools-sec" id="werkzeuge" aria-labelledby="tools-h">
  <div class="wrap">
    <div class="tools-head"><h2 id="tools-h" class="split">Selbst ausprobieren.</h2><p class="reveal">Acht Fragen, die uns Unternehmen oft stellen – und zu jeder ein kleines Werkzeug, mit dem Sie die Antwort für Ihren Fall sofort sehen.</p></div>
    <ul class="tools">{''.join(f'<li class="reveal"><a href="{f}#werkzeug"><span class="tl-i">{tool_icon(ic)}</span><span class="tl-q">{q}</span><span class="tl-n">{n}</span><span class="tl-a">{ARROW}</span></a></li>' for f, q, n, ic in TOOLS)}</ul>
  </div>
</section>'''
    guide = f'''
<section class="sec tight guide-sec" aria-labelledby="guide-h">
  <div class="wrap">
    <div class="guide-head"><h2 id="guide-h" class="split">Aus dem Ratgeber.</h2><a class="link reveal" href="faq.html">Häufige Fragen {ARROW}</a></div>
    <ul class="guide">{''.join(f'<li class="reveal"><a href="{a[0]}"><span class="gd-k">{BOLT}{TERMS[a[3]]}</span><b>{a[1]}</b><span class="gd-d">{a[2]}</span><span class="link">Weiterlesen {ARROW}</span></a></li>' for a in ARTICLES)}</ul>
  </div>
</section>'''
    return scene + hebel + tools + calc + refs + guide + about + contact_section('home')


def contact_section(where):
    opts = [('rechnung', 'Rechnungsprüfung'), ('beschaffung', 'Energiebeschaffung / Ausschreibung'), ('vertrag', 'Vertragsmanagement'), ('antrag', 'Antragsmanagement (Steuern & Umlagen)'),
            ('effizienz', 'Energieeffizienz / Energieaudit / ISO 50001'), ('contracting', 'Anlagen-Contracting'), ('immobilien', 'Immobilienwirtschaft'), ('mitarbeiter', 'Mitarbeiter-Tarife'), ('ausweis', 'Energieausweis'), ('sonstiges', 'Etwas anderes')]
    return f'''
<section class="sec contact-sec" id="anfrage" aria-labelledby="env-h">
  <div class="wrap env-grid">
    <div class="env-intro">
      <h2 id="env-h" class="split">Schicken Sie uns Ihre letzte Rechnung.</h2>
      <p class="reveal">Eine Strom- oder Gasrechnung reicht für den ersten Blick. Wir melden uns mit einer ehrlichen Einschätzung, ob sich eine genauere Prüfung lohnt.</p>
      <ul class="env-contact reveal">
        <li>{TEL}<a href="tel:{CO['telh']}">{CO['tel']}</a></li>
        <li>{MAIL}<a href="mailto:{CO['mail']}">{CO['mail']}</a></li>
        <li>{PIN}<span>{CO['street']}, {CO['zip']} {CO['city']}</span></li>
      </ul>
    </div>
    <div class="letter reveal">
        <form class="form" name="anfrage" method="POST" action="danke.html" data-netlify="true" netlify-honeypot="firma-web" enctype="multipart/form-data" novalidate>
          <input type="hidden" name="form-name" value="anfrage">
          <p class="hp"><label>Nicht ausfüllen <input name="firma-web" tabindex="-1" autocomplete="off"></label></p>
          <div class="fields">
            <div class="field"><label for="f-firma-{where}">Unternehmen</label><input id="f-firma-{where}" name="unternehmen" autocomplete="organization"></div>
            <div class="field"><label for="f-name-{where}">Ihr Name *</label><input id="f-name-{where}" name="name" required autocomplete="name"><span class="err">Bitte geben Sie Ihren Namen an.</span></div>
            <div class="field"><label for="f-mail-{where}">E-Mail *</label><input id="f-mail-{where}" name="email" type="email" required autocomplete="email"><span class="err">Bitte eine gültige E-Mail-Adresse.</span></div>
            <div class="field"><label for="f-tel-{where}">Telefon</label><input id="f-tel-{where}" name="telefon" type="tel" autocomplete="tel"></div>
            <div class="field full"><label for="f-thema-{where}">Worum geht es?</label><select id="f-thema-{where}" name="thema">{''.join(f'<option value="{v}">{t}</option>' for v, t in opts)}</select></div>
            <div class="field full"><label for="f-msg-{where}">Nachricht</label><textarea id="f-msg-{where}" name="nachricht" rows="3" placeholder="Verbrauch, Standorte, Vertragsende – was Sie schon wissen."></textarea></div>
            <div class="field full file"><label for="f-file-{where}">Rechnung anhängen (PDF oder Foto, optional, max. 8 MB)</label><input id="f-file-{where}" name="rechnung" type="file" accept=".pdf,image/*"></div>
            <div class="field full check"><input id="f-ds-{where}" type="checkbox" name="datenschutz" required><label for="f-ds-{where}">Ich habe die <a href="datenschutz.html">Datenschutzerklärung</a> gelesen und bin einverstanden, dass meine Angaben zur Bearbeitung der Anfrage gespeichert werden. *</label><span class="err">Bitte bestätigen Sie die Datenschutzerklärung.</span></div>
          </div>
          <button class="btn red big mag" type="submit">Anfrage absenden {ARROW}</button>
        </form>
    </div>
  </div>
</section>'''


# ============================ LEISTUNGEN ============================
def sec(inner, cls='', sid=None):
    i = f' id="{sid}"' if sid else ''
    return f'<section class="sec {cls}"{i}><div class="wrap">{inner}</div></section>'


def two(h, body, aside=''):
    return f'<div class="two"><h2 class="split">{h}</h2><div class="prose reveal">{body}</div>{aside}</div>'


def ticks(items):
    return '<ul class="ticks">' + ''.join(f'<li>{x}</li>' for x in items) + '</ul>'


def p_beschaffung():
    models = [('fest', 'Festpreis', 'Ein Einkaufszeitpunkt, ein Preis für die ganze Laufzeit. Planbar, aber alles hängt am gewählten Tag.'),
              ('tranchen', 'Tranchen', 'Die Menge wird in mehreren Teilen zu verschiedenen Zeitpunkten gekauft. Der Durchschnitt glättet Ausreißer nach oben und unten.'),
              ('spot', 'Spotmarkt', 'Der Preis folgt dem Markt, Monat für Monat. Chancen bei fallenden Preisen, volles Risiko bei steigenden.')]
    tool = f'''
<div class="model reveal" data-model>
  <div class="model-ctl" role="group" aria-label="Beschaffungsmodell wählen">{''.join(f'<button type="button" class="chip{" on" if k == "tranchen" else ""}" data-m="{k}" aria-pressed="{"true" if k == "tranchen" else "false"}">{n}</button>' for k, n, _ in models)}</div>
  <div class="model-fig">
    <svg viewBox="0 0 800 400" preserveAspectRatio="none" aria-hidden="true"><path class="grid-l" d="M0,100H800M0,200H800M0,300H800"/><path class="m-curve" d="{CURVE}"/>
      <path class="m-fest" d="M0,190 H800"/><path class="m-avg" d="M0,215.5 H800"/><path class="m-spot" d="{CURVE}"/></svg>
    <div class="m-pts"><span class="mp p-fest" style="--x:37.5%;--y:47.5%"></span><span class="mp p-t" style="--x:13.75%;--y:65.5%"></span><span class="mp p-t" style="--x:37.5%;--y:47.5%"></span><span class="mp p-t" style="--x:50%;--y:57.5%"></span><span class="mp p-t" style="--x:75%;--y:45%"></span></div>
    <span class="m-note">schematischer Verlauf zur Erklärung, keine Marktdaten</span>
  </div>
  <div class="model-txt" aria-live="polite">{''.join(f'<p data-m="{k}"{"" if k == "tranchen" else " hidden"}><b>{n}:</b> {t}</p>' for k, n, t in models)}</div>
</div>'''
    body = ph('Energiebeschaffung', 'Strom und Erdgas zu bestmöglichen Marktpreisen – ausgeschrieben, verhandelt und nur bei zuverlässigen Versorgern abgeschlossen.', 'preis',
              ['Ausschreibung in enger Absprache mit Ihnen', 'Festpreis, Tranchen oder strukturierte Beschaffung', 'Auf Wunsch Naturstrom aus erneuerbaren Quellen'], 'Energiebeschaffung')
    body += sec(two('Energie ist ein Kostenblock, kein Nebenthema.', '<p>Die Energiekosten spielen in allen wirtschaftlichen Bereichen eine immer größere Rolle. Durch den weltweiten Wettbewerb stehen Unternehmen, gerade bei hohen Produktions- und Lohnkosten, unter Druck, ihre Energiekosten so gering wie möglich zu halten. Oft stehen sie hinter den Personalkosten ganz oben auf der Ausgabenseite.</p><p>Sie möchten Zeit, Geld und Personal gewinnbringend einsetzen statt in Tarifvergleiche? Sie möchten einen Beitrag zum Klimaschutz leisten und Naturstrom beziehen? Wir übernehmen den Einkauf – vom Lastgang bis zur Unterschrift.</p>'))
    body += sec(f'<div class="sec-head"><h2 class="split">Wann kaufen? Drei Modelle im Vergleich.</h2><p class="reveal">Wählen Sie ein Modell und sehen Sie, wie es auf denselben Marktverlauf reagiert. Welches zu Ihnen passt, hängt von Ihrem Verbrauchsprofil und Ihrer Risikobereitschaft ab.</p></div>{tool}', 'gray', 'werkzeug')
    body += sec(two('Marktbeobachtung inklusive.', '<p>Durch unsere langjährige Erfahrung in der Energiewirtschaft erkennen wir Trends und geben Ihnen frühzeitig Handlungsempfehlungen. Mit unseren Marktberichten sind Sie stets auf dem aktuellen Stand der Preisentwicklung – auch zwischen zwei Ausschreibungen.</p>' + ticks(['Analyse Ihres Lastgangs und Ihrer Verbrauchsstruktur', 'Bündelung mehrerer Standorte zu einer Ausschreibung', 'Ausschreibung und Angebotsvergleich', 'Vertragsprüfung vor Unterzeichnung', 'Laufende Marktberichte und Handlungsempfehlungen'])))
    body += more('energiebeschaffung.html') + cta('Wann läuft Ihr Liefervertrag aus?', 'Je früher wir den Markt beobachten, desto mehr Spielraum bleibt beim Einkauf.', 'Ausschreibung anfragen', 'kontakt.html?thema=beschaffung')
    return body


def p_vertrag():
    tool = '''
<div class="frist reveal" data-frist>
  <div class="frist-in">
    <label class="fi-l" for="fr-end">Ihr Vertrag endet am</label><input id="fr-end" type="date" name="ende">
    <fieldset><legend>Kündigungsfrist laut Vertrag</legend><div class="chips">''' + ''.join(f'<button type="button" class="chip{" on" if v == 3 else ""}" data-v="{v}" aria-pressed="{"true" if v == 3 else "false"}">{l}</button>' for v, l in [(1, '1 Monat'), (3, '3 Monate'), (6, '6 Monate'), (12, '12 Monate')]) + '''</div></fieldset>
  </div>
  <ol class="frist-out" aria-live="polite">
    <li><span class="fo-l">Marktbeobachtung beginnen</span><b id="fr-a">–</b><span class="fo-n" id="fr-an"></span></li>
    <li><span class="fo-l">Ausschreibung abschließen</span><b id="fr-b">–</b><span class="fo-n" id="fr-bn"></span></li>
    <li class="hard"><span class="fo-l">Kündigung muss beim Versorger sein</span><b id="fr-c">–</b><span class="fo-n" id="fr-cn"></span></li>
  </ol>
  <p class="note">Die Kündigungsfrist ist verbindlich. Die beiden anderen Termine sind unsere Richtwerte: zwölf Monate Marktbeobachtung und vier Wochen Puffer vor Fristende. Maßgeblich ist immer Ihr Vertragstext.</p>
</div>'''
    body = ph('Vertragsmanagement', 'Wir legen Ihre Energielieferverträge auf Ihre Verbrauchsstruktur aus, prüfen alle Verträge und behalten Laufzeiten und Kündigungsfristen für Sie im Auge.', 'vertrag',
              ['Optimale Vertragsbedingungen schon in der Ausschreibung', 'Kein Risiko bei Produktionsschwankungen oder Kurzarbeit', 'Bestehende Verträge auf Potenzial geprüft'], 'Vertragsmanagement')
    body += sec(f'<div class="sec-head"><h2 class="split">Drei Termine, die Sie kennen sollten.</h2><p class="reveal">Tragen Sie das Vertragsende ein. Der Rechner zeigt, bis wann gekündigt sein muss und wann die Vorbereitung beginnen sollte.</p></div>{tool}', 'gray', 'werkzeug')
    body += sec(two('Das Kleingedruckte ist der teure Teil.', '<p>Mengentoleranzen, Pönalregelungen, automatische Verlängerungen: In Energielieferverträgen stecken Klauseln, die erst dann auffallen, wenn die Produktion schwankt. Wir minimieren die Risiken Ihrer Energiekosten bei Produktionsschwankungen oder Kurzarbeit und schließen Mengenbeschränkungen mit den damit verbundenen Pönalen aus.</p><p>Ebenso nehmen wir Ihre bereits abgeschlossenen Verträge genau unter die Lupe und decken Optimierungspotenziale auf.</p>' + ticks(['Vertragsbedingungen passend zu Ihrem Verbrauchsverhalten vorgeben', 'Verträge vor Unterzeichnung kontrollieren', 'Laufzeiten und Kündigungsfristen überwachen', 'Mengentoleranzen und Pönalen prüfen', 'Kommunikation mit Ihrem Versorger'])))
    body += more('vertragsmanagement.html') + cta('Auch Ihre Verträge sind bei uns in guten Händen.', 'Schicken Sie uns Ihren aktuellen Liefervertrag, wir prüfen ihn auf Fristen und Risiken.', 'Vertrag prüfen lassen', 'kontakt.html?thema=vertrag')
    return body


INVOICE_INFO = [
    ('Arbeitspreis Energie', 'Menge × Preis je kWh', 'Der eigentliche Energiepreis. Wir prüfen, ob der vereinbarte Preis angesetzt ist und ob die abgerechnete Menge zu den Zählerständen passt.'),
    ('Grundpreis', 'pro Monat oder Jahr', 'Fester Betrag je Abnahmestelle. Stimmt er mit dem Vertrag überein, und ist er nur einmal je Zähler berechnet?'),
    ('Netzentgelt Arbeitspreis', 'Menge × Netzentgelt je kWh', 'Die Gebühr des Netzbetreibers für den Transport. Sie hängt vom Preisblatt und der Jahresbenutzungsdauer ab – eine häufige Fehlerquelle.'),
    ('Netzentgelt Leistungspreis', 'Jahreshöchstleistung × € je kW', 'Bei leistungsgemessenen Kunden zählt die höchste Viertelstunde des Jahres. Wir prüfen den Wert und ob Sonderformen wie die atypische Netznutzung in Frage kommen.'),
    ('Messstellenbetrieb', 'pro Zähler und Jahr', 'Kosten für Zähler und Messung. Wir prüfen, ob Messstellen doppelt oder für stillgelegte Zähler berechnet werden.'),
    ('Konzessionsabgabe', 'Menge × Satz je kWh', 'Abgabe an die Gemeinde für die Nutzung öffentlicher Wege. Für Sondervertragskunden gilt ein niedriger Höchstsatz – ist er richtig angesetzt?'),
    ('KWKG-Umlage', 'Menge × Umlagesatz', 'Förderung der Kraft-Wärme-Kopplung. Stromkostenintensive Unternehmen können sie über die Besondere Ausgleichsregelung begrenzen.'),
    ('Offshore-Netzumlage', 'Menge × Umlagesatz', 'Finanziert die Anbindung von Offshore-Windparks. Begrenzung wie bei der KWKG-Umlage möglich.'),
    ('Aufschlag besondere Netznutzung', 'Menge × Aufschlag', 'Früher § 19-StromNEV-Umlage. Wir prüfen, ob der richtige Satz für Ihre Verbrauchsmenge angesetzt ist.'),
    ('Stromsteuer', 'Menge × Steuersatz', 'Unternehmen des Produzierenden Gewerbes und der Land- und Forstwirtschaft können eine Entlastung beantragen. Das übernimmt unser Antragsmanagement.'),
    ('Umsatzsteuer', '19 % auf die Nettosumme', 'Zum Schluss prüfen wir die Summenbildung und die Umsatzsteuer – und ob Abschläge und Gutschriften richtig verrechnet sind.'),
]


def p_rechnung():
    rows = ''.join(f'''<li class="iv-row"><button type="button" aria-expanded="false" aria-controls="iv-{i}"><span class="iv-n">{n}</span><span class="iv-f">{f}</span><span class="iv-plus" aria-hidden="true"></span></button><div class="iv-info" id="iv-{i}" hidden><p>{t}</p></div></li>''' for i, (n, f, t) in enumerate(INVOICE_INFO))
    tool = f'''
<div class="invoice reveal" data-invoice>
  <div class="iv-head"><div><b>Energierechnung</b><span>Muster, Abnahmestelle Gewerbe, Strom</span></div><div class="iv-logo" aria-hidden="true">{MARK}</div></div>
  <ul class="iv-list">{rows}</ul>
  <div class="iv-foot"><span>Summe</span><span class="iv-hint">Tippen Sie auf eine Position</span></div>
</div>'''
    body = ph('Rechnungsprüfung', 'Wir prüfen Ihre Verbrauchsabrechnungen, übernehmen das Clearing mit Ihrem Energieversorger und sorgen für eine stets korrekte Rechnungsstellung.', 'netz',
              ['Jede Position gegen Vertrag und Preisblatt', 'Clearing mit dem Versorger übernommen', 'Abrechnungen verständlich aufbereitet'], 'Rechnungsprüfung')
    body += sec(f'<div class="inv-grid"><div class="sec-head left"><h2 class="split">Elf Zeilen, elf mögliche Fehler.</h2><p class="reveal">So ist eine Stromrechnung für Gewerbekunden aufgebaut. Tippen Sie auf eine Position: Sie sehen, wie sie berechnet wird und was wir daran prüfen.</p><p class="note reveal">Musterrechnung ohne Beträge. Aufbau und Bezeichnungen können je nach Versorger abweichen.</p></div>{tool}</div>', 'gray', 'werkzeug')
    body += sec(two('Prüfen kostet Zeit. Nicht prüfen kostet Geld.', '<p>Durch gesetzliche Vorschriften, mengenabhängige Sätze der Abgaben und Umlagen sowie die Komplexität der Netznutzungsentgelte ist eine Prüfung der Rechnung sehr zeitintensiv und setzt ein großes Maß an energiewirtschaftlichem Hintergrundwissen voraus.</p><p>Damit bei Ihnen ausschließlich Ihr Produkt im Vordergrund steht, prüfen wir Ihre Verbrauchsabrechnungen, geben sie frei und bereiten sie verständlich und nachvollziehbar für Sie auf.</p>'))
    body += more('rechnungspruefung.html') + cta('Legen Sie uns Ihre letzte Rechnung hin.', 'Ein PDF oder ein Foto der Rechnung genügt für den ersten Blick.', 'Rechnung senden', 'kontakt.html?thema=rechnung')
    return body


def p_antrag():
    tool = '''
<div class="matrix reveal" data-matrix>
  <div class="mx-ctl">
    <fieldset><legend>Ihr Unternehmen gehört zu</legend><div class="chips" data-g="art">
      <button type="button" class="chip on" data-v="pg" aria-pressed="true">Produzierendes Gewerbe</button><button type="button" class="chip" data-v="luf" aria-pressed="false">Land- und Forstwirtschaft</button><button type="button" class="chip" data-v="dl" aria-pressed="false">Handel, Dienstleistung, Sonstiges</button></div></fieldset>
    <fieldset><legend>Sie beziehen (mehrere möglich)</legend><div class="chips multi" data-g="traeger">
      <button type="button" class="chip on" data-v="strom" aria-pressed="true">Strom</button><button type="button" class="chip" data-v="gas" aria-pressed="false">Erdgas</button><button type="button" class="chip" data-v="oel" aria-pressed="false">Heizöl</button></div></fieldset>
    <fieldset><legend>Besonderheiten</legend><div class="chips multi" data-g="extra">
      <button type="button" class="chip" data-v="intensiv" aria-pressed="false">Sehr hoher Stromverbrauch</button><button type="button" class="chip" data-v="prozess" aria-pressed="false">Energieintensive Prozesse (z. B. Metall, Glas, Keramik, Elektrolyse)</button></div></fieldset>
  </div>
  <div class="mx-out" aria-live="polite">
    <p class="mx-count"><b id="mx-n">1</b> mögliche Entlastung</p>
    <ul class="mx-list">
      <li data-if="strom" data-art="pg luf"><b>Stromsteuer-Entlastung (§ 9b StromStG)</b><span>Für betrieblich genutzten Strom. Seit 2026 bis auf den EU-Mindestsatz von 0,05 ct/kWh. Antrag beim Hauptzollamt.</span><i>Frist: 31.12. des Folgejahres</i></li>
      <li data-if="strom prozess" data-art="pg"><b>Steuerbefreiung für bestimmte Prozesse (§ 9a StromStG)</b><span>Elektrolyse, Glas, Keramik, Metallerzeugung und -bearbeitung, chemische Reduktion.</span><i>Frist: 31.12. des Folgejahres</i></li>
      <li data-if="gas" data-art="pg luf"><b>Energiesteuer-Entlastung für Erdgas (§ 54 EnergieStG)</b><span>Für Erdgas, das zu betrieblichen Zwecken verheizt wird.</span><i>Frist: 31.12. des Folgejahres</i></li>
      <li data-if="oel" data-art="pg luf"><b>Energiesteuer-Entlastung für Heizöl (§ 54 EnergieStG)</b><span>Für leichtes Heizöl zu betrieblichen Heizzwecken.</span><i>Frist: 31.12. des Folgejahres</i></li>
      <li data-if="gas prozess" data-art="pg"><b>Entlastung für bestimmte Prozesse (§ 51 EnergieStG)</b><span>Energieerzeugnisse für Metallherstellung, Glas, Keramik, chemische Reduktion und vergleichbare Verfahren.</span><i>Frist: 31.12. des Folgejahres</i></li>
      <li data-if="strom intensiv" data-art="pg dl luf"><b>Besondere Ausgleichsregelung (EnFG)</b><span>Begrenzung von KWKG- und Offshore-Netzumlage für stromkostenintensive Unternehmen. Antrag beim BAFA, Voraussetzungen im Einzelfall.</span><i>Frist: 30.06. für das Folgejahr</i></li>
      <li data-if="strom intensiv" data-art="pg dl luf"><b>Individuelle Netzentgelte (§ 19 StromNEV)</b><span>Bei atypischer Netznutzung oder sehr gleichmäßigem, hohem Verbrauch. Vereinbarung mit dem Netzbetreiber.</span><i>Frist: Anzeige bei der Bundesnetzagentur</i></li>
    </ul>
    <p class="mx-empty" hidden>Für diese Auswahl gibt es keine pauschale Entlastung. Wir prüfen trotzdem: Oft stecken Einsparungen in Netzentgelt, Vertrag oder Rechnung.</p>
  </div>
  <p class="note">Stand September 2026, vereinfachte Übersicht ohne Gewähr. Ob Sie die Voraussetzungen erfüllen, prüfen wir im Einzelfall. Der frühere Spitzenausgleich ist Ende 2023 ausgelaufen.</p>
</div>'''
    body = ph('Antragsmanagement', 'Auch bei den Steuern, Abgaben und Umlagen auf Strom und Erdgas liegt großes Potenzial. Wir holen bereits gezahlte Energiesteuern für Sie zurück.', 'steuern',
              ['Analyse aller Entlastungsmöglichkeiten', 'Unterlagen vorbereitet, Antrag gestellt', 'Erstattung geprüft, Fristen eingehalten'], 'Antragsmanagement')
    body += sec(f'<div class="sec-head"><h2 class="split">Welche Entlastung kommt für Sie in Frage?</h2><p class="reveal">Wählen Sie Branche und Energieträger. Die Matrix zeigt, welche Anträge grundsätzlich möglich sind – und bis wann sie gestellt sein müssen.</p></div>{tool}', 'gray', 'werkzeug')
    body += sec(two('Wir machen die Arbeit mit dem Hauptzollamt.', '<p>Durch die Analyse Ihrer Potenziale helfen wir Ihnen, bisher nicht genutzte Möglichkeiten auszuschöpfen, und arbeiten damit gegen den stetigen Anstieg der Energiekosten.</p>' + ticks(['Analyse der Voraussetzungen für alle Steuern, Abgaben und Umlagen', 'Vorbereitung der notwendigen Unterlagen', 'Antragsstellung bei der zuständigen Behörde', 'Prüfung der erhaltenen Erstattung', 'Einhaltung der gesetzlichen Fristen']) + '<p>Detaillierte Informationen zu den aktuellen Umlagen finden Sie bei den Übertragungsnetzbetreibern unter <a href="https://www.netztransparenz.de" rel="noopener" target="_blank">netztransparenz.de</a>.</p>'))
    body += more('antragsmanagement.html') + cta('Haben Sie die Entlastung für das Vorjahr schon beantragt?', 'Die Frist läuft bis zum 31. Dezember. Wir prüfen, was Ihnen zusteht.', 'Anträge prüfen lassen', 'kontakt.html?thema=antrag')
    return body


def p_effizienz():
    tool = '''
<div class="pflicht reveal" data-pflicht>
  <div class="pf-in">
    <fieldset><legend>Gesamtendenergieverbrauch pro Jahr (Durchschnitt der letzten drei Jahre, alle Energieträger)</legend>
      <div class="chips">''' + ''.join(f'<button type="button" class="chip{" on" if v == 3000 else ""}" data-v="{v}" aria-pressed="{"true" if v == 3000 else "false"}">{l}</button>' for v, l in [(800, 'unter 1 GWh'), (3000, '2,5 bis 7,5 GWh'), (9000, 'über 7,5 GWh')]) + '''</div>
      <label class="own">oder genau <input type="text" inputmode="numeric" name="mwh" placeholder="z. B. 4200" autocomplete="off"> MWh</label></fieldset>
    <fieldset><legend>Unternehmensgröße</legend><div class="chips" data-g="kmu"><button type="button" class="chip on" data-v="kmu" aria-pressed="true">KMU</button><button type="button" class="chip" data-v="gross" aria-pressed="false">kein KMU (ab 250 Beschäftigte oder über 50 Mio. € Umsatz)</button></div></fieldset>
  </div>
  <div class="pf-out" aria-live="polite">
    <div class="pf-gauge" aria-hidden="true"><span class="pf-mark m1" style="--p:25%">2,5 GWh</span><span class="pf-mark m2" style="--p:75%">7,5 GWh</span><span class="pf-fill"></span></div>
    <ul class="pf-list">
      <li data-p="ems"><b>Energie- oder Umweltmanagementsystem</b><span>ISO 50001 oder EMAS einführen (§ 8 EnEfG).</span></li>
      <li data-p="plan"><b>Umsetzungspläne veröffentlichen</b><span>Wirtschaftliche Effizienzmaßnahmen erfassen, bestätigen lassen und veröffentlichen (§ 9 EnEfG).</span></li>
      <li data-p="abw"><b>Abwärme melden</b><span>Angaben zur Abwärme an die Plattform für Abwärme übermitteln (§ 17 EnEfG).</span></li>
      <li data-p="audit"><b>Energieaudit alle vier Jahre</b><span>Nach DIN EN 16247-1, Pflicht für Nicht-KMU (EDL-G), entfällt mit Managementsystem.</span></li>
      <li data-p="frei"><b>Keine gesetzliche Pflicht</b><span>Eine freiwillige Energieberatung lohnt sich trotzdem und ist oft förderfähig.</span></li>
    </ul>
  </div>
  <p class="note">Vereinfachte Übersicht, Stand September 2026. Die Schwellen können sich mit der Umsetzung der EU-Energieeffizienzrichtlinie ändern. Wir prüfen Ihre Pflichten im Einzelfall.</p>
</div>'''
    offer = ['Energetische Beleuchtungsoptimierung', 'Reduzierung von Lastspitzen und Grundlast', 'Planung und Austausch von Wärme- und Kälteanlagen', 'Planung von Blockheizkraftwerken', 'Optimierung Ihrer Druckluftanlage', 'Messkonzepte und Software',
             'Analyse Ihrer Pumpen und deren Regelung', 'Messung auf der Strom- und Fluidseite (Durchflüsse, Temperaturen, Drücke)', 'Analyse der Raumlufttechnik', 'Eigenstromerzeugung', 'Visualisierung und Steuerung des Verbrauchsverhaltens', 'Organisation von Energieeffizienz-Netzwerken', 'Einführung eines Energiemanagementsystems nach ISO 50001', 'Energieaudit nach DIN EN 16247-1']
    body = ph('Energieeffizienz', 'Wir untersuchen Ihr Unternehmen in allen Teilbereichen auf Energieeffizienz, decken gemeinsam mit Ihnen Potenziale auf und setzen sie wirtschaftlich sinnvoll um – ohne Störung Ihrer Produktion.', 'menge',
              ['Geprüfte Energiemanager', 'Energieaudit und ISO 50001', 'Förderungen und Zuschüsse genutzt'], 'Energieeffizienz')
    body += sec(f'<div class="sec-head"><h2 class="split">Welche Pflichten gelten für Ihr Unternehmen?</h2><p class="reveal">Das Energieeffizienzgesetz knüpft seine Pflichten an den Verbrauch. Wählen Sie Ihre Größenordnung und sehen Sie, was auf Sie zukommt.</p></div>{tool}', 'gray', 'werkzeug')
    body += sec(two('Unser Effizienzangebot für Sie.', '<p>Wir bieten Ihnen die gesamte Palette der Energieeffizienz durch geprüfte Energiemanager und dazu alle Möglichkeiten, Förderungen und Zuschüsse für Effizienzmaßnahmen zu nutzen. Auch unsere Energieeffizienz-Netzwerke für Kommunen und Industrie bieten Ihnen viele Vorteile.</p>' + f'<ul class="cols">{"".join(f"<li>{x}</li>" for x in offer)}</ul>'))
    body += sec(two('Energieausweise für Gewerbe und Wohnen.', '<p>Ist Ihr Haus oder Ihr Gewerbeobjekt ein Energiefresser oder ein Energiesparer? Das zeigt der Energieausweis auf einen Blick. Verpflichtend ist er bei Verkauf oder Vermietung einer Immobilie, hilfreich beim Kauf und bei der Sanierung: Er liefert Hinweise auf Einsparpotenziale und konkrete Vorschläge für Sanierungsmaßnahmen.</p><p><a class="link" href="kontakt.html?thema=ausweis">Energieausweis anfragen ' + ARROW + '</a></p>'), 'tight')
    body += more('energieeffizienz.html') + cta('Wo verliert Ihr Betrieb Energie?', 'Wir beginnen mit einer Begehung und Ihren Verbrauchsdaten – danach wissen Sie, welche Maßnahme sich rechnet.', 'Effizienz-Check anfragen', 'kontakt.html?thema=effizienz')
    return body


def p_contracting():
    crit = [('liq', 'Keine Investition aus eigener Liquidität', 'c'), ('wart', 'Wartung und Reparaturen inklusive', 'c'), ('not', '24-Stunden-Notdienst an 365 Tagen', 'c'), ('fix', 'Fest kalkulierbare monatliche Kosten', 'c'),
            ('own', 'Anlage gehört sofort mir', 'e'), ('rate', 'Keine laufende monatliche Rate', 'e'), ('bil', 'Anlage in der eigenen Bilanz', 'e')]
    tool = f'''
<div class="waage reveal" data-waage>
  <div class="wg-fig" aria-hidden="true">
    <svg viewBox="0 0 600 300"><path class="wg-post" d="M300,110 V270 M240,270 H360"/><g class="wg-beam"><path class="wg-bar" d="M80,110 H520"/><circle cx="300" cy="110" r="9" class="wg-hub"/>
      <g class="wg-pan l"><path d="M80,110 V160"/><path class="pan" d="M30,160 H130 L112,186 H48 Z"/><text x="80" y="214">Eigene Anlage</text></g>
      <g class="wg-pan r"><path d="M520,110 V160"/><path class="pan" d="M470,160 H570 L552,186 H488 Z"/><text x="520" y="214">Contracting</text></g></g></svg>
  </div>
  <fieldset class="wg-ctl"><legend>Was ist Ihnen wichtig?</legend>{''.join(f'<label class="wg-c"><input type="checkbox" value="{k}" data-side="{s}"><span>{t}</span></label>' for k, t, s in crit)}</fieldset>
  <p class="wg-out" aria-live="polite">Wählen Sie aus, was Ihnen wichtig ist.</p>
</div>'''
    body = ph('Anlagen-Contracting', 'Ob Heizungsanlage, BHKW, Druckluftkompressor, PV-Anlage, Kälteanlage oder Warmwasserspeicher: Wir übernehmen Planung, Investition und Installation einer neuen, klimaschonenden Anlage.', 'menge',
              ['Modernste Technik ohne eigene Investition', '15 Jahre Vollgarantie auf die verbaute Technik', 'Keine Bindung an einen Energieversorger'], 'Anlagen-Contracting')
    body += sec(f'<div class="sec-head"><h2 class="split">Kaufen oder Contracting?</h2><p class="reveal">Beide Wege sind richtig – für unterschiedliche Unternehmen. Kreuzen Sie an, was Ihnen wichtig ist, und sehen Sie, wohin die Waage kippt.</p></div>{tool}', 'gray', 'werkzeug')
    body += sec(two('Unser Angebot.', ticks(['Übernahme der gesamten Planung, Investition und Installation', 'Modernste Technik ohne eigene Investition', 'Umsetzung mit Ihrem Wunsch-Fachhandwerker oder unseren Profi-Partnern aus ganz Deutschland', '15 Jahre Vollgarantie auf die verbaute Technik', 'Fest kalkulierbare Nebenkosten', 'Alle Wartungen und Reparaturen inklusive', '24-Stunden-Notdienst an 365 Tagen im Jahr', 'Keine Bindung an einen Energieversorger', 'Überschaubare monatliche Raten', 'Für Ihren privaten Haushalt oder Ihr Gewerbe'])))
    body += more('anlagen-contracting.html') + cta('Steht bei Ihnen eine Anlage zur Erneuerung an?', 'Wir rechnen Kauf und Contracting für Ihren Fall nebeneinander.', 'Contracting anfragen', 'kontakt.html?thema=contracting')
    return body


def p_immo():
    tool = '''
<div class="bundle reveal" data-bundle>
  <div class="bd-ctl" role="group" aria-label="Liegenschaft hinzufügen">
    <button type="button" class="chip" data-t="mfh">+ Mehrfamilienhaus</button><button type="button" class="chip" data-t="anl">+ Wohnanlage</button><button type="button" class="chip" data-t="weg">+ Eigentümergemeinschaft</button><button type="button" class="chip" data-t="gew">+ Gewerbeeinheit</button><button type="button" class="chip ghost" data-reset>Zurücksetzen</button>
  </div>
  <div class="bd-stage">
    <div class="bd-before"><p class="bd-h">Ohne Bündelung</p><ul class="bd-houses" aria-live="polite"></ul><p class="bd-sum"><b id="bd-n">0</b> Verträge, <b id="bd-f">0</b> Fristen, <b id="bd-r">0</b> Rechnungsläufe</p></div>
    <div class="bd-arrow" aria-hidden="true">''' + ARROW + '''</div>
    <div class="bd-after"><p class="bd-h">Mit Warin Energie</p><div class="bd-one"><span class="bd-bolt">''' + BOLT + '''</span><b>1 Ausschreibung</b><span id="bd-one-t">Fügen Sie Liegenschaften hinzu</span></div></div>
  </div>
</div>'''
    offer = ['Beschaffung von Strom und Erdgas zu bestmöglichen Marktpreisen', 'Abschluss nur bei zuverlässigen Energieversorgungsunternehmen', 'Bündelung der Energieverbräuche Ihrer Immobilien', 'Ausschreibung und Abschluss in enger Absprache mit Ihnen', 'Anlagen-Contracting für neue Heizungsanlagen und Blockheizkraftwerke', 'Vertragsmanagement', 'Rechnungsprüfung', 'Kommunikation mit Ihrem Energieversorger', 'Kontinuierliche Marktbeobachtung', 'Wirtschaftlichkeitsberechnung bestehender Anlagen und Verträge', 'Informationen über gesetzliche Änderungen']
    body = ph('Immobilienwirtschaft', 'Um die steigenden Nebenkosten für Mehrfamilienhäuser, Wohnanlagen und Eigentümergemeinschaften abzufangen, bieten wir einen besonderen Service für Verwalter und Eigentümer.', 'preis',
              ['Wirtschaftlichkeitsgebot sicher eingehalten', 'Niedrige Nebenkosten für Ihre Mieter', 'Alle Liegenschaften in einer Hand'], 'Immobilienwirtschaft')
    body += sec(f'<div class="sec-head"><h2 class="split">Aus vielen Verträgen wird einer.</h2><p class="reveal">Fügen Sie Ihre Liegenschaften hinzu. Links sehen Sie, was Sie heute einzeln verwalten, rechts, was davon bei uns übrig bleibt.</p></div>{tool}', 'gray', 'werkzeug')
    body += sec(two('Unser Angebot für Verwaltungen.', '<p>Mit uns gewährleisten Sie stets die Einhaltung des Wirtschaftlichkeitsgebots und sorgen für niedrige Nebenkosten.</p>' + f'<ul class="cols">{"".join(f"<li>{x}</li>" for x in offer)}</ul>'))
    body += more('immobilienwirtschaft.html') + cta('Wie viele Abnahmestellen verwalten Sie?', 'Schicken Sie uns eine Liste der Liegenschaften, wir melden uns mit einem Vorschlag zur Bündelung.', 'Bündelung anfragen', 'kontakt.html?thema=immobilien')
    return body


def p_mitarbeiter():
    views = {
        'u': ('Für das Unternehmen', ['Kostenlose Form der Mitarbeiterbindung', 'Keine Kosten, keine Verwaltung', 'Die Aktion ist einfach zu starten und läuft danach automatisch', 'Ein echter Mehrwert, der in jedem Haushalt ankommt']),
        'm': ('Für die Mitarbeitenden', ['Strom- und Gastarife zu sehr guten Konditionen', 'Wirkt wie eine Nettolohnerhöhung, ohne großen Aufwand', 'In Zusammenarbeit mit namhaften Energieversorgern', 'Freiwillig: Jede und jeder entscheidet selbst']),
    }
    tool = f'''
<div class="persp reveal" data-persp>
  <div class="ps-ctl" role="tablist" aria-label="Perspektive">{''.join(f'<button type="button" role="tab" id="ps-t-{k}" aria-controls="ps-{k}" aria-selected="{"true" if k == "u" else "false"}" class="ps-tab{" on" if k == "u" else ""}" data-v="{k}">{t}</button>' for k, (t, _) in views.items())}<span class="ps-ind" aria-hidden="true"></span></div>
  {''.join(f'<div class="ps-panel" role="tabpanel" id="ps-{k}" aria-labelledby="ps-t-{k}"{"" if k == "u" else " hidden"}><ul>{"".join(f"<li>{x}</li>" for x in items)}</ul></div>' for k, (t, items) in views.items())}
</div>'''
    flow = [('Aktion starten', 'Wir stimmen mit Ihnen ab, wie die Belegschaft informiert wird – Aushang, Intranet oder Infoveranstaltung.'),
            ('Tarif wählen', 'Ihre Mitarbeitenden vergleichen die Angebote und wechseln, wenn es sich für sie lohnt.'),
            ('Läuft von selbst', 'Wechsel, Kündigung beim alten Versorger und Abrechnung laufen direkt zwischen Versorger und Haushalt.')]
    body = ph('Mitarbeiter-Tarife', 'Wir bieten nicht nur eine Energiekostenoptimierung für Ihr Unternehmen an, sondern auch für Ihre Mitarbeitenden – als Incentive-Modell ohne Kosten für Sie.', 'preis',
              ['Kein Aufwand für die Personalabteilung', 'Tarife namhafter Versorger', 'Für die privaten Haushalte aller Mitarbeitenden'], 'Mitarbeiter-Tarife')
    body += sec(f'<div class="sec-head"><h2 class="split">Zwei Seiten, ein Gewinn.</h2><p class="reveal">Wechseln Sie die Perspektive.</p></div>{tool}', 'gray', 'werkzeug')
    fl = ''.join(f'<li class="reveal"><b>{h}</b><p>{t}</p></li>' for h, t in flow)
    body += sec(f'<div class="sec-head left"><h2 class="split">So kommt der Tarif in die Haushalte.</h2></div><ol class="flow">{fl}</ol>')
    body += more('mitarbeiter-tarife.html') + cta('Das Allerbeste daran: Dem Unternehmen entstehen keine Kosten.', 'Sprechen Sie uns an, wir stellen Ihnen das Modell in einem kurzen Termin vor.', 'Modell vorstellen lassen', 'kontakt.html?thema=mitarbeiter')
    return body


# ============================ WEITERE SEITEN ============================
def p_referenzen():
    wall = ''.join(f'<li class="lw">{logo_img(k, n, w, h)}</li>' for k, n, w, h in sorted(LOGOS, key=lambda x: x[1].lower()))
    body = ph('Referenzen', f'Ein Auszug der Unternehmen, die uns ihre Energiekosten anvertrauen: {len(LOGOS)} Namen von der Klinik über den Maschinenbau bis zur Hausverwaltung.', crumbs='Referenzen')
    body += sec(f'<ul class="logo-wall">{wall}</ul>', 'tight')
    body += sec(two('Erfahrung aus nahezu allen Branchen.', '<p>Unsere Erfahrungen stammen aus einer Vielzahl an Projekten in produzierenden und gewerblichen Betrieben, zum Beispiel in Automotive, CNC-Fertigung, Lebensmittel, Medizintechnik, Gesundheit, Gießereien, Papier, Verpackungen, Abfallwirtschaft und Immobilienwirtschaft.</p><p>Jede Branche hat ihr eigenes Lastprofil – und damit ihre eigenen Hebel. Deshalb beginnen wir immer mit Ihren Zahlen und nicht mit einem Standardangebot.</p>'), 'gray')
    return body + cta('Werden Sie die nächste Referenz.', 'Sprechen Sie uns an. Eine aktuelle Rechnung genügt für den Anfang.', 'Anfrage senden', 'kontakt.html')


def p_unternehmen():
    team = f'''<div class="team">
  <figure class="tm main reveal"><img src="img/christoph-warin.webp" width="292" height="350" alt="Christoph Warin" loading="lazy" decoding="async"><figcaption><b>Christoph Warin</b><span>Geschäftsführender Gesellschafter</span><span>Energiemanager für die Industrie</span><a href="tel:{CO['telh']}">{CO['tel']}</a><a href="mailto:{CO['mail']}">{CO['mail']}</a></figcaption></figure>
  <figure class="tm reveal"><span class="mono" aria-hidden="true">IF</span><figcaption><b>Ioanna Frangouli-Warin</b><span>Backoffice</span><a href="mailto:{CO['office']}">{CO['office']}</a></figcaption></figure>
  <figure class="tm reveal"><span class="mono" aria-hidden="true">EM</span><figcaption><b>Elisabeth Mystakidis</b><span>Backoffice</span><a href="mailto:{CO['office']}">{CO['office']}</a></figcaption></figure>
</div>'''
    body = ph('Unternehmen', 'Wir sind ein unabhängiges Unternehmen mit Sitz in Eschweiler und begleiten Sie in allen energierelevanten Aufgaben: Energieeinkauf, Energieeffizienz und Energiemanagement.', crumbs='Unternehmen')
    body += sec(two('Alles aus einer Hand.', '<p>Unser Know-how und die jahrelange Erfahrung in der Energiewirtschaft und in Unternehmen aller Branchen machen uns zu einem kompetenten Partner in allen energierelevanten Fragen, Herausforderungen und Situationen.</p><p>Das Wissen und die praktische Erfahrung im Bereich der Energieeffizienz runden unsere Beratung ab und liefern Ihnen die bestmöglichen Lösungen für den bewussten Umgang mit allen Energiearten. Dazu kommt unser Netzwerk mit Fachleuten aus allen Bereichen der Energieeffizienz und der Technik.</p><p>Wir betrachten die Gesamtheit eines Unternehmens – von der Beeinflussung des Energiepreises bis zur ganzen Bandbreite der Energieeffizienz. So können sich unsere Kunden voll und ganz ihren Kernaufgaben widmen: ihrer Produktion und dem Vertrieb ihrer Produkte.</p>'))
    body += sec(f'<div class="sec-head left"><h2 class="split">Ihre Ansprechpartner.</h2></div>{team}', 'gray')
    body += sec(two('Warum Unternehmen mit uns arbeiten.', ticks(['Ein hohes Maß an Fachkompetenz und Beratungsqualität', 'Energiekosten dauerhaft gesenkt statt einmalig verhandelt', 'Unabhängig von einzelnen Energieversorgern', 'Ein Ansprechpartner für Einkauf, Verträge, Rechnungen, Anträge und Effizienz', 'Netzwerk aus Fachleuten für Technik und Effizienz']) + '<p><a class="link" href="partner.html">Unsere Partner ' + ARROW + '</a></p>'))
    return body + cta('Lernen wir uns kennen.', 'Rufen Sie an oder schreiben Sie uns – wir melden uns zeitnah.', 'Kontakt aufnehmen', 'kontakt.html')


def p_partner():
    lst = ''.join(f'<li class="pt reveal">{logo_img(k, n, w, h)}<b>{n}</b></li>' for k, n, w, h in PARTNERS)
    body = ph('Unsere Partner', 'Zu unserer Beratung gehört ein Netzwerk aus Fachleuten für Energieeffizienz, Technik und Immobilien. So bekommen Sie auch Spezialwissen aus einer Hand.', crumbs='Partner')
    body += sec(f'<ul class="partners">{lst}</ul>', 'tight')
    return body + cta('Sie brauchen einen Spezialisten?', 'Fragen Sie uns. Wenn wir es nicht selbst machen, kennen wir jemanden.', 'Anfrage senden', 'kontakt.html')


ARTICLES = [
    ('ratgeber-stromsteuer-2026.html', 'Stromsteuer 2026: Entlastung für das Produzierende Gewerbe', 'Seit 2026 können Betriebe des Produzierenden Gewerbes die Stromsteuer fast vollständig zurückholen. Wer berechtigt ist und welche Frist gilt.', 'steuern', [
        ('Worum es geht', '<p>Der Regelsatz der Stromsteuer beträgt 20,50 € je Megawattstunde, also 2,05 ct/kWh. Unternehmen des Produzierenden Gewerbes sowie der Land- und Forstwirtschaft können sich für betrieblich genutzten Strom auf den europäischen Mindeststeuersatz von 0,50 € je Megawattstunde entlasten lassen (§ 9b Stromsteuergesetz). Was 2024 und 2025 befristet galt, ist seit dem 1. Januar 2026 dauerhaft geregelt.</p><p>Die Entlastung kommt nicht automatisch: Der Versorger berechnet zunächst den vollen Satz, die Differenz holen Sie sich per Antrag beim Hauptzollamt zurück.</p>'),
        ('Wer gehört zum Produzierenden Gewerbe?', '<p>Maßgeblich ist die Klassifikation der Wirtschaftszweige. Zum Produzierenden Gewerbe zählen Bergbau, das Verarbeitende Gewerbe, die Energie- und Wasserversorgung, die Abfallentsorgung und das Baugewerbe. Entscheidend ist der Schwerpunkt Ihres Unternehmens, nicht einzelne Tätigkeiten. Wer an der Grenze liegt, sollte die Einordnung vor dem Antrag prüfen lassen.</p>'),
        ('Welche Frist gilt?', '<p>Der Antrag ist spätestens bis zum 31. Dezember des Jahres zu stellen, das auf das Jahr der Stromentnahme folgt. Für Strom aus 2025 endet die Frist also am 31. Dezember 2026. Wer sie verpasst, verliert den Anspruch.</p>'),
        ('Was ist mit dem Spitzenausgleich?', '<p>Der frühere Spitzenausgleich nach § 10 Stromsteuergesetz ist Ende 2023 ausgelaufen. Verträge, Budgets oder Controlling-Vorlagen, die ihn noch einplanen, sollten angepasst werden.</p>'),
        ('So unterstützen wir Sie', '<p>Wir prüfen die Voraussetzungen, ermitteln die begünstigten Strommengen, bereiten die Anträge vor, reichen sie ein und kontrollieren die Erstattung. Auch Entlastungen bei der Energiesteuer für Erdgas und Heizöl nehmen wir gleich mit.</p><p class="note">Stand September 2026, ohne Gewähr. Maßgeblich sind die aktuellen Vorschriften und die Einzelfallprüfung.</p>')]),
    ('ratgeber-enefg-pflichten.html', 'Energieeffizienzgesetz: Wann ein Managementsystem Pflicht ist', 'Ab 2,5 und ab 7,5 Gigawattstunden Jahresverbrauch greifen neue Pflichten. Was das Energieeffizienzgesetz von Unternehmen verlangt.', 'menge', [
        ('Der Verbrauch entscheidet', '<p>Das Energieeffizienzgesetz (EnEfG) knüpft seine Pflichten an den durchschnittlichen Gesamtendenergieverbrauch der letzten drei abgeschlossenen Kalenderjahre – über alle Energieträger, also Strom, Gas, Öl und Kraftstoffe zusammen.</p>'),
        ('Ab 7,5 GWh: Managementsystem', '<p>Unternehmen mit mehr als 7,5 Gigawattstunden im Jahr müssen ein Energiemanagementsystem nach ISO 50001 oder ein Umweltmanagementsystem nach EMAS einrichten (§ 8 EnEfG). Dazu gehören unter anderem die Erfassung von Abwärme und die Bewertung von Effizienzmaßnahmen nach ihrer Wirtschaftlichkeit.</p>'),
        ('Ab 2,5 GWh: Umsetzungspläne', '<p>Schon ab 2,5 Gigawattstunden müssen Unternehmen für alle als wirtschaftlich erkannten Maßnahmen Umsetzungspläne erstellen, von unabhängiger Stelle bestätigen lassen und veröffentlichen (§ 9 EnEfG). Außerdem sind Angaben zur Abwärme an die Plattform für Abwärme zu übermitteln (§ 17 EnEfG).</p>'),
        ('Energieaudit für Nicht-KMU', '<p>Unabhängig davon gilt für Unternehmen, die kein KMU sind, die Pflicht zum Energieaudit nach DIN EN 16247-1 alle vier Jahre (Energiedienstleistungsgesetz). Wer ein Managementsystem betreibt, ist davon befreit.</p>'),
        ('Was sich noch ändern kann', '<p>Die EU-Energieeffizienzrichtlinie von 2023 stellt die Audit-Pflicht künftig von der Unternehmensgröße auf den Energieverbrauch um. Die deutschen Regeln werden daran angepasst. Wir behalten die Entwicklung für Sie im Blick und prüfen, welche Fassung für Ihr Unternehmen gilt.</p><p class="note">Stand September 2026, ohne Gewähr.</p>')]),
    ('ratgeber-liefervertrag.html', 'Energieliefervertrag: Fristen, Mengentoleranzen und Pönalen', 'Worauf Unternehmen bei Strom- und Gaslieferverträgen achten sollten, bevor sie unterschreiben – und bevor die Kündigungsfrist abläuft.', 'vertrag', [
        ('Vertragsende ist nicht Kündigungsfrist', '<p>Viele Gewerbeverträge verlängern sich automatisch, wenn nicht rechtzeitig gekündigt wird. Entscheidend ist nicht das Vertragsende, sondern der Tag, an dem die Kündigung spätestens beim Versorger eingegangen sein muss. Wer diesen Tag verpasst, bleibt oft ein weiteres Jahr zu den alten Konditionen gebunden.</p>'),
        ('Mengentoleranzen: das unterschätzte Risiko', '<p>Festpreisverträge gehen von einer prognostizierten Menge aus. Weicht Ihr Verbrauch stärker ab als das vereinbarte Band, werden Mehr- oder Mindermengen zu anderen Preisen abgerechnet oder mit Pönalen belegt. Bei Produktionsschwankungen, Kurzarbeit oder neuen Maschinen kann das teuer werden.</p>'),
        ('Welche Preisbestandteile sind fest?', '<p>„Festpreis“ bedeutet selten, dass die gesamte Rechnung feststeht. Meist ist nur der Energiepreis fixiert, während Netzentgelte, Umlagen und Steuern in ihrer jeweiligen Höhe weitergereicht werden. Prüfen Sie, welche Positionen der Versorger anpassen darf.</p>'),
        ('Unsere Empfehlung', '<p>Beginnen Sie etwa ein Jahr vor Vertragsende mit der Marktbeobachtung und schließen Sie die Ausschreibung mit etwas Puffer vor der Kündigungsfrist ab. Unser Fristen-Rechner auf der Seite <a href="vertragsmanagement.html">Vertragsmanagement</a> zeigt Ihnen die drei Termine.</p>')]),
]


def p_ratgeber():
    lst = ''.join(f'<li class="ra reveal"><a href="{f}"><span class="ra-k">{BOLT}{TERMS[k]}</span><h2>{t}</h2><p>{d}</p><span class="link">Weiterlesen {ARROW}</span></a></li>' for f, t, d, k, _ in ARTICLES)
    return ph('Ratgeber', 'Kurze Antworten auf Fragen, die uns Unternehmen oft stellen: zu Steuern, Pflichten und Verträgen rund um Energie.', crumbs='Ratgeber') + sec(f'<ul class="ra-list">{lst}</ul>', 'tight') + cta('Ihre Frage ist nicht dabei?', 'Rufen Sie an, wir antworten gern direkt.', 'Frage stellen', 'kontakt.html')


def p_article(a):
    f, t, d, k, parts = a
    toc = ''.join(f'<h2 class="split">{h}</h2><div class="prose reveal">{b}</div>' for h, b in parts)
    others = ''.join(f'<li><a href="{x[0]}">{x[1]}</a></li>' for x in ARTICLES if x[0] != f)
    body = ph(t, d, k, None, '<a href="ratgeber.html">Ratgeber</a>')
    body += f'<section class="sec"><div class="wrap article"><div class="art-body">{toc}</div><aside class="art-side"><p class="as-by"><b>Warin Energie GmbH</b><span>Stand: September 2026</span></p><p class="as-h">Weitere Artikel</p><ul>{others}</ul></aside></div></section>'
    return body + cta('Sollen wir das für Ihr Unternehmen prüfen?', 'Schildern Sie uns kurz Ihre Situation, wir melden uns.', 'Anfrage senden', 'kontakt.html')


FAQ = [
    ('Für wen arbeitet Warin Energie?', 'Für Unternehmen aus Produktion, Handwerk, Handel, Gesundheitswesen und Immobilienwirtschaft – vom Mittelständler bis zur Klinik. Energieausweise und Anlagen-Contracting bieten wir auch für private Haushalte an.'),
    ('Welche Unterlagen brauchen Sie für den Anfang?', 'Die letzten Jahresabrechnungen für Strom und Gas, den aktuellen Liefervertrag und, falls vorhanden, Ihren Lastgang. Für einen ersten Blick genügt oft schon eine einzige Rechnung.'),
    ('Muss ich dafür den Energieversorger wechseln?', 'Nein. Wir schreiben aus und vergleichen. Gewechselt wird nur, wenn es sich für Sie lohnt, und wir schließen nur bei zuverlässigen Versorgern ab.'),
    ('Was ist ein Lastgang?', 'Bei Kunden mit Leistungsmessung zeichnet der Zähler den Verbrauch in Viertelstunden auf. Diese Kurve zeigt, wann Sie wie viel Strom brauchen. Sie ist die Grundlage für einen passenden Einkauf und für das Kappen teurer Lastspitzen.'),
    ('Wer kann die Stromsteuer-Entlastung beantragen?', 'Unternehmen des Produzierenden Gewerbes sowie der Land- und Forstwirtschaft für betrieblich genutzten Strom. Der Antrag geht an das Hauptzollamt, die Frist endet am 31. Dezember des Folgejahres. Details stehen in unserem Ratgeber.'),
    ('Brauche ich ein Energieaudit oder ein Managementsystem?', 'Das hängt vom Energieverbrauch und von der Unternehmensgröße ab. Unser Pflichten-Check auf der Seite Energieeffizienz gibt eine erste Orientierung, die genaue Prüfung übernehmen wir.'),
    ('Was bedeutet Anlagen-Contracting?', 'Wir planen, finanzieren und installieren eine neue Anlage, zum Beispiel eine Heizung, ein BHKW oder einen Druckluftkompressor. Sie zahlen eine monatliche Rate, Wartung, Reparaturen und Notdienst sind enthalten.'),
    ('Arbeiten Sie nur in der Region?', 'Unser Sitz ist Eschweiler, viele Referenzen stammen aus der Region Aachen und Düren. Rechnungsprüfung, Anträge und Beschaffung erledigen wir ortsunabhängig, beim Contracting arbeiten wir mit Partnern aus ganz Deutschland.'),
    ('Was kostet die Beratung?', 'Das hängt von der Leistung ab. Die Konditionen besprechen wir mit Ihnen, bevor wir beginnen.'),
]


def p_faq():
    items = ''.join(f'<details class="qa reveal"><summary><span>{q}</span><i aria-hidden="true"></i></summary><div class="qa-a"><p>{a}</p></div></details>' for q, a in FAQ)
    return ph('Häufige Fragen', 'Was Unternehmen uns vor der Zusammenarbeit am häufigsten fragen.', crumbs='Häufige Fragen') + sec(f'<div class="faq">{items}</div>', 'tight') + cta('Noch eine Frage offen?', 'Wir antworten persönlich.', 'Frage stellen', 'kontakt.html')


def p_kontakt():
    body = ph('Kontakt', 'Schreiben Sie uns, rufen Sie an oder schicken Sie gleich Ihre Rechnung mit. Wir melden uns zeitnah.', crumbs='Kontakt')
    body += contact_section('k')
    body += sec(f'''<div class="k-grid">
  <div class="k-data reveal"><h2 class="h3">So erreichen Sie uns</h2><p><b>{CO['name']}</b><br>{CO['street']}<br>{CO['zip']} {CO['city']}</p>
    <p>{TEL} <a href="tel:{CO['telh']}">{CO['tel']}</a> <span class="muted">(Christoph Warin, mobil)</span><br>{MAIL} <a href="mailto:{CO['mail']}">{CO['mail']}</a><br>{MAIL} <a href="mailto:{CO['office']}">{CO['office']}</a> <span class="muted">(Backoffice)</span></p></div>
  <div class="map reveal" id="map"><button type="button" id="map-btn" class="btn line">{PIN} Karte laden</button><p>Beim Laden der Karte werden Daten an OpenStreetMap übertragen.</p></div>
</div>''', 'gray')
    return body


def p_danke():
    return f'''<section class="plain"><div class="wrap narrow"><div class="big-mark" aria-hidden="true">{MARK}</div><h1 class="split">Danke, Ihre Anfrage ist da.</h1><p class="lead reveal">Wir melden uns zeitnah bei Ihnen. Wenn es eilt, rufen Sie uns einfach an: <a href="tel:{CO['telh']}">{CO['tel']}</a>.</p><p class="reveal"><a class="btn red mag" href="index.html">Zur Startseite {ARROW}</a></p></div></section>'''


def p_404():
    return f'''<section class="plain"><div class="wrap narrow"><p class="err-code" aria-hidden="true">404</p><h1 class="split">Diese Seite gibt es nicht (mehr).</h1><p class="lead reveal">Vielleicht hat sich die Adresse mit der neuen Website geändert. Hier geht es weiter:</p><ul class="err-links reveal"><li><a href="index.html">Startseite</a></li>{''.join(f'<li><a href="{s[0]}">{s[1]}</a></li>' for s in SERVICES)}<li><a href="kontakt.html">Kontakt</a></li></ul></div></section>'''


def p_impressum():
    return ph('Impressum', 'Angaben gemäß § 5 Digitale-Dienste-Gesetz.', crumbs='Impressum') + f'''<section class="sec tight"><div class="wrap legal-t">
<h2>Anbieter</h2><p>{CO['name']}<br>{CO['street']}<br>{CO['zip']} {CO['city']}</p>
<h2>Vertreten durch</h2><p>Geschäftsführer: Christoph Warin</p>
<h2>Kontakt</h2><p>Telefon: +49 (0)163 8233713<br>E-Mail: <a href="mailto:{CO['mail']}">{CO['mail']}</a></p>
<h2>Registereintrag</h2><p>Eintragung im Handelsregister<br>Registergericht: Amtsgericht Aachen<br>Registernummer: HRB 30124</p>
<h2>Steuern</h2><p>Umsatzsteuer-Identifikationsnummer gemäß § 27a Umsatzsteuergesetz: DE304182335<br>Steuernummer: 202/5104/2967, Finanzamt Aachen-Kreis</p>
<h2>Verantwortlich für den Inhalt nach § 18 Abs. 2 MStV</h2><p>Christoph Warin, Anschrift wie oben</p>
<h2>Verbraucherstreitbeilegung</h2><p>Wir sind nicht bereit oder verpflichtet, an Streitbeilegungsverfahren vor einer Verbraucherschlichtungsstelle teilzunehmen.</p>
<h2>Haftung für Inhalte</h2><p>Die Inhalte dieser Website werden mit größtmöglicher Sorgfalt erstellt. Für die Richtigkeit, Vollständigkeit und Aktualität der Inhalte übernehmen wir jedoch keine Gewähr. Insbesondere die Angaben zu Steuern, Umlagen und gesetzlichen Pflichten sind vereinfacht und ersetzen keine Prüfung im Einzelfall.</p>
<h2>Haftung für Links</h2><p>Diese Website enthält Links zu Websites Dritter, auf deren Inhalte wir keinen Einfluss haben. Für die Inhalte der verlinkten Seiten ist stets der jeweilige Anbieter oder Betreiber verantwortlich. Bei Bekanntwerden von Rechtsverletzungen entfernen wir derartige Links umgehend.</p>
<h2>Urheberrecht</h2><p>Die auf dieser Website veröffentlichten Inhalte unterliegen dem deutschen Urheber- und Leistungsschutzrecht. Die Logos auf der Seite Referenzen und Partner sind Marken der jeweiligen Unternehmen und werden als Referenz gezeigt.</p>
</div></section>'''


def p_datenschutz():
    return ph('Datenschutz', 'Wie wir mit Ihren Daten umgehen, wenn Sie diese Website besuchen oder uns schreiben.', crumbs='Datenschutz') + f'''<section class="sec tight"><div class="wrap legal-t">
<h2>1. Verantwortlicher</h2><p>{CO['name']}, {CO['street']}, {CO['zip']} {CO['city']}<br>Telefon: +49 (0)163 8233713, E-Mail: <a href="mailto:{CO['mail']}">{CO['mail']}</a><br>Geschäftsführer: Christoph Warin</p>
<h2>2. Grundsätzliches</h2><p>Diese Website setzt keine Cookies, verwendet kein Tracking und keine Analyse-Werkzeuge. Schriften und Bilder werden von unserem eigenen Server geladen, es werden keine Inhalte von Google oder sozialen Netzwerken eingebunden.</p>
<h2>3. Hosting und Server-Protokolle</h2><p>Beim Aufruf dieser Website verarbeitet unser Hosting-Anbieter technisch notwendige Daten (IP-Adresse, Datum und Uhrzeit, aufgerufene Seite, Browser-Typ), um die Seite auszuliefern und ihre Sicherheit zu gewährleisten. Rechtsgrundlage ist Art. 6 Abs. 1 lit. f DSGVO. Mit dem Hosting-Anbieter besteht ein Vertrag zur Auftragsverarbeitung. Hosting-Anbieter: [wird vor dem Start ergänzt].</p>
<h2>4. Skript-Bibliotheken</h2><p>Für Animationen laden wir die Bibliotheken GSAP und Lenis über das Content-Delivery-Netzwerk jsDelivr. Dabei wird Ihre IP-Adresse an jsDelivr übermittelt. Rechtsgrundlage ist unser berechtigtes Interesse an einer schnellen und funktionsfähigen Website (Art. 6 Abs. 1 lit. f DSGVO).</p>
<h2>5. Kontaktformular und E-Mail</h2><p>Wenn Sie uns über das Formular oder per E-Mail schreiben, verarbeiten wir Ihre Angaben (Name, E-Mail, optional Unternehmen, Telefon, Nachricht und angehängte Rechnung), um Ihre Anfrage zu bearbeiten. Rechtsgrundlage ist Art. 6 Abs. 1 lit. b DSGVO (Anbahnung eines Vertrags) und Ihre Einwilligung nach Art. 6 Abs. 1 lit. a DSGVO. Die Formulardaten werden über unseren Hosting-Anbieter übermittelt. Wir löschen die Daten, sobald die Anfrage erledigt ist und keine gesetzlichen Aufbewahrungsfristen entgegenstehen.</p>
<h2>6. Karte</h2><p>Auf der Kontaktseite können Sie eine Karte von OpenStreetMap laden. Erst nach Ihrem Klick werden Daten (u. a. Ihre IP-Adresse) an die OpenStreetMap Foundation übertragen. Rechtsgrundlage ist Ihre Einwilligung (Art. 6 Abs. 1 lit. a DSGVO).</p>
<h2>7. Ihre Rechte</h2><p>Sie haben das Recht auf Auskunft, Berichtigung, Löschung, Einschränkung der Verarbeitung, Datenübertragbarkeit und Widerspruch sowie das Recht, eine Einwilligung jederzeit mit Wirkung für die Zukunft zu widerrufen. Außerdem können Sie sich bei einer Datenschutz-Aufsichtsbehörde beschweren, zum Beispiel bei der Landesbeauftragten für Datenschutz und Informationsfreiheit Nordrhein-Westfalen.</p>
<h2>8. Werbewiderspruch</h2><p>Der Nutzung der im Impressum veröffentlichten Kontaktdaten zur Übersendung nicht angeforderter Werbung wird widersprochen.</p>
<p class="muted">Stand: September 2026</p>
</div></section>'''


# ============================ SEITENLISTE ============================
def faq_ld():
    return {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in FAQ]}


def art_ld(a):
    return {"@context": "https://schema.org", "@type": "Article", "headline": a[1], "description": a[2], "datePublished": TODAY, "dateModified": TODAY, "inLanguage": "de",
            "author": {"@type": "Organization", "name": CO['name']}, "publisher": {"@type": "Organization", "name": CO['name'], "logo": {"@type": "ImageObject", "url": DOMAIN + "/apple-touch-icon.png"}},
            "image": DOMAIN + "/img/og.jpg", "mainEntityOfPage": DOMAIN + "/" + a[0]}


PAGES = [
    dict(file='index.html', title='Warin Energie: Energiekosten für Unternehmen senken', desc='Energieberatung für Unternehmen aus Eschweiler: Energiebeschaffung, Vertragsmanagement, Rechnungsprüfung, Steueranträge und Effizienz aus einer Hand.', body='home', fn=index, prio='1.0'),
    dict(file='energiebeschaffung.html', title='Energiebeschaffung für Unternehmen | Warin Energie', desc='Strom und Erdgas zu bestmöglichen Marktpreisen: Ausschreibung, Tranchen oder Festpreis, Marktbeobachtung inklusive. Warin Energie, Eschweiler.', fn=p_beschaffung),
    dict(file='immobilienwirtschaft.html', title='Energie für die Immobilienwirtschaft | Warin Energie', desc='Niedrige Nebenkosten für Mehrfamilienhäuser, Wohnanlagen und WEG: Bündelung, Ausschreibung, Vertragsmanagement und Rechnungsprüfung.', fn=p_immo),
    dict(file='mitarbeiter-tarife.html', title='Mitarbeiter-Tarife für Strom und Gas | Warin Energie', desc='Energietarife für die Haushalte Ihrer Belegschaft: Mitarbeiterbindung ohne Kosten für das Unternehmen, in Zusammenarbeit mit namhaften Versorgern.', fn=p_mitarbeiter),
    dict(file='vertragsmanagement.html', title='Vertragsmanagement für Energieverträge | Warin Energie', desc='Laufzeiten, Kündigungsfristen, Mengentoleranzen und Pönalen im Griff. Mit Fristen-Rechner für Ihren Strom- oder Gasliefervertrag.', fn=p_vertrag),
    dict(file='rechnungspruefung.html', title='Rechnungsprüfung Strom und Gas | Warin Energie', desc='Wir prüfen Ihre Energierechnungen Position für Position, übernehmen das Clearing mit dem Versorger und bereiten alles verständlich auf.', fn=p_rechnung),
    dict(file='antragsmanagement.html', title='Stromsteuer & Energiesteuer zurückholen | Warin Energie', desc='Entlastung bei Strom- und Energiesteuer, Besondere Ausgleichsregelung: Wir prüfen Voraussetzungen, stellen Anträge und halten die Fristen ein.', fn=p_antrag),
    dict(file='energieeffizienz.html', title='Energieeffizienz, Energieaudit & ISO 50001 | Warin Energie', desc='Energieaudit nach DIN EN 16247-1, ISO 50001, EnEfG-Pflichten, Förderung und Energieausweise. Mit Pflichten-Check für Ihr Unternehmen.', fn=p_effizienz),
    dict(file='anlagen-contracting.html', title='Anlagen-Contracting ohne Investition | Warin Energie', desc='Heizung, BHKW, Druckluft oder Kälte ohne eigene Investition: 15 Jahre Vollgarantie, Wartung und 24-Stunden-Notdienst inklusive.', fn=p_contracting),
    dict(file='referenzen.html', title='Referenzen | Warin Energie Eschweiler', desc='Ein Auszug unserer Referenzen: Unternehmen aus Industrie, Gesundheit, Handel und Immobilienwirtschaft vertrauen Warin Energie.', fn=p_referenzen, prio='0.7'),
    dict(file='unternehmen.html', title='Unternehmen & Ansprechpartner | Warin Energie', desc='Warin Energie GmbH aus Eschweiler: unabhängige Energieberatung für Unternehmen. Ihr Ansprechpartner: Christoph Warin, Energiemanager für die Industrie.', fn=p_unternehmen, prio='0.7'),
    dict(file='partner.html', title='Unsere Partner | Warin Energie', desc='Das Netzwerk von Warin Energie: Fachleute für Energieeffizienz, Technik, Statik und Immobilienbewertung.', fn=p_partner, prio='0.5'),
    dict(file='ratgeber.html', title='Ratgeber Energiekosten für Unternehmen | Warin Energie', desc='Stromsteuer-Entlastung, Energieeffizienzgesetz, Lieferverträge: kurze Antworten auf häufige Fragen von Unternehmen.', fn=p_ratgeber, prio='0.6'),
] + [dict(file=a[0], title=a[1][:52] + ' | Warin' if len(a[1]) > 52 else a[1] + ' | Warin Energie', desc=a[2], fn=(lambda a=a: p_article(a)), article=True, parent='ratgeber.html', ld=art_ld(a), prio='0.6') for a in ARTICLES] + [
    dict(file='faq.html', title='Häufige Fragen | Warin Energie', desc='Antworten auf häufige Fragen zu Energiebeschaffung, Rechnungsprüfung, Stromsteuer, Energieaudit und Contracting.', fn=p_faq, ld=faq_ld(), prio='0.6'),
    dict(file='kontakt.html', title='Kontakt | Warin Energie Eschweiler', desc='Warin Energie GmbH, Auf dem Hügel 21, 52249 Eschweiler. Telefon 0163 823 37 13. Schicken Sie uns Ihre Rechnung zur Prüfung.', fn=p_kontakt, prio='0.8'),
    dict(file='danke.html', title='Danke für Ihre Anfrage | Warin Energie', desc='Ihre Anfrage ist bei uns eingegangen.', fn=p_danke, noindex=True, body='plain-page'),
    dict(file='404.html', title='Seite nicht gefunden | Warin Energie', desc='Diese Seite gibt es nicht. Hier geht es weiter zu den Leistungen von Warin Energie.', fn=p_404, noindex=True, body='plain-page'),
    dict(file='impressum.html', title='Impressum | Warin Energie', desc='Impressum der Warin Energie GmbH, Auf dem Hügel 21, 52249 Eschweiler.', fn=p_impressum, body='legal', prio='0.2'),
    dict(file='datenschutz.html', title='Datenschutz | Warin Energie', desc='Datenschutzerklärung der Warin Energie GmbH: keine Cookies, kein Tracking, Kontaktformular und Karte erst auf Klick.', fn=p_datenschutz, body='legal', prio='0.2'),
]

if __name__ == '__main__':
    for p in PAGES:
        assert len(p['title']) <= 65, (p['file'], len(p['title']), p['title'])
        assert len(p['desc']) <= 155, (p['file'], len(p['desc']))
        if p['file'] in [s[0] for s in SERVICES]: p.setdefault('body', 'svc')
        with open(OUT + p['file'], 'w', encoding='utf-8') as fh:
            fh.write(head(p) + p['fn']() + foot(p))
    sm = ''.join(f'<url><loc>{DOMAIN}/{"" if p["file"] == "index.html" else p["file"]}</loc><lastmod>{TODAY}</lastmod><priority>{p.get("prio", "0.8")}</priority></url>' for p in PAGES if not p.get('noindex'))
    open(OUT + 'sitemap.xml', 'w').write(f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{sm}</urlset>\n')
    open(OUT + 'robots.txt', 'w').write(f'User-agent: *\nAllow: /\nDisallow: /danke.html\n\nSitemap: {DOMAIN}/sitemap.xml\n')
    open(OUT + 'favicon.svg', 'w').write(MARK.replace(' aria-hidden="true"', ''))
    print(len(PAGES), 'Seiten geschrieben')
