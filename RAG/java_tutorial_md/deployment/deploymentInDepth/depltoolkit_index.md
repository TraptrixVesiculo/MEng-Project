[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** Deployment
  
**Lesson:** Deployment In-Depth

[Deployment In-Depth](index.html)

Deployment Toolkit

[Deploying an Applet](runAppletFunction.html)

[Customizing the Loading Screen](customizeLoadingScreen.html)

[Deploying a Java Web Start Application](createWebStartLaunchButtonFunction.html)

[Changing the Launch Button](changeLaunchButtonOfJWS.html)

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

[« Previous](index.html) • [Trail](../TOC.html) • [Next »](runAppletFunction.html)

# Deployment Toolkit

The Deployment Toolkit script is a set of JavaScript functions that can help developers
deploy rich Internet applications (RIAs)
consistently across various browser and operating system configurations. The Deployment Toolkit
script evaluates the underlying browser and operating system, and deploys the RIA with the
correct HTML. This script can also ensure that the required version of the Java Runtime Environment (JRE)
software is present on the client machine. The Deployment Toolkit script was
introduced in the Java Platform, Standard Edition 6 update 10 release.

## Location of Deployment Toolkit Script

The Deployment Toolkit script exists at the following web addresses:

* `http://www.java.com/js/deployJava.js`
* `https://www.java.com/js/deployJava.js` – When deploying
  your applet on a secure page, use the Deployment
  Toolkit script from this secure location to avoid mixed content warnings
  when the page is loaded.

The JavaScript code in these locations has been minimized so that
it can load quickly. You can view the human readable version of the
JavaScript code with
associated comment blocks at   
[`http://www.java.com/js/deployJava.txt`](http://www.java.com/js/deployJava.txt).

---

**Note:** 
The JavaScript interpreter should be enabled in the client's browser so that the Deployment
Toolkit script can run and deploy your RIA properly.

---

[« Previous](index.html)
•
[Trail](../TOC.html)
•
[Next »](runAppletFunction.html)

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

**Previous page:** Deployment In-Depth
  
**Next page:** Deploying an Applet




A browser with JavaScript enabled is required for this page to operate properly.