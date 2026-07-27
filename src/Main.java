public final class Main {
    private Main() {
    }

    public static void main(String[] args) {
        Kuechengeraet geraet = KuechenSetup.initialisiereGeraet();
        System.out.println("Gerätetyp: " + geraet.getGeraetetyp());

        if (geraet instanceof Teekanne teekanne) {
            Tee tee = teekanne.teeKochen(new Wasser(250));
            System.out.println("Getränk: " + tee.getSorte());
            return;
        }

        if (geraet instanceof Kaffeemaschine kaffeemaschine) {
            Espresso espresso = kaffeemaschine.espresso(new Wasser(30));
            Cappuccino cappuccino = kaffeemaschine.cappuccino(
                    new Wasser(30),
                    new Milch(120)
            );

            System.out.println("Espresso: " + (espresso != null ? "bereit" : "fehlt"));
            System.out.println("Cappuccino: " + (cappuccino != null ? "bereit" : "fehlt"));
        }
    }
}
