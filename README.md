# CodeScape: Programmierquiz mit Replit

Dieses Repository enthält das vorbereitete Replit-Projekt für einen kleinen CScape-Escape-Room.

Die Spielenden bearbeiten in Replit die Datei `quiz.py`. Ein Flask-Server führt die Tests aus und stellt den aktuellen Status unter `/status` als JSON bereit. CScape fragt diese URL regelmäßig ab und schaltet nach korrekt gelösten Aufgaben die passenden Folien frei.

## Projektstruktur

```text
replit-setup/
├── quiz.py
├── tests.py
├── server.py
├── requirements.txt
├── .replit
├── .gitignore
└── README.md
```
## Anmelden
melde dich bei Replit an. Verwende oder erstelle dabei am besten einen Account, hinter dem keine kritischen Zahlungsinformationen oder andere Daten hinterlegt sind, da dieser Account den Spielenden zur Verfügung gestellt werden muss.
## Replit-Projekt importieren

Für dieses öffentliche GitHub-Repository kann der direkte Replit-Import verwendet werden:

```text
https://replit.com/github.com/melelelele/replit-setup
```

Alternativ:

1. Öffne `https://replit.com/import`.
2. Wähle **GitHub**.
3. Füge diese Repository-URL ein:

   ```text
   https://github.com/melelelele/replit-setup
   ```

4. Klicke auf **Import**.

Replit importiert die Dateien, Ordner, Abhängigkeiten und die übliche Startkonfiguration des Repositorys.

## Server in Replit starten

Klicke nach dem Import auf **Run**.

Der konfigurierte Startbefehl lautet:

```bash
python server.py
```

Falls Replit die Abhängigkeiten nicht automatisch installiert, führe in der Replit-Shell aus:

```bash
python -m pip install -r requirements.txt
```

Starte danach erneut:

```bash
python server.py
```

Der Server verwendet Port `3000`.

## Status-URL ermitteln

Wenn der Server läuft, zeigt Replit eine öffentliche Webansicht beziehungsweise Web-URL an.

Ergänze diese URL um:

```text
/status
```

Beispiel:

```text
https://deine-app.replit.dev/status
```

Die Antwort sollte am Anfang ungefähr so aussehen:

```json
{
  "all": false,
  "errors": [],
  "q1": false,
  "q2": false,
  "q3": false
}
```

Diese vollständige `/status`-URL wird in CScape eingetragen.

### Wichtig

Verwende nicht die Editor-URL:

```text
https://replit.com/@user/projektname
```

Verwende die öffentliche Web-URL des laufenden Servers mit `/status`.

## Aufgaben für die Spielenden

Die Spielenden bearbeiten `quiz.py`.

Zu Beginn enthält die Datei:

```python
def greet(name):
    # Aufgabe 1:
    # Gib "Hallo, <name>!" zurück.
    return ""


def add(a, b):
    # Aufgabe 2:
    # Gib die Summe von a und b zurück.
    return 0


def is_even(number):
    # Aufgabe 3:
    # Gib True zurück, wenn number gerade ist, sonst False.
    return False
```

Die Aufgaben sind:

1. `greet(name)` soll `Hallo, <name>!` zurückgeben.
2. `add(a, b)` soll die Summe von `a` und `b` zurückgeben.
3. `is_even(number)` soll `True` für gerade und `False` für ungerade Zahlen zurückgeben.

Der Server lädt `quiz.py` bei jeder Anfrage an `/status` neu. Normalerweise ist nach einer Änderung kein Neustart erforderlich.

## Tests manuell ausführen

In der Replit-Shell:

```bash
python tests.py
```

Am Anfang sollte ungefähr Folgendes erscheinen:

```text
{'q1': False, 'q2': False, 'q3': False, 'all': False, 'errors': []}
```

## Richtige Lösung

Die vollständige Lösung lautet:

```python
def greet(name):
    return f"Hallo, {name}!"


def add(a, b):
    return a + b


def is_even(number):
    return number % 2 == 0
```

Danach liefert `/status`:

```json
{
  "all": true,
  "errors": [],
  "q1": true,
  "q2": true,
  "q3": true
}
```

## CScape lokal starten

Wechsle lokal in den CScape-Ordner und starte CScape:

```bash
./run.sh
```

Alternativ aus dem übergeordneten Repository-Ordner:

```bash
./cscape/run.sh
```

Falls zusätzlich dynamische Sprachausgabe genutzt wird:

```bash
python3 tts_server.py
```

Öffne anschließend:

```text
http://localhost:5000
```

Auf der ersten Folie:

1. die vollständige Replit-`/status`-URL eintragen,
2. auf **Link speichern** klicken,
3. anschließend `quiz.py` in Replit bearbeiten.

## Architektur

```text
Spielende
    │
    ▼
Replit-Projekt
├── quiz.py       # wird von den Spielenden bearbeitet
├── tests.py      # prüft die Aufgaben
└── server.py     # stellt /status bereit
    │
    ▼
CScape lokal
```

## Bedeutung der Dateien

### `quiz.py`

Enthält die Aufgaben, die von den Spielenden bearbeitet werden.

### `tests.py`

Prüft die drei Funktionen und liefert für jede Aufgabe einen booleschen Status.

### `server.py`

Startet den Flask-Server und stellt `/status` bereit.

### `requirements.txt`

Enthält die Python-Abhängigkeiten:

```text
Flask
flask-cors
```

### `.replit`

Legt den Startbefehl fest:

```toml
run = "python server.py"
```
## Eigene Aufgaben
Um eigene, weitere Aufgaben zu erstellen, muss das GitHub-Repository github.com/melelelele/replit-setup geforkt und bearbeitet werden. Neue Aufgaben werden in quiz.py erstellt und entsprechende Tests werden in der test.py geschrieben. Der Status der Tests kann wie gewohnt in der game.py abgefragt werden und somit neue Slides in der index.html getriggert werden.
