# CodeScape: Programmierquiz mit Replit

Dieser Escape Room ist ein minimaler CScape-Raum, bei dem die Spielerinnen und Spieler kleine Programmieraufgaben in einem gemeinsamen Replit-Projekt lösen. CScape läuft lokal als Regiemodul und fragt regelmäßig eine Status-URL des Replit-Projekts ab. Sobald ein Test in Replit erfolgreich ist, wird die nächste Folie im Escape Room freigeschaltet.

## Idee des Escape Rooms

Die Spielenden arbeiten an einer Datei `quiz.py`. Dort sind drei Funktionen vorbereitet:

```python
def greet(name):
    return ""


def add(a, b):
    return 0


def is_even(number):
    return False
```

Die Aufgaben sind bewusst klein gehalten:

1. `greet(name)` soll einen Namen begrüßen.
2. `add(a, b)` soll zwei Zahlen addieren.
3. `is_even(number)` soll prüfen, ob eine Zahl gerade ist.

Ein kleiner Flask-Server in Replit stellt unter `/status` den aktuellen Teststatus als JSON bereit. CScape liest diese URL aus und prüft dadurch, ob die einzelnen Aufgaben gelöst sind.

Beispiel für `/status`:

```json
{
  "q1": true,
  "q2": false,
  "q3": false,
  "all": false,
  "errors": []
}
```

## Architektur

```text
Spielende / Regie
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

Der Replit-Link wird nicht fest in `game.py` eingetragen. Stattdessen fragt die erste Folie in der Story nach der Replit-URL und speichert sie im CScape-Store.

## Lokales CScape vorbereiten

Wechsle in den replit Ordner:

```bash
cd ~/Dokumente/GitHub/cscaperooms/replit/cscape
```

Starte dort wie gewohnt CScape.

Öffne danach im Browser:

```text
http://localhost:5000
```


## Replit-Projekt erstellen

### 1. Replit öffnen

Öffne Replit im Browser, melde dich an und erstelle ein neues Python-Projekt. Verwende dafür am Besten einen Account, der extra für diesen Zweck erstellt wurde, nicht eine wichtige E-Mail-Adresse von dir verwendet und keine Zahlungsinformationen hinterlegt hat, wenn Studierende den Escaperoom unbeaufsichtigt spielen sollen, um dich zu schützen.

### 2. Dateien in Replit anlegen

Lege diese Dateien an:

```text
quiz.py
tests.py
server.py
.replit
```

Falls `.replit` nicht sichtbar ist, aktiviere in der Dateiliste die Anzeige versteckter Dateien.

## Replit-Datei: `quiz.py`

Diese Datei bearbeiten die Spielenden.

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

## Replit-Datei: `tests.py`

Diese Datei enthält die Tests. Die Spielenden sollten diese Datei normalerweise nicht bearbeiten.

```python
import quiz


def run_tests():
    results = {
        "q1": False,
        "q2": False,
        "q3": False,
        "all": False,
        "errors": []
    }

    try:
        results["q1"] = (
            quiz.greet("Ada") == "Hallo, Ada!"
            and quiz.greet("Linus") == "Hallo, Linus!"
        )
    except Exception as error:
        results["errors"].append(f"q1: {type(error).__name__}: {error}")

    try:
        results["q2"] = (
            quiz.add(2, 3) == 5
            and quiz.add(-4, 10) == 6
            and quiz.add(0, 0) == 0
        )
    except Exception as error:
        results["errors"].append(f"q2: {type(error).__name__}: {error}")

    try:
        results["q3"] = (
            quiz.is_even(2) is True
            and quiz.is_even(7) is False
            and quiz.is_even(0) is True
        )
    except Exception as error:
        results["errors"].append(f"q3: {type(error).__name__}: {error}")

    results["all"] = results["q1"] and results["q2"] and results["q3"]
    return results


if __name__ == "__main__":
    print(run_tests())
```

## Replit-Datei: `server.py`

Diese Datei startet den Flask-Server und stellt `/status` bereit.

```python
from flask import Flask, jsonify
from flask_cors import CORS
import importlib
import tests
import quiz

app = Flask(__name__)
CORS(app)


@app.get("/")
def index():
    return """
    <h1>CodeScape Quiz Server</h1>
    <p>Open <a href="/status">/status</a> to see the current test status.</p>
    """


