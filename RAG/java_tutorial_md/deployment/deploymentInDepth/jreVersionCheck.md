[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** Deployment
  
**Lesson:** Deployment In-Depth
  
**Section:** Deployment Toolkit

[Deployment In-Depth](index.html)

[Deployment Toolkit](depltoolkit_index.html)

[Deploying an Applet](runAppletFunction.html)

[Customizing the Loading Screen](customizeLoadingScreen.html)

[Deploying a Java Web Start Application](createWebStartLaunchButtonFunction.html)

[Changing the Launch Button](changeLaunchButtonOfJWS.html)

Checking the Client JRE Software Version

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

[« Previous](changeLaunchButtonOfJWS.html) • [Trail](../TOC.html) • [Next »](jnlp.html)

# Checking the Client JRE Software Version

There are many reasons to check if a particular version of the
Java Runtime Environment (JRE) software is available
on a client machine. For example, you might want to launch a different version of your
rich Internet application (RIA) or redirect the user to a different page
depending on the client's JRE software version.

Use the Deployment Toolkit script's `versionCheck` function
to check if a particular version or range of JRE versions is
installed on the client.

**Function signature:** `versionCheck: function(versionPattern)`

**Parameters:**

* `versionPattern` – String specifying the version or range of versions to check for,
  such as such as "1.4", "1.5.0\*" (1.5.x family), and "1.6.0\_02+"
  (any version greater than or equal to 1.6.0\_02).

**Usage:** Creating a different user experience depending on the client's
JRE software version

In this example, a Launch button is created for the Notepad application only
if the version of JRE software on the client is greater than or equal to 1.6.
If not, the browser is redirect them to `java.sun.com`.

```
   
<script src="http://www.java.com/js/deployJava.js"></script>
<script>
    if (deployJava.versionCheck('1.6+')) {            
        var url = "http://java.sun.com/javase/technologies/desktop/javawebstart/apps/notepad.jnlp";
        deployJava.createWebStartLaunchButton(url, '1.6.0'); <!-- you can also invoke deployJava.runApplet here -->
    } else {
        document.location.href="http://java.sun.com";
    }
</script>		

```

---

**Note:** Depending on the client's operating system and version of the Java platform, you
might be able to verify version information for JRE software at the major version level
(for example, 1.6) or at a finer update level (for example, 1.6.0\_10).

---

[« Previous](changeLaunchButtonOfJWS.html)
•
[Trail](../TOC.html)
•
[Next »](jnlp.html)

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

**Previous page:** Changing the Launch Button
  
**Next page:** Java Network Launch Protocol




A browser with JavaScript enabled is required for this page to operate properly.