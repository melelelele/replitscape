import java.util.Objects;

public final class Cappuccino {
    private final Espresso espresso;
    private final Milchschaum milchschaum;

    public Cappuccino(Espresso espresso, Milchschaum milchschaum) {
        this.espresso = Objects.requireNonNull(espresso, "espresso darf nicht null sein");
        this.milchschaum = Objects.requireNonNull(
                milchschaum,
                "milchschaum darf nicht null sein"
        );
    }

    public Espresso getEspresso() {
        return espresso;
    }

    public Milchschaum getMilchschaum() {
        return milchschaum;
    }
}
