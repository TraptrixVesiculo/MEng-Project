[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** Deployment
  
**Lesson:** Doing More With Rich Internet Applications

[Doing More With Rich Internet Applications](index.html)

[Setting Trusted Arguments and Secure Properties](settingArgsProperties.html)

[System Properties](properties.html)

JNLP API

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

[« Previous](properties.html) • [Trail](../TOC.html) • [Next »](usingJNLPAPI.html)

# JNLP API

Rich Internet applications (RIAs) can use the Java Network Launch Protocol (JNLP)
API to perform extensive operations on the user's environment. When launched by using
JNLP, even unsigned RIAs can perform the following operations with the
user's permission:

* They can use the
  [`FileOpenService`](http://download.oracle.com/javase/7/docs/jre/api/javaws/jnlp/javax/jnlp/FileOpenService.html) and
  [`FileSaveService`](http://download.oracle.com/javase/7/docs/jre/api/javaws/jnlp/javax/jnlp/FileSaveService.html) API to access the user's file system..
* They can use the
  [`ClipboardService`](http://download.oracle.com/javase/7/docs/jre/api/javaws/jnlp/javax/jnlp/ClipboardService.html) API to access the shared system-wide clipboard.
* They can use the
  [`PrintService`](http://download.oracle.com/javase/7/docs/jre/api/javaws/jnlp/javax/jnlp/PrintService.html) API to access printing functions.* They can use the
    [`PersistenceService`](http://download.oracle.com/javase/7/docs/jre/api/javaws/jnlp/javax/jnlp/PersistenceService.html) API to access persistence storage.* They can use the
      [`DownloadService`](http://download.oracle.com/javase/7/docs/jre/api/javaws/jnlp/javax/jnlp/DownloadService.html) API to control how the RIA is downloaded and cached.
    * They can use the
      [`DownloadServiceListener`](http://download.oracle.com/javase/7/docs/jre/api/javaws/jnlp/javax/jnlp/DownloadServiceListener.html) API to determine progress of the RIA's download.
    * They can use the
      [`SingleInstanceService`](http://download.oracle.com/javase/7/docs/jre/api/javaws/jnlp/javax/jnlp/SingleInstanceService.html) API to decide how to handle arguments when multiple instances of the
      RIA are launched.
    * They can use the
      [`ExtendedService`](http://download.oracle.com/javase/7/docs/jre/api/javaws/jnlp/javax/jnlp/ExtendedService.html) API to request permission to open certain files that have not been opened before.

Check the
[JNLP API documentation](http://download.oracle.com/javase/7/docs/jre/api/javaws/jnlp/javax/jnlp/package-summary.html) to see the complete list of the functionality available to RIAs that are
launched by using JNLP.

[« Previous](properties.html)
•
[Trail](../TOC.html)
•
[Next »](usingJNLPAPI.html)

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

**Previous page:** System Properties
  
**Next page:** Accessing the Client Using JNLP API




A browser with JavaScript enabled is required for this page to operate properly.