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

Displaying Documents in the Browser

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

[« Previous](showStatus.html) • [Trail](../TOC.html) • [Next »](invokingJavaScriptFromApplet.html)

# Displaying Documents in the Browser

An applet can load a web page in a browser window using the
`showDocument` methods in the
[`java.applet.AppletContext`](http://download.oracle.com/javase/7/docs/api/java/applet/AppletContext.html) class.

Here are the two forms of `showDocument`:

```

public void showDocument(java.net.URL url)
public void showDocument(java.net.URL url, String targetWindow)

```

The one-argument form of `showDocument` simply instructs the browser
to display the document at the specified URL, without specifying the window in
which to display the document.

The two-argument form of `showDocument` lets you specify the window or
HTML frame in which to display the document. The second argument can have
one of the folllowing values:

* `"_blank"` – Display the document in a new, nameless window.
* `"windowName"` – Displays the document in a
  window named *windowName*. This window is created if necessary.
* `"_self"` – Display the document in the window
  and frame that contain the applet.
* `"_parent"` – Display the document in parent frame of the
  applet's frame. If the applet frame has no parent frame,
  this acts the same as `"_self"`.
* `"_top"` – Display the document in the top-level frame.
  If the applet's frame is the top-level frame,
  this acts the same as `"_self"`.

---

**Note:** 
In this discussion, *frame* refers not to a Swing `JFrame`,
but to an HTML frame within a browser window.

---

The following applet enables you try every argument of both forms of
`showDocument`. The applet opens a window that
lets you type in a URL and choose an option for the
`targetWindow` argument. When you press Return or click the
Show document button, the applet calls `showDocument`.

A browser with JavaScript enabled is required for this page to operate properly.

---

**Note:** If you don't see the applet running, make sure that you have at least the Java 2 Platform, Standard Edition (J2SE) 1.4.2 release on your client. If not, [download](http://java.sun.com/javase/downloads/index.jsp) and install the latest release of the Java SE Development Kit (JDK). 

---

---

**Note:** If you don't see the example running, you might need to enable the JavaScript interpreter in your browser so that the Deployment Toolkit script can function properly.

---

Following is the applet code that calls `showDocument`.
Here is the
[`whole program`](examples/applet_ShowDocument/src/ShowDocument.java).

```

        ...//In an Applet subclass:
        urlWindow = new URLWindow(getAppletContext());
        . . .

class URLWindow extends Frame {
    . . .
    public URLWindow(AppletContext appletContext) {
        . . .
        this.appletContext = appletContext;
        . . .
    }
    . . .
    public boolean action(Event event, Object o) {
        . . .
            String urlString = /* user-entered string */;
            URL url = null;
            try {
                url = new URL(urlString);
            } catch (MalformedURLException e) {
                ...//Inform the user and return...
            }

            if (url != null) {
                if (/* user doesn't want to specify the window */) {
                    appletContext.showDocument(url);
                } else {
                    appletContext.showDocument(url,
                                               /* user-specified window */);
                }
            }
        . . .

```

[Download source code](examplesIndex.html#ShowDocument) for the *Show Document* example to experiment further.

[« Previous](showStatus.html)
•
[Trail](../TOC.html)
•
[Next »](invokingJavaScriptFromApplet.html)

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

**Previous page:** Displaying Short Status Strings
  
**Next page:** Invoking JavaScript Code From an Applet




A browser with JavaScript enabled is required for this page to operate properly.