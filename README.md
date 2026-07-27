# JavaScape: Programmierquiz mit Replit

Dieses Repository enthält den CScape-Room **JavaScape: Die Teekanne** und das dazugehörige Java-Projekt für Replit.

Die Spielenden bearbeiten in Replit die Dateien eines fehlerhaften Küchen-Setups. Das Gerät startet als funktionierende Teekanne und wird in sechs aufeinander aufbauenden Aufgaben zu einer vollständigen Kaffeemaschine repariert.

Ein kleiner, direkt in Java implementierter HTTP-Server kompiliert das Projekt bei jeder Anfrage neu, führt die Tests aus und stellt den aktuellen Aufgabenstatus unter `/status` als JSON bereit. CScape ruft diesen Status regelmäßig ab. Normale Story-Folien laufen automatisch weiter; an den Aufgabenfolien wartet der Raum, bis die jeweilige Java-Aufgabe korrekt gelöst wurde.

## Vorbereitungen für den Spieler-PC

### Anmelden

Melde dich bei Replit an. Verwende oder erstelle dabei am besten einen Account, hinter dem keine kritischen Zahlungsinformationen oder anderen privaten Daten hinterlegt sind, da dieser Account den Spielenden während des Escape Rooms zur Verfügung gestellt werden muss.

### Replit-Projekt importieren

