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

Developing Draggable Applets

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

[« Previous](stdout.html) • [Trail](../TOC.html) • [Next »](iac.html)

# Developing Draggable Applets

An applet that is deployed by specifying the `draggable` parameter can be
dragged outside of the browser and dynamically transformed into a Java Web Start
application. The applet can be dragged by pressing the Alt key and the left mouse
button and dragging the mouse.
When the drag operation begins, the applet is removed from its parent
container (`Applet` or `JApplet`) and placed in a new
undecorated top-level window (`Frame` or `JFrame`).
A small floating Close button is displayed next to the dragged applet. When the
floating Close button is clicked, the applet is placed back in the browser.
Applets that can be dragged out of the browser shall henceforth be
referred to as *draggable applets*.

You can customize the behavior of a draggable applet in the following ways:

* You can change the keystroke and mouse button sequence that is used to drag the
  applet outside of the browser.
* You can add a desktop shortcut that can be used to launch your application
  outside of the browser.
* You can define how the applet should be closed after it has been dragged
  outside of the browser.

The following sections describe how to implement and customize a draggable applet.
The
[`MenuChooserApplet`](examples/applet_Draggable/src/MenuChooserApplet.java) class is used to demonstrate the development and deployment of
draggable applets. Open
[`AppletPage.html`](examples/dist/applet_Draggable/AppletPage.html) in a browser to view the Menu Chooser applet on a new page.

---

**Note:** If you don't see the applet running, you need to install at least the [Java SE Development Kit (JDK) 6 update 10](http://java.sun.com/javase/downloads/index.jsp) release.

---

---

**Note:** If you don't see the example running, you might need to enable the JavaScript interpreter in your browser so that the Deployment Toolkit script can function properly.

---

## Enabling the Capability to Drag an Applet

You can enable the capability to drag an applet by setting the
`draggable` parameter to `true` when deploying the applet,
as shown in the following code snippet:

```

<script src="http://www.java.com/js/deployJava.js"></script>
<script>
    var attributes = { code:'MenuChooserApplet', width:900, height:300 };
    var parameters = {jnlp_href: 'draggableapplet.jnlp', draggable: 'true'} ;
    deployJava.runApplet(attributes, parameters, '1.6');
</script>

```

## Changing the Keystroke and Mouse Button Sequence That Is Used to Drag an Applet

You can change the keystroke and mouse button sequence that is used to drag
an applet by implementing the
`isAppletDragStart` method. In the following code snippet, the applet
can be dragged by pressing the left mouse button and dragging the mouse:

```

 public boolean isAppletDragStart(MouseEvent e) {
        if(e.getID() == MouseEvent.MOUSE_DRAGGED) {
            return true;
        } else {
            return false;
        }
    }

```

## Enabling the Addition of a Desktop Shortcut When the Applet Is Disconnected From the Browser

If the user closes the browser window or navigates away from the page after
dragging an applet outside of the page, the applet is said to be *disconnected* from
the browser. You can create a desktop shortcut for the applet when the applet is
disconnected from the browser. The desktop shortcut can be used to launch the
application outside of the browser. To enable the creation of a desktop shortcut, add the
`offline-allowed` and `shortcut` tags to the applet's
Java Network Launch Protocol (JNLP) file.

```

<information>
    ...
    <offline-allowed />
    <shortcut online="false">
        <desktop />
    </shortcut>
</information>

```

---

**Note:** Depending on the setting for Shortcut Creation in the user's Java Control Panel,
the user might be prompted for confirmation before the shortcut is created.

---

## Defining How the Applet Should Be Closed

You can define how your applet can be closed. For example, your Swing applet
could have a `JButton` to close the applet instead of relying on the default
floating Close button.

The Java Plug-in software gives the applet an instance of the `ActionListener`
class. This instance of the `ActionListener` class, also referred to
as the *close listener*, can be used to modify the
default close behavior of the applet.

To define how the applet should be closed, implement the
`setAppletCloseListener` and
`appletRestored` methods in your applet.

In the following code
snippet, the
[`MenuChooserApplet`](examples/applet_Draggable/src/MenuChooserApplet.java) class receives the close listener and passes it on to the instance of the
[`MenuItemChooser`](examples/applet_Draggable/src/MenuItemChooser.java) class:

```

MenuItemChooser display = null;
...
display = new MenuItemChooser();
...
public void setAppletCloseListener(ActionListener cl) {
    display.setCloseListener(cl);
}

public void appletRestored() {
    display.setCloseListener(null);
}

```

The `MenuItemChooser` class is responsible for controlling
the applet's user interface. The `MenuItemChooser` class defines a
`JButton` labeled "Close." The following code is executed when the
user clicks this Close button:

```

private void close() {
    // invoke actionPerformed of closeListener received from
    // the Java Plug-in software.
    if (closeListener != null) {
        closeListener.actionPerformed(null);
    }
}

```

[Download source code](examplesIndex.html#DraggableApplet) for the *Draggable Applet* example to experiment further.

[« Previous](stdout.html)
•
[Trail](../TOC.html)
•
[Next »](iac.html)

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

**Previous page:** Writing Diagnostics to Standard Output and Error Streams
  
**Next page:** Communicating With Other Applets




A browser with JavaScript enabled is required for this page to operate properly.