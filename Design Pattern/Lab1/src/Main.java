import creator.Factory;
import creator.LaptopFactory;
import creator.SmartPhoneFactory;
import creator.TabletFactory;
import product.Device;

import java.util.Scanner;

public class Main {


    public static void main(String[] args) {
        int choice;
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter your choice\n");
        System.out.println("1.SmartPhone\n");
        System.out.println("2.Tablet\n");
        System.out.println("3.Laptop\n");
        System.out.println("What do you want to create: ");
        choice = sc.nextInt();
        sc.nextLine();
        Factory f;
        Device d;
        switch (choice){
            case 1 :
                f = new SmartPhoneFactory();
                d = f.createDevice();
                d.powerOff();
                d.powerOff();
                break;
            case 2 :
                f = new TabletFactory();
                d = f.createDevice();
                d.powerOff();
                d.powerOn();
                break;
            case 3 :
                f = new LaptopFactory();
                d = f.createDevice();
                d.powerOff();
                d.powerOn();
                break;
        }

    }


}
