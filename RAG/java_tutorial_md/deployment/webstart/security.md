[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** Deployment
  
**Lesson:** Java Web Start

[Java Web Start](index.html)

[Developing a Java Web Start Application](developing.html)

[Retrieving Resources](retrievingResources.html)

[Deploying a Java Web Start Application](deploying.html)

[Setting Up a Web Server](settingUpWebServerMimeType.html)

[Displaying a Customized Loading Progress Indicator](customProgressIndicatorForAppln.html)

[Running a Java Web Start Application](running.html)

Java Web Start and Security

[Common Java Web Start Problems](problems.html)

[Questions and Exercises](QandE/questions.html)

[Home Page](../../index.html)
>
[Deployment](../index.html)
>
[Java Web Start](index.html)

[« Previous](running.html) • [Trail](../TOC.html) • [Next »](problems.html)

# Java Web Start and Security

This section describes the basics of security for applications deployed through Java Web Start and includes:

* [Java Web Start Security Basics](#basics)
* [Signing JAR Files for Java Web Start Deployment](#signing)
* [Security and JNLP Files](#jnlp)
* [Dynamic Downloading of HTTPS Certificates](#https)

## Java Web Start Security Basics

Applications launched with Java Web Start are, by default, run in a restricted environment, known as a *sandbox*. In this sandbox, Java Web Start:

* Protects users against malicious code that could affect local files
* Protects enterprises against code that could attempt to access or destroy data on networks

Unsigned JAR files launched by Java Web Start remain in this sandbox, meaning they cannot access local files or the network.

## Signing JAR Files for Java Web Start Deployment

Java Web Start supports signed JAR files so that your application can work outside of the sandbox described above, so that the application can access local files and the network.

Java Web Start verifies that the contents of the JAR file have not changed since it was signed. If verification of a digital signature fails, Java Web Start does not run the application.

When the user first runs an application as a signed JAR file, Java Web Start opens a dialog box displaying the application's origin based on the signer's certificate. The user can then make an informed decision regarding running the application.

For more information, see the
[Signing and Verifying JAR Files](../jar/signindex.html) section.

## Security and JNLP Files

For a signed JAR file to have access to the local file system and network, you must specify security settings in the JNLP file. The `security` element contains security settings for the application.

The following example provides the application with complete access to the client system if all its JAR files are signed:

```

<security>
   <all-permissions/>
</security>

```

## Dynamic Downloading of HTTPS Certificates

Java Web Start dynamically imports certificates as browsers typically do. To do this, Java Web Start sets its own `https` handler, using the `java.protocol.handler.pkgs` system properties, to initialize defaults for the
[`SSLSocketFactory`](http://download.oracle.com/javase/7/docs/api/javax/net/ssl/SSLSocketFactory.html) and
[`HostnameVerifier`](http://download.oracle.com/javase/7/docs/api/javax/net/ssl/HostnameVerifier.html). It sets the defaults with the methods
[`HttpsURLConnection.setDefaultSSLSocketFactory`](http://download.oracle.com/javase/7/docs/api/javax/net/ssl/HttpsURLConnection.html#setDefaultSSLSocketFactory(javax.net.ssl.SSLSocketFactory)) and
[`HttpsURLConnection.setDefaultHostnameVerifier`](http://download.oracle.com/javase/7/docs/api/javax/net/ssl/HttpsURLConnection.html#setDefaultHostnameVerifier(javax.net.ssl.HostnameVerifier)).

If your application uses these two methods, ensure that they are invoked after the Java Web Start initializes the `https` handler, otherwise your custom handler will be replaced by the Java Web Start default handler.

You can ensure that your own customized `SSLSocketFactory` and `HostnameVerifiter` are used by doing one of the following:

* Install your own `https` handler, to replace the Java Web Start `https` handler. For more information, see the document
  [A New Era for Java Protocol Handlers](http://java.sun.com/developer/onlineTraining/protocolhandlers/).
* In your application, invoke `HttpsURLConnection.setDefaultSSLSocketFactory` or `HttpsURLConnection.setDefaultHostnameVerifier` only after the first `https URL` object is created, which executes the Java Web Start `https` handler initialization code first.

[« Previous](running.html)
•
[Trail](../TOC.html)
•
[Next »](problems.html)

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

**Previous page:** Running a Java Web Start Application
  
**Next page:** Common Java Web Start Problems




A browser with JavaScript enabled is required for this page to operate properly.