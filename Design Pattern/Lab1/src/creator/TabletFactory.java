package creator;

import product.Device;
import product.Tablet;

public class TabletFactory extends Factory {
    @Override
    public Device createDevice() {
        return new Tablet();
    }
}
