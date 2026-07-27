public final class Kaffeebohnen {
    private final String sorte;

    public Kaffeebohnen(String sorte) {
        if (sorte == null || sorte.isBlank()) {
            throw new IllegalArgumentException("Die Kaffeesorte darf nicht leer sein.");
        }
        this.sorte = sorte.strip();
    }

    public String getSorte() {
        return sorte;
    }
}
