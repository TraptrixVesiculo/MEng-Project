[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** Deployment
  
**Lesson:** Applets
  
**Section:** Doing More With Applets

[Applets](index.html)

[Getting Started With Applets](getStarted.html)

[Defining an Applet Subclass](subclass.html)

[Methods for Milestones](appletMethods.html)

[Life Cycle of an Applet](lifeCycle.html)

[Applet's Execution Environment](appletExecutionEnv.html)

[Developing an Applet](developingApplet.html)

[Deploying an Applet](deployingApplet.html)

[Deploying With the Applet Tag](html.html)

[Doing More With Applets](doingMoreWithApplets.html)

Finding and Loading Data Files

[Defining and Using Applet Parameters](param.html)

[Displaying Short Status Strings](showStatus.html)

[Displaying Documents in the Browser](browser.html)

[Invoking JavaScript Code From an Applet](invokingJavaScriptFromApplet.html)

[Invoking Applet Methods From JavaScript Code](invokingAppletMethodsFromJavaScript.html)

[Manipulating DOM of Applet's Web Page](manipulatingDOMFromApplet.html)

[Displaying a Customized Loading Progress Indicator](customProgressIndicatorForApplet.html)

[Writing Diagnostics to Standard Output and Error Streams](stdout.html)

[Developing Draggable Applets](draggableApplet.html)

[Communicating With Other Applets](iac.html)

[Working With a Server-Side Application](server.html)

[Network Client Applet Example](clientExample.html)

[What Applets Can and Cannot Do](security.html)

[Solving Common Applet Problems](problemsindex.html)

[Questions and Exercises](QandE/questions.html)

[Home Page](../../index.html)
>
[Deployment](../index.html)
>
[Applets](index.html)

[« Previous](doingMoreWithApplets.html) • [Trail](../TOC.html) • [Next »](param.html)

# Finding and Loading Data Files

Whenever an applet needs to load data from a file that is specified with a relative URL (a URL that doesn't completely specify the file's location), the applet usually uses either the code base or the document base to form the complete URL.

The code base, returned by the `JApplet` `getCodeBase` method, is a URL that specifies the directory
from which the applet's classes were loaded.

The document base, returned by the `JApplet` `getDocumentBase` method, specifies the directory of the HTML page that contains the applet.

Unless the `<applet>` tag specifies a code base,
both the code base and document base refer to the same directory on the same server.

Data that the applet might need, or needs to rely on as a backup,
is usually specified relative to the code base. Data that the applet developer specifies, often by using parameters, is usually specified relative to the document base.

---

**Note:** 
For security reasons, browsers limit the URLs from which untrusted applets can
read. For example, most browsers don't allow untrusted applets to use ".." to
access directories above the code base or document base. Also, because untrusted
applets cannot read files
except for those files on the applet's originating host, the document base is generally
not useful if the document and the untrusted applet reside
on different servers.

---

The `JApplet` class defines convenient forms of image-loading and
sound-loading methods that enable you to specify images and sounds relative to
a base URL. For example, assume an applet is set up
with one of the directory structures shown in the following figure.

![Two directory structures showing the image files and class files in separate locations, with different structures.](../../figures/deployment/applet/7pkg.png)

To create an `Image` object that uses
the `a.gif` image file under `imgDir`,
the applet can use the following code:

```

Image image = getImage(getCodeBase(), "imgDir/a.gif");

```

[« Previous](doingMoreWithApplets.html)
•
[Trail](../TOC.html)
•
[Next »](param.html)

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

**Previous page:** Doing More With Applets
  
**Next page:** Defining and Using Applet Parameters




A browser with JavaScript enabled is required for this page to operate properly.