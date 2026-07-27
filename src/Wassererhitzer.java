import java.util.Objects;

public final class Wassererhitzer {
    public HeissesWasser erhitzen(Wasser wasser) {
        // Der Wassererhitzer funktioniert bereits.
        // Als Teekanne konnte das Gerät schließlich schon heißes Wasser erzeugen.
        return new HeissesWasser(
                Objects.requireNonNull(wasser, "wasser darf nicht null sein")
        );
    }
}
