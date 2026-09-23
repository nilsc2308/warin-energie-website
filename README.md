# Warin Energie GmbH – Website (Entwurf)

Statischer Mehrseiter, 22 Seiten, kein Build. Gestaltung siehe `DESIGN.md`, offene Punkte siehe `LAUNCH-CHECKLISTE.md`.

- **Ansehen:** im Ordner `python3 -m http.server 8768` starten, dann http://localhost:8768 öffnen.
- **Ändern:** Texte stehen in `_build.py`. Nach jeder Änderung `python3 _build.py` ausführen – das erzeugt alle HTML-Dateien, `sitemap.xml`, `robots.txt` und `favicon.svg` neu. Bei CSS/JS-Änderungen in `_build.py` die Zahl `VER` erhöhen.
- **Dateien:** `styles.css` (Gestaltung), `main.js` (Animationen, Rechner, Formular), `fonts/` (IBM Plex, lokal), `img/` (Porträt, Logos, og.jpg).
- **Alte Website:** gesicherte Texte und Bilder in `_quelle/alte-website/` (wird nicht veröffentlicht).
