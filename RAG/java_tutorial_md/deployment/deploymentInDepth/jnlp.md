[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** Deployment
  
**Lesson:** Deployment In-Depth

[Deployment In-Depth](index.html)

[Deployment Toolkit](depltoolkit_index.html)

[Deploying an Applet](runAppletFunction.html)

[Customizing the Loading Screen](customizeLoadingScreen.html)

[Deploying a Java Web Start Application](createWebStartLaunchButtonFunction.html)

[Changing the Launch Button](changeLaunchButtonOfJWS.html)

[Checking the Client JRE Software Version](jreVersionCheck.html)

Java Network Launch Protocol

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

[« Previous](jreVersionCheck.html) • [Trail](../TOC.html) • [Next »](jnlpFileSyntax.html)

# Java Network Launch Protocol

The Java Network Launch Protocol (JNLP) enables an application to be launched
on a client desktop by using resources that are hosted on a remote web server.
Java Plug-in software and
Java Web Start software are considered JNLP clients because they can launch remotely hosted
applets and applications on a client desktop. See
[Java Network Launching Protocol and API Specification](http://java.sun.com/javase/technologies/desktop/javawebstart/download-spec.html) for details.

Recent improvements in deployment technologies enable us to launch rich Internet
applications (RIAs) by using JNLP. Both applets and Java Web Start applications can be
launched by using this protocol. RIAs that are launched by using JNLP also have access to
JNLP APIs. These JNLP APIs allow the RIAs to access the client desktop with the user's permission.

JNLP is enabled by a RIA's JNLP file. The
JNLP file describes the RIA. The JNLP file specifies the name of the main JAR file,
the version of Java Runtime Environment software that is required to run the RIA,
name and display
information, optional packages, runtime parameters, system properties, and so on.

You can find more information about deploying RIAs by using JNLP in the
following topics:

* [Deploying an Applet](../../deployment/applet/deployingApplet.html)
* [Deploying a Java Web Start Application](../../deployment/webstart/deploying.html)
* [JNLP API](../../deployment/doingMoreWithRIA/jnlpAPI.html)
* [Structure of the JNLP File](../../deployment/deploymentInDepth/jnlpFileSyntax.html)

[« Previous](jreVersionCheck.html)
•
[Trail](../TOC.html)
•
[Next »](jnlpFileSyntax.html)

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

**Previous page:** Checking the Client JRE Software Version
  
**Next page:** Structure of the JNLP File




A browser with JavaScript enabled is required for this page to operate properly.