@app.get("/status")
def status():
    try:
        importlib.reload(quiz)
        importlib.reload(tests)

        response = jsonify(tests.run_tests())
        response.headers["Cache-Control"] = "no-store, no-cache, must-revalidate, max-age=0"
        response.headers["Pragma"] = "no-cache"
        response.headers["Expires"] = "0"
        return response

    except Exception as error:
        response = jsonify({
            "q1": False,
            "q2": False,
            "q3": False,
            "all": False,
            "errors": [f"{type(error).__name__}: {error}"]
        })
        response.headers["Cache-Control"] = "no-store, no-cache, must-revalidate, max-age=0"
        return response


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)
```

## Replit-Datei: `.replit`

Diese Datei legt fest, was beim Start ausgeführt wird.

```toml
run = "python server.py"
```

Falls in `.replit` bereits andere Inhalte stehen, sollte mindestens der `run`-Eintrag auf `python server.py` zeigen.

## Flask in Replit installieren

Öffne in Replit die Shell und installiere:

```bash
pip install flask flask-cors
```


## Replit-Server starten

Starte in Replit entweder über den Start-/Run-Button oder in der Shell:

```bash
python server.py
```

Wenn der Server läuft, erscheint in der Shell ungefähr:

```text
Running on http://127.0.0.1:3000
Running on http://0.0.0.0:3000
```

Replit zeigt außerdem einen Hinweis, dass Port `3000` geöffnet wurde. Klicke auf den angezeigten Replit-Link.

Öffne dann:

```text
DEINE-REPLIT-WEB-URL/status
```

Du solltest JSON sehen, zum Beispiel:

```json
{
  "all": false,
  "errors": [],
  "q1": false,
  "q2": false,
  "q3": false
}
```

Diese `/status`-URL ist die URL, die du in CScape am Anfang einträgst.

Wichtig: Nicht die Editor-URL eintragen.

Falsch:

```text
https://replit.com/@user/Quiz-Status?replId=...
```

Richtig:

```text
https://irgendeine-replit-web-url.replit.dev/status
```

oder:

```text
https://quiz-status.user.replit.app/status
```

## CScape mit Replit verbinden

1. Starte lokal CScape.
2. Öffne `http://localhost:5000`.
3. Auf der ersten Folie erscheint ein Eingabefeld für den Replit-Link.
4. Trage die `/status`-URL ein.
5. Klicke auf „Link speichern“.
6. CScape prüft, ob die URL JSON mit den Keys `q1`, `q2`, `q3` und `all` liefert.
7. Wenn die Verbindung stimmt, wird die nächste Folie freigeschaltet.

## Richtige Lösung für das Quiz

Die Spielenden sollen im Verlauf ungefähr diese Lösung erreichen:

```python
def greet(name):
    return f"Hallo, {name}!"


def add(a, b):
    return a + b


def is_even(number):
    return number % 2 == 0
```

Danach sollte `/status` so aussehen:

```json
{
  "all": true,
  "errors": [],
  "q1": true,
  "q2": true,
  "q3": true
}
```
## Spielbetrieb

Für den Spielbetrieb empfiehlt sich:
- Der Spielleiter erstellt das Replit-Projekt wie oben beschrieben.
- Der Spielleiter startet CScape auf einem Raspberry Pi oder einem anderen Computer.
- Der Spielleiter trägt in CScape die Replit-Status-URL ein.
- Die Spielenden bearbeiten die quiz.py-Datei entsprechend der cscape-Story.
- CScape läuft weiter und prüft automatisch die Aufgaben.
- Nach jeder korrekt gelösten Aufgabe schaltet CScape die passende Erfolgsfolie frei.

## Erweiterungsmöglichkeiten

Du kannst später weitere Aufgaben ergänzen, indem du:

1. Eine neue Funktion in `quiz.py` anlegst.
2. Einen neuen Test in `tests.py` ergänzt.
3. Im JSON einen neuen Key ergänzt, zum Beispiel `q4`.
4. In `game.py` eine neue Check-Funktion anlegst, zum Beispiel `check_q4_done`.
5. In `index.html` eine neue CScape-Folie mit `data-cscape-check="check_q4_done"` ergänzt.


## Kurzfassung

```text
Replit:
- quiz.py wird bearbeitet
- tests.py prüft Aufgaben
- server.py stellt /status bereit

CScape:
- erste Folie speichert Replit-/status-URL
- game.py fragt /status ab
- Slides werden durch check_q1_done, check_q2_done, check_q3_done und check_all_done freigeschaltet
```
