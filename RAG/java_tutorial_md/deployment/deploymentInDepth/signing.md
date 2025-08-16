[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** Deployment
  
**Lesson:** Deployment In-Depth
  
**Section:** Deployment Best Practices

[Deployment In-Depth](index.html)

[Deployment Toolkit](depltoolkit_index.html)

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

Signing JAR Files Only When Necessary

[Ensuring the Presence of the JRE Software](ensuringJRE.html)

[Questions and Exercises](QandE/questions.html)

[Home Page](../../index.html)
>
[Deployment](../index.html)
>
[Deployment In-Depth](index.html)

[« Previous](avoidingUnnecessaryUpdateChecks.html) • [Trail](../TOC.html) • [Next »](ensuringJRE.html)

# Signing JAR Files Only When Necessary

Signed rich Internet applications (RIAs) display security warnings when
the user tries to launch and use the RIA. When users are trying to access a simple
RIA, security dialog boxes might unnerve them and turn them away from the application.
Hence, sign your RIA only if you need to (for example, when accessing
native libraries).

Recent enhancements to the RIA technology eliminate the need to sign your
RIA in the following cases:

* Accessing services on web sites other than the RIA's own domain –
  In the past, RIAs could only communicate with the server from which they
  were launched. The Java Plug-in software and the Java Web Start software now
  support cross-domain policy files. If a third-party
  site has set up cross-domain policies and allows access from other domains,
  your unsigned RIAs can invoke
  services from this site.
* Setting trusted Java Virtual Machine arguments and secure properties –
  You do not need to sign your RIA to set trusted Java Virtual Machine
  arguments or secure properties. You can set secure arguments and properties
  in the Java Network Launch Protocol (JNLP) file.
  See
  [System Properties](../../deployment/doingMoreWithRIA/properties.html) for more information.
* Accessing certain client resources –
  RIAs that are launched by using JNLP can access the client's resources with the
  user's permission. See
  [JNLP API](../../deployment/doingMoreWithRIA/jnlpAPI.html) for details on how to use the JNLP API to access the client.

See the following topics for more security related information about RIAs.

* [What Applets Can and Cannot Do](../../deployment/applet/security.html)
* [Java Web Start and Security](../../deployment/webstart/security.html)

[« Previous](avoidingUnnecessaryUpdateChecks.html)
•
[Trail](../TOC.html)
•
[Next »](ensuringJRE.html)

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

**Previous page:** Avoiding Unnecessary Update Checks
  
**Next page:** Ensuring the Presence of the JRE Software




A browser with JavaScript enabled is required for this page to operate properly.