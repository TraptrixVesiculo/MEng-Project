[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../../search.html)

**Trail:** Deployment
  
**Lesson:** Java Web Start

[Home Page](../../../index.html)
>
[Deployment](../../index.html)
>
[Java Web Start](../index.html)

[« Previous](../QandE/questions.html) • [TOC](../../TOC.html)

# Answers to Questions and Exercises: Java Web Start

## Questions

1. **Question: **In a link that is to run a Java Web Start application, which file is specified as the `a` tag's `href` attribute?****

   **Answer: **You use the application's `JNLP` file name as the value of the `href` attribute. When a user clicks the link to the `JNLP` file, Java Web Start loads the application specified by that `JNLP` file.****
2. **Question: **Which MIME type must a Web server recognize in order for it to host Java Web Start applications?****

   **Answer: **You must configure the Web server so that files with the .jnlp extension are set to the `application/x-java-jnlp-file` MIME type.****
3. **Question: **In an application's `JNLP` file, which two elements must be specified within the `resources` element?****

   **Answer: **The `resources` element must contain:****

   * The `j2se` element, which specifies the Java platform on which to run the application.
   * The `jar` element, which specifies the JAR file for the application.
4. **Question: **Which interface provides the ability to an application to control how its own resources are cached?****

   1. `BasicService`
   2. `DownloadService`
   3. `PersistenceService`
   4. `ExtendedService`

   **Answer: **B. The `DownloadService` interface provides the ability to an application to control how its own resources are cached.****
5. **Question: **True or False: Java Web Start applications run in a secure *sandbox* by default.****

   **Answer: ****True**.****
6. **Question: **True or False: If a Java Web Start application is running in a secure sandbox, JAR files for the application can reside on different servers.****

   **Answer: ****False**. All JAR files for the application must reside on the same server.****
7. **Question: **For a Java Web Start application to support operations outside of the secure sandbox, what must you do with its JAR files?****

   **Answer: **You must sign JAR files to enable your application can work outside of the sandbox.****

## Exercises

1. **Exercise: **Write the XML code you would add to a `JNLP` file in order to request that the application have complete access to the client system.****

   **Answer:**

   ```

   <security>
      <all-permissions/>
   </security>

   ```
2. **Exercise: **For a Java Web Start application, you have two icons, `one.gif` and `two.gif`, in the `images` directory in a JAR file. Write the application code you would use to access these images.****

   **Answer:**

   ```

   // Get current classloader
   ClassLoader cl = this.getClass().getClassLoader();
   // Create icons
   Icon firstIcon  = new ImageIcon(cl.getResource("images/one.gif"));
   Icon secondIcon   = new ImageIcon(cl.getResource("images/two.gif"));

   ```

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

**Previous page:** Questions and Exercises: Java Web Start




A browser with JavaScript enabled is required for this page to operate properly.