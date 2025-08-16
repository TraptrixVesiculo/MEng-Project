[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** Deployment
  
**Lesson:** Java Web Start

[Java Web Start](index.html)

[Developing a Java Web Start Application](developing.html)

[Retrieving Resources](retrievingResources.html)

[Deploying a Java Web Start Application](deploying.html)

[Setting Up a Web Server](settingUpWebServerMimeType.html)

Displaying a Customized Loading Progress Indicator

[Running a Java Web Start Application](running.html)

[Java Web Start and Security](security.html)

[Common Java Web Start Problems](problems.html)

[Questions and Exercises](QandE/questions.html)

[Home Page](../../index.html)
>
[Deployment](../index.html)
>
[Java Web Start](index.html)

[« Previous](settingUpWebServerMimeType.html) • [Trail](../TOC.html) • [Next »](running.html)

# Displaying a Customized Loading Progress Indicator

A Java Web Start application
can display a customized loading progress indicator that shows the progress of download of
the application's resources.

Consider the Weather application and the `CustomProgress` class to understand
how to implement a customized loading progress indicator for a Java Web Start application.
For the purpose of demonstrating a large and prolonged download, this
Java Web Start application's JAR file has been artifically
inflated and the `customprogress-webstart.jnlp` file
specifies additional JAR files as resources.

## Developing a Customized Loading Progress Indicator

To develop a customized loading progress indicator for your Java Web Start application, create a class that
implements the
[`DownloadServiceListener`](http://download.oracle.com/javase/7/docs/jre/api/javaws/jnlp/javax/jnlp/DownloadServiceListener.html) interface.

The constructor of the loading progress indicator class should not have any
parameters.

```

import javax.jnlp.DownloadServiceListener;
import java.awt.Container;
import java.applet.AppletStub;
import netscape.javascript.*;
...
public class CustomProgress implements DownloadServiceListener {   
    JFrame frame = null;
    JProgressBar progressBar = null;
    boolean uiCreated = false;

    public CustomProgress() {
    }
...
}    

```

The following code snippet shows how to build the UI for the loading
progress indicator:

```

private void create() {
    JPanel top = createComponents();
    frame = new JFrame(); // top level custom progress indicator UI
    frame.getContentPane().add(top, BorderLayout.CENTER);
    frame.setBounds(300,300,400,300);
    frame.pack();
    updateProgressUI(0);
}

private JPanel createComponents() {
    JPanel top = new JPanel();
    top.setBackground(Color.WHITE);
    top.setLayout(new BorderLayout(20, 20));
 
    String lblText = "<html><font color=green size=+2>JDK Documentation</font>" + 
               "<br/> The one-stop shop for Java enlightenment! <br/></html>";
    JLabel lbl = new JLabel(lblText);
    top.add(lbl, BorderLayout.NORTH);
    ...
    progressBar = new JProgressBar(0, 100);
    progressBar.setValue(0);
    progressBar.setStringPainted(true);
    top.add(progressBar, BorderLayout.SOUTH);

    return top;
}

```

Create and update the loading progress indicator in the following methods based on the
`overallPercent` argument. These methods are invoked regularly by the
Java Web Start software to communicate the progress of the application's download.
Java Web Start software will always send a message
when download and validation of resources is 100% complete.

```

public void progress(URL url, String version, long readSoFar,
                     long total, int overallPercent) {        
    updateProgressUI(overallPercent);

}

public void upgradingArchive(java.net.URL url,
                  java.lang.String version,
                  int patchPercent,
                  int overallPercent) {
    updateProgressUI(overallPercent);
}

public void validating(java.net.URL url,
            java.lang.String version,
            long entry,
            long total,
            int overallPercent) {
    updateProgressUI(overallPercent);
}

private void updateProgressUI(int overallPercent) {
    if (overallPercent > 0 && overallPercent < 99) {
        if (!uiCreated) {
            uiCreated = true;
            // create custom progress indicator's UI only if 
            // there is more work to do, meaning overallPercent > 0 and < 100
            // this prevents flashing when RIA is loaded from cache
            create();
        }
        progressBar.setValue(overallPercent);
        SwingUtilities.invokeLater(new Runnable() {
            public void run() {
                frame.setVisible(true);
            }
        });
    } else {
        // hide frame when overallPercent is above 99
        SwingUtilities.invokeLater(new Runnable() {
            public void run() {
                frame.setVisible(false);
                frame.dispose();
            }
        });
    }
}

```

Compile the loading progress indicator class and build a JAR file with all the
resources needed to display the loading progress indicator.
Include the `<your JRE directory>/lib/javaws.jar` file in your
`classpath` to enable compilation.

The loading progress indicator class is now ready for use. The next step is to
specify this loading progress indicator JAR file as your Java Web Start
application's progress indicator.

## Specifying a Customized Loading Progress Indicator for a Java Web Start Application

To specify a customized loading progress indicator for a Java Web Start application,
include the following information in the application's JNLP file:

* `jar` tag with the `download="progress"` attribute
* `progress-class` attribute with the fully qualified name of the
  customized loading progress class.

The following code snippet from the
[`customprogress-webstart.jnlp`](examples/webstart_AppWithCustomProgressIndicator/src/customprogress-webstart.jnlp) file displays the usage of the `download="progress"` and
`progress-class` attributes.

```

<jnlp spec="1.0+" codebase="http://download.oracle.com/javase/tutorialJWS/deployment/webstart/ex6" 
      href="webstart_AppWithCustomProgressIndicator/customprogress-webstart.jnlp">
...
  <resources>
    <j2se version="1.6+"/>
    <jar href="webstart_AppWithCustomProgressIndicator/webstart_AppWithCustomProgressIndicator.jar" />
    <jar href="webstart_CustomProgressIndicator/webstart_CustomProgressIndicator.jar"
         download="progress" />
    <jar href="webstart_AppWithCustomProgressIndicator/lib/IconDemo.jar" />
    <jar href="webstart_AppWithCustomProgressIndicator/lib/SplitPaneDemo.jar" />
    <jar href="webstart_AppWithCustomProgressIndicator/lib/SplitPaneDemo2.jar" />
    <jar href="webstart_AppWithCustomProgressIndicator/lib/TextBatchPrintingDemo.jar" />
    <jar href="webstart_AppWithCustomProgressIndicator/lib/ToolBarDemo.jar" />
    <jar href="webstart_AppWithCustomProgressIndicator/lib/ToolBarDemo2.jar" />
    <jar href="webstart_AppWithCustomProgressIndicator/lib/SwingSet2.jar" />
  </resources>
  <application-desc 
      main-class="customprogressindicatordemo.Main"
      progress-class="customprogressindicator.CustomProgress"
  />
...
</jnlp>

```

Deploy the Java Web Start application in a web page. Open
[`JavaWebStartAppPage.html`](examples/dist/webstart_AppWithCustomProgressIndicator/JavaWebStartAppPage.html) in a web browser to view the customized loading progress indicator for the Weather application.

---

**Note:** To view the example properly, you need to install at least the [Java SE Development Kit (JDK) 6 update 18](http://java.sun.com/javase/downloads/index.jsp) release.

---

---

**Note:**  If you have viewed this Java Web Start application before, clear your cache by using the Java Control
Panel before viewing the application again. You will not be able to see a progress
indicator for a previously cached application.

---

---

**Note:** If you don't see the example running, you might need to enable the JavaScript interpreter in your browser so that the Deployment Toolkit script can function properly.

---

[Download source code](examplesIndex.html#AppWithCustomProgressIndicator) for the *Java Web Start Application With Customized Loading Progress Indicator* example to experiment further.

See the
[Customizing the Loading Experience](../../deployment/doingMoreWithRIA/customizeRIALoadingExperience.html) topic for more information about customizing the rich Internet application (RIA) loading experience.

[« Previous](settingUpWebServerMimeType.html)
•
[Trail](../TOC.html)
•
[Next »](running.html)

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

**Previous page:** Setting Up a Web Server
  
**Next page:** Running a Java Web Start Application




A browser with JavaScript enabled is required for this page to operate properly.