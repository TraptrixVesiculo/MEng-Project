[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** Custom Networking
  
**Lesson:** Working With Cookies

[Working With Cookies](index.html)

HTTP State Management With Cookies

[CookieHandler Callback Mechanism](cookiehandler.html)

[Default CookieManager](cookiemanager.html)

[Custom CookieManager](custom.html)

[Home Page](../../index.html)
>
[Custom Networking](../index.html)
>
[Working With Cookies](index.html)

[« Previous](index.html) • [Trail](../TOC.html) • [Next »](cookiehandler.html)

# HTTP State Management With Cookies

The HTTP state management mechanism specifies a way to create a stateful
session with HTTP requests and responses.

Generally, HTTP request/response pairs are independent of each other. However,
the state management mechanism enables clients and servers that can
exchange state information to put these pairs in a larger context,
which is called a *session*. The state information used to create and
maintain the session is called a *cookie*.

A cookie is a piece of data that can be stored in a browser's cache. If you
visit a web site and then revisit it, the cookie data can be used to identify
you as a return visitor. Cookies enable state information, such as an
online shopping cart, to be remembered. A cookie can be short term, holding data
for a single web session, that is, until you close the browser, or a cookie
can be longer term, holding data for a week or a year.

For more information about HTTP state management, see
[RFC 2965: HTTP State Management Mechanism](http://www.ietf.org/rfc/rfc2965.txt).

[« Previous](index.html)
•
[Trail](../TOC.html)
•
[Next »](cookiehandler.html)

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

**Previous page:** Working With Cookies
  
**Next page:** CookieHandler Callback Mechanism




A browser with JavaScript enabled is required for this page to operate properly.