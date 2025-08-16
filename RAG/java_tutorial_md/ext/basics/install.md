[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** The Extension Mechanism
  
**Lesson:** Creating and Using Extensions

[Creating and Using Extensions](index.html)

Installed Extensions

[Download Extensions](download.html)

[Understanding Extension Class Loading](load.html)

[Home Page](../../index.html)
>
[The Extension Mechanism](../index.html)
>
[Creating and Using Extensions](index.html)

[« Previous](index.html) • [Trail](../TOC.html) • [Next »](download.html)

# Installed Extensions

Installed extensions are JAR files in the lib/ext
directory of the Java Runtime Environment
(JRETM) software.
As its name
implies, the JRE is the runtime portion of the Java Development Kit
containing the platform's core API but without development tools such
as compilers and debuggers. The JRE is available either by itself or
as part of the Java Development Kit.

As of the
Java 1.2 platform, the JRE is a strict subset of the
JDKTM software. A subset of the JDK
software directory tree looks like this:

![JDK software directory tree](../../figures/ext/extb1.gif)

The JRE consists of those directories within the highlighted box in
the diagram. Whether your JRE is stand-alone or part of the
JDK software, any JAR file in the lib/ext of the JRE
directory is automatically treated by the runtime environment
as an extension.

Since installed extensions extend the platform's core API, use them
judiciously. They are rarely appropriate for interfaces used by a single, or
small set of applications.

Furthermore, since the symbols defined by installed extensions will be visible
in all Java processes, care should be taken to ensure that all visible symbols
follow the appropriate "reverse domain name" and "class hierarchy"
conventions. For example, com.mycompany.MyClass.

As of Java 6, extension JAR files may also be placed in a location that is
independent of any particular JRE,
so that extensions can be shared by all JREs that are installed on a system.
Prior to Java 6, the value of java.ext.dirs referred to
a single directory, but as of Java 6 it is a list of directories (like
CLASSPATH) that specifies the locations in which extensions are
searched for.
The first element of the path is always the lib/ext directory of the
JRE.
The second element is a directory outside of the JRE.
This other location allows extension JAR files to be installed once and used
by several JREs installed on that system.
The location varies depending on the operating system:

* SolarisTM Operating System: /usr/jdk/packages/lib/ext
* Linux: /usr/java/packages/lib/ext
* Microsoft Windows: %SystemRoot%\Sun\Java\lib\ext

Note that an installed extension placed in one of the above directories
extends the platform of *each* of the JREs (Java 6 or later) on
that system.

### A Simple Example

> Let's create a simple installed extension. Our extension consists
> of one class, RectangleArea, that computes the areas of rectangles:
>
> ```
>
> public final class RectangleArea {
>     public static int area(java.awt.Rectangle r) {
>         return r.width * r.height;
>     }
> }
>
> ```
>
> This class has a single method, area, that takes an instance of
> java.awt.Rectangle and returns the rectangle's area.
>
> Suppose that you want to test RectangleArea with an application
> called `AreaApp`:
>
> ```
>
> import java.awt.*;
>
> public class AreaApp {
>     public static void main(String[] args) {
>         int width = 10;
>         int height = 5;
>
>         Rectangle r = new Rectangle(width, height);
>         System.out.println("The rectangle's area is " 
>                            + RectangleArea.area(r));
>     }
> }
>
> ```
>
> This application instantiates a 10 x 5 rectangle, and then
> prints out the rectangle's area using the
> RectangleArea.area method.
>
> ### Running AreaApp Without the Extension Mechanism
>
> Let's first review how you would run the `AreaApp` application
> without using the extension mechanism. We'll assume that the
> RectangleArea class is bundled in a JAR file named area.jar.
>
> The RectangleArea class is not part of the Java platform, of
> course, so you would need to place the area.jar file on the
> class path in order to run `AreaApp` without getting a runtime
> exception. If area.jar was in the directory /home/user,
> for example, you could use this command:
>
> ```
>
> java -classpath .:/home/user/area.jar AreaApp 
>
> ```
>
> The class path specified in this command contains both the current
> directory, containing AreaApp.class, and the path to
> the JAR file containing the RectangleArea package. You would
> get the desired output by running this command:
>
> ```
>
> The rectangle's area is 50
>
> ```
>
> ### Running AreaApp by Using the Extension Mechanism
>
> Now let's look at how you would run `AreaApp` by using the
> RectangleArea class as an extension.
>
> To make the RectangleArea class into an extension, you place the
> file area.jar in the lib/ext directory of the JRE.
> Doing so automatically gives the RectangleArea the status of being
> an installed extension.
>
> With area.jar installed as an extension, you can run
> `AreaApp` without needing to specify the class path:
>
> ```
>
> java AreaApp 
>
> ```
>
> Because you're using area.jar as an installed extension, the
> runtime environment will be able to find and to load the
> `RectangleArea` class even though you haven't specified it on
> the class path. Similarly, any applet or application being run by any user
> on your system would be able to find and use the RectangleArea class.
>
> If there are multiple JREs (Java 6 or later) installed on a system and want the
> RectangleArea class to be available as an extension to all of them,
> instead of installing it in the lib/ext directory of a particular
> JRE, install it in the system-wide location.
> For example, on system running Linux, install area.jar in the
> directory /usr/java/packages/lib/ext.
> Then AreaApp can run using different JREs that are installed on that
> system, for example if different browsers are configured to use different
> JREs.

[« Previous](index.html)
•
[Trail](../TOC.html)
•
[Next »](download.html)

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

**Previous page:** Creating and Using Extensions
  
**Next page:** Download Extensions




A browser with JavaScript enabled is required for this page to operate properly.