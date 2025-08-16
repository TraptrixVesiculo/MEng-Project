[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** Creating a GUI With JFC/Swing
  
**Lesson:** Modifying the Look and Feel

[Modifying the Look and Feel](index.html)

[How to Set the Look and Feel](plaf.html)

[The Synth Look and Feel](synth.html)

[A Synth Example](synthExample.html)

Nimbus Look and Feel

[Changing the Look of Nimbus](custom.html)

[Resizing a Component](size.html)

[Changing the Color Theme](color.html)

[For More Information](info.html)

[Home Page](../../index.html)
>
[Creating a GUI With JFC/Swing](../index.html)
>
[Modifying the Look and Feel](index.html)

[« Previous](synthExample.html) • [Trail](../TOC.html) • [Next »](custom.html)

# Nimbus Look and Feel

---

 **This section was updated to reflect features and conventions of the upcoming Java SE 7 release. You can download the current [JDK7 snapshot](http://download.java.net/jdk7/binaries/) from `java.net`.** 

---

Nimbus is a polished cross-platform look and feel introduced in the
Java SE 6 Update 10 (6u10) release. The following screen capture, from
SwingSet3 shows the Nimbus look and feel.

![SwingSet3 Screen capture Using Nimbus Look and Feel](../../figures/uiswing/lookandfeel/nimbus.png)

Nimbus uses Java 2D vector graphics to draw the user interface (UI),
rather than static bitmaps,
so the UI can be crisply rendered at any resolution.

Nimbus is highly customizable.
You can use the Nimbus look and feel as is, or you can *skin*
(customize) the look with your own brand.

### Enabling the Nimbus Look and Feel

For backwards compatibility, Metal is still the default Swing look and feel,
but you can change to Nimbus in one of three ways:

* Add the following code to the event-dispatching
  thread before creating the graphical user interface (GUI):

  ```

  import javax.swing.UIManager.*;

  try {
      for (LookAndFeelInfo info : UIManager.getInstalledLookAndFeels()) {
          if ("Nimbus".equals(info.getName())) {
              UIManager.setLookAndFeel(info.getClassName());
              break;
          }
      }
  } catch (Exception e) {
      // If Nimbus is not available, you can set the GUI to another look and feel.
  }

  ```

  The first line of code retrieves the list of all installed look
  and feel implementations for the platform and then iterates through the list to
  determine if Nimbus is available.
  If so, Nimbus is set as the look and feel.

  ---

  **Version Note:** Do not set the Nimbus look and feel explicitly
  by invoking the `UIManager.setLookAndFeel` method because
  not all versions or implementations of Java SE 6 support Nimbus.
  Additionally, the location of the Nimbus package changed between
  the 6u10 and Java SE 7 releases.
  Iterating through all installed look and feel implementations is a more robust
  approach because if Nimbus is not available, the default look and
  feel is used.
  For the Java SE 6 Update 10 release, the Nimbus package is located at
  `com.sun.java.swing.plaf.nimbus.NimbusLookAndFeel`.

  ---

  * Specify Nimbus as the default look and feel for a particular
    application at the command line, as follows:

    ```

    java -Dswing.defaultlaf=javax.swing.plaf.nimbus.NimbusLookAndFeel MyApp

    ```

    * Permanently set the default look and feel to Nimbus by adding
      the following line
      to the `<JAVA_HOME>/lib/swing.properties` file:

      ```

      swing.defaultlaf=javax.swing.plaf.nimbus.NimbusLookAndFeel

      ```

      If the `swing.properties` file does not yet exist, you
      need to create it.

[« Previous](synthExample.html)
•
[Trail](../TOC.html)
•
[Next »](custom.html)

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

**Previous page:** A Synth Example
  
**Next page:** Changing the Look of Nimbus




A browser with JavaScript enabled is required for this page to operate properly.