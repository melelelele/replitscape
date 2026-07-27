import java.util.Objects;

public final class HeissesWasser {
    private final Wasser wasser;

    public HeissesWasser(Wasser wasser) {
        this.wasser = Objects.requireNonNull(wasser, "wasser darf nicht null sein");
    }

    public Wasser getWasser() {
        return wasser;
    }
}
