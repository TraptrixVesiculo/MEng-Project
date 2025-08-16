[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

Working With Cookies

[HTTP State Management With Cookies](definition.html)

[CookieHandler Callback Mechanism](cookiehandler.html)

[Default CookieManager](cookiemanager.html)

[Custom CookieManager](custom.html)

**Trail:** Custom Networking

[Home Page](../../index.html)
>
[Custom Networking](../index.html)

[« Previous](../nifs/index.html) • [Trail](../TOC.html) • [Next »](definition.html)

# Lesson: Working With Cookies

Though you are probably already familiar with cookies, you might not
know how to take advantage of them in your Java application. This lesson
guides you through the concept of cookies and explains how to set a cookie
handler so that your HTTP URL connections will use it.

Java SE provides one main class for this functionality,
[`java.net.CookieHandler`](http://download.oracle.com/javase/7/docs/api/java/net/CookieHandler.html), and the following supporting classes and interfaces:
[`java.net.CookieManager`](http://download.oracle.com/javase/7/docs/api/java/net/CookieManager.html),
[`java.net.CookiePolicy`](http://download.oracle.com/javase/7/docs/api/java/net/CookiePolicy.html),
[`java.net.CookieStore`](http://download.oracle.com/javase/7/docs/api/java/net/CookieStore.html), and
[`java.net.HttpCookie`](http://download.oracle.com/javase/7/docs/api/java/net/HttpCookie.html).

## [HTTP State Management With Cookies](definition.html)

This page describes cookies and explains how they are used to provide sessions.

## [CookieHandler Callback Mechanism](cookiehandler.html)

This page explains how a cookie handler is called when you access
a web site and how to set a cookie handler.

## [Default CookieManager](cookiemanager.html)

Java SE provides a default cookie handler implementation that is sufficient
in most cases and highly customizable.

## [Custom CookieManager](custom.html)

Here are some examples of how to customize the cookie policy
and write your own cookie store.

[« Previous](../nifs/index.html)
•
[Trail](../TOC.html)
•
[Next »](definition.html)

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

**Previous page:** Previous Lesson
  
**Next page:** HTTP State Management With Cookies




A browser with JavaScript enabled is required for this page to operate properly.