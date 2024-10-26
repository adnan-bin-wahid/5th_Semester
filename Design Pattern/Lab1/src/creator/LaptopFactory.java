package creator;

import product.Device;
import product.Laptop;

public class LaptopFactory extends Factory {

    @Override
    public Device createDevice() {
        return new Laptop();
    }
}
