[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** Deployment
  
**Lesson:** Applets
  
**Section:** Doing More With Applets

[Applets](index.html)

[Getting Started With Applets](getStarted.html)

[Defining an Applet Subclass](subclass.html)

[Methods for Milestones](appletMethods.html)

[Life Cycle of an Applet](lifeCycle.html)

[Applet's Execution Environment](appletExecutionEnv.html)

[Developing an Applet](developingApplet.html)

[Deploying an Applet](deployingApplet.html)

[Deploying With the Applet Tag](html.html)

[Doing More With Applets](doingMoreWithApplets.html)

[Finding and Loading Data Files](data.html)

[Defining and Using Applet Parameters](param.html)

[Displaying Short Status Strings](showStatus.html)

[Displaying Documents in the Browser](browser.html)

[Invoking JavaScript Code From an Applet](invokingJavaScriptFromApplet.html)

[Invoking Applet Methods From JavaScript Code](invokingAppletMethodsFromJavaScript.html)

[Manipulating DOM of Applet's Web Page](manipulatingDOMFromApplet.html)

Displaying a Customized Loading Progress Indicator

[Writing Diagnostics to Standard Output and Error Streams](stdout.html)

[Developing Draggable Applets](draggableApplet.html)

[Communicating With Other Applets](iac.html)

[Working With a Server-Side Application](server.html)

[Network Client Applet Example](clientExample.html)

[What Applets Can and Cannot Do](security.html)

[Solving Common Applet Problems](problemsindex.html)

[Questions and Exercises](QandE/questions.html)

[Home Page](../../index.html)
>
[Deployment](../index.html)
>
[Applets](index.html)

[« Previous](manipulatingDOMFromApplet.html) • [Trail](../TOC.html) • [Next »](stdout.html)

# Displaying a Customized Loading Progress Indicator

An applet can display a customized loading progress indicator that shows the
progress of download of the applet's resources as well as other applet specific data..

Consider the Weather applet and the `CustomProgress` class to understand
how to implement a customized loading progress indicator for an applet. For the purpose of demonstrating
a large and prolonged download, this applet's JAR file has been artifically
inflated and the `customprogress-applet.jnlp` file specifies additional JAR files
as resources.

## Developing a Customized Loading Progress Indicator

To develop a customized loading progress indicator for your applet, create a class that
implements the
[`DownloadServiceListener`](http://download.oracle.com/javase/7/docs/jre/api/javaws/jnlp/javax/jnlp/DownloadServiceListener.html) interface.

The constructor of the loading progress indicator class will vary depending on
how the UI should be displayed and the capabilities needed by the class. The
following guidelines should be applied:

* To display the loading progress indicator in a separate top level window,
  create a constructor that does not have any parameters.
* To display the loading progress indicator for an applet in the applet's
  container, create a constructor that takes an `Object` as a parameter.
  The `Object`
  argument can be typecast to an instance of the
  [`java.awt.Container`](http://download.oracle.com/javase/7/docs/api/java/awt/Container.html) class.
* If the loading progress indicator class needs to access the applet's parameters,
  create two constructors as follows:
  + Create a constructor that takes an `Object` as a parameter as described
    previously.
  + Create a constructor that takes two parameters of type `Object`. The
    first argument can be typecast to an instance of the
    [`java.awt.Container`](http://download.oracle.com/javase/7/docs/api/java/awt/Container.html) class and the second argument can be typecast to an instance of the
    [`java.applet.AppletStub`](http://download.oracle.com/javase/7/docs/api/java/applet/AppletStub.html) class.

  The Java Plug-in software will invoke the appropriate constructor depending
  on the capabilities of the JRE software on the client machine.

```

import javax.jnlp.DownloadServiceListener;
import java.awt.Container;
import java.applet.AppletStub;
import netscape.javascript.*;
...
public class CustomProgress implements DownloadServiceListener {   
    Container surfaceContainer = null;
    AppletStub appletStub = null;
    JProgressBar progressBar = null;
    JLabel statusLabel = null;
    boolean uiCreated = false;

    public CustomProgress(Object surface) {
       init(surface, null);
    }

    public CustomProgress(Object surface, Object stub) {
        init(surface, stub);
    }

    public void init(Object surface, Object stub) {
        try {
            surfaceContainer = (Container) surface;
            appletStub = (AppletStub) stub;
        } catch (ClassCastException cce) {
            ...
        }
    }
...
}    

```

The following code snippet shows how to build the UI for the loading
progress indicator. Use the instance of the
[`java.applet.AppletStub`](http://download.oracle.com/javase/7/docs/api/java/applet/AppletStub.html) class to
retrieve the applet's parameters. Invoke the `JSObject.getWindow(null)`
method to obtain a reference to the applet's parent web page and invoke JavaScript
code on that page.

```

private void create() {
    JPanel top = createComponents();
    if (surfaceContainer != null) {
        // lay out loading progress UI in the given Container
        surfaceContainer.add(top, BorderLayout.NORTH);
        surfaceContainer.invalidate();
        surfaceContainer.validate();
    }     
}
private JPanel createComponents() {
    JPanel top = new JPanel();
    ...
    // get applet parameter using an instance of the AppletStub class
    // "tagLine" parameter specified in applet's JNLP file
    String tagLine = "";
    if (appletStub != null) {
        tagLine = appletStub.getParameter("tagLine");
    }
    String lblText = "<html><font color=red size=+2>JDK Documentation</font><br/>" +
                        tagLine + " <br/></html>";
    JLabel lbl = new JLabel(lblText);
    top.add(lbl, BorderLayout.NORTH);

    // use JSObject.getWindow(null) method to retrieve a reference to 
    // the web page and make JavaScript calls. Duke logo displayed if 
    // displayLogo variable set to "true" in the web page
    String displayLogo = "false";    
    JSObject window = JSObject.getWindow(null);        
    if (window != null) {
        displayLogo = (String)window.getMember("displayLogo");
    }
    if (displayLogo.equals("true")) {
        lbl = new JLabel();
        ImageIcon logo = createImageIcon("images/DukeWave.gif", "logo");
        lbl.setIcon(logo);
        top.add(lbl, BorderLayout.EAST);
    }

    statusLabel = new JLabel("html><font color=green size=-2>Loading applet...</font></html>");
    top.add(statusLabel, BorderLayout.CENTER);

    // progress bar displays progress
    progressBar = new JProgressBar(0, 100);
    progressBar.setValue(0);
    progressBar.setStringPainted(true);
    top.add(progressBar, BorderLayout.SOUTH);

    return top;
}

```

Create and update the progress indicator in the following methods based on the
`overallPercent` argument. These methods are invoked regularly by the
Java Plug-in software to communicate progress of the applet's download.
Java Plug-in software will always send a message when
download and validation of resources is 100% complete.

```

public void progress(URL url, String version, long readSoFar,
                     long total, int overallPercent) {        
    // check progress of download and update display
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
    if (!uiCreated && overallPercent > 0 && overallPercent < 100) {
        // create custom progress indicator's UI only if 
        // there is more work to do, meaning overallPercent > 0 and < 100
        // this prevents flashing when RIA is loaded from cache
        create(); 
        uiCreated = true;            
    }
    if (uiCreated) {
        progressBar.setValue(overallPercent);
    }
}

```

Compile the loading progress indicator class and build a JAR file with all the
resources needed to display the loading progress indicator.
Include the following JAR files in your `classpath` to enable compilation:

* `<your JRE directory>/lib/javaws.jar`
* `<your JRE directory>/lib/plugin.jar` – This JAR file
  is required only if your loading progress indicator class uses the `JSObject.getWindow`
  method to invoke JavaScript code in the applet's parent web page.

The loading progress indicator class is now ready for use. The next step is to
specify this loading progress indicator JAR file as your applet's loading progress
indicator.

## Specifying a Loading Progress Indicator for an Applet

To specify a customized loading progress indicator for an applet, include the following
information in the applet's JNLP file:

* `jar` tag with the `download="progress"` attribute
* `progress-class` attribute with the fully qualified name of the
  loading progress class.

The following code snippet from the
[`customprogress-applet.jnlp`](examples/applet_AppletWithCustomProgressIndicator/src/customprogress-applet.jnlp) file displays the usage of the `download="progress"` and
`progress-class` attributes.

```

<jnlp spec="1.0+" codebase="http://download.oracle.com/javase/tutorial/deployment" href="">
...
  <resources>
    ...
    <jar href="applet/examples/dist/applet_AppletWithCustomProgressIndicator" main="true" />    
    <jar href="applet/examples/dist/applet_CustomProgressIndicator/applet_CustomProgressIndicator.jar" 
            download="progress" />
  </resources>
  <applet-desc
     name="customprogressindicatordemo.WeatherApplet"
     main-class="customprogressindicatordemo.WeatherApplet"
     progress-class="customprogressindicator.CustomProgress"
     width="600"
     height="200">
     <param name="tagLine" value="Information straight from the horse's mouth!"/>
  </applet-desc>
...
</jnlp>

```

Deploy the applet in a web page. Open
[`AppletPage.html`](examples/dist/applet_AppletWithCustomProgressIndicator/AppletPage.html) in a web browser to view the loading progress indicator for the Weather applet.

---

**Note:** To view the example properly, you need to install at least the [Java SE Development Kit (JDK) 6 update 21](http://java.sun.com/javase/downloads/index.jsp) release.

---

---

**Note:**  If you have viewed this applet before, clear your cache by using the Java Control
Panel before viewing the applet again. You will not be able to see a progress
indicator for a previously cached applet.

---

---

**Note:** If you don't see the example running, you might need to enable the JavaScript interpreter in your browser so that the Deployment Toolkit script can function properly.

---

## Integrating the Loading Progress Indicator With Applet UI

You can also integrate the loading progress indicator into the applet's UI.
Open
[`AppletPage.html`](examples/dist/applet_AppletWithIntegratedProgressIndicator/AppletPage.html) in a web browser to view the loading progress indicator integrated into the Weather applet's UI.
View the
[`IntegratedProgressIndicator.java`](examples/applet_AppletWithIntegratedProgressIndicator/src/integratedprogressdemo/IntegratedProgressIndicator.java) class and the inline comments for more information.

Download source code for the following examples to experiment further:

* [*Applet With Customized Loading Progress Indicator*](examplesIndex.html#AppletWithCustomProgressIndicator)
* [*Applet With Integrated Progress Indicator*](examplesIndex.html#AppletWithIntegratedProgressIndicator)

See the
[Customizing the Loading Experience](../../deployment/doingMoreWithRIA/customizeRIALoadingExperience.html) topic for more information about customizing the rich Internet application (RIA) loading experience.

[« Previous](manipulatingDOMFromApplet.html)
•
[Trail](../TOC.html)
•
[Next »](stdout.html)

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

**Previous page:** Manipulating DOM of Applet's Web Page
  
**Next page:** Writing Diagnostics to Standard Output and Error Streams




A browser with JavaScript enabled is required for this page to operate properly.