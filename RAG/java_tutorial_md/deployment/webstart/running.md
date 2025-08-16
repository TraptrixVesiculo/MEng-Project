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

Running a Java Web Start Application

[Java Web Start and Security](security.html)

[Common Java Web Start Problems](problems.html)

[Questions and Exercises](QandE/questions.html)

[Home Page](../../index.html)
>
[Deployment](../index.html)
>
[Java Web Start](index.html)

[« Previous](customProgressIndicatorForAppln.html) • [Trail](../TOC.html) • [Next »](security.html)

# Running a Java Web Start Application

Users can run Java Web Start applications in the following ways:

* [Running a Java Web Start Application From a Browser](#web)
* [Running a Java Web Start Application From the Java Cache Viewer](#cache)
* [Running a Java Web Start Application From the Desktop](#desktop)

---

**Note:** To run applications deployed with Java Web Start technology, you must have a
compatible version of the Java Runtime Environment (JRE) software.
The complete Java Standard Edition Development Kit (JDK) is not required.

---

## Running a Java Web Start Application From a Browser

You can run a Java Web Start application from a browser
by clicking a link to the application's JNLP file. The following text is
an example of a link to a JNLP file.

```

<a href="/some/path/Notepad.jnlp">Launch Notepad Application</a>

```

Java Web Start software loads and runs the application based on instructions
in the JNLP file.

Try it now:
[Run Notepad](http://download.oracle.com/javase/tutorialJWS/deployment/webstart/examples/Notepad.jnlp)


## Running a Java Web Start Application From the Java Cache Viewer

If you are using at least Java Platform, Standard Edition 6, you can run a
Java Web Start application through the Java Cache Viewer.

When Java Web Start software first loads an application, information from the
application's JNLP file is stored in the local Java Cache Viewer.
To launch the application again, you do not need to return to the web page
where you first launched it; you can launch it from the Java Cache Viewer.

To open the Java Cache Viewer:

1. Open the Control Panel.
2. Double click on the Java icon. The Java Control Panel opens.
3. Select the General tab.
4. Click View. The Java Cache Viewer opens.

The application is listed on the Java Cache Viewer screen.

![A screen shot of the Java Cache Viewer application](../../figures/deployment/webstart/jws_cache_viewer.png)

**Java Cache Viewer application**

To run the application, select it and click the Run button,
![The Run button](../../figures/deployment/webstart/JCRun.png),
or double click the application. The application starts just
as it did from the web page.

## Running a Java Web Start Application From the Desktop

You can add a desktop shortcut to a Java Web Start
application. Select the application in the Java Cache Viewer.
Right-click and select Install Shortcuts
or click the Install button,
![The Install button](../../figures/deployment/webstart/JCInstall.png).

A shortcut is added to the desktop.

![](../../figures/deployment/webstart/shortcut.png)

You can then launch the Java Web Start application just as you would launch
any native application.

[« Previous](customProgressIndicatorForAppln.html)
•
[Trail](../TOC.html)
•
[Next »](security.html)

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

**Previous page:** Displaying a Customized Loading Progress Indicator
  
**Next page:** Java Web Start and Security




A browser with JavaScript enabled is required for this page to operate properly.