import java.util.Objects;

public final class Espresso {
    private final GemahlenerKaffee kaffee;
    private final HeissesWasser wasser;

    public Espresso(GemahlenerKaffee kaffee, HeissesWasser wasser) {
        this.kaffee = Objects.requireNonNull(kaffee, "kaffee darf nicht null sein");
        this.wasser = Objects.requireNonNull(wasser, "wasser darf nicht null sein");
    }

    public GemahlenerKaffee getKaffee() {
        return kaffee;
    }

    public HeissesWasser getWasser() {
        return wasser;
    }
}
