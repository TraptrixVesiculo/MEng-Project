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

[Finding and Loading Data Files](data.html)

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

What Applets Can and Cannot Do

[Solving Common Applet Problems](problemsindex.html)

[Questions and Exercises](QandE/questions.html)

[Home Page](../../index.html)
>
[Deployment](../index.html)
>
[Applets](index.html)

[« Previous](clientExample.html) • [Trail](../TOC.html) • [Next »](problemsindex.html)

# What Applets Can and Cannot Do

Applets are loaded on a client when the user visits a page containing an
applet. The security model behind applets has been
designed with the goal of protecting the user from malicious applets.

Applets that are not signed using a security certificate are considered
to be untrusted and
referred to as *unsigned applets*. When running on a client, unsigned
applets operate within a security sandbox that allows only a set of safe
operations.

Applets can be signed using a security certificate to indicate that they come
from a trusted source. Signed applets operate
outside the security sandbox and have extensive capabilities to access the client.
A signed applet will run outside the security sandbox only if the user
accepts the applet's security certificate. If the user refuses to accept the
certificate, the applet will run within the security sandbox similar to an
unsigned applet.

With recent improvements to the Java Plug-in software, unsigned applets
launched using Java Network Launch Protocol (JNLP) can safely access the
client *with the user's permission*. It is recommended that you launch
your applet
using JNLP to leverage expanded capabilities and improve user experience. See
[Deploying an Applet](deployingApplet.html) for step by step instructions on applet deployment.

In this, topic we will discuss the security restrictions and
capabilities of applets.

## Unsigned Applets

Unsigned applets *can* perform the following operations:

* They can make network connections to the host they came from.
* They can easily display HTML documents using the `showDocument` method of the `java.applet.AppletContext` class.
* They can invoke public methods of other applets on the same page.
* They that are loaded from the local file system (from a directory in the user's `CLASSPATH`) have none of the restrictions that applets loaded over the network do.
* They can read secure system properties. See
  [System Properties](../../deployment/doingMoreWithRIA/properties.html) for a list of secure system properties.
* When launched by using JNLP, unsigned applets can also perform the
  following operations:
  + They can open, read, and save files on the client.
  + They can access the shared system-wide clipboard.
  + They can access printing functions.
  + They can store data on the client, decide how applets should be
    downloaded and cached, and much more. See
    [JNLP API](../../deployment/doingMoreWithRIA/jnlpAPI.html) for more information about developing applets by using the JNLP API.

Unsigned applets *cannot* perform the following operations:

* They cannot access client resources such as
  the local filesystem, executable files, system clipboard, and printers.
* They cannot connect to or retrieve resources from any third
  party server (any server other than the server it originated from).
* They cannot load native libraries.
* They cannot change the SecurityManager.
* They cannot create a ClassLoader.
* They cannot read certain system properties. See
  [System Properties](../../deployment/doingMoreWithRIA/properties.html) for a list of forbidden system properties.

## Signed Applets

Signed applets do not have the security restrictions that are imposed on
unsigned applets and can run outside the security sandbox.

---

**Note:** 
When a signed applet is accessed from JavaScript code in an HTML page, the applet is
executed *within* the security sandbox. This implies that the signed
applet essentially behaves likes an unsigned applet.

---

## Additional Information

For more information about applet security dialog boxes, see
[Exploring Security Warning Functionality](http://java.sun.com/developer/technicalArticles/GUI/SecurityWarning/AppletWarning.html) (article on java.sun.com)

[« Previous](clientExample.html)
•
[Trail](../TOC.html)
•
[Next »](problemsindex.html)

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

**Previous page:** Network Client Applet Example
  
**Next page:** Solving Common Applet Problems




A browser with JavaScript enabled is required for this page to operate properly.