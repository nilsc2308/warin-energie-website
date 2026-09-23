# Launch-Checkliste – Warin Energie GmbH (Stand 23.9.2026, 2. Fassung)

Unbeauftragter Entwurf auf Basis von www.warin-energie.de (IONOS-Baukasten). **Vor jeder Veröffentlichung unter der echten Domain: Einverständnis von Christoph Warin einholen.**

## Offene Kundenangaben (müssen vom Kunden kommen)
- [ ] **Einverständnis** zum Neubau und zur Nutzung der Inhalte
- [ ] **Referenzlogos (31) und Partnerlogos (5):** Freigabe, dass sie weiter als Referenz gezeigt werden dürfen
- [ ] **Sechs Branchen-Fotos sind Unsplash-Platzhalter** (Industriehalle, Produktion, Umspannwerk, Strommasten, Hochspannung, Leitstand – Nachweis in img/BILDNACHWEIS.md). Vor dem Start durch eigene Fotos ersetzen oder bewusst behalten
- [ ] **Porträt Christoph Warin:** Rechte bestätigen, höher aufgelöste Fassung erbitten (jetzt nur 292 × 350 px); Fotos von Ioanna Frangouli-Warin und Elisabeth Mystakidis (jetzt Initialen)
- [ ] **Logo als Vektordatei** (SVG/PDF) – jetzt nach der Bilddatei nachgebaut
- [ ] **Handelsregister:** HRB 30124, Amtsgericht Aachen (aus Registerauskunft northdata; Eintragungsdatum dort 25.7.2026) – bestätigen
- [ ] **Festnetznummer:** Im alten Portfolio-PDF stand 02403 7499583 und die Adresse Eschenweg 40 – veraltet? Auf der Seite steht nur das Handy 0163 823 37 13
- [ ] **Hosting-Anbieter** in Datenschutz Punkt 3 eintragen (Platzhalter „[wird vor dem Start ergänzt]“)
- [ ] **Partner:** kurze Beschreibung und Website-Links der fünf Partner (jetzt nur Namen)
- [ ] **Konditionen:** Die Seite macht keine Preisangaben und verspricht keine kostenlose Ersteinschätzung – falls es die gibt, ergänzen
- [ ] **Sicherheitshinweis:** Die alte Seite warnt, dass das E-Mail-Postfach am 21.09.2026 missbraucht wurde. Nicht übernommen (wäre zum Start veraltet). Kunde entscheidet, ob ein Hinweis nötig ist

## Fachlich prüfen lassen (Richtwerte, Stand September 2026)
- [ ] Antrags-Matrix und Ratgeber Stromsteuer: Entlastung § 9b StromStG auf 0,50 €/MWh seit 1.1.2026 dauerhaft, Frist 31.12. des Folgejahres, Spitzenausgleich Ende 2023 ausgelaufen, § 9a/§ 51/§ 54, Besondere Ausgleichsregelung (EnFG, BAFA, 30.6.), § 19 StromNEV
- [ ] Pflichten-Check und Ratgeber EnEfG: Schwellen 2,5 GWh (§ 9 Umsetzungspläne, § 17 Abwärme) und 7,5 GWh (§ 8 Managementsystem), Audit-Pflicht Nicht-KMU (EDL-G); Änderungen durch Umsetzung der EU-Effizienzrichtlinie
- [ ] Musterrechnung: Positionsbezeichnungen (u. a. „Aufschlag für besondere Netznutzung“ statt § 19-Umlage)
- [ ] Fristen-Rechner: Richtwerte 12 Monate Marktbeobachtung und 4 Wochen Puffer vor der Kündigungsfrist
- [ ] Kostenhebel-Rechner: reine Multiplikation, keine Einsparzusage (so gekennzeichnet)
- [ ] Contracting: „15 Jahre Vollgarantie“, „24-Stunden-Notdienst“ – von der alten Seite übernommen, noch aktuell?

## Recht
- [x] Impressum mit allen Angaben der alten Seite + Registereintrag + § 18 MStV + Verbraucherstreitbeilegung
- [x] Datenschutzerklärung neu (keine Cookies, kein Tracking, jsDelivr, Formular mit Dateianhang, OpenStreetMap erst per Klick)
- [x] Kein Cookie-Banner nötig: Schriften lokal (IBM Plex), keine Google-Dienste, Karte erst nach Klick
- [x] Formular mit Pflicht-Einwilligung zur Datenschutzerklärung
- [ ] Datenschutzerklärung vom Kunden / Anwalt gegenlesen lassen

