[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** Deployment
  
**Lesson:** Doing More With Rich Internet Applications

[Doing More With Rich Internet Applications](../index.html)

[Setting Trusted Arguments and Secure Properties](../settingArgsProperties.html)

[System Properties](../properties.html)

[JNLP API](../jnlpAPI.html)

[Accessing the Client Using JNLP API](../usingJNLPAPI.html)

[Cookies](../cookies.html)

[Accessing Cookies](../accessingCookies.html)

[Customizing the Loading Experience](../customizeRIALoadingExperience.html)

Questions and Exercises

[Home Page](../../../index.html)
>
[Deployment](../../index.html)
>
[Doing More With Rich Internet Applications](../index.html)

[« Previous](../customizeRIALoadingExperience.html) • [Trail](../../TOC.html) • [Next »](../../deploymentInDepth/index.html)

# Questions and Exercises: Doing More With Rich Internet Applications

## Questions

1. True or False:
   Rich Internet applications (RIAs) can set secure properties by prefixing
   the property name with `"jnlp."`.
2. True or False:
   Only signed RIAs can use JNLP API to access files on the client.

## Exercises

1. To the following JNLP file, add a secure property called
   `jnlp.foo` and set its value to `true`.

   ```

   <?xml version="1.0" encoding="UTF-8"?>
   <jnlp spec="1.0+" codebase="" href="">
       <information>
           <title>Dynamic Tree Demo</title>
           <vendor>Dynamic Team</vendor>

       </information>
       <resources>
           <!-- Application Resources -->
           <j2se version="1.6+"
                 href="http://java.sun.com/products/autodl/j2se" />
           <jar href="DynamicTreeDemo.jar" main="true" />
       </resources>
       <applet-desc 
            name="Dynamic Tree Demo Applet"
            main-class="components.DynamicTreeApplet"
            width="300"
            height="300">
        </applet-desc>
        <update check="background"/>
   </jnlp>				

   ```

[Check your answers.](answers.html)

[« Previous](../customizeRIALoadingExperience.html)
•
[Trail](../../TOC.html)
•
[Next »](../../deploymentInDepth/index.html)

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

**Previous page:** Customizing the Loading Experience
  
**Next page:** Deployment In-Depth




A browser with JavaScript enabled is required for this page to operate properly.