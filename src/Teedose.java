public final class Teedose {
    private final String sorte;

    public Teedose(String sorte) {
        if (sorte == null || sorte.isBlank()) {
            throw new IllegalArgumentException("Die Teesorte darf nicht leer sein.");
        }
        this.sorte = sorte.strip();
    }

    public String entnehmen() {
        return sorte;
    }
}
