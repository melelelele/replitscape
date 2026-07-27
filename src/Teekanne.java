import java.util.Objects;

public final class Teekanne implements Kuechengeraet {
    private final Wassererhitzer wassererhitzer;
    private final Teedose teedose;

    public Teekanne(Wassererhitzer wassererhitzer, Teedose teedose) {
        this.wassererhitzer = Objects.requireNonNull(
                wassererhitzer,
                "wassererhitzer darf nicht null sein"
        );
        this.teedose = Objects.requireNonNull(teedose, "teedose darf nicht null sein");
    }

    @Override
    public String getGeraetetyp() {
        return "Teekanne";
    }

    public Tee teeKochen(Wasser wasser) {
        HeissesWasser heissesWasser = wassererhitzer.erhitzen(wasser);
        return new Tee(teedose.entnehmen(), heissesWasser);
    }
}
