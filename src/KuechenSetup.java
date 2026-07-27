public final class KuechenSetup {
    private KuechenSetup() {
        // Diese Klasse enthält ausschließlich die zentrale Initialisierung.
    }

    public static Kuechengeraet initialisiereGeraet() {
        // Aufgabe 6:
        // Der Praktikant hat hier eine Teekanne initialisiert.
        // Ersetze sie durch eine Kaffeemaschine mit:
        // - einer Kaffeedose mit Arabica-Kaffeebohnen,
        // - einem Mahlwerk,
        // - einem Wassererhitzer,
        // - einem Milchaufschaeumer.
        return new Teekanne(
                new Wassererhitzer(),
                new Teedose("Kamillentee")
        );
    }
}
