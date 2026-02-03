# Design Decisions – TaskScore

Diese Datei dokumentiert zentrale technische und konzeptionelle Entscheidungen während der Entwicklung.

---

## 1. Entscheidung: Punktesystem statt Zeitangaben

**Problem:**  
Zeitangaben sind subjektiv und schwer einzuschätzen.

**Lösung:**  
Ein einfaches Punktesystem (0–100 pro Woche).

**Begründung:**  
Punkte sind flexibler, leichter verständlich und zwingen zur Priorisierung.

---

## 2. Entscheidung: Kein externes Frontend (React etc.)

**Problem:**  
Zusätzliche Komplexität ohne Mehrwert.

**Lösung:**  
Reines Server-Side-Rendering mit Jinja2.

**Begründung:**  
- Einfacher Debug
- Kein Build-System
- Klarer HTML-Flow

---

## 3. Entscheidung: User-System mit Session

**Problem:**  
Mehrere Nutzer sollen getrennte Aufgaben haben.

**Lösung:**  
Session-basierte Authentifizierung mit SQLite.

**Begründung:**  
- Keine externe Abhängigkeit
- Klar nachvollziehbar
---

## 6. Entscheidung: Bewusst simples UI

**Problem:**  
Zu viele Features führen zu kognitiver Überlastung.

**Lösung:**  
Reduziertes UI mit Cards und klarer Navigation.

**Begründung:**  
Fokus liegt auf Funktion, nicht auf Design-Spielereien.

---

## 7. Entscheidung: Kein automatisches Speichern

**Problem:**  
Komplexere Zustandsverwaltung nötig.

**Lösung:**  
Explizite Buttons (Submit / Toggle / Delete).

**Begründung:**  
- Nutzerkontrolle
- Weniger Bugs
- Klarer Request-Flow

---
## 8. Aktuelle technische Probleme und deren Lösungen

Während der finalen Entwicklungsphase traten mehrere praxisnahe Probleme auf.

Problem 1: Aufgaben über mehrere Tage anlegen

Problem:
Ursprünglich konnte eine Aufgabe nur einem einzelnen Wochentag zugeordnet werden. Für wiederkehrende Aufgaben (z.B. „Sport“ an mehreren Tagen) war dies unpraktisch.

Lösung:
Ein eigenes Multi-Select-Dropdown wurde implementiert, mit dem mehrere Wochentage ausgewählt werden können. Im Backend wird daraus eine Liste erzeugt und für jeden Tag eine eigene Aufgabe gespeichert.

Begründung:
Die Datenbank bleibt normalisiert (eine Aufgabe = ein Tag), während die Benutzeroberfläche trotzdem komfortabel bleibt.

⸻

Problem 2: Score ging beim Löschen von Aufgaben verloren

Problem:
Wenn erledigte Aufgaben gelöscht wurden, wurde der Fortschritt (Done Score) zurückgesetzt.

Lösung:
Ein separates Feld rewarded sowie eine eigene Tabelle user_stats wurden eingeführt. Der Score wird nur einmal beim erstmaligen Erledigen erhöht und bleibt unabhängig vom Löschen der Aufgabe bestehen.

Begründung:
Dadurch wird historischer Fortschritt korrekt gespeichert und nicht durch spätere Aktionen verfälscht.


## Zusammenfassung

Alle Designentscheidungen folgen drei Prinzipien:

1. **Einfachheit**
2. **Nachvollziehbarkeit**
3. **Lehrbarkeit**
