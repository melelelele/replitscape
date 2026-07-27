public final class Wasser {
    private final int milliliter;

    public Wasser(int milliliter) {
        if (milliliter <= 0) {
            throw new IllegalArgumentException("Die Wassermenge muss größer als 0 ml sein.");
        }
        this.milliliter = milliliter;
    }

    public int getMilliliter() {
        return milliliter;
    }
}
