import java.util.Objects;

public final class Tee {
    private final String sorte;
    private final HeissesWasser wasser;

    public Tee(String sorte, HeissesWasser wasser) {
        if (sorte == null || sorte.isBlank()) {
            throw new IllegalArgumentException("Die Teesorte darf nicht leer sein.");
        }
        this.sorte = sorte.strip();
        this.wasser = Objects.requireNonNull(wasser, "wasser darf nicht null sein");
    }

    public String getSorte() {
        return sorte;
    }

    public HeissesWasser getWasser() {
        return wasser;
    }
}
