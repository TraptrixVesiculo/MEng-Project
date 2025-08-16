[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** Deployment
  
**Lesson:** Applets
  
**Section:** Getting Started With Applets

[Applets](index.html)

[Getting Started With Applets](getStarted.html)

[Defining an Applet Subclass](subclass.html)

[Methods for Milestones](appletMethods.html)

Life Cycle of an Applet

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

[What Applets Can and Cannot Do](security.html)

[Solving Common Applet Problems](problemsindex.html)

[Questions and Exercises](QandE/questions.html)

[Home Page](../../index.html)
>
[Deployment](../index.html)
>
[Applets](index.html)

[« Previous](appletMethods.html) • [Trail](../TOC.html) • [Next »](appletExecutionEnv.html)

# Life Cycle of an Applet

An applet can react to major events in the following ways:

* It can *initialize* itself.* It can *start* running.* It can *stop* running.* It can perform a *final cleanup*,
        in preparation for being unloaded.

This section
introduces a new applet, `Simple`, that uses all of these methods.
Unlike Java applications, applets do *not* need to implement a
`main` method.

Here is the `Simple` applet.



A browser with JavaScript enabled is required for this page to operate properly.

---

**Note:** If you don't see the example running, you might need to enable the JavaScript interpreter in your browser so that the Deployment Toolkit script can function properly.

---

The following is the source code for the `Simple` applet.
This applet displays a descriptive string
whenever it encounters a major milestone in its life, such as when the user
first visits the page the applet is on.

```



import java.applet.Applet;
import java.awt.Graphics;

//No need to extend JApplet, since we don't add any components;
//we just paint.
public class Simple extends Applet {

    StringBuffer buffer;

    public void init() {
        buffer = new StringBuffer();
        addItem("initializing... ");
    }

    public void start() {
        addItem("starting... ");
    }

    public void stop() {
        addItem("stopping... ");
    }

    public void destroy() {
        addItem("preparing for unloading...");
    }

    private void addItem(String newWord) {
        System.out.println(newWord);
        buffer.append(newWord);
        repaint();
    }

    public void paint(Graphics g) {
	//Draw a Rectangle around the applet's display area.
        g.drawRect(0, 0, 
		   getWidth() - 1,
		   getHeight() - 1);

	//Draw the current string inside the rectangle.
        g.drawString(buffer.toString(), 5, 15);
    }
}

```

---

**Note:** In this example, the `Applet` class is extended, not the
Swing `JApplet` class, as Swing components do not need to be added
to this applet.

---

## Loading the Applet

As a result of the applet being loaded, you should see the text
"initializing... starting...".
When an applet is loaded, here's what happens:

* An instance of the applet's controlling class (an `Applet` subclass) is created.* The applet initializes itself.* The applet starts running.

## Leaving and Returning to the Applet's Page

When the user leaves the page, for example, to go to another page,
the browser stops and destroys the applet. The state of the
applet is not preserved. When the user
returns to the page, the browser intializes and starts a new instance of the applet.

## Reloading the Applet

When you refresh or reload a browser page, the current instance of the applet
is stopped and destroyed and a new instance is created.

## Quitting the Browser

When the user quits the browser,
the applet has the opportunity to stop itself and perform a final cleanup
before the browser exits.

[Download source code](examplesIndex.html#Simple) for the *Simple Applet* example to experiment further.

[« Previous](appletMethods.html)
•
[Trail](../TOC.html)
•
[Next »](appletExecutionEnv.html)

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

**Previous page:** Methods for Milestones
  
**Next page:** Applet's Execution Environment




A browser with JavaScript enabled is required for this page to operate properly.