package product;


public class Laptop implements Device{

    public String LaptopModel;

    public void laptopBehavior(){
        System.out.println("Laptop is running");
    }

    @Override
    public void powerOff() {
        System.out.println(" Laptop is On");
    }

    @Override
    public void powerOn() {
        System.out.println(" Laptop is Off");
    }
}