Die Beispieldateien für diesen Escape Room befinden sich in [diesem Repository](https://github.com/melelelele/replit-setup).

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

Replit importiert die Dateien, Ordner und die Startkonfiguration des Repositorys. Das Projekt ist für Java 17 eingerichtet.

## Server in Replit starten

Klicke nach dem Import auf **Run**.

Das Startskript kompiliert `Server.java` und startet den Java-HTTP-Server. Der eigentliche Aufgaben-Code im Ordner `src/` wird anschließend bei jeder Anfrage an `/status` erneut kompiliert und getestet. Nach Änderungen an einer Aufgaben-Datei ist deshalb normalerweise kein Neustart des Replit-Servers erforderlich.

### Status-URL ermitteln

Wenn der Server läuft, zeigt Replit eine öffentliche Webansicht beziehungsweise Web-URL an.

Ergänze diese URL um:

```text
/status
```

Beispiel:

```text
https://deine-app.replit.dev/status
```

Die Antwort sollte im ungelösten Startzustand ungefähr so aussehen:

```json
{
  "q1": false,
  "q2": false,
  "q3": false,
  "q4": false,
  "q5": false,
  "q6": false,
  "all": false,
  "errors": []
}
```

Diese vollständige `/status`-URL wird in der `game.py` des CScape-Projekts als `REPLIT_STATUS_URL` eingetragen.

#### Wichtig

Verwende nicht die Editor-URL:

```text
https://replit.com/@user/projektname
```

Verwende die öffentliche Web-URL des laufenden Servers mit angehängtem `/status`.

Bei einem Kompilierungs- oder Laufzeitfehler bleiben die betroffenen Aufgaben auf `false`. Zusätzliche Hinweise stehen dann im Feld `errors`.

## Aufgaben für die Spielenden

Die Spielenden bearbeiten ausschließlich die folgenden sechs Aufgabenstellen im Ordner `src/`.

### Aufgabe 1: Kaffeebohnen entnehmen

Datei:

```text
src/Kaffeedose.java
```

Die Methode `entnehmen()` soll die im Feld `bohnen` gespeicherten Kaffeebohnen zurückgeben.

### Aufgabe 2: Kaffeebohnen mahlen

Datei:

```text
src/Mahlwerk.java
```

Die Methode `mahlen(...)` soll aus den übergebenen `Kaffeebohnen` ein neues `GemahlenerKaffee`-Objekt erzeugen und zurückgeben.

### Aufgabe 3: Espresso zubereiten

Datei:

```text
src/Kaffeemaschine.java
```

Die Methode `espresso(...)` soll:

1. Kaffeebohnen aus der Kaffeedose entnehmen,
2. die Bohnen mit dem Mahlwerk mahlen,
3. das Wasser mit dem Wassererhitzer erhitzen,
4. aus gemahlenem Kaffee und heißem Wasser einen Espresso erzeugen.

### Aufgabe 4: Milch aufschäumen

Datei:

```text
src/Milchaufschaeumer.java
```

Die Methode `aufschaeumen(...)` soll aus der übergebenen Milch ein neues `Milchschaum`-Objekt erzeugen und zurückgeben.

### Aufgabe 5: Cappuccino zubereiten

Datei:

```text
src/Kaffeemaschine.java
```

Die Methode `cappuccino(...)` soll:

1. mit `espresso(...)` einen Espresso zubereiten,
2. die Milch mit dem Milchaufschäumer aufschäumen,
3. aus Espresso und Milchschaum einen Cappuccino erzeugen.

### Aufgabe 6: Kaffeemaschine initialisieren

Datei:

```text
src/KuechenSetup.java
```

Die bisherige Teekanne soll durch eine vollständige Kaffeemaschine ersetzt werden. Die Kaffeemaschine benötigt:

- eine `Kaffeedose` mit Arabica-Kaffeebohnen,
- ein `Mahlwerk`,
- einen `Wassererhitzer`,
- einen `Milchaufschaeumer`.

Der Wassererhitzer ist bereits korrekt implementiert. Das ist innerhalb der Geschichte logisch, weil das Gerät schon als Teekanne heißes Wasser erzeugen und Kamillentee kochen kann.

## Richtige Lösung

> **Hinweis für die Spielleitung:** Dieser Abschnitt enthält die vollständigen Lösungen. Er sollte nicht in einer Version stehen, die die Spielenden einsehen können.

### Aufgabe 1 – `Kaffeedose.entnehmen()`

```java
return bohnen;
```

### Aufgabe 2 – `Mahlwerk.mahlen(...)`

```java
return new GemahlenerKaffee(bohnen);
```

### Aufgabe 3 – `Kaffeemaschine.espresso(...)`

```java
Kaffeebohnen bohnen = kaffeedose.entnehmen();
GemahlenerKaffee kaffee = mahlwerk.mahlen(bohnen);
HeissesWasser heissesWasser = wassererhitzer.erhitzen(wasser);

return new Espresso(kaffee, heissesWasser);
```

### Aufgabe 4 – `Milchaufschaeumer.aufschaeumen(...)`

```java
return new Milchschaum(milch);
```

### Aufgabe 5 – `Kaffeemaschine.cappuccino(...)`

```java
Espresso espresso = espresso(wasser);
Milchschaum milchschaum = milchaufschaeumer.aufschaeumen(milch);

return new Cappuccino(espresso, milchschaum);
```

### Aufgabe 6 – `KuechenSetup.initialisiereGeraet()`

```java
return new Kaffeemaschine(
        new Kaffeedose(new Kaffeebohnen("Arabica")),
        new Mahlwerk(),
        new Wassererhitzer(),
        new Milchaufschaeumer()
);
```

Danach liefert `/status`:

```json
{
  "q1": true,
  "q2": true,
  "q3": true,
  "q4": true,
  "q5": true,
  "q6": true,
  "all": true,
  "errors": []
}
```

Die Tests sind aufeinander aufbauend. Eine spätere Aufgabe wird nur als gelöst markiert, wenn auch die vorherigen Voraussetzungen erfüllt sind.

## Manuelle Prüfung in Replit

Die Tests können zusätzlich direkt im Replit-Terminal ausgeführt werden:

```bash
bash test.sh
```

Das Skript kompiliert die Java-Dateien gemeinsam mit `TestRunner.java` und gibt den gleichen JSON-Status aus wie der Endpunkt `/status`.

## Setup für den Raspberry Pi

Klone dieses CScape-Repository auf den Raspberry Pi und wechsle in den lokalen Projektordner.

Bearbeite anschließend die `game.py` und setze darin die vollständige öffentliche Replit-`/status`-URL:

```python
REPLIT_STATUS_URL = "https://deine-app.replit.dev/status"
```

Danach starte CScape wie gewohnt:

```bash
./run.sh
```

Falls die dynamische Sprachausgabe verwendet wird, muss zusätzlich der TTS-Server gestartet werden. Öffne dafür ein zweites Terminal im Projektordner:

```bash
python3 tts_server.py
```

Der TTS-Server läuft standardmäßig unter:

```text
http://localhost:8765
```

Öffne anschließend den CScape-Room im Browser:

```text
http://localhost:5000
```

Die `game.py` startet außerdem eine lokale Status-Bridge unter:

```text
http://127.0.0.1:5001/status
```

Diese lokale URL wird von der `index.html` verwendet. Die öffentliche Replit-URL muss deshalb nur einmal in der `game.py` eingetragen werden.

## Bedeutung der Dateien in Replit

### Projektsteuerung

| Datei | Bedeutung |
|---|---|
| `.replit` | Legt fest, welcher Befehl beim Klick auf **Run** ausgeführt wird. |
| `replit.nix` | Stellt die benötigte Java-Umgebung in Replit bereit. |
| `run.sh` | Kompiliert `Server.java` und startet den HTTP-Server. |
| `test.sh` | Kompiliert das Aufgabenprojekt und führt `TestRunner` manuell aus. |
| `.gitignore` | Schließt erzeugte Build-Ordner und temporäre Dateien von Git aus. |

### Server und Tests

| Datei | Bedeutung |
|---|---|
| `Server.java` | Stellt `/`, `/health` und `/status` bereit. Bei `/status` werden die Dateien in `src/` neu kompiliert und getestet. |
| `TestRunner.java` | Prüft die sechs Aufgaben und erzeugt die JSON-Werte `q1` bis `q6`, `all` und `errors`. |
| `build/` | Wird automatisch erzeugt und enthält die kompilierten Klassen. Der Ordner muss nicht manuell bearbeitet werden. |

### Aufgaben- und Modellklassen

| Datei | Bedeutung |
|---|---|
| `src/Kuechengeraet.java` | Gemeinsames Interface für Teekanne und Kaffeemaschine. |
| `src/Teekanne.java` | Funktionierendes Startgerät mit Wassererhitzer und Teedose. |
| `src/Teedose.java` | Speichert die Teesorte und gibt sie beim Entnehmen zurück. |
| `src/Tee.java` | Repräsentiert einen zubereiteten Tee. |
| `src/Kaffeedose.java` | Speichert die Kaffeebohnen; enthält Aufgabe 1. |
| `src/Kaffeebohnen.java` | Repräsentiert Kaffeebohnen einer bestimmten Sorte. |
| `src/Mahlwerk.java` | Mahlt Kaffeebohnen; enthält Aufgabe 2. |
| `src/GemahlenerKaffee.java` | Repräsentiert gemahlenen Kaffee und speichert dessen Sorte. |
| `src/Wasser.java` | Repräsentiert eine Wassermenge in Millilitern. |
| `src/Wassererhitzer.java` | Erhitzt Wasser und funktioniert bereits im Startzustand. |
| `src/HeissesWasser.java` | Repräsentiert erhitztes Wasser. |
| `src/Kaffeemaschine.java` | Verbindet die Komponenten; enthält die Aufgaben 3 und 5. |
| `src/Espresso.java` | Besteht aus gemahlenem Kaffee und heißem Wasser. |
| `src/Milch.java` | Repräsentiert eine Milchmenge in Millilitern. |
| `src/Milchaufschaeumer.java` | Schäumt Milch auf; enthält Aufgabe 4. |
| `src/Milchschaum.java` | Repräsentiert aufgeschäumte Milch. |
| `src/Cappuccino.java` | Besteht aus Espresso und Milchschaum. |
| `src/KuechenSetup.java` | Baut das Startgerät auf; enthält Aufgabe 6. |
| `src/Main.java` | Kleine Demonstration des aktuell initialisierten Geräts. |

## Verbindung zwischen Replit und CScape

Die Statuskette besteht aus drei Stufen:

1. Der Java-Server in Replit kompiliert und testet das Projekt.
2. Die `game.py` ruft die öffentliche Replit-URL ab und stellt das Ergebnis lokal unter Port `5001` bereit.
3. Die `index.html` fragt die lokale Status-Bridge ab und wartet auf Aufgabenfolien auf den jeweiligen Schlüssel `q1` bis `q6`.

Die Replit-URL steht dadurch nicht in der `index.html`. Sie wird ausschließlich in der `game.py` gepflegt.

## Eigene Aufgaben

Um eigene oder weitere Aufgaben zu erstellen, muss das GitHub-Repository [replit-setup](https://github.com/melelelele/replit-setup) geforkt und angepasst werden.

Für eine zusätzliche Aufgabe, beispielsweise `q7`, sind Änderungen an mehreren Stellen notwendig.

### 1. Neue Java-Aufgabe erstellen

Ergänze eine neue unvollständige Methode oder Klasse im Ordner `src/`. Die Aufgabenstellung sollte direkt als Kommentar an der zu bearbeitenden Stelle stehen.

Achte darauf, dass:

- nur die vorgesehene Stelle unvollständig ist,
- alle benötigten Hilfsklassen bereits funktionieren,
- die neue Aufgabe logisch auf den vorherigen Aufgaben aufbaut,
- das Projekt auch im ungelösten Zustand kompiliert.

### 2. Test in `TestRunner.java` ergänzen

Erstelle eine neue Prüfmethode, beispielsweise:

```java
private static boolean testQ7(List<String> errors) {
    try {
        // Lösung fachlich prüfen
        return true;
    } catch (Throwable error) {
        errors.add(formatError("q7", error));
        return false;
    }
}
```

Ergänze `q7` anschließend in der Statusberechnung und in der ausgegebenen JSON-Struktur. `all` darf erst dann `true` werden, wenn auch `q7` gelöst wurde.

Die Tests sollten nicht nur prüfen, ob ein Ergebnis ungleich `null` ist. Prüfe nach Möglichkeit auch:

- die verwendeten Eingabewerte,
- die enthaltenen Komponenten,
- Mengen oder Sorten,
- mehrere unterschiedliche Testfälle,
- die Abhängigkeit von früheren Aufgaben.

### 3. Statusschlüssel in `game.py` ergänzen

Erweitere:

```python
STATUS_KEYS = ("q1", "q2", "q3", "q4", "q5", "q6", "q7", "all")
```

Ergänze bei Bedarf außerdem eine CScape-Prüfmethode:

```python
def check_q7_done(self):
    return self.safe_check("q7")
```

Die aktuelle Aufgaben-Sperrlogik der `index.html` verwendet zwar direkt die lokalen Statuswerte, die Prüfmethode ist aber sinnvoll, wenn die Aufgabe zusätzlich über `data-cscape-check` genutzt werden soll.

### 4. Aufgabenfolie in `index.html` ergänzen

Eine Aufgabenfolie benötigt:

```html
<section
    data-layout="dialogue"
    data-wait-key="q7"
    data-speaker="PROFESSOR NULLPOINTER"
    data-avatar="pics/nullpointer.png"
    data-dialogue="Hier steht der zur Geschichte passende Dialog."
    data-task="Hier steht die konkrete Programmieraufgabe.">
    <div class="scene"></div>
</section>
```

Wichtig:

- Die Aufgabenfolie erhält **kein** `data-after-ready-delay`.
- `data-wait-key` muss exakt dem JSON-Schlüssel aus Replit entsprechen.
- Die nachfolgende Erfolgsfolie kann wieder `data-after-ready-delay="2"` verwenden.
- Dialog und Aufgabe sollten getrennt bleiben: Storytext in `data-dialogue`, konkrete Arbeitsanweisung in `data-task`.

### 5. Dokumentation und Lösungen aktualisieren

Ergänze die neue Aufgabe in:

- dieser README,
- einer gegebenenfalls getrennten Lehrkraft-Lösungsdatei,
- der Aufgabenübersicht,
- dem erwarteten `/status`-Beispiel.

Teste danach mindestens:

1. den vollständig ungelösten Zustand,
2. jede einzelne Zwischenstufe,
3. die vollständig gelöste Variante,
4. den `/status`-Endpunkt über die öffentliche Replit-URL,
5. das Warten und automatische Fortsetzen im CScape-Room.

## Hinweise zur Modellierung

Das Projekt ist bewusst übersichtlich gehalten:

- Die Zutaten und Getränke sind kleine, unveränderliche Objekte.
- Konstruktoren prüfen ungültige Mengen sowie leere oder fehlende Werte.
- `Teedose` und `Kaffeedose` sind beide zustandsbehaftet.
- `GemahlenerKaffee` speichert die Kaffeesorte und nicht unverändert das vollständige Bohnenobjekt als fachlichen Zustand.
- `KuechenSetup` ist der zentrale Ort, an dem das vollständige Gerät zusammengesetzt wird.
- Der Wassererhitzer ist keine Aufgabe, weil er bereits für die Teekanne benötigt wird.

## Hinweis zu Story Styles

Dieser Escape Room verwendet die Story-Styles-Erweiterung für CScape. Sie ermöglicht einen dialogbasierten Escape Room im Stil eines Text-Adventures beziehungsweise Visual Novels.

Die Erweiterung unterstützt unter anderem:

- Figurenporträts,
- Dialog- und Aufgaben-Panels,
- Typewriter-Text,
- Hintergrundmusik und Figurensounds,
- dynamische Sprachausgabe,
- automatische Folienwechsel,
- die Verbindung mit CScape-Aufgabenprüfungen.

Weitere Informationen befinden sich im Repository [story-styles](https://github.com/melelelele/story-styles).
