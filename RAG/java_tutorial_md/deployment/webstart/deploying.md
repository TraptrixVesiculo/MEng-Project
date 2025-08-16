[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** Deployment
  
**Lesson:** Java Web Start

[Java Web Start](index.html)

[Developing a Java Web Start Application](developing.html)

[Retrieving Resources](retrievingResources.html)

Deploying a Java Web Start Application

[Setting Up a Web Server](settingUpWebServerMimeType.html)

[Displaying a Customized Loading Progress Indicator](customProgressIndicatorForAppln.html)

[Running a Java Web Start Application](running.html)

[Java Web Start and Security](security.html)

[Common Java Web Start Problems](problems.html)

[Questions and Exercises](QandE/questions.html)

[Home Page](../../index.html)
>
[Deployment](../index.html)
>
[Java Web Start](index.html)

[« Previous](retrievingResources.html) • [Trail](../TOC.html) • [Next »](settingUpWebServerMimeType.html)

# Deploying a Java Web Start Application

To deploy your Java Web Start application, first compile
the source code and package it as a JAR file.

Java Web Start applications are launched by using the
Java Network Launch Protocol (JNLP).
Hence, you must create a JNLP file to deploy your application.

The Deployment Toolkit script contains useful JavaScript functions that can be used
to deploy Java Web Start applications on a web page.

If you are unfamiliar with these deployment technologies, review the
[Deployment In-Depth](../../deployment/deploymentInDepth/index.html) lesson before proceeding.

Here are some step-by-step instructions to package and deploy your application. The
Dynamic Tree Demo application is used to illustrate the deployment of
Java Web Start applications.
You might want to
set up build scripts to execute some of the following steps.

Click the following Launch button to launch the Dynamic Tree Demo application.


A browser with JavaScript enabled is required for this page to operate properly.


---

**Note:** If you don't see the Java Web Start application running, make sure that you have at least the Java 2 Platform, Standard Edition (J2SE) 1.4.2 release on your client. If not, [download](http://java.sun.com/javase/downloads/index.jsp) and install the latest release of the Java SE Development Kit (JDK). 

---

---

**Note:** If you don't see the example running, you might need to enable the JavaScript interpreter in your browser so that the Deployment Toolkit script can function properly.

---

1. Compile your application's Java code and make sure that all class files and
   resources such as images are in a separate directory.

   In the
   Dynamic Tree Demo application, the compiled classes are placed in the
   `build/classes/webstartComponentArch` directory.
2. Create a JAR file containing your application's class files and resources.

   For example, the following command creates a JAR file with the class files in
   the `build/classes/webstartComponentArch` directory.

   ```

       cd build/classes
       jar cvf  DynamicTreeDemo.jar  webstartComponentArch

   ```

   See the
   [Packaging Programs in JAR Files](../../deployment/jar/index.html) lesson to learn more about creating and using JAR files.
3. Create a JNLP file that describes how your application should be launched.

   Here is the
   JNLP file that is used to launch the Dynamic Tree Demo application.
   The source for
   [`dynamictree-webstart.jnlp`](examples/webstart_ComponentArch_DynamicTreeDemo/src/dynamictree-webstart.jnlp) follows:

   ```
       
   <?xml version="1.0" encoding="UTF-8"?>
   <jnlp spec="1.0+" 
       codebase="http://download.oracle.com/javase/tutorialJWS/deployment/webstart/ex6/webstart_ComponentArch_DynamicTreeDemo" 
       href="dynamictree-webstart.jnlp">
       <information>
           <title>Dynamic Tree Demo</title>
           <vendor>Dynamic Team</vendor>
       </information>
       <resources>
           <!-- Application Resources -->
           <j2se version="1.6+"
                 href="http://java.sun.com/products/autodl/j2se"/>
           <jar href="DynamicTreeDemo.jar" main="true" />

       </resources>
       <application-desc
            name="Dynamic Tree Demo Application"
            main-class="webstartComponentArch.DynamicTreeApplication"
            width="300"
            height="300">
        </application-desc>
        <update check="background"/>
   </jnlp>					

   ```

   [Structure of the JNLP File](../../deployment/deploymentInDepth/jnlpFileSyntax.html) describes the JNLP file syntax and options.

   ---

   **Note:** 
   The `codebase` and `href` attributes are optional
   when deploying Java Web Start applications that will run on at least the
   Java SE 6 update 18 release or later.
   You must specify the `codebase` and `href`
   attributes when deploying Java Web Start applications that will run
   with previous releases of the Java Runtime Environment software.

   ---
4. Create the HTML page from which your application will be launched.
   Invoke Deployment Toolkit
   functions to deploy the Java Web Start application.

   In the example, the Dynamic
   Tree Demo application is deployed in
   [`JavaWebStartAppPage.html`](examples/dist/webstart_ComponentArch_DynamicTreeDemo/JavaWebStartAppPage.html).

   ```

   <body>
       ....
       <script src="http://www.java.com/js/deployJava.js"></script>
       <script>
           // using JavaScript to get location of JNLP file relative to HTML page
           var dir = location.href.substring(0, location.href.lastIndexOf('/')+1);
           var url = dir + "dynamictree-webstart.jnlp";
           deployJava.createWebStartLaunchButton(url, '1.6.0');
       </script>
       ....
   </body>

   ```

   If you are not sure whether your end users will have the JavaScript
   interpreter enabled in
   their browsers, you can deploy the Java Web Start application directly by
   creating a link to the JNLP file as follows:

   ```

   <a href="/absolute path to JNLP file/dynamictree-webstart.jnlp">Launch Notepad Application</a>

   ```

   If you deploy the Java Web Start application with a direct link,
   you cannot take advantage of the
   additional checks that the Deployment Toolkit functions provide. See
   [Deploying a Java Web Start Application](../../deployment/deploymentInDepth/createWebStartLaunchButtonFunction.html) in the Deployment In-Depth lesson for details.
5. Place the application's JAR file, JNLP file, and HTML page in the appropriate
   folders.

   For this example, place `DynamicTreeDemo.jar`,
   `dynamictree-webstart.jnlp`, and
   `JavaWebStartAppPage.html` in the same directory on the
   local machine or a web server. A web server is not required to test
   the Java Web Start application.
6. Open the application's HTML page in a browser to view the application.
   Check the Java Console log for error and debugging messages.

[Download source code](examplesIndex.html#DynamicTreeDemo) for the *Dynamic Tree Demo* example to experiment further.

[« Previous](retrievingResources.html)
•
[Trail](../TOC.html)
•
[Next »](settingUpWebServerMimeType.html)

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

**Previous page:** Retrieving Resources
  
**Next page:** Setting Up a Web Server




A browser with JavaScript enabled is required for this page to operate properly.