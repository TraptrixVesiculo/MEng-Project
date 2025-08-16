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

[JNLP API](jnlpAPI.html)

[Accessing the Client Using JNLP API](usingJNLPAPI.html)

Cookies

[Accessing Cookies](accessingCookies.html)

[Customizing the Loading Experience](customizeRIALoadingExperience.html)

[Questions and Exercises](QandE/questions.html)

[Home Page](../../index.html)
>
[Deployment](../index.html)
>
[Doing More With Rich Internet Applications](index.html)

[« Previous](usingJNLPAPI.html) • [Trail](../TOC.html) • [Next »](accessingCookies.html)

# Cookies

Web applications are typically a series of Hypertext Transfer Protocol (HTTP)
requests and responses. As HTTP is a stateless protocol, information is not
automatically saved between HTTP requests. Web applications use cookies
to store state information on the client. Cookies can be used to store information about
the user, the user's shopping cart, and so on.

#### Types of Cookies

The two types of cookies follow:

* Session cookies – Session cookies are stored in memory and are
  accessible as long as the user is using the web application. Session cookies
  are lost when the user exits the web application. Such cookies are identified
  by a session ID and are most commonly used to store details of a shopping cart.
* Permanent cookies – Permanent cookies are used to store long-term
  information such as user preferences and user identification information.
  Permanent cookies are stored in persistent storage and are not lost when the
  user exits the application. Permanent cookies are lost when they expire.

#### Cookie Support in Rich Internet Applications

Rich Internet applications (applets and Java Web Start applications)
support session and permanent cookies. The underlying cookie store depends on the
browser and the operating system on the client.

To learn more about cookies, see the following:

* [Working With Cookies](../../networking/cookies/index.html) lesson in the Java Tutorial
* [API Documentation for CookieManager](http://download.oracle.com/javase/7/docs/api/java/net/CookieManager.html) and related classes

[« Previous](usingJNLPAPI.html)
•
[Trail](../TOC.html)
•
[Next »](accessingCookies.html)

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

**Previous page:** Accessing the Client Using JNLP API
  
**Next page:** Accessing Cookies




A browser with JavaScript enabled is required for this page to operate properly.