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

Working With a Server-Side Application

[Network Client Applet Example](clientExample.html)

[What Applets Can and Cannot Do](security.html)

[Solving Common Applet Problems](problemsindex.html)

[Questions and Exercises](QandE/questions.html)

[Home Page](../../index.html)
>
[Deployment](../index.html)
>
[Applets](index.html)

[« Previous](iac.html) • [Trail](../TOC.html) • [Next »](clientExample.html)

# Working With a Server-Side Application

Applets, like other Java programs,
can use the API defined in the `java.net` package
to communicate across the network.
An applet can communicate with server applications
that run on the same host as the applet. This communication does not require
any special setup on the server.

---

**Note:** Depending on the networking environment that
an applet is loaded into, and depending on the browser that
runs the applet, an applet might be unable to communicate
with its originating host. For example, browsers running on
hosts inside firewalls often cannot obtain much information about
the world outside the firewall. As a result, some browsers
might not allow applet communication to hosts outside the firewall.

---

To determine which host an applet came from,
use the `Applet` `getCodeBase` method
and the `java.net.URL` `getHost` method,
as follows:

```

String host = getCodeBase().getHost();

```

After you have the correct host name,
you can use all the networking code
that is documented in the
[Custom Networking](../../networking/index.html) trail.

---

**Note:** 
Not all browsers support all networking code flawlessly.
For example, one widely used browser compatible with
Java technology doesn't support posting to a URL.

---

For an example of implementing an applet that is a network client, see
[Network Client Applet Example](clientExample.html).

[« Previous](iac.html)
•
[Trail](../TOC.html)
•
[Next »](clientExample.html)

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

**Previous page:** Communicating With Other Applets
  
**Next page:** Network Client Applet Example




A browser with JavaScript enabled is required for this page to operate properly.