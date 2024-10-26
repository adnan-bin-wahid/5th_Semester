package product;

import javax.swing.text.Style;

public class SmartPhone implements Device{

    public String SmartPhoneModel;
    public void SmartPhonebehavior(){
        System.out.println("Smartphone is running");
    }
    @Override
    public void powerOff() {
        System.out.println("Smart Phone is On");
    }

    @Override
    public void powerOn() {
        System.out.println("Smart Phone is Off");
    }
}
