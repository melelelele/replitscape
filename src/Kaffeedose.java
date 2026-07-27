import java.util.Objects;

public final class Kaffeedose {
    private final Kaffeebohnen bohnen;

    public Kaffeedose(Kaffeebohnen bohnen) {
        this.bohnen = Objects.requireNonNull(bohnen, "bohnen dürfen nicht null sein");
    }

    public Kaffeebohnen entnehmen() {
        // Aufgabe 1:
        // Gib die im Feld bohnen gespeicherten Kaffeebohnen zurück.
        return null;
    }
}
