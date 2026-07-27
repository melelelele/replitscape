import java.util.Objects;

public final class GemahlenerKaffee {
    private final String sorte;

    public GemahlenerKaffee(Kaffeebohnen bohnen) {
        Kaffeebohnen sichereBohnen = Objects.requireNonNull(
                bohnen,
                "bohnen dürfen nicht null sein"
        );
        this.sorte = sichereBohnen.getSorte();
    }

    public String getSorte() {
        return sorte;
    }
}
