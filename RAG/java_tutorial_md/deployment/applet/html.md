[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** Deployment
  
**Lesson:** Applets
  
**Section:** Getting Started With Applets
  
**Subsection:** Deploying an Applet

[Applets](index.html)

[Getting Started With Applets](getStarted.html)

[Defining an Applet Subclass](subclass.html)

[Methods for Milestones](appletMethods.html)

[Life Cycle of an Applet](lifeCycle.html)

[Applet's Execution Environment](appletExecutionEnv.html)

[Developing an Applet](developingApplet.html)

[Deploying an Applet](deployingApplet.html)

Deploying With the Applet Tag

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

[« Previous](deployingApplet.html) • [Trail](../TOC.html) • [Next »](doingMoreWithApplets.html)

# Deploying With the Applet Tag

If you are not sure whether your end users' browsers will have
the JavaScript interpreter enabled,
you can deploy your applet by manually coding the
`<applet>` HTML tag, instead of
using the Deployment Toolkit functions.
Depending on the browsers you need to support, you may need to deploy your
applet using the `<object>` or `<embed>` HTML tag. Check the
[W3C HTML Specification](http://www.w3.org/TR/1999/REC-html401-19991224/) for details on the usage of these tags.

You can launch your applet using Java
Network Launch Protocol (JNLP) or specify the launch attributes directly in the
`<applet>` tag.

## Preparing for Deployment

Follow the steps described in the
[Deploying An Applet](./deployingApplet.html) topic to compile your source code, create jar file and JNLP file if necessary.
The overall steps for deployment are still relevant. Only the contents of your
HTML page containing the applet will change.

## Manually Coding Applet Tag, Launching Using JNLP

The
[`AppletPage_WithAppletTag.html`](examples/dist/applet_ComponentArch_DynamicTreeDemo/AppletPage_WithAppletTagUsingJNLP.html) page deploys the Dynamic Tree Demo applet with an `<applet>` tag that has
been manually coded (meaning, the applet is not deployed using the Deployment
Toolkit which automatically generates the required HTML). The applet is still
launched using JNLP. The JNLP file is specified in the `jnlp_href`
attribute.

```

<applet code = 'appletComponentArch.DynamicTreeApplet' 
        jnlp_href = 'dynamictree-applet.jnlp', 
        width = 300, 
        height = 300 />

```

## Manually Coding Applet Tag, Launching Without JNLP

If your applet does not need special permissions to perform certain sensitive
operations, you can also deploy your applet without a JNLP file.

The
[`AppletPage_WithAppletTagNoJNLP.html`](examples/dist/applet_ComponentArch_DynamicTreeDemo/AppletPage_WithAppletTagNoJNLP.html) deploys the Dynamic Tree Demo applet as shown in the following code snippet.

```

<applet code = 'appletComponentArch.DynamicTreeApplet' 
    archive = 'DynamicTreeDemo.jar', 
    width = 300, 
    height = 300 />

```

where

* `code` is the name of the applet class
* `archive` is the name of jar file containing the applet and its resources
* `width` is the width of the applet
* `height` is the height of the applet

[« Previous](deployingApplet.html)
•
[Trail](../TOC.html)
•
[Next »](doingMoreWithApplets.html)

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

**Previous page:** Deploying an Applet
  
**Next page:** Doing More With Applets




A browser with JavaScript enabled is required for this page to operate properly.