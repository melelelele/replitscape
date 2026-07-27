import java.util.Objects;

public final class Milchschaum {
    private final Milch milch;

    public Milchschaum(Milch milch) {
        this.milch = Objects.requireNonNull(milch, "milch darf nicht null sein");
    }

    public Milch getMilch() {
        return milch;
    }
}
