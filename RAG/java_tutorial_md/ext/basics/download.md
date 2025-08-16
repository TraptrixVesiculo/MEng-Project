[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** The Extension Mechanism
  
**Lesson:** Creating and Using Extensions

[Creating and Using Extensions](index.html)

[Installed Extensions](install.html)

Download Extensions

[Understanding Extension Class Loading](load.html)

[Home Page](../../index.html)
>
[The Extension Mechanism](../index.html)
>
[Creating and Using Extensions](index.html)

[« Previous](install.html) • [Trail](../TOC.html) • [Next »](load.html)

# Download Extensions

Download extensions are sets of classes (and related resources) in JAR files.
A JAR file's manifest can contain headers that refer to one or more download extensions.
The extensions can be referenced in one of two ways:

* by a Class-Path header
* by an Extension-List header

Note that at most one of each is allowed in a manifest.
Download extensions indicated by a Class-Path header are downloaded
only for the lifetime of the application that downloads them, such as a web
browser.
Their advantage is that nothing is installed on the client; their disadvantage
is that they are downloaded each time they are needed.
Download extensions that are downloaded by an Extension-List header are
installed into the /lib/ext directory of the JRE that downloads them.
Their advantage is that they are downloaded the first time they're needed;
subsequently they can be used without downloading.
But as shown later in this tutorial, they are more complex to deploy.

Since download extensions that use the Class-Path headers are
simpler, lets consider them first.
Assume for example that a.jar and b.jar are
two JAR files in the same directory, and that the manifest of a.jar
contains this header:

```

Class-Path: b.jar

```

Then the classes in b.jar serve as extension classes for purposes
of the classes in a.jar. The classes in a.jar can invoke classes in
b.jar without b.jar's classes having to be
named on the class path. a.jar may or may not itself be an extension.
If b.jar weren't in the same directory as a.jar, then
the value of the Class-Path header should be set to the relative
pathname of b.jar.

There's nothing special about the classes that are playing
the role of a download extension. They are treated as extensions solely
because they're referenced by the manifest of some other JAR file.

To get a better understanding of how download extensions work, let's
create one and put it to use.

### An Example

> Suppose you want to create an applet that makes use of the
> `RectangleArea` class of the previous
> section:
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
> In the previous section, you made the RectangleArea class
> into an installed extension by placing the JAR file containing it into
> the lib/ext directory of the JRE. By making it an installed
> extension, you enabled any application to use the RectangleArea
> class as if it were part of the Java platform.
>
> If you want to be able to use the RectangleArea class from an
> applet, the situation is a little different. Suppose, for example,
> that you have an applet, `AreaApplet`, that makes use of class
> RectangleArea:
>
> ```
>
> import java.applet.Applet;
> import java.awt.*;
>
> public class AreaApplet extends Applet {
>     Rectangle r;
>
>     public void init() {    
>         int width = 10;
>         int height = 5;
>
>         r = new Rectangle(width, height);
>     }
>
>     public void paint(Graphics g) {
>         g.drawString("The rectangle's area is " 
>                       + RectangleArea.area(r), 10, 10);
>     }
> }
>
> ```
>
> This applet instantiates a 10 x 5 rectangle and then displays
> the rectangle's area by using the RectangleArea.area method.
>
> However, you can't assume that everyone
> who downloads and uses your applet is going to have the RectangleArea
> class available on their system, as an installed extension or
> otherwise. One way around that problem is
> to make the RectangleArea class available from the server side,
> and you can do that by using it as a download extension.
>
> To see how that's done, let's assume that you've bundled
> `AreaApplet` in a
> JAR file called AreaApplet.jar and that the class
> RectangleArea is bundled in RectangleArea.jar. In order for
> RectangleArea.jar to be treated as a download extension,
> RectangleArea.jar must be listed in the
> Class-Path header in AreaApplet.jar's manifest.
> AreaApplet.jar's manifest might look like this, for example:
>
> ```
>
> Manifest-Version: 1.0
> Class-Path: RectangleArea.jar
>
> ```
>
> The value of the Class-Path header in this manifest is
> RectangleArea.jar with no path specified, indicating that
> RectangleArea.jar is located in the same directory as the applet's
> JAR file.

### More about the Class-Path Header

> If an applet or application uses more than one extension, you can list
> multiple URLs in a manifest. For example, the following is a valid header:
>
> ```
>
> Class-Path: area.jar servlet.jar images/
>
> ```
>
> In the Class-Path header any URLs listed
> that don't end with '/' are assumed to be JAR files. URLs
> ending in '/' indicate directories. In the
> preceding example, images/ might be a directory containing
> resources needed by the applet or the application.
>
> Note that only one Class-Path header is allowed in a manifest file, and that
> each line in a manifest must be no more than 72 characters long. If you need to
> specify more class path entries than will fit on one line, you can extend them
> onto subsequent continuation lines. Begin each continuation line with two
> spaces. For example:
>
> ```
>
> Class-Path: area.jar servlet.jar monitor.jar datasource.jar
>   provider.jar gui.jar
>
> ```
>
> A future release may remove the limitation of having only one instance of each
> header, and of limiting lines to only 72 characters.
>
> Download extensions can be "daisy chained", meaning that the manifest of
> one download extension can have a Class-Path header that
> refers to a second extension, which can refer to a third extension, and so on.

### Installing Download Extensions

> In the above example, the extension downloaded by the applet is available only
> while the browser which loaded the applet is still running.
> However, applets can trigger installation of extensions, if additional
> information is included in the manifests of both the applet and the extension.
>
> Since this mechanism extends the platform's core API, its use
> should be judiciously applied. It is rarely appropriate for interfaces used
> by a single, or small set of applications. All visible symbols should follow
> reverse domain name and class hierarchy conventions.
>
> The basic requirements are that both the applet and the extensions it uses
> provide version information in their manifests, and that they be signed.
> The version information allows Java Plug-in to ensure that the extension
> code has the version expected by the applet. For example, the
> AreaApplet could specify an areatest extension in its
> manifest:
>
> ```
>
> Manifest-Version: 1.0
> Extension-List: areatest
> areatest-Extension-Name: area
> areatest-Specification-Version: 1.1
> areatest-Implementation-Version: 1.1.2
> areatest-Implementation-Vendor-Id: com.sun
> areatest-Implementation-URL: http://www.sun.com/test/area.jar
>
> ```
>
> (Please note that there is no area.jar file at the above URL;
> this is just an example!)
> The manifest in area.jar would provide corresponding information:
>
> ```
>
> Manifest-Version: 1.0
> Extension-Name: area
> Specification-Vendor: Sun Microsystems, Inc
> Specification-Version: 1.1
> Implementation-Vendor-Id: com.sun
> Implementation-Vendor: Sun Microsystems, Inc
> Implementation-Version: 1.1.2
>
> ```
>
> Both the applet and the extension must be signed, by the same signer.
> Signing the jar files will modify them in-place, providing more information in
> their manifest files.
> Signing helps ensure that only trusted code gets installed.
> A simple way to sign jar files is to first create a keystore, and then
> use that to hold certificates for the applet and extension.
> For example:
>
> ```
>
> keytool -genkey -dname "cn=Fred" -alias test -keypass mykeypass -storepass mystorepass -validity 180
>
> ```
>
> Then the jar files can be signed:
>
> ```
>
> jarsigner -storepass mystorepass -keypass mykeypass AreaApplet.jar test
> jarsigner -storepass mystorepass -keypass mykeypass area.jar test
>
> ```
>
> More information on keytool, jarsigner, and other security
> tools is at the
> [Summary of Tools for the Java 2 Platform Security](http://download.oracle.com/javase/7/docs/technotes/guides/security/SecurityToolsSummary.html).
>
> Here is AreaDemo.html, which loads the applet and causes the
> extension code to be downloaded and installed:
> > ```
> >
> > <html>
> > <body>
> >   <applet code="AreaApplet.class" archive="AreaApplet.jar"/>
> > </body>
> > </html>
> >
> > ```
>
> When the page is loaded for the first time, the user is told that the applet
> requires installation of the extension.
> A subsequent dialog informs the user about the signed applet.
> Accepting both installs the extension in the lib/ext folder
> of the JRE and runs the applet.
>
> After restarting the web browser and load the same web page, only the dialog
> about the applet's signer is presented, because area.jar is already installed.
> This is also true if AreaDemo.html is opened in a different web
> browser (assuming both browsers use the same JRE).
>
> For more information about installing download extensions, please see
> [Deploying Java Extensions](http://download.oracle.com/javase/7/docs/technotes/guides/plugin/developer_guide/extensions.html).
> A more detailed example is at
> [Deploying Java Media Framework as Java Extension](http://download.oracle.com/javase/7/docs/technotes/guides/plugin/developer_guide/extensions_example.html).

[« Previous](install.html)
•
[Trail](../TOC.html)
•
[Next »](load.html)

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

**Previous page:** Installed Extensions
  
**Next page:** Understanding Extension Class Loading




A browser with JavaScript enabled is required for this page to operate properly.