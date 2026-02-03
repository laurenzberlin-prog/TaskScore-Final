# TaskScore-Final

## Projektbeschreibung
**TaskScore** ist eine webbasierte Task-Management-Anwendung zur Wochenplanung.  
Nutzer können Aufgaben auf einzelne Wochentage verteilen und hierfür ein Punktesystem nutzen, um Prioritäten zu setzen und den zeitlichen Aufwand der Tasks besser einzuschätzen.  
Der Fortschritt der geplanten Aufgaben wird dauerhaft visuell dargestellt.

Ziel des Projekts ist die Entwicklung einer einfachen, nachvollziehbaren Anwendung zur Selbstorganisation.

---

## Team
- **Laurenz Brödemann** – Matrikelnummer: 77211922572  
- **Elhasan Kandil** – Matrikelnummer: 77211982350  

---

## Abgabeinhalte
Dieses Repository enthält:
- den vollständigen Quellcode der Anwendung  
- eine ausführliche Projektdokumentation (GitHub Pages)   
- Anleitung zur lokalen Ausführung der Anwendung  
- Präsentationsfolien (PDF)  
- Quellenverzeichnis  

---

## Veröffentlichtes Projekt / Dokumentation
Die vollständige Projektdokumentation ist über **GitHub Pages** erreichbar:

👉 **https://laurenzberlin-prog.github.io/TaskScore-Final/**

---

## Lokale Installation und Start der Anwendung
Diese Anleitung beschreibt Schritt für Schritt, wie die Anwendung lokal ausgeführt werden kann.

### 1. Benötigte Software installieren

#### 1.1 Git
Git wird benötigt, um das Repository zu klonen.  
Download: https://git-scm.com/downloads

#### 1.2 Python
Die Anwendung benötigt **Python 3**.  
Download: https://www.python.org/downloads/

(Optional, empfohlen unter macOS) **Homebrew**  
Homebrew ist ein Paketmanager für macOS.

Installation (Terminal):
```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
brew install python
```
#### 1.3 Visual Studio Code
Download: https://code.visualstudio.com/

#### 2. Repository klonen (im VS Code Terminal)
git clone https://github.com/laurenzberlin-prog/TaskScore-Final.git
cd TaskScore-Final

#### 3. Virtuelle Umgebung erstellen

Auf macOS/Linus:
python3 -m venv venv
source venv/bin/activate

Auf Windows:

python -m venv venv
.\venv\Scripts\Activate.ps1


#### 4. Abhängigkeiten installieren
pip install -r requirements.txt

#### 5. Anwendung starten
python3 app.py

Im Terminal erscheint:
Running on http://127.0.0.1:5000

#### 6. Anwendung im Browser öffnen
http://127.0.0.1:5000