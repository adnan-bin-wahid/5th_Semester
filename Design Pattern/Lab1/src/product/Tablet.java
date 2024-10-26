package product;

public class Tablet implements Device{

    public String TabletMode;
    public void tabletBehavior(){
        System.out.println("Tablet is running");
    }
    @Override
    public void powerOff() {
        System.out.println("Tablet is On");
    }

    @Override
    public void powerOn() {
        System.out.println("Tablet is Off");
    }
}
