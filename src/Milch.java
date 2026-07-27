public final class Milch {
    private final int milliliter;

    public Milch(int milliliter) {
        if (milliliter <= 0) {
            throw new IllegalArgumentException("Die Milchmenge muss größer als 0 ml sein.");
        }
        this.milliliter = milliliter;
    }

    public int getMilliliter() {
        return milliliter;
    }
}
