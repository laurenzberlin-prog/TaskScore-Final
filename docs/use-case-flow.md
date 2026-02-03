# Use Case Flow – TaskScore

## Use Case Flow – Übersicht

![Use Case Flow](screenshots/UseCaseFlow.png)

Das folgende Diagramm zeigt den Ablauf der Anwendung pro Screen
vom ersten Aufruf bis zum Logout.

```mermaid
flowchart TD

A[Browser öffnet App] --> B{Session vorhanden?}

B -- Nein --> L[Login Screen]
B -- Ja --> H[Home Screen]

%% LOGIN
L --> L1[Username + Passwort eingeben]
L1 --> L2[Login absenden]
L2 --> L3{Credentials gültig?}
L3 -- Nein --> L4[Fehlermeldung anzeigen]
L4 --> L
L3 -- Ja --> L5[Session setzen]
L5 --> H

%% REGISTER
L --> R[Register Screen]
R --> R1[Registrierung absenden]
R1 --> R2{Username frei?}
R2 -- Nein --> R3[Fehler anzeigen]
R3 --> R
R2 -- Ja --> R4[User anlegen]
R4 --> L

%% HOME
H --> N1[Zu Tasks]
H --> N2[Zu Weekly Plan]
H --> N3[Zu Progress]
H --> O[Logout]

O --> L

%% TASKS
N1 --> T[Tasks Screen]
T --> T1[Neue Aufgabe speichern]
T1 --> T2{Budget ok?}
T2 -- Nein --> T3[Fehlermeldung]
T3 --> T
T2 -- Ja --> T4[Task speichern]
T4 --> T

T --> T5[Status toggeln]
T --> T6[Task löschen]

%% PLAN
N2 --> P[Weekly Plan]

%% PROGRESS
N3 --> G[Progress]