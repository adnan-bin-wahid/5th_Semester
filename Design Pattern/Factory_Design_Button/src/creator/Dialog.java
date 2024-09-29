package creator;

import product.Button;

public abstract class Dialog {
    public void renderWindow(){
        Button okButton = createButton();
        okButton.onClick();
        okButton.render();
    }

    protected abstract Button createButton();
}