## Technik (gemessen 23.9.2026, lokaler Server)
- [x] 22 Seiten: Start, 8 Leistungen, Referenzen, Unternehmen, Partner, Ratgeber + 3 Artikel, FAQ, Kontakt, Danke, 404, Impressum, Datenschutz
- [x] **JS-Fehler: 0** auf allen 22 Seiten in Chromium und WebKit, je 1400 px und 390 px (jede Seite komplett durchgescrollt)
- [x] **Horizontales Scrollen: keins** (scrollWidth = clientWidth auf allen Seiten, beide Browser, beide Größen)
- [x] **Kaputte Bilder: 0**
- [x] **Ladegröße Startseite bis „load“: 449 KB** Desktop und Handy (Ziel < 900 / < 500 KB), gemessen per Resource Timing bis loadEventStart; Fotos 2–5 der Szene (ca. 500 KB) laden erst danach
- [x] Links: 68 interne Ziele vorhanden, externe (jsDelivr ×3, netztransparenz.de) antworten 200, alle Anker vorhanden
- [x] Formular automatisiert getestet: leeres Absenden → Name, E-Mail, Datenschutz markiert; falsche E-Mail → markiert; korrekt → Weiterleitung auf danke.html; `?thema=antrag` wählt das Thema vor; Anhang > 8 MB wird abgewiesen
- [x] Rechner getestet: Kostenhebel (2 Mio. kWh × 2 ct × 3 Jahre = 40.000 €/Jahr, 120.000 €), Fristen (Ende 31.12.2027, 3 Monate → Kündigung bis 30.9.2027), Pflichten (800 MWh → keine Pflicht; 3.000 → Pläne + Abwärme; 9.000 → + Managementsystem; Nicht-KMU 3.000 → + Audit), Matrix, Rechnung, Waage
- [x] Netlify-Forms-fertig (data-netlify, Honeypot, multipart für Anhang). Auf GitHub Pages wird das Formular nicht verschickt, sondern führt nur zur Danke-Seite
- [x] `netlify.toml` mit Sicherheits-Headern (CSP, HSTS, X-Frame-Options …) und Weiterleitungen der alten Adressen (/leistungen/, /referenzen/, /unternehmen/, /unsere-partner/, /impressum-datenschutz/, /energiecheck/, /sitemap/, /app/download/*)
- [x] CSS/JS mit Versionsnummer (`?v=20260923-8`)
- [x] 2. Fassung: Szene 520vh statt 700vh, sonst kein festhängender Abschnitt mehr; Texte der Szene in 25 Schritten (Desktop) und 22 Schritten (Handy) geprüft – nie zwei Texte gleichzeitig
- [ ] Lighthouse-Messung auf dem echten Hosting (mit Kompression)

## Barrierefreiheit
- [x] Reduzierte Bewegung in drei Stufen: Szene wird zu einer Fotoreihe mit Bildunterschriften (Fotos laden nur dann), Logo-Reihen stehen als Raster, kein Parallax; Reveals als 150-ms-Blende; Fokus-Ringe und Hover bleiben
- [x] Alt-Texte: 0 Bilder ohne alt; Logos mit Firmennamen als Alt-Text
- [x] Tastatur: Skip-Link, Fokus-Ringe, Menü mit Fokusfalle und Escape, Tabs mit Pfeiltasten, Leistungen-Menü per Klick/Tastatur und Escape, Rechnungszeilen und Chips als Buttons mit aria-pressed/aria-expanded
- [x] Kontraste: Rot #d00000 auf Weiß 5,9 : 1, Grau #6e6e73 auf Weiß 5,0 : 1
- [x] Startseite hat zwei h1 (Szene und statische Fassung) – je nach Modus ist nur eine sichtbar

## SEO
- [x] Meta-Titel ≤ 65, Descriptions ≤ 155 Zeichen (im Generator erzwungen)
- [x] Canonical, OG-Tags + eigenes og.jpg 1200 × 630 auf allen 22 Seiten
- [x] JSON-LD: ProfessionalService auf allen Seiten (Adresse, Geo, USt-ID), FAQPage, Article ×3 – alle Blöcke gültiges JSON
- [x] sitemap.xml (20 Seiten, ohne Danke/404), robots.txt
- [x] favicon.svg + apple-touch-icon.png
- [ ] Nach dem Start: Google Search Console + Google-Unternehmensprofil (Adresse Auf dem Hügel 21) prüfen
- [ ] Analytics: bewusst keins (sonst Cookie-Banner nötig)

## Domain & Start
- [ ] Domain warin-energie.de liegt bei IONOS – DNS auf neues Hosting umstellen
- [ ] Nach Umstellung: alte URLs testen (Weiterleitungen), Formular-Eingang testen
