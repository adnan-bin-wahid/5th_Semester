package creator;

import product.Button;
import product.HTMLButton;

public class WebDialog extends Dialog{
    @Override
    protected Button createButton() {
        return new HTMLButton();
    }
}
