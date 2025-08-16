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

Invoking JavaScript Code From an Applet

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

[« Previous](browser.html) • [Trail](../TOC.html) • [Next »](invokingAppletMethodsFromJavaScript.html)

# Invoking JavaScript Code From an Applet

Applets can invoke JavaScript functions present in the same web page as the applet.
The
[LiveConnect Specification](http://java.sun.com/javase/6/webnotes/6u10/plugin2/liveconnect/index.html) describes details about how JavaScript code communicates with Java code.

The `netscape.javascript.JSObject` class enables applets to retrieve a
reference to JavaScript objects and interact with the web page. The Data Summary
applet described next invokes JavaScript code to retrieve information from the web
page and writes a data summary back to the web page.

Assume you have a web page with a few JavaScript functions. The example
[`AppletPage.html`](examples/dist/applet_InvokingJavaScriptFromApplet/AppletPage.html) has JavaScript functions to retrieve age, address, and phone numbers. There is
also a variable called `userName` which has no value at the outset.

```

<head>
<title>Data Summary Applet Page - Java to JavaScript LiveConnect</title>
<meta http-equiv="Content-Type" content="text/html; charset=windows-1252"/>
<script language="javascript">
    var userName = "";
    
    // returns number
    function getAge() { 
        return 25;
    }
    // returns an object
    function address() { 
        this.street = "1566 Greenwood Lane";
        this.city = "Santa Clara";
        this.state = "CA";
    }
    // returns an array
    function getPhoneNums() { 
        return ["408-111-2222", "408-333-4444"];
    } 
    function writeSummary(summary) {
        summaryElem = document.getElementById("summary");
        summaryElem.innerHTML = summary;
    }
    </script>

  ....      
</head>
<body>
    <script src="http://www.java.com/js/deployJava.js"></script>
    <script> 
        ...
        deployJava.runApplet(attributes, parameters, '1.6'); 
    </script>          
    ...
    <p id="summary"/>  // this HTML element contains the summary 
    ...
</body>
...

```

Next, consider an applet class called `DataSummaryApplet`.
The `DataSummaryApplet` class performs the following operations.

* Invokes the `JSObject`'s `setMember` method to
  set the `userName` variable to "John Doe".
* Retrieves the age, address, and phone numbers and builds a string
  containing a summary of this data.
* Invokes the `writeSummary` JavaScript function to write the
  summary back to the web page.

This applet
first needs to retrieve a reference to `JSObject` as follows:

```

...
JSObject window = JSObject.getWindow(this);
...

```

Put the preceding statement in a try ...catch.. block to handle
`netscape.javascript.JSException`.

Now that the applet has a reference to `JSObject`, it can invoke the
relevant JavaScript functions by using the `eval` and `call`
methods of `JSObject`.

```


package javatojs;

import java.applet.Applet;
import netscape.javascript.*; // add plugin.jar to classpath during compilation

public class DataSummaryApplet extends Applet {
    public void start() {
        try {
            JSObject window = JSObject.getWindow(this);

            String userName = "John Doe";

            // set JavaScript variable
            window.setMember("userName", userName);

            // invoke JavaScript function
            Number age = (Number) window.eval("getAge()");

            // get a JavaScript object and retrieve its contents
            JSObject address = (JSObject) window.eval("new address();");
            String addressStr = (String) address.getMember("street") + ", " +
                    (String) address.getMember("city") + ", " +
                    (String) address.getMember("state");

            // get an array from JavaScript and retrieve its contents
            JSObject phoneNums = (JSObject) window.eval("getPhoneNums()");
            String phoneNumStr = (String) phoneNums.getSlot(0) + ", " +
                    (String) phoneNums.getSlot(1);

            // dynamically change HTML in page; write data summary
            String summary = userName + " : " + age + " : " +
                    addressStr + " : " + phoneNumStr;
            window.call("writeSummary", new Object[] {summary})   ;
        } catch (JSException jse) {
            jse.printStackTrace();
        }
    }
}

```

To compile Java code that has a reference to classes in the
`netscape.javascript` package, include
`<your JDK path>/jre/lib/plugin.jar` in your classpath.
At runtime, the Java Plug-in software automatically makes these classes
available to applets.

The Data Summary applet displays the following result on the web page:

```

Result of applet's Java calls to JavaScript on this page
                
John Doe : 25 : 1566 Greenwood Lane, Santa Clara, CA : 408-111-2222, 408-333-4444

```

Open
[`AppletPage.html`](examples/dist/applet_InvokingJavaScriptFromApplet/AppletPage.html) in a browser to view the Data Summary applet
.

---

**Note:** If you don't see the applet running, you need to install at least the [Java SE Development Kit (JDK) 6 update 10](http://java.sun.com/javase/downloads/index.jsp) release.

---

---

**Note:** If you don't see the example running, you might need to enable the JavaScript interpreter in your browser so that the Deployment Toolkit script can function properly.

---

[Download source code](examplesIndex.html#InvokingJavaScriptFromApplet) for the *Invoking JavaScript Code From Applet* example to experiment further.

[« Previous](browser.html)
•
[Trail](../TOC.html)
•
[Next »](invokingAppletMethodsFromJavaScript.html)

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

**Previous page:** Displaying Documents in the Browser
  
**Next page:** Invoking Applet Methods From JavaScript Code




A browser with JavaScript enabled is required for this page to operate properly.