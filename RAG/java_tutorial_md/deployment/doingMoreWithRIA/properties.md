[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** Deployment
  
**Lesson:** Doing More With Rich Internet Applications
  
**Section:** Setting Trusted Arguments and Secure Properties

[Doing More With Rich Internet Applications](index.html)

[Setting Trusted Arguments and Secure Properties](settingArgsProperties.html)

System Properties

[JNLP API](jnlpAPI.html)

[Accessing the Client Using JNLP API](usingJNLPAPI.html)

[Cookies](cookies.html)

[Accessing Cookies](accessingCookies.html)

[Customizing the Loading Experience](customizeRIALoadingExperience.html)

[Questions and Exercises](QandE/questions.html)

[Home Page](../../index.html)
>
[Deployment](../index.html)
>
[Doing More With Rich Internet Applications](index.html)

[« Previous](settingArgsProperties.html) • [Trail](../TOC.html) • [Next »](jnlpAPI.html)

# System Properties

This topic lists system properties that can be accessed by *unsigned*
rich Internet applications (RIAs) that are launched with or without the
Java Network Launch Protocol (JNLP). Some system properties cannot be accessed
by unsigned RIAs.

## Secure System Properties Accessible by All RIAs

All RIAs can retrieve the following secure
system properties:

* `java.class.version`
* `java.vendor`
* `java.vendor.url`
* `java.version`
* `os.name`
* `os.arch`
* `os.version`
* `file.separator`
* `path.separator`
* `line.separator`

## Secure System Properties Accessible by RIAs Launched by Using JNLP

RIAs launched by using JNLP can set and retrieve the
following secure properties:

* `awt.useSystemAAFontSettings`
* `http.agent`
* `http.keepAlive`
* `java.awt.syncLWRequests`
* `java.awt.Window.locationByPlatform`
* `javaws.cfg.jauthenticator`
* `javax.swing.defaultlf`
* `sun.awt.noerasebackground`
* `sun.awt.erasebackgroundonresize`
* `sun.java2d.d3d`
* `sun.java2d.dpiaware`
* `sun.java2d.noddraw`
* `sun.java2d.opengl`
* `swing.boldMetal`
* `swing.metalTheme`
* `swing.noxp`
* `swing.useSystemFontSettings`

## Forbidden System Properties

Unsigned RIAs cannot access the following
system properties:

* `java.class.path`
* `java.home`
* `user.dir`
* `user.home`
* `user.name`

[« Previous](settingArgsProperties.html)
•
[Trail](../TOC.html)
•
[Next »](jnlpAPI.html)

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

**Previous page:** Setting Trusted Arguments and Secure Properties
  
**Next page:** JNLP API




A browser with JavaScript enabled is required for this page to operate properly.