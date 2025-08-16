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

[Java Network Launch Protocol](jnlp.html)

[Structure of the JNLP File](jnlpFileSyntax.html)

Deployment Best Practices

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

[« Previous](jnlpFileSyntax.html) • [Trail](../TOC.html) • [Next »](reducingDownloadTime.html)

# Deployment Best Practices

You can improve the user experience of your rich Internet application (RIA)
using the best practices described in this topic.

* Optimize the size of JAR files and related resources so
  that your RIA can load quickly. See
  [Reducing the Download Time](../../deployment/deploymentInDepth/reducingDownloadTime.html) for optimization techniques.
* Enable the version download protocol and use background update checks to enable your
  RIA to start quickly. See
  [Avoiding Unnecessary Update Checks](../../deployment/deploymentInDepth/avoidingUnnecessaryUpdateChecks.html) to learn more about the version download protocol and update checks.
* Sign JAR files only when absolutely necessary. See
  [Signing JAR Files Only When Necessary](../../deployment/deploymentInDepth/signing.html) to learn when to sign your RIA.
* Make sure that the client has the required version of the Java Runtime
  Environment software. See
  [Ensuring the Presence of the JRE Software](../../deployment/deploymentInDepth/ensuringJRE.html) for details on how the Deployment Toolkit script can be used for this purpose.
* Preload your Java Web Start application, if possible.
  If you plan to deploy your RIA as a Java Web Start application
  in an enterprise where you have
  some administrative control, you can preload your application to various
  clients so that it is cached and ready to use.
  Use the following command to preload your Java Web Start application:

  ```

  javaws -import -silent 

  ```

[« Previous](jnlpFileSyntax.html)
•
[Trail](../TOC.html)
•
[Next »](reducingDownloadTime.html)

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

**Previous page:** Structure of the JNLP File
  
**Next page:** Reducing the Download Time




A browser with JavaScript enabled is required for this page to operate properly.