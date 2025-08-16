[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** Deployment
  
**Lesson:** Doing More With Rich Internet Applications
  
**Section:** Cookies

[Doing More With Rich Internet Applications](index.html)

[Setting Trusted Arguments and Secure Properties](settingArgsProperties.html)

[System Properties](properties.html)

[JNLP API](jnlpAPI.html)

[Accessing the Client Using JNLP API](usingJNLPAPI.html)

[Cookies](cookies.html)

Accessing Cookies

[Customizing the Loading Experience](customizeRIALoadingExperience.html)

[Questions and Exercises](QandE/questions.html)

[Home Page](../../index.html)
>
[Deployment](../index.html)
>
[Doing More With Rich Internet Applications](index.html)

[« Previous](cookies.html) • [Trail](../TOC.html) • [Next »](customizeRIALoadingExperience.html)

# Accessing Cookies

You can set and retrieve cookies in your rich Internet application (RIA).
Cookies can enhance the capabilities of your RIA. For example, consider
the scenario where you have applets on various web pages.
An applet on a web page cannot directly access or share information with an applet
on another web page. In this scenario, cookies provide an important connection between
applets and help one applet pass information to another applet on a different web page.
Java Web Start applications can also use cookies to store information on the client.

The Cookie Applet example has a
[`CookieAccessor`](examples/applet_AccessingCookies/src/CookieAccessor.java ) class that retrieves and sets cookies.

#### Retrieving Cookies

The following code snippet shows the `getCookieUsingCookieHandler`
method of the `CookieAccessor` class:

```

public void getCookieUsingCookieHandler() { 
    try {       
        // Instantiate CookieManager; make sure to set CookiePolicy
        CookieManager manager = new CookieManager();
        manager.setCookiePolicy(CookiePolicy.ACCEPT_ALL);
        CookieHandler.setDefault(manager);

        // get content from URLConnection; cookies are set by web site
        URL url = new URL("http://www.sun.com");
        URLConnection connection = url.openConnection();
        connection.getContent();

        // get cookies from underlying CookieStore
        CookieStore cookieJar = manager.getCookieStore();
        List  cookies = cookieJar.getCookies();
        for (HttpCookie cookie: cookies) {
          System.out.println("CookieHandler retrieved cookie: " + cookie);
        }
    } catch(Exception e) {
        System.out.println("Unable to get cookie using CookieHandler");
        e.printStackTrace();
    }
}  

```

The
[`CookieManager`](http://download.oracle.com/javase/7/docs/api/java/net/CookieManager.html) class is the main entry point for cookie management. Create an instance of
the `CookieManager` class and set its
[`CookiePolicy`](http://download.oracle.com/javase/7/docs/api/java/net/CookiePolicy.html). Set this instance of the `CookieManager` as the default
[`CookieHandler`](http://download.oracle.com/javase/7/docs/api/java/net/CookieHandler.html).

Open a
[`URLConnection`](http://download.oracle.com/javase/7/docs/api/java/net/URLConnection.html) to the web site of your choice. In the example, the cookies
that are set by the web site `wwww.sun.com` are retrieved.

Next, retrieve cookies from the underlying
[`CookieStore`](http://download.oracle.com/javase/7/docs/api/java/net/CookieStore.html) by using the `getCookies` method.

#### Setting Cookies

The following code snippet shows the `setCookieUsingCookieHandler`
method of the `CookieAccessor` class:

```

public void setCookieUsingCookieHandler() {
    try {
        // instantiate CookieManager
        CookieManager manager = new CookieManager();
        CookieHandler.setDefault(manager);
        CookieStore cookieJar = manager.getCookieStore();

        // create cookie
        HttpCookie cookie = new HttpCookie("UserName", "John Doe");

        // add cookie to CookieStore for a particular URL
        URL url = new URL("http://www.sun.com");
        cookieJar.add(url.toURI(), cookie);
        System.out.println("Added cookie using cookie handler");
    } catch(Exception e) {
        System.out.println("Unable to set cookie using CookieHandler");
        e.printStackTrace();
    }
}

```

As shown in [Retrieving Cookies](#retrieving), the
[`CookieManager`](http://download.oracle.com/javase/7/docs/api/java/net/CookieManager.html) class is the main entry point for cookie management. Create an instance of the
`CookieManager` class and set the instance as the default
[`CookieHandler`](http://download.oracle.com/javase/7/docs/api/java/net/CookieHandler.html).

Create the desired
[`HttpCookie`](http://download.oracle.com/javase/7/docs/api/java/net/HttpCookie.html) with the necessary information. In our example, we have created a new
`HttpCookie` that sets the `UserName` as
`John Doe`.

Next, add the cookie to the underlying cookie store.

---

**Note:** You must sign your RIA JAR file in order to access cookies. See the documentation
for the
[`jarsigner`](http://download.oracle.com/javase/7/docs/technotes/tools/index.html#security) tool to learn how to sign JAR files.

---

#### Running the Cookie Applet Example

Open
[`AppletPage.html`](examples/dist/applet_AccessingCookies/AppletPage.html) in a browser to run the Cookie Applet example. Check the Java Console log for
details of cookies that have been set
and retrieved. You should see the following output in the Java Console log
(session details vary).

```

---- Access cookies using CookieHandler ---
CookieHandler retrieved cookie: JSESSIONID=3bc935c18b8d36319be9497fb892
CookieHandler retrieved cookie: JROUTE=eKVJ4oW0NOer888s
Added cookie using cookie handler
...

```

---

**Note:** If you don't see the applet running, you need to install at least the [Java SE Development Kit (JDK) 6 update 10](http://java.sun.com/javase/downloads/index.jsp) release.

---

---

**Note:** If you don't see the example running, you might need to enable the JavaScript interpreter in your browser so that the Deployment Toolkit script can function properly.

---

[Download source code](examplesIndex.html#AccessingCookies) for the *Cookie Applet* example to experiment further.

[« Previous](cookies.html)
•
[Trail](../TOC.html)
•
[Next »](customizeRIALoadingExperience.html)

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

**Previous page:** Cookies
  
**Next page:** Customizing the Loading Experience




A browser with JavaScript enabled is required for this page to operate properly.