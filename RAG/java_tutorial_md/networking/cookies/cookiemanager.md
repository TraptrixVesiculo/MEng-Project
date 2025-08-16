[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** Custom Networking
  
**Lesson:** Working With Cookies

[Working With Cookies](index.html)

[HTTP State Management With Cookies](definition.html)

[CookieHandler Callback Mechanism](cookiehandler.html)

Default CookieManager

[Custom CookieManager](custom.html)

[Home Page](../../index.html)
>
[Custom Networking](../index.html)
>
[Working With Cookies](index.html)

[« Previous](cookiehandler.html) • [Trail](../TOC.html) • [Next »](custom.html)

# Default CookieManager

[`java.net.CookieManager`](http://download.oracle.com/javase/7/docs/api/java/net/CookieManager.html) provides a concrete implementation of a `CookieHandler`
and for most users is sufficient for handling HTTP state management.
`CookieManager` separates the storage of cookies from the policy surrounding,
accepting, and rejecting them. A `CookieManager` is initialized with a
[`java.net.CookieStore`](http://download.oracle.com/javase/7/docs/api/java/net/CookieStore.html) and a
[`java.net.CookiePolicy`](http://download.oracle.com/javase/7/docs/api/java/net/CookiePolicy.html). `CookieStore` manages the storage of the cookies.
`CookiePolicy` makes policy decisions on cookie acceptance and rejection.

The following code shows how to create and set a system-wide CookieManager:

```

  java.net.CookieManager cm = new java.net.CookieManager();
  java.net.CookieHandler.setDefault(cm);

```

The first line calls the default `CookieManager` constructor to create
the instance. The second line calls the static `setDefault` method
of `CookieHander` to set the system-wide handler.

The default `CookieManager` constructor creates a new
`CookieManager` instance with a default cookie store and accept policy.
`CookieStore` is the place where any accepted HTTP cookie is stored.
If not specified when created, a `CookieManager` instance will use an
internal in-memory implementation. This implementation is not persistent and
only lives for the lifetime of the Java Virtual Machine. Users requiring a
persistent store must implement their own store.

The default cookie policy used by `CookieManager` is
`CookiePolicy.ACCEPT_ORIGINAL_SERVER`, which only accepts cookies from
the original server. So, the `Set-Cookie` response from the server must
have a “domain” attribute set, and it must match the domain of the
host in the URL. For more information, see
[`java.net.HttpCookie.domainMatches`](http://download.oracle.com/javase/7/docs/api/java/net/HttpCookie.html#domainMatches(java.lang.String,%20java.lang.String)). Users requiring a different policy must implement the `CookiePolicy`
interface and pass it to the `CookieManager` constructor or set it to an already
constructed `CookieManager` instance by using the
`setCookiePolicy(cookiePolicy)` method.

When retrieving cookies from the cookie store, `CookieManager` also enforces
the path-match rule from section 3.3.4 of
[RFC 2965](http://www.ietf.org/rfc/rfc2965.txt). So, a cookie must also have its
“path” attribute set so that the path-match rule can be applied before the
cookie is retrieved from the cookie store.

In summary, `CookieManager` provides the framework for handling
cookies and provides a good default implementation for `CookieStore`.
`CookieManager` is highly customizable by enabling you to set your own
`CookieStore`, `CookiePolicy`, or both.

[« Previous](cookiehandler.html)
•
[Trail](../TOC.html)
•
[Next »](custom.html)

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

**Previous page:** CookieHandler Callback Mechanism
  
**Next page:** Custom CookieManager




A browser with JavaScript enabled is required for this page to operate properly.