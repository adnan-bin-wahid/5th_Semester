package product;

public class WindowsButton implements Button{
    @Override
    public void render() {
        System.out.println("Render a Windows Button");
    }

    @Override
    public void onClick() {
        System.out.println("Windows button Clicked");
    }
}
