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

Defining and Using Applet Parameters

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

[« Previous](data.html) • [Trail](../TOC.html) • [Next »](showStatus.html)

# Defining and Using Applet Parameters

Parameters are to applets what command-line arguments are to applications.
They enable the user to customize the applet's operation.
By defining parameters, you can increase your applet's flexibility, making your
applet work in multiple situations without recoding and recompiling it.

## Specifying an Applet's Input Parameters

You can specify an applet's input parameters in the applet's
Java Network Launch Protocol (JNLP) file or
in the `<parameter>` element of the `<applet>`
tag. It is usually better to specify the parameters in the applet's JNLP file
so that the parameters can be supplied consistently even if the applet is deployed
on multiple web pages. If the applet's parameters will vary by web page, then you
should specify the parameters in the `<parameter>` element of the
`<applet>` tag.

If you are unfamiliar with JNLP, see the
[Java Network Launch Protocol](../../deployment/deploymentInDepth/jnlp.html) topic for more information.

Consider an applet that takes three parameters. The
`paramStr` and `paramInt` parameters are specified in the
applet's JNLP file,
[`applettakesparams.jnlp`](examples/applet_AppletWithParameters/src/applettakesparams.jnlp).

```

<?xml version="1.0" encoding="UTF-8"?>
<jnlp spec="1.0+" codebase="" href="">
    ...
    <applet-desc
         name="Applet Takes Params"
         main-class="AppletTakesParams"
         width="800"
         height="50">
             <param name="paramStr" value="someString"/>
             <param name="paramInt" value="22"/>
     </applet-desc>
     ...
</jnlp>

```

The `paramOutsideJNLPFile` parameter is specified
in the `parameters` variable passed to the
Deployment Toolkit script's `runApplet` function in
[`AppletPage.html`](examples/dist/applet_AppletWithParameters/AppletPage.html).

```

<html>
  <head>
    <title>Applet Takes Params</title>
    <meta http-equiv="Content-Type" content="text/html; charset=windows-1252">
  </head>
  <body>
    <h1>Applet Takes Params</h1>

    <script src="http://www.java.com/js/deployJava.js"></script>
    <script>
        var attributes = { code:'AppletTakesParams.class',
            archive:'applet_AppletWithParameters.jar',  width:800, height:50} ;
        var parameters = {jnlp_href: 'applettakesparams.jnlp', paramOutsideJNLPFile: 'fooOutsideJNLP'} ;
        deployJava.runApplet(attributes, parameters, '1.4');
    </script>

  </body>
</html>

```

See
[Deploying an Applet](../../deployment/deploymentInDepth/runAppletFunction.html) for more information about the `runApplet` function.

## Retrieving the Applet's Input Parameters

You can retrieve the applet's input parameters by using the
[`getParameter`](http://download.oracle.com/javase/7/docs/api/java/applet/Applet.html#getParameter(java.lang.String)) method of the `Applet` class. The
[`AppletTakesParams.java`](examples/applet_AppletWithParameters/src/AppletTakesParams.java) applet retrieves and displays all its input parameters
(`paramStr`,
`paramInt`, and
`paramOutsideJNLPFile`).

```


import javax.swing.JApplet;
import javax.swing.SwingUtilities;
import javax.swing.JLabel;

public class AppletTakesParams extends JApplet {
    public void init() {
        final String  inputStr = getParameter("paramStr");        
        final int inputInt = Integer.parseInt(getParameter("paramInt"));
        final String inputOutsideJNLPFile = getParameter("paramOutsideJNLPFile");

        try {
            SwingUtilities.invokeAndWait(new Runnable() {
                public void run() {
                    createGUI(inputStr, inputInt, inputOutsideJNLPFile);
                }
            });
        } catch (Exception e) {
            System.err.println("createGUI didn't successfully complete");
        }
    }
    private void createGUI(String inputStr, int inputInt, String inputOutsideJNLPFile) {
        String text = "Applet's parameters are -- inputStr: " + inputStr +
                ",   inputInt: " + inputInt +
                ",   paramOutsideJNLPFile: " + inputOutsideJNLPFile;
        JLabel lbl = new JLabel(text);
        add(lbl);
    }
}

```

The `AppletTakesParams` applet is shown next.



A browser with JavaScript enabled is required for this page to operate properly.

---

**Note:** If you don't see the applet running, you need to install at least the [Java SE Development Kit (JDK) 6 update 10](http://java.sun.com/javase/downloads/index.jsp) release.

---

---

**Note:** If you don't see the example running, you might need to enable the JavaScript interpreter in your browser so that the Deployment Toolkit script can function properly.

---

[Download source code](examplesIndex.html#AppletWithParameters) for the *Applet With Parameters* example to experiment further.

[« Previous](data.html)
•
[Trail](../TOC.html)
•
[Next »](showStatus.html)

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

**Previous page:** Finding and Loading Data Files
  
**Next page:** Displaying Short Status Strings




A browser with JavaScript enabled is required for this page to operate properly.