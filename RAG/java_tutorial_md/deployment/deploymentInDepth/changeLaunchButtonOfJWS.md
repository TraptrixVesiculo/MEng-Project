[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** Deployment
  
**Lesson:** Deployment In-Depth
  
**Section:** Deployment Toolkit
  
**Subsection:** Deploying a Java Web Start Application

[Deployment In-Depth](index.html)

[Deployment Toolkit](depltoolkit_index.html)

[Deploying an Applet](runAppletFunction.html)

[Customizing the Loading Screen](customizeLoadingScreen.html)

[Deploying a Java Web Start Application](createWebStartLaunchButtonFunction.html)

Changing the Launch Button

[Checking the Client JRE Software Version](jreVersionCheck.html)

[Java Network Launch Protocol](jnlp.html)

[Structure of the JNLP File](jnlpFileSyntax.html)

[Deployment Best Practices](bestPractices.html)

[Reducing the Download Time](reducingDownloadTime.html)

[Avoiding Unnecessary Update Checks](avoidingUnnecessaryUpdateChecks.html)

[Signing JAR Files Only When Necessary](signing.html)

[Ensuring the Presence of the JRE Software](ensuringJRE.html)

[Questions and Exercises](QandE/questions.html)

[Home Page](../../index.html)
>
[Deployment](../index.html)
>
[Deployment In-Depth](index.html)

[« Previous](createWebStartLaunchButtonFunction.html) • [Trail](../TOC.html) • [Next »](jreVersionCheck.html)

# Changing the Launch Button

You can change your Java Web Start application's Launch button image, if you don't like the default
![Launch button](http://java.sun.com/products/jfc/tsc/articles/swing2d/webstart.png)
button or if you
have another image that you have standardized on.

Use the `deployJava.launchButtonPNG` variable to point to the location
of your Launch button's image.

**Variable:** `deployJava.launchButtonPNG`

**Usage:** Providing an alternate image URL

In this example, the Notepad application's
Launch button is now an image of Duke waving.

```
		
<script src="http://www.java.com/js/deployJava.js"></script>
<script>
    deployJava.launchButtonPNG='http://download.oracle.com/javase/tutorial/images/DukeWave.gif';
    var url = "http://java.sun.com/javase/technologies/desktop/javawebstart/apps/notepad.jnlp";
    deployJava.createWebStartLaunchButton(url, '1.6.0');
</script>

```

The Notepad application's new Launch button (Duke waving) follows.
Click on Duke's image to launch the Notepad application.



A browser with JavaScript enabled is required for this page to operate properly.

---

**Note:** If you don't see the example running, you might need to enable the JavaScript interpreter in your browser so that the Deployment Toolkit script can function properly.

---

[« Previous](createWebStartLaunchButtonFunction.html)
•
[Trail](../TOC.html)
•
[Next »](jreVersionCheck.html)

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

**Previous page:** Deploying a Java Web Start Application
  
**Next page:** Checking the Client JRE Software Version




A browser with JavaScript enabled is required for this page to operate properly.