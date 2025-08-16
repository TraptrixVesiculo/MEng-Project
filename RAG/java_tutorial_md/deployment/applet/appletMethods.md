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

Methods for Milestones

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

[What Applets Can and Cannot Do](security.html)

[Solving Common Applet Problems](problemsindex.html)

[Questions and Exercises](QandE/questions.html)

[Home Page](../../index.html)
>
[Deployment](../index.html)
>
[Applets](index.html)

[« Previous](subclass.html) • [Trail](../TOC.html) • [Next »](lifeCycle.html)

# Methods for Milestones

The
[`Applet`](http://download.oracle.com/javase/7/docs/api/java/applet/Applet.html) class provides a framework for applet execution,
defining methods that the system calls when milestones occur.
Milestones are major events in an applet's life cycle.
Most applets override some or all of these methods to respond
appropriately to milestones.

## `init` Method

The `init` method is useful for one-time initialization
that doesn't take very long. The `init` method typically
contains the code that you would normally put into a constructor.
The reason applets don't usually have constructors is that they aren't
guaranteed to have a full environment until their `init` method is called.
Keep the `init` method short so that your applet can load quickly.

## `start` Method

Every applet that performs tasks after initialization
(except in direct response to user actions)
must override the `start` method.
The `start` method starts the execution of the applet.
It is good practice to return quickly from the `start` method.
If you need to perform computationally intensive operations it might be
better to start a new thread
for this purpose.

## `stop` Method

Most applets that override the `start` should also override the
`stop` method. The `stop` method should suspend the
applet's execution, so that it doesn't take up system resources
when the user isn't viewing the applet's page. For example, an applet that
displays an animation should stop trying to draw the animation
when the user isn't viewing it.

## `destroy` Method

Many applets don't need to override the `destroy` method because
their `stop` method (which is called before `destroy`)
will perform all tasks necessary to shut down the applet's execution.
However, the `destroy` method is available
for applets that need to release additional resources.

---

**Note:** Keep implementations of the `destroy` method as short as possible,
because there is no guarantee that this method will be completely executed.
The Java Virtual Machine might exit before a long `destroy`
method has completed.

---

[« Previous](subclass.html)
•
[Trail](../TOC.html)
•
[Next »](lifeCycle.html)

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

**Previous page:** Defining an Applet Subclass
  
**Next page:** Life Cycle of an Applet




A browser with JavaScript enabled is required for this page to operate properly.