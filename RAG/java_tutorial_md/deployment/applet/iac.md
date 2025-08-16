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

Communicating With Other Applets

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

[« Previous](draggableApplet.html) • [Trail](../TOC.html) • [Next »](server.html)

# Communicating With Other Applets

An applet can communicate with other applets by using JavaScript functions
in the parent web page. JavaScript functions enable communication between applets
by receiving messages from one applet and invoking methods of other applets. See
the following topics for more information about the interaction between Java code
and JavaScript code:

* [Invoking JavaScript Code From an Applet](../../deployment/applet/invokingJavaScriptFromApplet.html)
* [Invoking Applet Methods From JavaScript Code](../../deployment/applet/invokingAppletMethodsFromJavaScript.html)

You should avoid using the following mechanisms to find other applets and
share data between applets:

* Avoid using static variables to share data between applets.
* Do not use the `getApplet` and `getApplets`
  methods of the
  [`AppletContext`](http://download.oracle.com/javase/7/docs/api/java/applet/AppletContext.html) class to find other applets. These methods only find applets that are running
  in the same instance of the Java Runtime Environment software.

Applets must originate from the same directory on the server in order to
communicate with each other.

The Sender and Receiver applets are shown next. When a user clicks the button
to increment the counter, the Sender applet invokes a
JavaScript function to send a request to the Receiver applet. Upon receiving the
request, the Receiver applet increments a counter variable and displays the value
of the variable.



A browser with JavaScript enabled is required for this page to operate properly.

Sender Applet


  
  

Receiver Applet



---

**Note:** If you don't see the applet running, you need to install at least the [Java SE Development Kit (JDK) 6 update 10](http://java.sun.com/javase/downloads/index.jsp) release.

---

---

**Note:** If you don't see the example running, you might need to enable the JavaScript interpreter in your browser so that the Deployment Toolkit script can function properly.

---

To enable communication with another applet, obtain a reference to an instance of the
`netscape.javascript.JSObject` class. Use this instance to invoke
JavaScript functions.
The
[`Sender`](examples/applet_SenderReceiver/src/Sender.java) applet uses an instance of the
`netscape.javascript.JSObject` class to invoke a
JavaScript function called `sendMsgToIncrementCounter`.

```

try {
    JSObject window = JSObject.getWindow(this);
    window.eval("sendMsgToIncrementCounter()");
} catch (JSException jse) {
    ...
}

```

---

**Note:** To compile Java code that has a reference to classes in the
`netscape.javascript` package, include
`<your JDK path>/jre/lib/plugin.jar`
in your classpath. At runtime, the Java Plug-in software automatically makes
these classes available to applets.

---

Write the JavaScript function that will receive requests from one applet and
invoke methods of another applet on the web page.
The `sendMsgToIncrementCounter` JavaScript function invokes
the Receiver applet's `incrementCounter` method.

```

<script>
    function sendMsgToIncrementCounter() {            
        receiver.incrementCounter();
    }
<script>

```

Note that the JavaScript code uses the name `receiver` to obtain a
reference to the Receiver applet on the web page. This name should be the same as the
value of the `id` attribute that is specified when you deploy the
Receiver applet.

The
[`Receiver`](examples/applet_SenderReceiver/src/Receiver.java) applet's `incrementCounter` method is shown next.

```

public void incrementCounter() {
    ctr++;
    String text = " Current Value Of Counter: " + (new Integer(ctr)).toString();
    ctrLbl.setText(text);
}

```

Deploy the applets on the web page as shown in the following code snippet.
You can view the Sender and Receiver applets and associated JavaScript code in
[`AppletPage.html`](examples/dist/applet_SenderReceiver/AppletPage.html).

```

<!-- Sender Applet -->
<script src="http://www.java.com/js/deployJava.js"></script>
<script> 
    var attributes = { code:'Sender.class',
        archive:'examples/dist/applet_SenderReceiver/applet_SenderReceiver.jar',  width:300, height:50} ;
    var parameters = {};
    deployJava.runApplet(attributes, parameters, '1.6');
</script>

<!-- Receiver Applet -->
<script> 
    var attributes = { id:'receiver', code:'Receiver.class',
        archive:'examples/dist/applet_SenderReceiver/applet_SenderReceiver.jar',  width:300, height:50} ;
    var parameters = {};
    deployJava.runApplet(attributes, parameters, '1.6');
</script>

```

[Download source code](examplesIndex.html#SenderReceiver) for the *Sender Receiver Applets* example to experiment further.

[« Previous](draggableApplet.html)
•
[Trail](../TOC.html)
•
[Next »](server.html)

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

**Previous page:** Developing Draggable Applets
  
**Next page:** Working With a Server-Side Application




A browser with JavaScript enabled is required for this page to operate properly.