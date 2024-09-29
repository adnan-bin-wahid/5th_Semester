package product;

public class HTMLButton implements Button{
    @Override
    public void render() {
        System.out.println("<button>Render an HTML button</button>");
    }

    @Override
    public void onClick() {
        System.out.println("HTML button clicked!");
    }
}
