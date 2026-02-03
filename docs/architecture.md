# Architektur – TaskScore

## 1. Überblick

Die Anwendung *TaskScore* basiert auf einer klassischen Web-Architektur nach dem Client-Server-Prinzip.  
Der Nutzer interagiert über einen Webbrowser (Client) mit der Anwendung, während die eigentliche Logik auf einem Flask-Webserver (Server) ausgeführt wird.

Die Architektur folgt dem Model-View-Controller-Prinzip (MVC):

- **Model:** `database.py` (Datenhaltung in SQLite)  
- **View:** HTML-Templates mit Jinja2 (`home.html`, `tasks.html`, `plan.html`, `progress.html`, `login.html`, `register.html`)
- **Controller:** Flask-Routen in `app.py`  

---

## 2. Komponenten

### 2.1 Flask-Anwendung (Controller)

Die Datei `app.py` stellt den zentralen Einstiegspunkt der Anwendung dar.  
Hier werden alle Routen definiert, unter anderem:

- `/` – Startseite (Hauptmenü, nur mit Session)  
- `/login` – Login (GET Formular anzeigen, POST prüfen & Session setzen)  
- `/register` – Registrierung (GET Formular anzeigen, POST User anlegen)  
- `/logout` – Logout (Session löschen, zurück zum Login)  
- `/tasks` – Aufgabenverwaltung  
- `/plan` – Wochenplan  
- `/progress` – Fortschritt  
- `/api/status` – JSON-API  

Zusätzlich wird für den Zugriffsschutz eine Session verwendet:
- Bei erfolgreichem Login wird `session["user_id"]` gesetzt.
- Geschützte Seiten prüfen, ob eine Session vorhanden ist (sonst Redirect zu `/login`).
1. Entgegennahme der HTTP-Anfrage  
2. Aufruf der passenden Datenbankfunktion  
3. Übergabe der Ergebnisse an ein Template  
4. Rückgabe der generierten HTML-Seite  

---

### 2.2 Templates (View)

Die Benutzeroberfläche wird über HTML-Templates realisiert, die mit der Template-Engine **Jinja2** gerendert werden.

Im Projekt werden unter anderem folgende Template-Mechanismen verwendet:

{% raw %}

**Variablen:**  
`{{ current_total }}`, `{{ budget }}`

**Schleifen:**  
`{% for t in tasks %} ... {% endfor %}`

**Bedingungen:**  
`{% if error %} ... {% endif %}`

**Berechnungen im Template:**  
`{% set percent = (done_points / total_points * 100) if total_points > 0 else 0 %}`

{% endraw %}

> Hinweis:  
> Die gezeigten Jinja2-Ausdrücke dienen ausschließlich der Dokumentation.  
> GitHub Pages interpretiert diese Syntax nicht, da sie hier nur als Text dargestellt wird.

Durch den Einsatz von Templates kann die Darstellung dynamisch an die aktuellen Daten angepasst werden, ohne die Anwendungslogik zu verändern.

---

### 2.3 Datenbank (Model)

Die Datei `database.py` kapselt sämtliche Zugriffe auf die SQLite-Datenbank.  
Die Datenbank enthält mehrere Tabellen, unter anderem:

- `tasks`: speichert alle Aufgaben eines Nutzers  
- `user_stats`: speichert aggregierte Kennzahlen (z.B. Done Score)  

Alle SQL-Zugriffe erfolgen ausschließlich über klar definierte Funktionen, z.B.:

- `get_all_tasks()`  
- `insert_task(...)`  
- `toggle_task_status(...)`  
- `get_weekly_points()`  

Dadurch ist die Datenhaltung klar von der Anwendungslogik getrennt und leicht wartbar.

---

## 3. Ablauf eines typischen Requests

Am Beispiel **„Neue Aufgabe anlegen“**:

1. Der Nutzer füllt das Formular auf `/tasks` aus und klickt auf „Aufgabe hinzufügen“.  
2. Der Browser sendet einen POST-Request an `/tasks`.  
3. Flask liest die Formulardaten über `request.form`.  
4. Die Funktion `insert_task(...)` speichert die Aufgabe in der Datenbank.  
5. Anschließend erfolgt ein Redirect auf `/tasks`.  
6. Die aktualisierte Aufgabenliste wird aus der Datenbank geladen.  
7. Das Template `tasks.html` wird mit den neuen Daten gerendert.  
8. Die fertige HTML-Seite wird an den Browser zurückgegeben.

---

## 4. JSON-API

Zusätzlich zur grafischen Benutzeroberfläche existiert der Endpunkt `/api/status`.  
Dieser liefert Statusinformationen im JSON-Format, z.B.:

- aktuelles Wochenbudget  
- erledigte Punkte  
- Anzahl der Aufgaben  

Der Endpunkt ermöglicht zukünftige Erweiterungen, etwa:

- Mobile Anwendungen  
- Dashboards  
- externe Visualisierungen  

---

## 5. Vorteile der gewählten Architektur

Die gewählte Architektur bietet mehrere Vorteile:

- klare Trennung von Logik, Daten und Darstellung  
- gute Wartbarkeit und Erweiterbarkeit  
- hohe Verständlichkeit für Lern- und Lehrzwecke  

Insbesondere für didaktische Zwecke eignet sich Flask in Kombination mit SQLite sehr gut, da der gesamte technische Stack überschaubar bleibt und die Funktionsweise leicht nachvollzogen werden kann.