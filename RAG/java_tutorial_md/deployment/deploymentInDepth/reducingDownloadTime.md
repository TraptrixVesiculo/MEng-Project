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

Reducing the Download Time

[Avoiding Unnecessary Update Checks](avoidingUnnecessaryUpdateChecks.html)

[Signing JAR Files Only When Necessary](signing.html)

[Ensuring the Presence of the JRE Software](ensuringJRE.html)

[Questions and Exercises](QandE/questions.html)

[Home Page](../../index.html)
>
[Deployment](../index.html)
>
[Deployment In-Depth](index.html)

[« Previous](bestPractices.html) • [Trail](../TOC.html) • [Next »](avoidingUnnecessaryUpdateChecks.html)

# Reducing the Download Time

Rich Internet applications (RIAs) are downloaded from a web site when the user
tries to access them. (RIAs can be cached after the initial download to improve
performance). The time taken to download a RIA depends on the size of the
RIA's JAR file. Larger JAR files take longer to download.

You can reduce the download time of your RIA by applying the following techniques:

* Compress your RIA's JAR file by using the
  [`pack200`](http://download.oracle.com/javase/7/docs/technotes/tools/share/pack200.html) tool.
* Remove unnecessary white space from the Java Network Launch Protocol
  (JNLP) file and the JavaScript files.
* Optimize images and animation.

`pack200` compression for signed and unsigned RIAs is discussed
in greater detail in this topic.

#### Compressing the JAR File for an Unsigned RIA

The following steps describe how to create and deploy a compressed
JAR file for an unsigned RIA.

1. Compress the JAR file of your RIA.

   ```

   // compresses DynamicTreeDemo.jar to produce DynamicTreeDemo.jar.pack.gz
   pack200 DynamicTreeDemo.jar.pack.gz DynamicTreeDemo.jar

   ```
2. Set the `jnlp.packEnabled` property to `true` in the RIA's
   JNLP file.

   ```

   <resources>    
   		<j2se version="1.6+"
   		    href="http://java.sun.com/products/autodl/j2se"
   				max-heap-size="128m" />
   		<jar href="DynamicTreeDemo.jar" main="true"/>
   		<property name="jnlp.packEnabled" value="true"/>
   		...
   		...
   </resources>

   ```

#### Compressing and Signing RIA JAR File

The following steps describe how to create and deploy a compressed JAR file for a
signed RIA. See the topic,
[Signing JAR Files Only When Necessary](../../deployment/deploymentInDepth/signing.html), to understand the impact of signing JAR files.

1. Normalize the JAR file using the `--repack` option.

   This step
   ensures that the security certificate and JAR file will pass verification
   checks when the RIA is launched.

   ```

   pack200 --repack DynamicTreeDemo.jar

   ```
2. Sign the normalized JAR file.

   ```

   jarsigner -keystore myKeyStore DynamicTreeDemo.jar me

   ```

   where `myKeyStore` is the name of the keystore and `me`
   is the alias for the keystore.
3. Pack the signed the JAR file

   ```

   pack200 DynamicTreeDemo.jar.pack.gz DynamicTreeDemo.jar    

   ```
4. Set the `jnlp.packEnabled` property to `true` in the RIA's
   JNLP file.

   ```

   <resources>    
   		<j2se version="1.6+"
   		    href="http://java.sun.com/products/autodl/j2se"
   				max-heap-size="128m" />
   		<jar href="DynamicTreeDemo.jar" main="true"/>
   		<property name="jnlp.packEnabled" value="true"/>
   		...
   		...
   </resources>

   ```

When the `jnlp.packEnabled` property is set in the JNLP file,
the Java Plug-in software looks for the compressed JAR file with the
`.pack.gz` extension
(for example, `DynamicTreeDemo.jar.pack.gz`).
If found, the Java Plug-in software automatically unpacks and loads the JAR file.
If a file with the `.pack.gz` extension is not found,
then the Java Plug-in software attempts to load the regular JAR file
(for example, `DynamicTreeDemo.jar`).

---

**Note:**  You need to deploy your RIA on a web server to test the
`jnlp.packEnabled` property.

---

[« Previous](bestPractices.html)
•
[Trail](../TOC.html)
•
[Next »](avoidingUnnecessaryUpdateChecks.html)

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

**Previous page:** Deployment Best Practices
  
**Next page:** Avoiding Unnecessary Update Checks




A browser with JavaScript enabled is required for this page to operate properly.