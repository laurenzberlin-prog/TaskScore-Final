# Quellenverzeichnis (TaskScore)
---

## 1) Python / Flask / Web-Routing
- Flask Dokumentation (Quickstart, Routing, Templates, Request, Redirects):
  https://flask.palletsprojects.com/en/latest/quickstart/
- Flask – `render_template`, `request`, `redirect`, `url_for`:
  https://flask.palletsprojects.com/en/latest/api/
- Flask – Sessions (`session`, `secret_key`):
  https://flask.palletsprojects.com/en/latest/quickstart/#sessions
- https://www.youtube.com/playlist?list=PL-osiE80TeTs4UjLw5MM6OjgkjFeUxCYH
- https://www.youtube.com/watch?v=Z1RJmh_OqeA
- https://www.youtube.com/watch?v=2XG9-Wm5qg4

Bezug im Projekt:
- `app.py`: Routen `@app.route("/")`, `@app.route("/tasks")`, Login/Register/Logout, `session["user_id"]`

---

## 2) Jinja2 / Template-Logik
- Jinja2 Dokumentation (Variablen, Filter, if/for):
  https://jinja.palletsprojects.com/en/latest/templates/
- Jinja2 – Control Structures (`for`, `if`):
  https://jinja.palletsprojects.com/en/latest/templates/#list-of-control-structures
- Jinja2 – Filter (z. B. `round`):
  https://jinja.palletsprojects.com/en/latest/templates/#filters
- https://www.youtube.com/watch?v=bxhXQG1qJPM

Bezug im Projekt:
- Templates: Schleifen für Aufgabenlisten, Tagespunkte, Prozentberechnung (`percent|round(0)`)

---

## 3) SQLite / Python sqlite3
- Python sqlite3 Modul:
  https://docs.python.org/3/library/sqlite3.html
- sqlite3 – Row Factory (Dictionary-ähnliche Rows):
  https://docs.python.org/3/library/sqlite3.html#sqlite3.Connection.row_factory
- SQLite – SQL Syntax (CREATE TABLE, ALTER TABLE, SELECT, UPDATE, DELETE):
  https://www.sqlite.org/lang.html

Bezug im Projekt:
- `database.py`: Tabellen `tasks`, `users`, Spalte `user_id`, CRUD-Funktionen, Summen/Counts

---

## 4) Login/Passwort-Hashing / Werkzeug Security
- Werkzeug – `generate_password_hash`, `check_password_hash`:
  https://werkzeug.palletsprojects.com/en/latest/utils/#werkzeug.security.generate_password_hash
  https://werkzeug.palletsprojects.com/en/latest/utils/#werkzeug.security.check_password_hash
- https://www.youtube.com/watch?v=71EU8gnZqZQ

Bezug im Projekt:
- `database.py`: Funktionen `create_user()` und `verify_user()` (Registrierung/Login)

---

## 5) HTML & CSS Grundlagen
- MDN – HTML Grundlagen:
  https://developer.mozilla.org/en-US/docs/Web/HTML
- MDN – CSS Grundlagen:
  https://developer.mozilla.org/en-US/docs/Web/CSS
- MDN – CSS Box Model (padding/margin, box-sizing):
  https://developer.mozilla.org/en-US/docs/Learn/CSS/Building_blocks/The_box_model
- MDN – `display: inline-block`, Hover:
  https://developer.mozilla.org/en-US/docs/Web/CSS/display
  https://developer.mozilla.org/en-US/docs/Web/CSS/:hover
- https://www.youtube.com/watch?v=pQN-pnXPaVg
-https://www.youtube.com/watch?v=J9EJ6oG2i3s

Bezug im Projekt:
- Templates: Buttons/Links im `.nav`, Hover-Effekte, Cards, Layout

---

## 6) JSON API (Status Endpoint)
- Flask – `jsonify`:
  https://flask.palletsprojects.com/en/latest/api/#flask.json.jsonify

Bezug im Projekt:
- `app.py`: `/api/status` liefert Budget/Points/Score/Task-Count als JSON

---

## 7) KI-Hilfsmittel (Offenlegung)
- ChatGPT (OpenAI) wurde als Hilfsmittel genutzt (siehe `docs/ai-usage.md`).
 https://chatgpt.com
---

## Zuordnung „Quelle → Projektteil“ (Kurz)
- Flask Docs → Routing, Templates, Sessions in `app.py`
- Jinja2 Docs → Schleifen/If/Filter in Templates (`tasks.html`, `plan.html`, `progress.html`)
- sqlite3 + SQLite Lang → Tabellen/Abfragen in `database.py`
- Werkzeug Security → Passwort-Hashing im Login/Registration
- MDN → HTML/CSS Struktur, Buttons, Hover, Layout
