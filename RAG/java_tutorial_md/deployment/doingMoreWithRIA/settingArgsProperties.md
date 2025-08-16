[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** Deployment
  
**Lesson:** Doing More With Rich Internet Applications

[Doing More With Rich Internet Applications](index.html)

Setting Trusted Arguments and Secure Properties

[System Properties](properties.html)

[JNLP API](jnlpAPI.html)

[Accessing the Client Using JNLP API](usingJNLPAPI.html)

[Cookies](cookies.html)

[Accessing Cookies](accessingCookies.html)

[Customizing the Loading Experience](customizeRIALoadingExperience.html)

[Questions and Exercises](QandE/questions.html)

[Home Page](../../index.html)
>
[Deployment](../index.html)
>
[Doing More With Rich Internet Applications](index.html)

[« Previous](index.html) • [Trail](../TOC.html) • [Next »](properties.html)

# Setting Trusted Arguments and Secure Properties

You can set certain Java Virtual Machine arguments and secure properties
for your rich Internet
application (RIA) in the RIA's Java Network Launch Protocol (JNLP) file.
For applets, you can also set arguments in the
`java_arguments` parameter of the `<applet>` tag.
Although there is a predefined set of secure properties, you can also define new
secure properties by prefixing the property name with "`jnlp.`"
or "`javaws.`".
Properties can be retrieved in your RIA by using the `System.getProperty`
method.

Consider the Properties and Arguments Demo applet.
The following Java Virtual Machine arguments and properties are set in the applet's
JNLP file,
[`appletpropsargs.jnlp`](examples/applet_PropertiesAndVMArgs/src/appletpropsargs.jnlp).

* `-Xmx` – A secure argument set equal to "256M"
* `sun.java2d.noddraw` – A predefined secure property
  set equal to "true"
* `jnlp.myProperty` – A user-defined secure property
  set equal to "a user-defined property"

```

<?xml version="1.0" encoding="UTF-8"?>
<jnlp spec="1.0+" codebase="" href="">
    <information>
        <title>Properties and Arguments Demo Applet</title>
        <vendor>Dynamic Team</vendor>
    </information>
    <resources>
        <!-- Application Resources -->
        <j2se version="1.6+"
              href="http://java.sun.com/products/autodl/j2se"
              java-vm-args="-Xmx256M"/> <!-- secure java vm argument -->
        <jar href="applet_PropertiesAndVMArgs.jar" main="true" />
            <!-- secure properties -->
        <property name="sun.java2d.noddraw" value="true"/>
        <property name="jnlp.myProperty" value="a user-defined property"/>
    </resources>
    <applet-desc 
         name="Properties and Arguments Demo Applet"
         main-class="PropertiesArgsDemoApplet"
         width="800"
         height="50">             
     </applet-desc>
     <update check="background"/>
</jnlp>

```

The
[`PropertiesArgsDemoApplet`](examples/applet_PropertiesAndVMArgs/src/PropertiesArgsDemoApplet.java) class uses the `System.getProperty` method to retrieve the
`java.version` property and other properties that
are set in the JNLP file. The `PropertiesArgsDemoApplet` class
also displays the properties.

```


import javax.swing.JApplet;
import javax.swing.SwingUtilities;
import javax.swing.JLabel;

public class PropertiesArgsDemoApplet extends JApplet {
    public void init() {
        final String javaVersion = System.getProperty("java.version");
        final String  swing2dNoDrawProperty = System.getProperty("sun.java2d.noddraw");
        final String  jnlpMyProperty = System.getProperty("jnlp.myProperty");        

        try {
            SwingUtilities.invokeAndWait(new Runnable() {
                public void run() {
                    createGUI(javaVersion, swing2dNoDrawProperty, jnlpMyProperty);
                }
            });
        } catch (Exception e) {
            System.err.println("createGUI didn't successfully complete");
        }
    }
    private void createGUI(String javaVersion, String swing2dNoDrawProperty, String jnlpMyProperty) {
        String text = "Properties: java.version = " + javaVersion + 
                ",  sun.java2d.noddraw = " + swing2dNoDrawProperty +
                ",   jnlp.myProperty = " + jnlpMyProperty;
        JLabel lbl = new JLabel(text);
        add(lbl);
    }
}

```

The Properties and Arguments Demo applet is shown next. You can also see the
applet running in
[`AppletPage.html`](examples/dist/applet_PropertiesAndVMArgs/AppletPage.html).



A browser with JavaScript enabled is required for this page to operate properly.

---

**Note:** If you don't see the applet running, you need to install at least the [Java SE Development Kit (JDK) 6 update 10](http://java.sun.com/javase/downloads/index.jsp) release.

---

---

**Note:** If you don't see the example running, you might need to enable the JavaScript interpreter in your browser so that the Deployment Toolkit script can function properly.

---

[Download source code](examplesIndex.html#PropertiesAndVMArgs) for the *Properties and Arguments Demo Applet* example to experiment further.

See
[System Properties](properties.html) for a complete set of system properties that can be accessed by RIAs.

[« Previous](index.html)
•
[Trail](../TOC.html)
•
[Next »](properties.html)

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

**Previous page:** Doing More With Rich Internet Applications
  
**Next page:** System Properties




A browser with JavaScript enabled is required for this page to operate properly.