[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** Creating a GUI With JFC/Swing
  
**Lesson:** Modifying the Look and Feel

[Modifying the Look and Feel](index.html)

How to Set the Look and Feel

[The Synth Look and Feel](synth.html)

[A Synth Example](synthExample.html)

[Nimbus Look and Feel](nimbus.html)

[Changing the Look of Nimbus](custom.html)

[Resizing a Component](size.html)

[Changing the Color Theme](color.html)

[For More Information](info.html)

[Home Page](../../index.html)
>
[Creating a GUI With JFC/Swing](../index.html)
>
[Modifying the Look and Feel](index.html)

[« Previous](index.html) • [Trail](../TOC.html) • [Next »](synth.html)

# How to Set the Look and Feel

The architecture of Swing is designed so that you may change the "look and feel" (L&F) of your application's GUI (see
[A Swing Architecture Overview](http://java.sun.com/products/jfc/tsc/articles/architecture/index.html)).
"Look" refers to the appearance of GUI widgets (more formally,
`JComponents`) and "feel" refers to the way the widgets behave.

Swing's architecture enables multiple L&Fs by separating every
component into two distinct classes: a `JComponent` subclass
and a corresponding `ComponentUI` subclass.
For example, every `JList`
instance has a concrete implementation of `ListUI` (`ListUI` extends
`ComponentUI`). The `ComponentUI` subclass is referred to by various names
in Swing's documentation—"the UI," "component UI," "UI delegate," and
"look and feel delegate" are all used to identify the `ComponentUI` subclass.

Most developers never need to
interact with the UI delegate directly. For the most part, the UI
delegate is used internally by the `JComponent` subclass for crucial
functionality, with cover methods provided by the `JComponent` subclass
for all access to the UI delegate. For example, all painting in
`JComponent` subclasses is delegated to the UI delegate. By delegating
painting, the 'look' can vary depending upon the L&F.

It is the responsibility of each L&F to provide a concrete
implementation for each of the `ComponentUI` subclasses defined by Swing.
For example, the Java Look and Feel creates an instance of
`MetalTabbedPaneUI` to provide the L&F for `JTabbedPane`.
The actual creation of the UI delegate is handled by Swing for you—for the
most part you never need to interact directly with the UI delegate.

The rest of this section discusses the following subjects:

* [Available Look and Feels](#available)* [Programatically Setting the Look and Feel](#programmatic)* [Specifying the Look and Feel: Command Line](#commandLine)* [Specifying the Look and Feel: swing.properties](#properties)* [How the UI Manager Chooses the Look and Feel](#steps)* [Changing the Look and Feel After Startup](#dynamic)* [An Example](#example)* [Themes](#themes)* [The SwingSet2 Demonstration Program](#swingset2)

### Available Look and Feels

Sun's JRE provides the following L&Fs:

1. `CrossPlatformLookAndFeel`—this is the "Java L&F" (also called "Metal") that looks the same on all
   platforms. It is part of the Java API (`javax.swing.plaf.metal`) and
   is the default that will be used if you do nothing in your code to set a different L&F.

- `SystemLookAndFeel`—here, the application uses the L&F that is native to the system it is running on.
  The System L&F is determined at runtime, where
  the application asks the system to return the name of the appropriate L&F.

- Synth—the basis for creating your own look and feel with an XML file.

- Multiplexing— a way to have the UI methods delegate to a number
  of different look and feel implementations at the same time.

For Linux and Solaris, the System L&Fs are "GTK+" if GTK+ 2.2 or later is installed, "Motif" otherwise. For Windows,
the System L&F is
"Windows," which mimics the L&F of the particular Windows OS that is running—classic Windows, XP, or Vista.
The GTK+, Motif, and Windows L&Fs are provided by Sun and shipped with the Java SDK and JRE, although they are not
part of the Java API.

Apple provides its own JVM which includes their proprietary L&F.

In summary, when you use the `SystemLookAndFeel`, this is what you will see:

System Look and Feel| **Platform** | **Look and Feel** |
| Solaris, Linux with GTK+ 2.2 or later | GTK+ |
| Other Solaris, Linux | Motif |
| IBM UNIX | IBM\* |
| HP UX | HP\* |
| Classic Windows | Windows |
| Windows XP | Windows XP |
| Windows Vista | Windows Vista |
| Macintosh | Macintosh\* |

\* Supplied by the system vendor.

You don't see the System L&F in the API. The GTK+, Motif, and Windows packages that it requires are shipped with the Java SDK as:

```

com.sun.java.swing.plaf.gtk.GTKLookAndFeel
com.sun.java.swing.plaf.motif.MotifLookAndFeel
com.sun.java.swing.plaf.windows.WindowsLookAndFeel

```

Note that the path includes `java`, and not `javax`.

---

**Note:** The GTK+ L&F will only run on UNIX or Linux systems with GTK+ 2.2 or later installed, while the Windows L&F runs only on
Windows systems.
Like the Java (Metal) L&F, the Motif L&F will run on any platform.

---

All of Sun's L&Fs have a great deal of commonality. This commonality is defined in the
`Basic`  look and feel in the API (`javax.swing.plaf.basic`). The Motif and Windows L&Fs are
each built by extending
the UI delegate classes in `javax.swing.plaf.basic` (a custom L&F can be built by doing the same thing).
The "Basic" L&F is not
used without being extended.

In the API you will see four L&F packages:

* `javax.swing.plaf.basic`—basic UI Delegates to be extended when creating a custom L&F

* `javax.swing.plaf.metal`—the Java L&F, also known as the CrossPlatform L&F
  ("Metal" was the Sun project name for this L&F) The current default "theme" (discussed below) for this L&F is "Ocean,
  so this is often referred to as the Ocean L&F.

* `javax.swing.plaf.multi`—a multiplexing look and feel that
  allows the UI methods to delegate to a
  number of look and feel implementations at the same time.
  It can be used to augment the behavior of a particular look and feel, for
  example with a L&F that provides audio cues on top of the Windows look and feel.
  This is a way of creating a handicapped-accessible look and feel.

* `javax.swing.plaf.synth`—an easily configured L&F using XML
  files (discussed in the next section of this lesson)

You aren't limited to the L&Fs supplied with
the Java platform. You can use any L&F that is in your program's class path. External L&Fs are usually provided in one or more JAR files that you add to your program's class path at runtime. For example:

```

java -classpath .;C:\java\lafdir\customlaf.jar YourSwingApplication

```

Once an external L&F is in your program's class path,
your program can use it just like any of the L&Fs
shipped with the Java platform.

### Programatically Setting the Look and Feel

> ---
>
> **Note:** If you are going to set the L&F,
> you should do it as the very first step in your application.
> Otherwise you run the risk of initializing the Java L&F
> regardless of what L&F you've
> requested. This can happen inadvertently when a static field
> references a Swing class, which causes the L&F
> to be loaded. If no L&F has yet been
> specified, the default L&F for the JRE is loaded. For Sun's JRE the default is the Java L&F,
> for Apple's JRE the Apple L&F, and so forth.
>
> ---
>
> The L&F that Swing components use is specified by way of the `UIManager` class in the `javax.swing`
> package. Whenever a Swing component is created,the component asks the UI manager for the
> UI delegate that implements the component's L&F. For example, each `JLabel` constructor
> queries the UI manager for the UI delegate object appropriate for the label. It then uses that UI delegate
> object to implement all of its drawing and event handling.
>
> To programatically specify a L&F,
> use the `UIManager.setLookAndFeel()` method with the fully qualified name of the appropriate subclass of
> `LookAndFeel` as its argument.
> For example, the bold code in the following snippet
> makes the program use the cross-platform Java L&F:
>
> ```
>
> public static void main(String[] args) {
>     try {
> 	    // Set cross-platform Java L&F (also called "Metal")
>         UIManager.setLookAndFeel(
>             UIManager.getCrossPlatformLookAndFeelClassName());
>     } 
>     catch (UnsupportedLookAndFeelException e) {
>        // handle exception
>     }
>     catch (ClassNotFoundException e) {
>        // handle exception
>     }
>     catch (InstantiationException e) {
>        // handle exception
>     }
>     catch (IllegalAccessException e) {
>        // handle exception
>     }
> 	
>     new SwingApplication(); //Create and show the GUI.
> }
>
> ```
>
> Alternatively, this code makes the program use the System L&F:
>
> ```
>
> public static void main(String[] args) {
>     try {
> 	    // Set System L&F
>         UIManager.setLookAndFeel(
>             UIManager.getSystemLookAndFeelClassName());
>     } 
>     catch (UnsupportedLookAndFeelException e) {
>        // handle exception
>     }
>     catch (ClassNotFoundException e) {
>        // handle exception
>     }
>     catch (InstantiationException e) {
>        // handle exception
>     }
>     catch (IllegalAccessException e) {
>        // handle exception
>     }
>
>     new SwingApplication(); //Create and show the GUI.
> }
>
> ```
>
> You can also use the actual class name of a Look and Feel as the argument to
> `UIManager.setLookAndFeel()`. For example,
>
> ```
>
> // Set cross-platform Java L&F (also called "Metal")
> UIManager.setLookAndFeel("javax.swing.plaf.metal.MetalLookAndFeel");
>
> ```
>
> or
>
> ```
>
> // Set Motif L&F on any platform
> UIManager.setLookAndFeel("com.sun.java.swing.plaf.motif.MotifLookAndFeel");
>
> ```
>
> You aren't limited to the preceding arguments.
> You can specify the name for any L&F
> that is in your program's class path.

### Specifying the Look and Feel: Command Line

> You can specify the L&F at the command line by
> using the `-D` flag to set the
> `swing.defaultlaf` property. For example:
>
> ```
>
> java -Dswing.defaultlaf=com.sun.java.swing.plaf.gtk.GTKLookAndFeel MyApp
>
> java -Dswing.defaultlaf=com.sun.java.swing.plaf.windows.WindowsLookAndFeel MyApp
>
> ```

### Specifying the Look and Feel: swing.properties File

> Yet another way to specify the current L&F is to use the
> `swing.properties` file to set the `swing.defaultlaf`
> property. This file, which you may need to create, is located
> in the `lib` directory of Sun's Java release (other vendors of Java may
> use a different location).
> For example, if you're using the Java interpreter
> in `javaHomeDirectory\bin`,
> then the `swing.properties` file (if it exists)
> is in `javaHomeDirectory\lib`.
> Here is an example of the contents of a
> [`swing.properties`](swing.properties)
> file:
>
> ```
>
> # Swing properties
> swing.defaultlaf=com.sun.java.swing.plaf.windows.WindowsLookAndFeel
>
> ```

### How the UI Manager Chooses the Look and Feel

> Here are the look-and-feel determination steps
> that occur when the UI manager needs to set a L&F:
>
> 1. If the program sets the L&F
>    before a look and feel is needed,
>    the UI manager tries to create an instance
>    of the specified look-and-feel class.
>    If successful,
>    all components use that L&F.
>
>    - If the program hasn't successfully specified
>      a L&F, then the UI manager uses the
>      L&F specified by the `swing.defaultlaf`
>      property. If the property is specified in both
>      the `swing.properties`
>      file *and* on the command line, the command-line
>      definition takes precedence.
>
>      - If none of these steps has resulted in a valid
>        L&F,
>        Sun's JRE uses the Java L&F. Other vendors, such as Apple, will use their default L&F.

### Changing the Look and Feel After Startup

> You can change the L&F
> with `setLookAndFeel`
> even after the program's GUI is visible.
> To make existing components reflect the new L&F,
> invoke the
> `SwingUtilities` `updateComponentTreeUI` method
> once per top-level container.
> Then you might wish to resize each top-level container
> to reflect the new sizes of its contained components.
> For example:
>
> ```
>
> UIManager.setLookAndFeel(lnfName);
> SwingUtilities.updateComponentTreeUI(frame);
> frame.pack();
>
> ```

### An Example

> In the following example, `LookAndFeelDemo.java`, you can experiment with
> different Look and Feels. The program creates a simple GUI with a button and a label.
> Every time you click the button, the label increments.
>
> You can change the L&F by changing the `LOOKANDFEEL` constant on line 18. The comments on the preceding lines
> tell you what values are acceptable:
>
> ```
>
>     // Specify the look and feel to use by defining the LOOKANDFEEL constant
>     // Valid values are: null (use the default), "Metal", "System", "Motif",
>     // and "GTK"
>     final static String LOOKANDFEEL = "Motif";
>
> ```
>
> Here the constant is set to "Motif", which is a L&F that will run on any platform (as will the default, "Metal"). "GTK+" will not run on Windows,
> and "Windows" will run only on Windows. If you choose a L&F that will not run, you will get the Java, or Metal, L&F.
>
> In the section of the code where the L&F is actually set, you will see several different ways to set it, as discussed above:
>
> ```
>
> if (LOOKANDFEEL.equals("Metal")) {
>    lookAndFeel = UIManager.getCrossPlatformLookAndFeelClassName();
>    //  an alternative way to set the Metal L&F is to replace the 
>    // previous line with:
>    // lookAndFeel = "javax.swing.plaf.metal.MetalLookAndFeel";
>
> ```
>
> You can verify that both arguments work by commenting/un-commenting the two alternatives.
>
> Here is a listing of the
> [`LookAndFeelDemo`](../examples/lookandfeel/LookAndFeelDemoProject/src/lookandfeel/LookAndFeelDemo.java)
> source file:
>
> ```
>
>
> package lookandfeel;
>
> import javax.swing.*;          
> import java.awt.*;
> import java.awt.event.*;
> import javax.swing.plaf.metal.*;
>
> public class LookAndFeelDemo implements ActionListener {
>     private static String labelPrefix = "Number of button clicks: ";
>     private int numClicks = 0;
>     final JLabel label = new JLabel(labelPrefix + "0    ");
>
>     // Specify the look and feel to use by defining the LOOKANDFEEL constant
>     // Valid values are: null (use the default), "Metal", "System", "Motif",
>     // and "GTK"
>     final static String LOOKANDFEEL = "Metal";
>     
>     // If you choose the Metal L&F, you can also choose a theme.
>     // Specify the theme to use by defining the THEME constant
>     // Valid values are: "DefaultMetal", "Ocean",  and "Test"
>     final static String THEME = "Test";
>     
>
>     public Component createComponents() {
>         JButton button = new JButton("I'm a Swing button!");
>         button.setMnemonic(KeyEvent.VK_I);
>         button.addActionListener(this);
>         label.setLabelFor(button);
>
>         JPanel pane = new JPanel(new GridLayout(0, 1));
>         pane.add(button);
>         pane.add(label);
>         pane.setBorder(BorderFactory.createEmptyBorder(
>                                         30, //top
>                                         30, //left
>                                         10, //bottom
>                                         30) //right
>                                         );
>
>         return pane;
>     }
>
>     public void actionPerformed(ActionEvent e) {
>         numClicks++;
>         label.setText(labelPrefix + numClicks);
>     }
>
>     private static void initLookAndFeel() {
>         String lookAndFeel = null;
>        
>         if (LOOKANDFEEL != null) {
>             if (LOOKANDFEEL.equals("Metal")) {
>                 lookAndFeel = UIManager.getCrossPlatformLookAndFeelClassName();
>               //  an alternative way to set the Metal L&F is to replace the 
>               // previous line with:
>               // lookAndFeel = "javax.swing.plaf.metal.MetalLookAndFeel";
>                 
>             }
>             
>             else if (LOOKANDFEEL.equals("System")) {
>                 lookAndFeel = UIManager.getSystemLookAndFeelClassName();
>             } 
>             
>             else if (LOOKANDFEEL.equals("Motif")) {
>                 lookAndFeel = "com.sun.java.swing.plaf.motif.MotifLookAndFeel";
>             } 
>             
>             else if (LOOKANDFEEL.equals("GTK")) { 
>                 lookAndFeel = "com.sun.java.swing.plaf.gtk.GTKLookAndFeel";
>             } 
>             
>             else {
>                 System.err.println("Unexpected value of LOOKANDFEEL specified: "
>                                    + LOOKANDFEEL);
>                 lookAndFeel = UIManager.getCrossPlatformLookAndFeelClassName();
>             }
>
>             try {
>             	
>             	
>                 UIManager.setLookAndFeel(lookAndFeel);
>                 
>                 // If L&F = "Metal", set the theme
>                 
>                 if (LOOKANDFEEL.equals("Metal")) {
>                   if (THEME.equals("DefaultMetal"))
>                      MetalLookAndFeel.setCurrentTheme(new DefaultMetalTheme());
>                   else if (THEME.equals("Ocean"))
>                      MetalLookAndFeel.setCurrentTheme(new OceanTheme());
>                   else
>                      MetalLookAndFeel.setCurrentTheme(new TestTheme());
>                      
>                   UIManager.setLookAndFeel(new MetalLookAndFeel()); 
>                 }	
>                 	
>                 	
>                   
>                 
>             } 
>             
>             catch (ClassNotFoundException e) {
>                 System.err.println("Couldn't find class for specified look and feel:"
>                                    + lookAndFeel);
>                 System.err.println("Did you include the L&F library in the class path?");
>                 System.err.println("Using the default look and feel.");
>             } 
>             
>             catch (UnsupportedLookAndFeelException e) {
>                 System.err.println("Can't use the specified look and feel ("
>                                    + lookAndFeel
>                                    + ") on this platform.");
>                 System.err.println("Using the default look and feel.");
>             } 
>             
>             catch (Exception e) {
>                 System.err.println("Couldn't get specified look and feel ("
>                                    + lookAndFeel
>                                    + "), for some reason.");
>                 System.err.println("Using the default look and feel.");
>                 e.printStackTrace();
>             }
>         }
>     }
>
>     private static void createAndShowGUI() {
>         //Set the look and feel.
>         initLookAndFeel();
>
>         //Make sure we have nice window decorations.
>         JFrame.setDefaultLookAndFeelDecorated(true);
>
>         //Create and set up the window.
>         JFrame frame = new JFrame("SwingApplication");
>         frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
>
>         LookAndFeelDemo app = new LookAndFeelDemo();
>         Component contents = app.createComponents();
>         frame.getContentPane().add(contents, BorderLayout.CENTER);
>
>         //Display the window.
>         frame.pack();
>         frame.setVisible(true);
>     }
>
>     public static void main(String[] args) {
>         //Schedule a job for the event dispatch thread:
>         //creating and showing this application's GUI.
>         javax.swing.SwingUtilities.invokeLater(new Runnable() {
>             public void run() {
>                 createAndShowGUI();
>             }
>         });
>     }
> }
>
> ```

### Themes

> Themes were introduced as a way of easily changing the colors and fonts of the
> cross-platform Java (Metal) Look and Feel.
> In the sample program, `LookAndfeelDemo.java`, listed above,
> you can change the theme of the Metal L&F by
> setting the `THEME` constant on line 23 to one of three values:
>
> * `DefaultMetal`
> * `Ocean`
> * `Test`
>
> `Ocean`, which is a bit softer than the pure Metal look,
> has been the default theme for the Metal (Java) L&F since Java SE 5.
> Despite its name, `DefaultMetal` is not the default theme for Metal
> (it was before Java SE 5, which explains its name).
> The `Test` theme is a theme defined in
> [`TestTheme.java`](../examples/lookandfeel/LookAndFeelDemoProject/src/lookandfeel/TestTheme.java), which you must compile
> with `LookAndfeelDemo.java`.
> As it is written, `TestTheme.java` sets
> the three primary colors (with somewhat bizarre results).
> You can modify `TestTheme.java` to test any colors you like.
>
> The section of code where the theme is set is found beginning on line 92
> of `LookAndfeelDemo.java`.
> Note that you must be using the Metal L&F to set a theme.
>
> ```
>
>  if (LOOKANDFEEL.equals("Metal")) {
>     if (THEME.equals("DefaultMetal"))
>        MetalLookAndFeel.setCurrentTheme(new DefaultMetalTheme());
>     else if (THEME.equals("Ocean"))
>        MetalLookAndFeel.setCurrentTheme(new OceanTheme());
>     else
>        MetalLookAndFeel.setCurrentTheme(new TestTheme());
>                      
>     UIManager.setLookAndFeel(new MetalLookAndFeel()); 
>  }	
>
> ```

### The SwingSet2 Demonstration Program

> In your JDK 6 installation, there is a `demo\jfc` folder that contains a
> demonstration program called `SwingSet2`. This program has a graphically rich
> GUI and allows you to change the Look and Feel from the menu. Further,
> if you are using the Java (Metal) Look and Feel, you can choose a variety of different
> themes. The files for the various themes (for example, `RubyTheme.java`) are found
> in the `SwingSet2\src` folder.
>
> This is the "Ocean" theme, which is the default for the cross-platform Java (Metal) Look and Feel:
>
> ![](../../figures/uiswing/lookandfeel/OceanLAF.gif)
>
> This is the "Steel" theme, which was the original theme for the cross-platform Java (Metal) Look and Feel:
>
> ![](../../figures/uiswing/lookandfeel/MetalLAF.gif)
>
> To run the `SwingSet2` demo program on a system that has the JDK installed, use this command:
>
> ```
>
> java -jar SwingSet2.jar
>
> ```
>
> This will give you the default theme of Ocean.
>
> To get the metal L&F, run this:
>
> ```
>
> java -Dswing.metalTheme=steel -jar SwingSet2.jar
>
> ```
>
> It is also possible to run the SwingSet2 demo program with Java Web Start:
>
> ```
>
> http://java.sun.com/products/jfc/jws/SwingSet2.jnlp
> ```

[« Previous](index.html)
•
[Trail](../TOC.html)
•
[Next »](synth.html)

---

Problems with the examples? Try [Compiling and Running
the Examples: FAQs](../../information/run-examples.html).
  
Complaints? Compliments? Suggestions? [Give
us your feedback](http://download.oracle.com/javase/feedback.html).

Your use of this page and all the material on pages under "The Java Tutorials" banner,
and all the material on pages under "The Java Tutorials" banner is subject to the [Java SE Tutorial Copyright
and License](../../information/license.html).
Additionally, any example code contained in any of these Java
Tutorials pages is licensed under the
[Code
Sample License](http://developers.sun.com/license/berkeley_license.html).

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| |  |  | | --- | --- | | duke image | Oracle logo | | [About Oracle](http://www.oracle.com/us/corporate/index.html) | [Oracle Technology Network](http://www.oracle.com/technology/index.html) | [Terms of Service](https://www.samplecode.oracle.com/servlets/CompulsoryClickThrough?type=TermsOfService) | Copyright © 1995, 2011 Oracle and/or its affiliates. All rights reserved. |

**Previous page:** Modifying the Look and Feel
  
**Next page:** The Synth Look and Feel




A browser with JavaScript enabled is required for this page to operate properly.