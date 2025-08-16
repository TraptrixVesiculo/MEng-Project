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

Avoiding Unnecessary Update Checks

[Signing JAR Files Only When Necessary](signing.html)

[Ensuring the Presence of the JRE Software](ensuringJRE.html)

[Questions and Exercises](QandE/questions.html)

[Home Page](../../index.html)
>
[Deployment](../index.html)
>
[Deployment In-Depth](index.html)

[« Previous](reducingDownloadTime.html) • [Trail](../TOC.html) • [Next »](signing.html)

# Avoiding Unnecessary Update Checks

Rich Internet applications (RIAs) are cached locally to improve startup time.
However, before launching a RIA, the launch software
checks to make sure that every JAR file referenced in the RIA's
Java Network Launch Protocol (JNLP) file is up-to-date.
In other words, the launch software makes sure that you
are running the latest version of the RIA and not an older cached copy. These
update checks can take up to a few hundred milliseconds depending on the number
of JAR files and network speed. Use the techniques described in this topic to
avoid unnecessary update checks and to enhance the start up time of your RIA.

---

**Note:**  The term "launch software" is used here to collectively refer to the
Java Plug-in software and the Java Web Start software. The Java Plug-in software
launches applets while the Java Web Start software launches Java Web Start
applications.

---

## Leveraging the Version Download Protocol

You can leverage the *version download protocol* to eliminate unnecessary
version checks. See the following steps to enable this protocol.

1. Rename the JAR files to include a version number suffix with the following naming convention:

   ```
       
       <JAR file name> "__V" <version number> ".jar"

   ```

   For example, rename `DynamicTreeDemo.jar` to `DynamicTreeDemo__V1.0.jar`.
2. In the JNLP file, specify a version for every JAR file, and set the
   `jnlp.versionEnabled` property to `true`.

   ```

   <resources>
       <!-- Application Resources -->
       <j2se version="1.6+"
           href="http://java.sun.com/products/autodl/j2se"
               max-heap-size="128m" />
       <jar href="DynamicTreeDemo.jar" main="true" version="1.0"/>   
       <jar href="SomeOther.jar" version="2.0"/>
       <property name="jnlp.versionEnabled" value="true"/>
       ...
   </resources>

   ```

   When the `jnlp.versionEnabled` property is enabled, the
   launch software performs only *one* update check to make sure
   that the JNLP file is up-to-date.
   The software compares the version numbers that are specified in
   the JNLP file with the corresponding
   JAR file versions (according to the naming convention mentioned in
   step 1) and updates only
   the outdated JAR files. This approach is efficient because only the update check for
   the JNLP file occurs over the network. All other version checks occur locally.

   If a file with the correct version number is not found, the launch software
   attempts to load the default JAR file (for example, `DynamicTreeDemo.jar`).

## Performing Update Checks in the Background

If it is not critical for the user to immediately run the latest version of
your RIA, you can specify that all update checks should occur in the background.
In this case, the launch software launches the locally cached copy for
immediate usage and downloads a newer version of the RIA in the background.
The newer version of the RIA will be
launched the next time the user attempts to use your RIA.
To enable background update checks,
add the following line to your JNLP file:

```

<update check='background'/>

```

The following code snippet shows a sample JNLP file with the
background update check enabled:

```

<?xml version="1.0" encoding="UTF-8"?>
<jnlp spec="1.0+" codebase="" href="">
    <information>
        <title>Applet Takes Params</title>
        <vendor>Dynamic Team</vendor>
    </information>
    <resources>
        <!-- Application Resources -->
        <j2se version="1.6+"
              href="http://java.sun.com/products/autodl/j2se"/>
        <jar href="applet_AppletWithParameters.jar" main="true" />
    </resources>
    <applet-desc 
         name="Applet Takes Params"
         main-class="AppletTakesParams"
         width="800"
         height="50">
             <param name="paramStr" value="someString"/>
             <param name="paramInt" value="22"/>
     </applet-desc>
     <update check="background"/>
</jnlp>

```

[« Previous](reducingDownloadTime.html)
•
[Trail](../TOC.html)
•
[Next »](signing.html)

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

**Previous page:** Reducing the Download Time
  
**Next page:** Signing JAR Files Only When Necessary




A browser with JavaScript enabled is required for this page to operate properly.