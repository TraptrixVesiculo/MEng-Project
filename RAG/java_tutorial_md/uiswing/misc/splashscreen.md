[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** Creating a GUI With JFC/Swing
  
**Lesson:** Using Other Swing Features

[Using Other Swing Features](index.html)

[How to Integrate with the Desktop Class](desktop.html)

[How to Create Translucent and Shaped Windows](trans_shaped_windows.html)

[How to Decorate Components with JLayer](jlayer.html)

[How to Use Actions](action.html)

[How to Use Swing Timers](timer.html)

[How to Support Assistive Technologies](access.html)

[How to Use the Focus Subsystem](focus.html)

[How to Use Key Bindings](keybinding.html)

[How to Use Modality in Dialogs](modality.html)

[How to Print Tables](printtable.html)

[How to Print Text](printtext.html)

How to Create a Splash Screen

[How to Use the System Tray](systemtray.html)

[Solving Common Problems Using Other Swing Features](problems.html)

[Home Page](../../index.html)
>
[Creating a GUI With JFC/Swing](../index.html)
>
[Using Other Swing Features](index.html)

[« Previous](printtext.html) • [Trail](../TOC.html) • [Next »](systemtray.html)

# How to Create a Splash Screen

Almost all modern applications have a splash screen. Typically splash screens are used for the
following purposes:

* Advertising a product
* Indicating to the user that the application is launching during long
  startup times
* Providing information that is only needed once per visit

Java Foundation Classes, both Swing and Abstract Windowing Toolkit (AWT), enable a developer to create splash screens in
Java technology applications. However, because the main purpose of a splash screen is to provide the user
with feedback about the application's startup, the delay between the application's startup
and the moment when the splash screen pops up should be minimal.
Before the splash screen can pop up, the application has to load and initialize the Java™ Virtual Machine (JVM),
AWT, Swing, and sometimes application-dependent libraries as well.
The resulting delay of several seconds has made the use of a Java™ technology-based splash screen less than desirable.

Fortunately, Java™ SE 6 provides a solution that allows the application to display
the splash screen much earlier, even before the virtual machine starts.
A Java application launcher is able to decode an image and display it in a simple non-decorated window.

The splash screen can display any `gif`, `png`, or `jpeg` image,
with transparency, translucency, and animation.
The figure below represents an example of the Java application splash screen developed as an animated `gif` file.

![Splash Screen for Java Application](../../figures/uiswing/misc/splash.gif)

The
[`SplashScreen`](http://download.oracle.com/javase/7/docs/api/java/awt/SplashScreen.html) class is used to close the splash screen, change the splash-screen image, obtain the image position or size,
and paint in the splash screen.
An application cannot create an instance of this class. Only a single instance created within this class can exist,
and this instance can be obtained using the `getSplashScreen()` static method.
If the application has not created the splash screen at startup through the command-line or manifest-file option,
the `getSplashScreen` method returns null.

Typically, a developer wants to keep the splash-screen image on the screen and display something over the image.
The splash-screen window has an overlay surface with an alpha channel,
and this surface can be accessed with a traditional `Graphics2D` interface.

The following code snippet shows how to obtain a `SplashScreen` object,
then how to create a graphics context with the `createGraphics()` method:

```

...
        final SplashScreen splash = SplashScreen.getSplashScreen();
        if (splash == null) {
            System.out.println("SplashScreen.getSplashScreen() returned null");
            return;
        }
        Graphics2D g = splash.createGraphics();
        if (g == null) {
            System.out.println("g is null");
            return;
        }
...

```

Find the demo's complete code in the
[`SplashDemo.java`](../examples/misc/SplashDemoProject/src/misc/SplashDemo.java) file.

---

**Note:** The SplashDemo application uses fixed coordinates to display overlay information.
These coordinates are image-dependent and calculated individually for each splash screen.

---

The native splash screen can be displayed in the following ways:

* Command-line argument
* Java™ Archive (JAR) file with the specified manifest option

### How to Use the Command-Line Argument to Display a Splash Screen
> To display a splash screen from the command line use the `-splash:` command-line argument.
> This argument is a Java application launcher option that displays a splash screen:
>
> ```
>
> java -splash:<file name> <class name>
>
> ```
>
> ---
>
> **Try this:**
>
> 1. Compile the
>    [`SplashDemo.java`](../examples/misc/SplashDemoProject/src/misc/SplashDemo.java) file.
> 2. Save the
>    [`splash.gif`](../examples/misc/SplashDemoProject/src/misc/images/splash.gif) image in the `images` directory.
> 3. Run the application from the command line with the following arguments:
>
>    ```
>
>    java -splash:images/splash.gif SplashDemo
>
>    ```
> 4. Wait until the splash screen has been completely displayed.
> 5. The application window appears. To close the window choose File|Exit from the
>    pop-up menu or click the X.
> 6. Change the splash screen name to a non-existent image, for example, `nnn.gif`.
>    Run the application as follows:
>
>    ```
>
>    java -splash:images/nnn.gif SplashDemo
>
>    ```
> 7. You will see the following output string:
>
>    ```
>
>    SplashScreen.getSplashScreen() returned null
>
>    ```
>
> ---

### How to Use a JAR File to Display Splash Screen
> If your application is packaged in a JAR file, you can use the `SplashScreen-Image` option
> in a manifest file to show a splash screen. Place the image in the JAR file and specify the path in the option as follows:
>
> ```
>
> Manifest-Version: 1.0
> Main-Class: <class name>
> SplashScreen-Image: <image name>
>
> ```
>
> ---
>
> **Try this:**
>
> 1. Compile the
>    [`SplashDemo.java`](../examples/misc/SplashDemoProject/src/misc/SplashDemo.java) file.
> 2. Save the
>    [`splash.gif`](../examples/misc/SplashDemoProject/src/misc/images/splash.gif) image in the `images` directory.
> 3. Prepare the `splashmanifest.mf` file as follows:
>
>    ```
>
>    Manifest-Version: 1.0
>    Main-Class: SplashDemo
>    SplashScreen-Image: images/splash.gif
>
>    ```
> 4. Create a JAR file using the following command:
>
>    ```
>
>    jar cmf splashmanifest.mf splashDemo.jar SplashDemo*.class images/splash.gif
>
>    ```
>
>    For more information about JAR files, see
>    [Using JAR Files](../../deployment/jar/basicsindex.html) in the
>    [Packaging Programs in JAR Files](../../deployment/jar/index.html) page.
> 5. Run the application:
>
>    ```
>
>    java -jar splashDemo.jar
>
>    ```
> 6. Wait until the splash screen has been completly displayed.
> 7. The application window appears. To close the window choose File|Exit from the
>    pop-up menu or click the X.
>
> ---
>
> ### The Splash Screen API
>
> > The `SplashScreen` class cannot be used to create the splash screen. Only a single instance created within this class can exist.
> >
> > | Method | Purpose |
> > | --- | --- |
> > | [getSplashScreen()](http://download.oracle.com/javase/7/docs/api/java/awt/SplashScreen.html#getSplashScreen()) | Returns the `SplashScreen` object used for Java startup splash screen control. |
> > | [createGraphics()](http://download.oracle.com/javase/7/docs/api/java/awt/SplashScreen.html#createGraphics()) | Creates a graphics context (as a `Graphics2D` object) for the splash screen overlay image, which allows you to draw over the splash screen. |
> > | [getBounds()](http://download.oracle.com/javase/7/docs/api/java/awt/SplashScreen.html#getBounds()) | Returns the bounds of the splash screen window as a `Rectangle`. |
> > | [close()](http://download.oracle.com/javase/7/docs/api/java/awt/SplashScreen.html#close()) | Closes the splash screen and releases all associated resources. |
>
> ### Example That Uses the SplashScreen API
> > The following table lists the
> > example that uses splash screen.
> >
> > | Example | Where Described | Notes |
> > | --- | --- | --- |
> > | [`SplashDemo`](../examples/misc/index.html#SplashDemo) | This section | Shows a splash screen before opening the application window. |

[« Previous](printtext.html)
•
[Trail](../TOC.html)
•
[Next »](systemtray.html)

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

**Previous page:** How to Print Text
  
**Next page:** How to Use the System Tray




A browser with JavaScript enabled is required for this page to operate properly.