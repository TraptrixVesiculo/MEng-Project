[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** Deployment
  
**Lesson:** Deployment In-Depth
  
**Section:** Deployment Best Practices

[Deployment In-Depth](index.html)

[Deployment Toolkit](depltoolkit_index.html)

[Deploying an Applet](runAppletFunction.html)

[Customizing the Loading Screen](customizeLoadingScreen.html)

[Deploying a Java Web Start Application](createWebStartLaunchButtonFunction.html)

[Changing the Launch Button](changeLaunchButtonOfJWS.html)

[Checking the Client JRE Software Version](jreVersionCheck.html)

[Java Network Launch Protocol](jnlp.html)

[Structure of the JNLP File](jnlpFileSyntax.html)

[Deployment Best Practices](bestPractices.html)

[Reducing the Download Time](reducingDownloadTime.html)

[Avoiding Unnecessary Update Checks](avoidingUnnecessaryUpdateChecks.html)

[Signing JAR Files Only When Necessary](signing.html)

Ensuring the Presence of the JRE Software

[Questions and Exercises](QandE/questions.html)

[Home Page](../../index.html)
>
[Deployment](../index.html)
>
[Deployment In-Depth](index.html)

[« Previous](signing.html) • [Trail](../TOC.html) • [Next »](QandE/questions.html)

# Ensuring the Presence of the JRE Software

Rich Internet applications (RIAs) usually need a minimum version of the
Java Runtime Environment (JRE) software to be present on the client machine.
When deploying a RIA, you need to ensure that client
machines have the required version of the JRE software so that your RIA
can function well.
With the Deployment Toolkit script, you have at least two ways to handle this
requirement.

* You can check the version of client JRE software as soon as users
  access your web site and install the latest version if necessary.
* You can let users navigate the web site, and check and install the
  latest JRE only when they attempt to use your RIA.

## Checking and Installing the Latest JRE Software When the User Accesses Your Web Site

The following example checks if a user has at least version 1.6.0\_13 of the JRE software
installed. If not, the code installs the latest JRE software .
See inline comments in the code.

```

<script src="http://www.java.com/js/deployJava.js"></script>
<script>
    
    // check if current JRE version is greater than 1.6.0 
    alert("versioncheck " + deployJava.versionCheck('1.6.0_10+'));
    if (deployJava.versionCheck('1.6.0_10+') == false) {                   
        userInput = confirm("You need the latest Java(TM) Runtime Environment. Would you like to update now?");        
        if (userInput == true) {  
    
            // Set deployJava.returnPage to make sure user comes back to 
            // your web site after installing the JRE
            deployJava.returnPage = location.href;
            
            // install latest JRE or redirect user to another page to get JRE from.
            deployJava.installLatestJRE(); 
        }
    }
</script>

```

## Installing the Correct JRE Software Only When the User Attempts to Use Your RIA

When you specify the minimum version of the JRE software in the `runApplet` or
`createWebStartLaunchButton` function, the Deployment Toolkit script makes sure
that the required version of the JRE software exists on the client before running
your RIA.

Use the `runApplet` function to deploy an applet, as shown in the
following example. The last parameter of the `runApplet` function is the
minimum version that is required to the run your applet (version 1.6).

```
    
<script src="http://www.java.com/js/deployJava.js"></script>
<script>
    var attributes = { code:'components.DynamicTreeApplet',  width:300, height:300};
    var parameters = {jnlp_href: 'dynamictree-applet.jnlp'};
    deployJava.runApplet(attributes, parameters, '1.6');
</script>

```

To deploy a Java Web Start application, use the `createWebStartLaunchButton`
function with the correct minimum version parameter (version 1.6).

```

<script src="http://www.java.com/js/deployJava.js"></script>
<script>
    var url = "dynamictree-applet.jnlp";
    deployJava.createWebStartLaunchButton(url, '1.6.0');
</script>

```

The `runApplet` and `createWebStartLaunchButton`
functions check the client's version of the JRE software. If the minimum version is not
installed, the funtions install the latest version of the JRE software.

[« Previous](signing.html)
•
[Trail](../TOC.html)
•
[Next »](QandE/questions.html)

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

**Previous page:** Signing JAR Files Only When Necessary
  
**Next page:** Questions and Exercises: Deployment In-Depth




A browser with JavaScript enabled is required for this page to operate properly.