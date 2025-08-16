[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** Deployment
  
**Lesson:** Deployment In-Depth
  
**Section:** Deployment Toolkit
  
**Subsection:** Deploying an Applet

[Deployment In-Depth](index.html)

[Deployment Toolkit](depltoolkit_index.html)

[Deploying an Applet](runAppletFunction.html)

Customizing the Loading Screen

[Deploying a Java Web Start Application](createWebStartLaunchButtonFunction.html)

[Changing the Launch Button](changeLaunchButtonOfJWS.html)

[Checking the Client JRE Software Version](jreVersionCheck.html)

[Java Network Launch Protocol](jnlp.html)

[Structure of the JNLP File](jnlpFileSyntax.html)

[Deployment Best Practices](bestPractices.html)

[Reducing the Download Time](reducingDownloadTime.html)

[Avoiding Unnecessary Update Checks](avoidingUnnecessaryUpdateChecks.html)

[Signing JAR Files Only When Necessary](signing.html)

[Ensuring the Presence of the JRE Software](ensuringJRE.html)

[Questions and Exercises](QandE/questions.html)

[Home Page](../../index.html)
>
[Deployment](../index.html)
>
[Deployment In-Depth](index.html)

[« Previous](runAppletFunction.html) • [Trail](../TOC.html) • [Next »](createWebStartLaunchButtonFunction.html)

# Customizing the Loading Screen

A default loading screen is displayed when an applet is being loaded in
the web page. You can display a customized splash screen by specifying the following
parameters when you deploy the applet:

* `image` - the image to be displayed in the splash screen
* `boxbgcolor` - the background color of the area in which the applet will be displayed
* `boxborder` - whether the applet should have a border; defaults to `true`
* `centerimage` - the position of the image; defaults to `false`

The splash screen can
display a static image or an animated gif.

The code snippet from
[`AppletPage.html`](examples/dist/depltoolkit_CustomizingSplashScreen/AppletPage.html) shows how to customize the splash screen to display
an animation of the Duke, the Java mascot.

```

<script src="http://www.java.com/js/deployJava.js"></script>
<script> 
    var attributes = {code:'SwingSet2Applet.class', archive:'SwingSet2.jar', width:695, height:525} ; 
    <!-- customize splash screen display options -->
    var parameters = {jnlp_href: 'SwingSet2.jnlp', 
                    image: 'dukeanimated.gif', 
                    boxbgcolor: 'cyan', 
                    boxborder: 'true', 
                    centerimage: 'true'   
                    } ; 
    deployJava.runApplet(attributes, parameters, '1.6'); 
</script>

```

Open
[`AppletPage.html`](examples/dist/depltoolkit_CustomizingSplashScreen/AppletPage.html) in a browser to view the splash screen when the SwingSet2 Demo applet is loaded.
If you've clicked this link before and viewed the SwingSet2 Demo applet, make sure
to clear your cache using the Java Control Panel. You may not see the splash screen
if the applet loads quickly.

---

**Note:** If you don't see the applet running, you need to install at least the [Java SE Development Kit (JDK) 6 update 10](http://java.sun.com/javase/downloads/index.jsp) release.

---

---

**Note:** If you don't see the example running, you might need to enable the JavaScript interpreter in your browser so that the Deployment Toolkit script can function properly.

---

See the
[Displaying a Customized Loading Progress Indicator](../../deployment/applet/customProgressIndicatorForApplet.html) topic for information about displaying a customized loading progress indicator
when the applet's resources are being downloaded.

[Download source code](examplesIndex.html#CustomizingSplashScreen) for the *Customizing Splash Screen* example to experiment further.

[« Previous](runAppletFunction.html)
•
[Trail](../TOC.html)
•
[Next »](createWebStartLaunchButtonFunction.html)

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

**Previous page:** Deploying an Applet
  
**Next page:** Deploying a Java Web Start Application




A browser with JavaScript enabled is required for this page to operate properly.