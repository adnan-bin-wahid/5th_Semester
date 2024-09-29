import com.phone.*;
public class FactoryMain {
    public static void main(String[] args) {
        OSfactory osf = new OSfactory();
        OS obj1 = osf.getInstance("Die");
        obj1.spec();
    }
}
