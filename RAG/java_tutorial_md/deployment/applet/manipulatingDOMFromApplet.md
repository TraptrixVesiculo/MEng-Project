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

Manipulating DOM of Applet's Web Page

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

[« Previous](invokingAppletMethodsFromJavaScript.html) • [Trail](../TOC.html) • [Next »](customProgressIndicatorForApplet.html)

# Manipulating DOM of Applet's Web Page

Every web page is composed of a series of nested objects. These objects make
up the Document Object Model (DOM). An applet can traverse and modify objects of
its parent web page using the
[`Common DOM API`](http://download.oracle.com/javase/7/docs/jre/api/plugin/dom/index.html).

Consider an example of an applet that dumps the contents of its parent
web page.

In order to traverse and manipulate the DOM tree, you must first obtain a reference
to the `Document` object for the web page. You can do so by using the
`getDocument` method in the `com.sun.java.browser.plugin2.DOM`
class. Here is a code snippet that retrieves a reference to a `Document` object
in the
[`DOMDump`](examples/applet_TraversingDOM/src/DOMDump.java) applet's `start` method. See inline comments
in the code.

```

public void start() {
    try {
        // use reflection to get document
        Class c = Class.forName("com.sun.java.browser.plugin2.DOM");
        Method m = c.getMethod("getDocument",
                               new Class[] { java.applet.Applet.class });
        
        // cast object returned as HTMLDocument; then traverse or modify DOM
        HTMLDocument doc = (HTMLDocument) m.invoke(null, new Object[] { this });
        HTMLBodyElement body = (HTMLBodyElement) doc.getBody();
        dump(body, INDENT);
    } catch (Exception e) {
        System.out.println("New Java Plug-In not available");
        // In this case, you could fallback to the old bootstrapping mechanism 
        // available in the com.sun.java.browser.plugin.dom package
    }
}


```

Now that you have a reference to the `Document` object, you can
traverse and modify the DOM tree using the Common DOM API. The `DOMDump`
applet traverses the DOM tree and writes its contents to the Java Console log.

```

private void dump(Node root, String prefix) {
    if (root instanceof Element) {
        System.out.println(prefix + ((Element) root).getTagName() + 
                              " / " + root.getClass().getName());
    } else if (root instanceof CharacterData) {
        String data = ((CharacterData) root).getData().trim();
        if (!data.equals("")) {
            System.out.println(prefix + "CharacterData: " + data);
        }
    } else {
        System.out.println(prefix + root.getClass().getName());
    }
    NamedNodeMap attrs = root.getAttributes();
    if (attrs != null) {
        int len = attrs.getLength();
        for (int i = 0; i < len; i++) {
            Node attr = attrs.item(i);
            System.out.print(prefix + HALF_INDENT + "attribute " + i + ": " +
                             attr.getNodeName());
            if (attr instanceof Attr) {
                System.out.print(" = " + ((Attr) attr).getValue());
            }
            System.out.println();
        }
    }

    if (root.hasChildNodes()) {
        NodeList children = root.getChildNodes();
        if (children != null) {
            int len = children.getLength();
            for (int i = 0; i < len; i++) {
                dump(children.item(i), prefix + INDENT);
            }
        }
    }
}

```

Open
[`AppletPage.html`](examples/dist/applet_TraversingDOM/AppletPage.html) in a browser to view the `DOMDump` applet running.
Check the Java
Console log for a dump of the DOM tree of the web page.

---

**Note:** If you don't see the applet running, you need to install at least the [Java SE Development Kit (JDK) 6 update 10](http://java.sun.com/javase/downloads/index.jsp) release.

---

---

**Note:** If you don't see the example running, you might need to enable the JavaScript interpreter in your browser so that the Deployment Toolkit script can function properly.

---

[Download source code](examplesIndex.html#ManipulatingDOM) for the *DOM Dump* example to experiment further.

[« Previous](invokingAppletMethodsFromJavaScript.html)
•
[Trail](../TOC.html)
•
[Next »](customProgressIndicatorForApplet.html)

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

**Previous page:** Invoking Applet Methods From JavaScript Code
  
**Next page:** Displaying a Customized Loading Progress Indicator




A browser with JavaScript enabled is required for this page to operate properly.