# TaskScore – Finalabgabe

## Projektbeschreibung
TaskScore ist eine webbasierte Task-Management-Anwendung zur Wochenplanung.  
Nutzer können Aufgaben auf Wochentage verteilen und nutzen hierfür ein Punktesystem, um sich eingenständig Prioriäten zu setzen und den Zeitaufwand der Tasks einzuschätzen. Fortschritte der geplanten Aufgaben sind dauerhaft visuell dargestellt.

Ziel des Projekts ist die Entwicklung einer einfachen, nachvollziehbaren Anwendung zur Selbstorganisation.

## Team
- Laurenz Brödemann – Matrikelnummer: 77211922572  
- Elhasan Kandil – Matrikelnummer: 77211982350  

## Abgabeinhalte
Dieses Repository enthält:
- Quellcode der Anwendung
- Ausführliche Projektdokumentation
- Value Proposition
- Anleitung zum Ausführen der Anwendung
- Präsentationsfolien (PDF)  
- Quellenverzeichnis   

## Veröffentlichtes Projekt
Website / Demo:
Lokaler Start der Anwendung über:
http://127.0.0.1:5000/
(Die Anwendung ist eine lokale Flask-Webapp und wird nach Installation (siehe unten) der Abhängigkeiten lokal ausgeführt.)

## Lokale Installation und Start der Anwendung
Diese Anleitung beschreibt Schritt für Schritt, wie die Anwendung auf einem Rechner installiert und gestartet werden kann.

1. Benötigte Software installieren
1.1 Git installieren

Git wird benötigt, um das Repository zu klonen.
Download: https://git-scm.com/downloads

1.2 Python installieren

Die Anwendung benötigt Python 3.
Download: https://www.python.org/downloads/

(Optional, empfohlen auf macOS) Homebrew
Homebrew ist ein Paketmanager für macOS.
Installieren(in der Konsole):
  /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
dann: 
  brew install python

1.3 VS Code (empfohlen)

Als Code-Editor wird Visual Studio Code empfohlen.
Download: https://code.visualstudio.com/

2. Repository klonen ab hier im VSCode Terminal
  git clone https://github.com/laurenzberlin-prog/Taskscore-FinalAbgabe.git
  cd Taskscore-FinalAbgabe

3. Virtuelle Umgebung erstellen
Eine virtuelle Umgebung isoliert die Python-Abhängigkeiten.
macOS/Linux:
  python3 -m venv venv
  source venv/bin/activate
Windows:
  python -m venv venv
  .\venv\Scripts\Activate.ps1
Nach Aktivierung steht im Terminal (venv).

4. Abhängigkeiten installieren
   pip install -r requirements.txt

5. Anwendung starten
   python3 app.py
Im Terminal erscheint:
  Running on http://127.0.0.1:5000

6. Anwendung im Browser öffnen
     http://127.0.0.1:5000

--

## Rechtliche Erklärung
Die eidesstattliche Erklärung aller Teammitglieder befindet sich unter:  
`docs/declaration.md`
