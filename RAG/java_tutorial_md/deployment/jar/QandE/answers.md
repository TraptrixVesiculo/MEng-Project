[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../../search.html)

**Trail:** Deployment
  
**Lesson:** Packaging Programs in JAR Files

[Home Page](../../../index.html)
>
[Deployment](../../index.html)
>
[Packaging Programs in JAR Files](../index.html)

[« Previous](../QandE/questions.html) • [TOC](../../TOC.html)

# Answers to Questions and Exercises: JAR

### Questions

1. Question:
   How do you invoke an applet that is packaged as a JAR file?

   Answer:
   To invoke an applet packaged as a JAR file, open a page containing the applet:

   ```

   <applet code=AppletClassName.class
           archive="JarFileName.jar"
           width=320 height=240>
   </applet>

   ```

- Question:
  What is the purpose of the `-e` option in a `jar` command?

  Answer:
  This option is available since Java SE 6. It sets the entrypoint as the application entry point for stand-alone applications bundled into executable jar file. The use of this option creates or overrides the Main-Class attribute value in the manifest file. This option can be used during creation of jar file or while updating the jar file. This option specifies the application entry point without editing or creating the manifest file.
  For example, this command creates Main.jar where the Main-Class attribute value in the manifest is set to Main:

  ```

  jar cfe Main.jar Main Main.class

  ```

- Question:
  What is the significance of the manifest in a JAR file?

  Answer:
  A JAR file's manifest provides meta-information about the other contents of
  the JAR file. The manifest itself resides in META-INF/MANIFEST.mf. The
  meta-information can include
  * Dependencies on other jar files
  * The name of a class to run when "java -jar file.jar" is invoked
  * Versioning information
  * Security information

- Question:
  How do you modify a JAR's manifest file?

  Answer:
  Typically, modifying the default manifest involves adding
  special-purpose headers to the manifest that allow the JAR
  file to perform a particular desired function.

  To modify the manifest, you must first prepare a text file
  with a complete and valid manifest file.
  You then use the JAR tool's `m` option to add the
  information in your file to the manifest.

  The manifest file your prepare must end with a new line or carriage return.
  The last line will not be parsed properly if it does not end with a new line or carriage return.

[« Previous](../QandE/questions.html)
•
[TOC](../../TOC.html)


---

Problems with the examples? Try [Compiling and Running
the Examples: FAQs](../../../information/run-examples.html).
  
Complaints? Compliments? Suggestions? [Give
us your feedback](http://download.oracle.com/javase/feedback.html).

Your use of this page and all the material on pages under "The Java Tutorials" banner,
and all the material on pages under "The Java Tutorials" banner is subject to the [Java SE Tutorial Copyright
and License](../../../information/license.html).
Additionally, any example code contained in any of these Java
Tutorials pages is licensed under the
[Code
Sample License](http://developers.sun.com/license/berkeley_license.html).

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| |  |  | | --- | --- | | duke image | Oracle logo | | [About Oracle](http://www.oracle.com/us/corporate/index.html) | [Oracle Technology Network](http://www.oracle.com/technology/index.html) | [Terms of Service](https://www.samplecode.oracle.com/servlets/CompulsoryClickThrough?type=TermsOfService) | Copyright © 1995, 2011 Oracle and/or its affiliates. All rights reserved. |

**Previous page:** Questions and Exercises: JAR




A browser with JavaScript enabled is required for this page to operate properly.