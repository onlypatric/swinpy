JFRAME_STR = """
import javax.swing.*;
import javax.swing.border.*;

import java.awt.*;

import java.util.prefs.Preferences;
/**
 * GUI class
 */
public class Application extends JFrame {
    private static final String WIDTH_KEY = "width";
    private static final String HEIGHT_KEY = "height";
    private static final String POS_X = "x";
    private static final String POS_Y = "y";
    private Container cp;
    
    private Preferences preferences;
    public Application(){
        super();
        cp=this.getContentPane();
        cp.setLayout({LAYOUT});
        this.setTitle("Application");
        this.setDefaultCloseOperation(EXIT_ON_CLOSE);
        preferences = Preferences.userNodeForPackage(Application.class);
        int width = preferences.getInt(WIDTH_KEY, 300);
        int height = preferences.getInt(HEIGHT_KEY, 400);
        int posx = preferences.getInt(POS_X, 100);
        int posy = preferences.getInt(POS_Y, 100);
        
        this.setSize(width, height);
        this.setLocation(posx, posy);
        this.addWindowListener(new java.awt.event.WindowAdapter() {
            @Override
            public void windowClosing(java.awt.event.WindowEvent windowEvent) {
                saveUserDimensions();
                System.exit(0);
            }
        });
        this.setupApp();
    }
    private void setupApp(){
{CHILDS}
    }

    public void saveUserDimensions() {
        preferences.putInt(WIDTH_KEY, getWidth());
        preferences.putInt(HEIGHT_KEY, getHeight());
        preferences.putInt(POS_X, getX());
        preferences.putInt(POS_Y, getY());
    }

    public void startApp(boolean packElements){
        if(packElements) this.pack();
        this.setVisible(true);
    }
    public static void main(String[] args) {
        Application app = new Application();
        app.startApp(false);
    }
}"""
