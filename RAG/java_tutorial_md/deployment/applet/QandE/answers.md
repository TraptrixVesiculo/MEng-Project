[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../../search.html)

**Trail:** Deployment
  
**Lesson:** Applets

[Home Page](../../../index.html)
>
[Deployment](../../index.html)
>
[Applets](../index.html)

[« Previous](../QandE/questions.html) • [TOC](../../TOC.html)

# Answers to Questions and Exercises: Applets

## Questions

1. Question: Which classes can an applet extend?

   Answer: An applet can extend the `java.applet.Applet` class or the `java.swing.JApplet` class.

   The `java.applet.Applet` class extends the `java.awt.Panel` class and enables you to use the GUI tools in the AWT package.

   The `java.swing.JApplet` class is a subclass of `java.applet.Applet` that also enables you to use the Swing GUI tools.
2. Question: For what do you use the `start()` method?

   Answer: You use the `start()` method when the applet must perform a task after it is initialized, before receiving user input. The `start()` method either performs the applet's work or (more likely) starts up one or more threads to perform the work.
3. Question: True or false: An applet can make network connections to any host on the Internet.

   Answer: **False**: An applet can only connect to the host that it came from.
4. Question: How do you get the value of a parameter specified in the JNLP file from within the applet's code?

   Answer: You use the `getParameter("Parameter name")` method, which returns the String value of the parameter.
5. Question: Which class enables applets to interact with JavaScript code in the applet's web page?

   Answer: The `netscape.javascript.JSObject` class enables applets to interact with JavaScript code in the applet's web page.
6. Question: True or False: Applets can modify the contents of the parent web page.

   Answer: **True**:Applets can modify the contents of the parent web page by using the `getDocument` method of the `com.sun.java.browser.plugin2.DOM` class and the Common DOM API.

## Exercises

1. Exercise: The `Exercise` applet's parent web page has a JavaScript variable called
   `memberId`. Write the code to set the value of the
   `memberId` equal to "123489" in the applet's
   `start` method.

   Answer:

   ```

   import java.applet.Applet;
   import netscape.javascript.*; // add plugin.jar to classpath during compilation

   public class Exercise extends Applet {
       public void start() {
           try {
               JSObject window = JSObject.getWindow(this);
               window.setMember("memberId", "123489");
           } catch (JSException jse) {
               jse.printStackTrace();
           }
       }
   }

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

**Previous page:** Questions and Exercises: Applets




A browser with JavaScript enabled is required for this page to operate properly.