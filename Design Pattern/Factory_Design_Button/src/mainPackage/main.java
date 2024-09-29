package mainPackage;

import creator.Dialog;
import creator.WebDialog;
import creator.WindowDIalog;

public class main {
    public static Dialog dialog;

    public static void main(String[] args) {
        configure();
        dialog.renderWindow();
    }

    static void configure(){
        String osName = System.getProperty("os.name").toLowerCase();

        if(osName.contains("windows")){
            dialog = new WindowDIalog();
        }else{
            dialog = new WebDialog();
        }
    }
}
