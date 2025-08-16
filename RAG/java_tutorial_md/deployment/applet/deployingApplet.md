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

[Life Cycle of an Applet](lifeCycle.html)

[Applet's Execution Environment](appletExecutionEnv.html)

[Developing an Applet](developingApplet.html)

Deploying an Applet

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

[« Previous](developingApplet.html) • [Trail](../TOC.html) • [Next »](html.html)

# Deploying an Applet

To deploy your applet, first compile the source code and package
it as a JAR file.

Applets can be launched in two ways.

* You can launch an applet by specifying the applet's launch properties
  directly in the applet tag. This old way of deploying applets
  imposes severe security restrictions on the applet.
* Alternatively, you can launch your applet by using Java Network
  Launch Protocol (JNLP).
  Applets launched by using JNLP have access to powerful JNLP APIs and extensions.

The Deployment Toolkit script contains useful JavaScript functions that can be used
to deploy applets in a web page.

If you are unfamiliar with these deployment technologies, review the
[Deployment In-Depth](../../deployment/deploymentInDepth/index.html) lesson before proceeding further.

Here are some step-by-step instructions to package and deploy your applet. The
Dynamic Tree Demo applet is used to illustrate applet deployment. You might want to
set up build scripts to execute some of the following steps.



A browser with JavaScript enabled is required for this page to operate properly.

---

**Note:** If you don't see the applet running, make sure that you have at least the Java 2 Platform, Standard Edition (J2SE) 1.4.2 release on your client. If not, [download](http://java.sun.com/javase/downloads/index.jsp) and install the latest release of the Java SE Development Kit (JDK). 

---

---

**Note:** If you don't see the example running, you might need to enable the JavaScript interpreter in your browser so that the Deployment Toolkit script can function properly.

---

1. Compile your applet's Java code and make sure all class files and
   resources such as images are in a separate directory.

   In the
   case of the DynamicTree Demo applet, the compiled classes are placed in the
   `build/classes/appletComponentArch` directory.
2. Create a JAR file containing your applet's class files and resources.

   For example, the following command creates a JAR file with the class files in
   the `build/classes/appletComponentArch` directory.

   ```

       cd build/classes
       jar cvf  DynamicTreeDemo.jar  appletComponentArch

   ```

   See the
   [Packaging Programs in JAR Files](../../deployment/jar/index.html) lesson to learn more about creating and using JAR files.
3. Create a JNLP file that describes how your applet should be launched.

   Here is the
   JNLP file used to launch the Dynamic Tree Demo applet.

   The source for
   [`dynamictree-applet.jnlp`](examples/applet_ComponentArch_DynamicTreeDemo/src/dynamictree-applet.jnlp) follows:

   ```
       
   <?xml version="1.0" encoding="UTF-8"?>
   <jnlp spec="1.0+" codebase="" href="">
       <information>
           <title>Dynamic Tree Demo</title>
           <vendor>Dynamic Team</vendor>
       </information>
       <resources>
           <!-- Application Resources -->
           <j2se version="1.6+"
                 href="http://java.sun.com/products/autodl/j2se" />
           <jar href="DynamicTreeDemo.jar" main="true" />

       </resources>
       <applet-desc 
            name="Dynamic Tree Demo Applet"
            main-class="components.DynamicTreeApplet"
            width="300"
            height="300">
        </applet-desc>
        <update check="background"/>
   </jnlp>					

   ```

   The topic,
   [Structure of the JNLP File](../../deployment/deploymentInDepth/jnlpFileSyntax.html), describes JNLP file syntax and options.
4. Create the HTML page that will display the applet. Invoke Deployment Toolkit
   functions to deploy the applet.

   In our example, the Dynamic
   Tree Demo applet is deployed in
   [`AppletPage.html`](examples/dist/applet_ComponentArch_DynamicTreeDemo/AppletPage.html).

   ```

   <body>
       ....
       <script src="http://www.java.com/js/deployJava.js"></script>
       <script> 
           var attributes = { code:'components.DynamicTreeApplet',  width:300, height:300} ; 
           var parameters = {jnlp_href: 'dynamictree-applet.jnlp'} ; 
           deployJava.runApplet(attributes, parameters, '1.6'); 
       </script>
       ....
   </body>

   ```
5. Place the applet's JAR file, JNLP file and HTML page in the appropriate
   folder(s).

   For this example, place `DynamicTreeDemo.jar`,
   `dynamictree-applet.jnlp`, and
   `AppletPage.html` in the same directory on the
   local machine or a web server. A web server is not required for testing this applet.
6. Open the applet's HTML page in a browser to view the applet.
   Check the Java Console log for error and debugging messages.

[Download source code](examplesIndex.html#ComponentArchDynamicTreeDemo) for the *Dynamic Tree Demo Applet* example to experiment further.

[« Previous](developingApplet.html)
•
[Trail](../TOC.html)
•
[Next »](html.html)

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

**Previous page:** Developing an Applet
  
**Next page:** Deploying With the Applet Tag




A browser with JavaScript enabled is required for this page to operate properly.