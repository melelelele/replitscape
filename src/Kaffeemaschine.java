import java.util.Objects;

public final class Kaffeemaschine implements Kuechengeraet {
    private final Kaffeedose kaffeedose;
    private final Mahlwerk mahlwerk;
    private final Wassererhitzer wassererhitzer;
    private final Milchaufschaeumer milchaufschaeumer;

    public Kaffeemaschine(
            Kaffeedose kaffeedose,
            Mahlwerk mahlwerk,
            Wassererhitzer wassererhitzer,
            Milchaufschaeumer milchaufschaeumer
    ) {
        this.kaffeedose = Objects.requireNonNull(
                kaffeedose,
                "kaffeedose darf nicht null sein"
        );
        this.mahlwerk = Objects.requireNonNull(mahlwerk, "mahlwerk darf nicht null sein");
        this.wassererhitzer = Objects.requireNonNull(
                wassererhitzer,
                "wassererhitzer darf nicht null sein"
        );
        this.milchaufschaeumer = Objects.requireNonNull(
                milchaufschaeumer,
                "milchaufschaeumer darf nicht null sein"
        );
    }

    @Override
    public String getGeraetetyp() {
        return "Kaffeemaschine";
    }

    public Espresso espresso(Wasser wasser) {
        // Aufgabe 3:
        // 1. Hole die Kaffeebohnen aus der Kaffeedose.
        // 2. Mahle die Bohnen mit dem Mahlwerk.
        // 3. Erhitze das Wasser mit dem Wassererhitzer.
        // 4. Erzeuge daraus einen Espresso und gib ihn zurück.
        return null;
    }

    public Cappuccino cappuccino(Wasser wasser, Milch milch) {
        // Aufgabe 5:
        // 1. Bereite mit espresso(...) einen Espresso zu.
        // 2. Schäume die Milch mit dem Milchaufschäumer auf.
        // 3. Erzeuge daraus einen Cappuccino und gib ihn zurück.
        return null;
    }
}
