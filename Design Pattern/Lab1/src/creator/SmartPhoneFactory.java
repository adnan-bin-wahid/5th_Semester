package creator;

import product.Device;
import product.SmartPhone;

public class SmartPhoneFactory extends Factory {
    @Override
    public Device createDevice() {
        return new SmartPhone();
    }
}
