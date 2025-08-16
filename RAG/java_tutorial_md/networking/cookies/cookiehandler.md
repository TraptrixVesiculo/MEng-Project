[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** Custom Networking
  
**Lesson:** Working With Cookies

[Working With Cookies](index.html)

[HTTP State Management With Cookies](definition.html)

CookieHandler Callback Mechanism

[Default CookieManager](cookiemanager.html)

[Custom CookieManager](custom.html)

[Home Page](../../index.html)
>
[Custom Networking](../index.html)
>
[Working With Cookies](index.html)

[« Previous](definition.html) • [Trail](../TOC.html) • [Next »](cookiemanager.html)

# CookieHandler Callback Mechanism

HTTP state management is implemented in Java SE through the
[`java.net.CookieHandler`](http://download.oracle.com/javase/7/docs/api/java/net/CookieHandler.html) class.
A `CookieHandler` object provides a callback mechanism to provide
an HTTP state management
policy implementation in the HTTP protocol handler. That is, URLs that use
HTTP as the protocol, `new URL("http://java.sun.com")` for example,
will use the HTTP protocol handler. This protocol handler calls back
to the `CookieHander` object, if set, to handle the state management.

The `CookieHandler` class is an abstract class that has two pairs
of related methods. The first pair, `getDefault()` and
`setDefault(cookieHandler)`, are static methods that enable you to
discover the current handler that is installed and to install your own handler.

No default handler is installed, and installing a handler is done on a
system-wide basis. For applications running within a secure environment, that is,
they have a security manager installed, you must have special permission to get
and set the handler. For more information, see
[`java.net.CookieHandler.getDefault`](http://download.oracle.com/javase/7/docs/api/java/net/CookieHandler.html#getDefault()).

The second pair of related methods, `put(uri, responseHeaders)` and
`get(uri, requestHeaders)`, enable you to set and get all the applicable
cookies to and from a cookie cache for the specified URI in the response/request headers,
respectively. These methods are abstract, and a concrete implementation
of a `CookieHandler` must provide the implementation.

Java Web Start and Java Plug-in have a default `CookieHandler` installed.
However, if you are running a stand-alone application and want to enable HTTP state
management, you must set a system-wide handler. The next two pages
in this lesson show you how to do so.

[« Previous](definition.html)
•
[Trail](../TOC.html)
•
[Next »](cookiemanager.html)

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

**Previous page:** HTTP State Management With Cookies
  
**Next page:** Default CookieManager




A browser with JavaScript enabled is required for this page to operate properly.