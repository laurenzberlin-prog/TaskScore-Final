# Projektbeschreibung – TaskScore

## 1. Ausgangssituation und Problemstellung

Viele Studierende und Berufstätige haben Schwierigkeiten, ihre täglichen Aufgaben realistisch zu planen und Prioritäten sinnvoll zu setzen. Klassische To-Do-Listen erfassen zwar Aufgaben, geben jedoch kaum Auskunft darüber, wie aufwendig oder relevant einzelne Tätigkeiten sind.

Häufig werden entweder zu viele Aufgaben eingeplant oder wichtige Tätigkeiten zugunsten kurzfristiger Ablenkungen verschoben. Dadurch entsteht ein Mangel an Transparenz über den eigenen Arbeitsaufwand und den tatsächlichen Fortschritt.

## 2. Ziel des Projekts

Ziel des Projekts *TaskScore* ist die Entwicklung einer webbasierten Anwendung zur strukturierten Wochenplanung. Aufgaben werden nicht nur erfasst, sondern zusätzlich mit einem Punktwert versehen, der den geschätzten Zeit- oder Arbeitsaufwand widerspiegelt.

Durch ein festes Wochenbudget (z.B. 100 Punkte) sollen Nutzer gezwungen werden, realistische Entscheidungen über ihre Kapazitäten zu treffen und Aufgaben bewusst zu priorisieren.

## 3. Zielgruppe

Die primäre Zielgruppe sind:
- Studierende  
- Schüler  
- Berufseinsteiger  
- Personen mit selbstorganisiertem Arbeitsalltag  

Die Anwendung richtet sich insbesondere an Nutzer, die:
- ihre Produktivität steigern möchten  
- ihren Arbeitsaufwand besser einschätzen wollen  
- visuelles Feedback über ihren Fortschritt bevorzugen  

## 4. Grundidee der Anwendung

TaskScore kombiniert klassische Aufgabenverwaltung mit einem spielerischen Punktesystem. Jede Aufgabe erhält einen Punktwert, der zum Wochenbudget addiert wird.

Zusätzlich wird jede erledigte Aufgabe mit einem sogenannten *Done Score* belohnt. Dieser dient als langfristige Motivationskennzahl und steigt unabhängig vom Wochenbudget.

Die Anwendung bietet somit zwei Ebenen:
- kurzfristige Planung (Wochenbudget)  
- langfristige Motivation (Done Score)

## 5. Funktionaler Überblick

Die Anwendung bietet folgende Kernfunktionen:

- Registrieren bzw. Einloggen mit eigenem Profil

- Anlegen neuer Aufgaben mit:
  - Titel  
  - Beschreibung  
  - Wochentag(e) 
  - Punktwert  

- Anzeige aller geplanten Aufgaben  
- Umschalten des Status einer Aufgabe (OPEN / DONE)  
- Löschen von Aufgaben  
- Visualisierung der Punktverteilung pro Wochentag  
- Anzeige des Fortschritts in Prozent  
- JSON-API-Endpunkt zur externen Statusabfrage  

