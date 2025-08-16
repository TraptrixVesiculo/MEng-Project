[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../../search.html)

**Trail:** Deployment
  
**Lesson:** Deployment In-Depth

[Home Page](../../../index.html)
>
[Deployment](../../index.html)
>
[Deployment In-Depth](../index.html)

[« Previous](../QandE/questions.html) • [TOC](../../TOC.html)

# Answers to Questions and Exercises: Deployment In-Depth

### Questions

> 1. Question:
>    What script contains functions to deploy applets and Java Web Start
>    applications?
>
>    Answer:
>    The Deployment Toolkit script contains JavaScript functions that can be used to
>    deploy applets and Java Web Start applications.
>
> - Question:
>   True or False:
>   You should always sign your RIA just to be sure it will always work.
>
>   Answer:
>   **False**: You should not sign your RIA unless absolutely necessary.

### Exercises

> 1. Exercise:
>    Write the JavaScript code to deploy the `Exercise`
>    applet using the `ex.jnlp` file.
>
>    Answer:
>
>    ```
>
>    <script src="http://www.java.com/js/deployJava.js"></script>
>    <script> 
>        var attributes = {code:'Exercise', width:300, height:300} ; 
>        var parameters = {jnlp_href: 'ex.jnlp'} ; 
>        deployJava.runApplet(attributes, parameters, '1.6'); 
>    </script>
>
>    ```

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

**Previous page:** Questions and Exercises: Deployment In-Depth




A browser with JavaScript enabled is required for this page to operate properly.