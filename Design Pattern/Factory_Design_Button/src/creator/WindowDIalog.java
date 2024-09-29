package creator;

import product.Button;
import product.WindowsButton;

public class WindowDIalog extends Dialog{
    @Override
    protected Button createButton() {
        return new WindowsButton();
    }
}
