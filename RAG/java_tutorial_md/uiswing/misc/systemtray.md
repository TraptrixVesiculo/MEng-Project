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

[How to Create a Splash Screen](splashscreen.html)

How to Use the System Tray

[Solving Common Problems Using Other Swing Features](problems.html)

[Home Page](../../index.html)
>
[Creating a GUI With JFC/Swing](../index.html)
>
[Using Other Swing Features](index.html)

[« Previous](splashscreen.html) • [Trail](../TOC.html) • [Next »](problems.html)

# How to Use the System Tray

The system tray is a specialized area of the desktop
where users can access currently running programs. This area may be referred to differently on various
operating systems. On Microsoft Windows, the system tray
is referred to as the Taskbar Status Area, while on the GNU Network Object Model Environment (GNOME) Desktop it is
referred to as the Notification Area. On K Desktop Environment (KDE) this area is referred to as the System Tray.
However, on each system the tray area is shared by all applications running on the desktop.

The
[`java.awt.SystemTray`](http://download.oracle.com/javase/7/docs/api/java/awt/SystemTray.html) class introduced in Java™ SE version 6 represents the system tray for a desktop.
The system tray can be accessed by calling the static `SystemTray.getSystemTray()` method.
Before calling this method, use the static method
[`isSupported()`](http://download.oracle.com/javase/7/docs/api/java/awt/SystemTray.html#isSupported()) to check that the system tray is supported.
If the system tray is not supported on this platform, the `isSupported()`
method returns false. If the application attempts to call the `getSystemTray()` method in such a case,
the method will throw a `java.lang.UnsupportedOperationException`.

An application cannot create an instance of the `SystemTray` class.
Only a single instance created within this class can exist, and this instance can be obtained using the
[`getSystemTray()`](http://download.oracle.com/javase/7/docs/api/java/awt/SystemTray.html#getSystemTray()) method.

The system tray contains one or more tray icons which are added to the tray using the
[`add(java.awt.TrayIcon)`](http://download.oracle.com/javase/7/docs/api/java/awt/SystemTray.html#add(java.awt.TrayIcon)) method.
They can be removed when they are no longer needed with the
[`remove(java.awt.TrayIcon)`](http://download.oracle.com/javase/7/docs/api/java/awt/SystemTray.html#remove(java.awt.TrayIcon)) method.

---

**Note:** The `add()` method can throw an `AWTException` if the operating system or the Java runtime determines that
the icon cannot be added to the system tray. For example, an `AWTException` will be thrown by X-Window desktops if the
system tray does not exist on the desktop.

---

The
[`TrayIcon`](http://download.oracle.com/javase/7/docs/api/java/awt/TrayIcon.html) class functionality goes beyond the icon that is displayed in the tray.
It also includes a text tooltip, a pop-up menu, ballon messages, and a set of listeners associated with it.
A `TrayIcon` object generates various mouse events and supports the addition
of corresponding listeners to receive notification of these events.
The `TrayIcon` class processes some of the events itself. For example, by default, when a right-click
is performed on the tray icon, it displays the specified pop-up menu.
When a double-click is performed, the `TrayIcon` object generates an `ActionEvent` to launch an application.
When the mouse pointer hovers over the tray icon, the tooltip is displayed. The icon image
is automatically resized to fit the space allocated for the image on the tray.

The following demo, developed using the AWT package, demonstrates the features of SystemTray and TrayIcon classes.

![System Tray with opened pop-up menu](../../figures/uiswing/misc/systemtray.gif)

Unfortunately, the current implementation of the `TrayIcon` class provides limited support of the
Swing pop-up menu (the `JPopupMenu` class) and does not enable an application
to use all of the capabilities of the `javax.swing` package. The workaround proposal for this
issue is described in the Bug Database, see Bug ID
[6285881](http://bugs.sun.com/bugdatabase/view_bug.do?bug_id=6285881).

---

**Try this:**

1. Place the
   [`bulb.gif`](../examples/misc/TrayIconDemoProject/src/misc/images/bulb.gif) image file in the `image` directory.
   Compile and run the example, consult the
   [example index](../examples/misc/index.html#TrayIconDemo).
2. The tray icon will appear in the system tray.

   ![Tray icon image](../../figures/uiswing/misc/bulb32x32.gif)
3. Double-click the tray icon to launch the corresponding application. The dialog box will be displayed.
4. Hover the mouse pointer over the tray icon and click the right mouse button. The pop-up menu appears.
5. Select the Set auto size checkbox menu item. Notice that the icon appearance is changed as follows.

   ![Tray icon image is resized](../../figures/uiswing/misc/bulb16x16.gif)
6. Select the Set tooltip checkbox menu item. Hover the mouse pointer over the tray icon. The tooltip appears.
7. Choose the About menu item. The dialog box appears. Close the dialog box.
8. Choose any of the Display submenu items. Each of these items displays a message dialog box of a particular type:
   error, warning, info, or standard.
9. Use the Exit menu item to quit the application.

The following code snippet shows how to add a tray icon to the system tray and apply a pop-up menu:

```

...
        //Check the SystemTray is supported
        if (!SystemTray.isSupported()) {
            System.out.println("SystemTray is not supported");
            return;
        }
        final PopupMenu pop-up = new PopupMenu();
        final TrayIcon trayIcon =
                new TrayIcon(createImage("images/bulb.gif", "tray icon"));
        final SystemTray tray = SystemTray.getSystemTray();
       
        // Create a pop-up menu components
        MenuItem aboutItem = new MenuItem("About");
        CheckboxMenuItem cb1 = new CheckboxMenuItem("Set auto size");
        CheckboxMenuItem cb2 = new CheckboxMenuItem("Set tooltip");
        Menu displayMenu = new Menu("Display");
        MenuItem errorItem = new MenuItem("Error");
        MenuItem warningItem = new MenuItem("Warning");
        MenuItem infoItem = new MenuItem("Info");
        MenuItem noneItem = new MenuItem("None");
        MenuItem exitItem = new MenuItem("Exit");
       
        //Add components to pop-up menu
        pop-up.add(aboutItem);
        pop-up.addSeparator();
        pop-up.add(cb1);
        pop-up.add(cb2);
        pop-up.addSeparator();
        pop-up.add(displayMenu);
        displayMenu.add(errorItem);
        displayMenu.add(warningItem);
        displayMenu.add(infoItem);
        displayMenu.add(noneItem);
        pop-up.add(exitItem);
       
        trayIcon.setPopupMenu(pop-up);
       
        try {
            tray.add(trayIcon);
        } catch (AWTException e) {
            System.out.println("TrayIcon could not be added.");
        }
...

```

The complete code for this demo is available in the
[`TrayIconDemo.java`](../examples/misc/TrayIconDemoProject/src/misc/TrayIconDemo.java) file. This demo also uses the
[`bulb.gif`](../examples/misc/TrayIconDemoProject/src/misc/images/bulb.gif) image file.

Removing the current limitations on applying Swing components will
enable developers to add such components as `JMenuItem` (with image),
`JRadioButtonMenuItem`, and `JCheckBoxMenuItem`.

### The SystemTray API

> Only a single instance created within `SystemTray` class can exist.
>
> | Method | Purpose |
> | --- | --- |
> | [add](http://download.oracle.com/javase/7/docs/api/java/awt/SystemTray.html#add(java.awt.TrayIcon)) | Adds a tray icon to the system tray. The tray icon becomes visible in the system tray once it is added. The order in which icons are displayed in a tray is not specified — it is platform- and implementation-dependent. |
> | [getSystemTray](http://download.oracle.com/javase/7/docs/api/java/awt/SystemTray.html#getSystemTray()) | Gets the `SystemTray` instance that represents the desktop's tray area. This method always returns the same instance per application. On some platforms the system tray may not be supported. Use the `isSupported()` method to check if the system tray is supported. |
> | [isSupported](http://download.oracle.com/javase/7/docs/api/java/awt/SystemTray.html#isSupported()) | Returns information as to whether the system tray is supported on the current platform. In addition to displaying the tray icon, minimal system tray support includes either a pop-up menu (see the `TrayIcon.setPopupMenu(PopupMenu)` method) or an action event (see the `TrayIcon.addActionListener(ActionListener)`). |
> |

### The TrayIcon API

> A `TrayIcon` object represents a tray icon that can
> be added to the system tray. A `TrayIcon` object can have a tooltip (text), an image, a pop-up menu,
> and a set of listeners associated with it.
>
> | Method | Purpose |
> | --- | --- |
> | [setImageAutoSize](http://download.oracle.com/javase/7/docs/api/java/awt/TrayIcon.html#setImageAutoSize(boolean)) | Sets the auto-size property. Auto-size determines whether the tray image is automatically sized to fit the space allocated for the image on the tray. By default, the auto-size property is set to `false`. |
> | [setPopupMenu](http://download.oracle.com/javase/7/docs/api/java/awt/TrayIcon.html#setPopupMenu(java.awt.PopupMenu)) | Sets the pop-up menu for this `TrayIcon` object. If pop-up is `null`, no pop-up menu will be associated with this `TrayIcon` object. |
> | [setToolTip](http://download.oracle.com/javase/7/docs/api/java/awt/TrayIcon.html#setToolTip(java.lang.String)) | Sets the tooltip string for this `TrayIcon` object. The tooltip is displayed automatically when the mouse hovers over the icon. Setting the tooltip to `null` removes any tooltip text. When displayed, the tooltip string may be truncated on some platforms; the number of characters that may be displayed is platform-dependent. |
> |

### Examples That Use the SystemTray API
> The following table lists the
> example that uses tray icons added to the system tray.
>
> | Example | Where Described | Notes |
> | --- | --- | --- |
> | [`TrayIconDemo`](../examples/misc/index.html#TrayIconDemo) | This section | Creates the tray icon in the system tray, adds a pop-up menu to the tray icon. |

[« Previous](splashscreen.html)
•
[Trail](../TOC.html)
•
[Next »](problems.html)

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

**Previous page:** How to Create a Splash Screen
  
**Next page:** Solving Common Problems Using Other Swing Features




A browser with JavaScript enabled is required for this page to operate properly.