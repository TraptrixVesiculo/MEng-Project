[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** Deployment
  
**Lesson:** Doing More With Rich Internet Applications
  
**Section:** JNLP API

[Doing More With Rich Internet Applications](index.html)

[Setting Trusted Arguments and Secure Properties](settingArgsProperties.html)

[System Properties](properties.html)

[JNLP API](jnlpAPI.html)

Accessing the Client Using JNLP API

[Cookies](cookies.html)

[Accessing Cookies](accessingCookies.html)

[Customizing the Loading Experience](customizeRIALoadingExperience.html)

[Questions and Exercises](QandE/questions.html)

[Home Page](../../index.html)
>
[Deployment](../index.html)
>
[Doing More With Rich Internet Applications](index.html)

[« Previous](jnlpAPI.html) • [Trail](../TOC.html) • [Next »](cookies.html)

# Accessing the Client Using JNLP API

When launched by using the Java Network Launch Protocol (JNLP),
rich Internet applications (RIAs)
can access the client with the user's permission. Consider the
Text Editor applet example to understand how to
use JNLP API based services.
The Text Editor has a text area and buttons labeled Open, Save, and SaveAs. The
Text Editor can be used to open an existing text file, edit it, and save it back to disk.

The Text Editor applet is shown next.



A browser with JavaScript enabled is required for this page to operate properly.

---

**Note:** If you don't see the applet running, you need to install at least the [Java SE Development Kit (JDK) 6 update 10](http://java.sun.com/javase/downloads/index.jsp) release.

---

---

**Note:** If you don't see the example running, you might need to enable the JavaScript interpreter in your browser so that the Deployment Toolkit script can function properly.

---

The
[`TextEditor`](examples/applet_JNLP_API/src/TextEditor.java) and
[`TextEditorApplet`](examples/applet_JNLP_API/src/TextEditor.java) classes lay out the user interface and display it as an applet. The
[`FileHandler`](examples/applet_JNLP_API/src/FileHandler.java) class contains the core functionality with respect to using JNLP API based services.

Remember, the techniques
described in this topic apply to Java Web Start applications as well.

To make use of a JNLP service, first retrieve a
reference to the service. The `initialize` method of the
`FileHandler` class retrieves references to JNLP services as
shown in the following code snippet:

```

private static synchronized void initialize() {
    ...
    try {
        
        fos = (FileOpenService) ServiceManager.lookup("javax.jnlp.FileOpenService");
        fss = (FileSaveService) ServiceManager.lookup("javax.jnlp.FileSaveService");
        
    } catch (UnavailableServiceException e) {
        ...
    }
}

```

After you have a reference to the required services, invoke methods on
the service to perform the necessary operations. The `open` method of the
`FileHandler` class invokes the `openFileDialog` method of the
[`FileOpenService`](http://download.oracle.com/javase/7/docs/jre/api/javaws/jnlp/javax/jnlp/FileOpenService.html) class to display a file chooser. The `open` method returns the contents of the
selected file.

```

public static String open() {
    initialize();
    try {
        fc = fos.openFileDialog(null, null);
        return readFromFile(fc);
    } catch (IOException ioe) {
        ioe.printStackTrace(System.out);
        return null;
    }
}

```

Similarly, the `save` and `saveAs` methods
of the `FileHandler` class invoke corresponding methods of the
[`FileSaveService`](http://download.oracle.com/javase/7/docs/jre/api/javaws/jnlp/javax/jnlp/FileSaveService.html) class to enable the user to select a file name and
save the contents of the text area to disk.

```

public static void saveAs(String txt) {
    initialize();
    try {
        if (fc == null) {
            // If not already saved. Save-as is like save
            save(txt);
        } else {
            fc = fss.saveAsFileDialog(null, null, fc);
            save(txt);
        }
    } catch (IOException ioe) {
        ioe.printStackTrace(System.out);
    }
}

```

At runtime, when the RIA attempts to open or save a file, users see a
security dialog asking them if they want to allow the action. The operation will
proceed only if users allow the RIA to access their environment.

The complete source of the
[`FileHandler`](examples/applet_JNLP_API/src/FileHandler.java) class is shown next. You can also see source code for a complete text editor
called WebPad in the `sample`
directory in your JDK installation (`your jdk path/sample/jnlp/webpad`). WebPad
makes extensive use of the JNLP API.

```


// add javaws.jar to the classpath during compilation 
import javax.jnlp.FileOpenService;
import javax.jnlp.FileSaveService;
import javax.jnlp.FileContents;
import javax.jnlp.ServiceManager;
import javax.jnlp.UnavailableServiceException;
import java.io.*;

public class FileHandler {

    static private FileOpenService fos = null;
    static private FileSaveService fss = null;
    static private FileContents fc = null;

    // retrieves a reference to the JNLP services
    private static synchronized void initialize() {
        if (fss != null) {
            return;
        }
        try {
            fos = (FileOpenService) ServiceManager.lookup("javax.jnlp.FileOpenService");
            fss = (FileSaveService) ServiceManager.lookup("javax.jnlp.FileSaveService");
        } catch (UnavailableServiceException e) {
            fos = null;
            fss = null;
        }
    }

    // displays open file dialog and reads selected file using FileOpenService
    public static String open() {
        initialize();
        try {
            fc = fos.openFileDialog(null, null);
            return readFromFile(fc);
        } catch (IOException ioe) {
            ioe.printStackTrace(System.out);
            return null;
        }
    }

    // displays saveFileDialog and saves file using FileSaveService
    public static void save(String txt) {
        initialize();
        try {
            // Show save dialog if no name is already given
            if (fc == null) {
                fc = fss.saveFileDialog(null, null,
                        new ByteArrayInputStream(txt.getBytes()), null);
                // file saved, done
                return;
            }
            // use this only when filename is known
            if (fc != null) {
                writeToFile(txt, fc);
            }
        } catch (IOException ioe) {
            ioe.printStackTrace(System.out);
        }
    }

    // displays saveAsFileDialog and saves file using FileSaveService
    public static void saveAs(String txt) {
        initialize();
        try {
            if (fc == null) {
                // If not already saved. Save-as is like save
                save(txt);
            } else {
                fc = fss.saveAsFileDialog(null, null, fc);
                save(txt);
            }
        } catch (IOException ioe) {
            ioe.printStackTrace(System.out);
        }
    }

    private static void writeToFile(String txt, FileContents fc) throws IOException {
        int sizeNeeded = txt.length() * 2;
        if (sizeNeeded > fc.getMaxLength()) {
            fc.setMaxLength(sizeNeeded);
        }
        BufferedWriter os = new BufferedWriter(new OutputStreamWriter(fc.getOutputStream(true)));
        os.write(txt);
        os.close();
    }

    private static String readFromFile(FileContents fc) throws IOException {
        if (fc == null) {
            return null;
        }
        BufferedReader br = new BufferedReader(new InputStreamReader(fc.getInputStream()));
        StringBuffer sb = new StringBuffer((int) fc.getLength());
        String line = br.readLine();
        while (line != null) {
            sb.append(line);
            sb.append("\n");
            line = br.readLine();
        }
        br.close();
        return sb.toString();
    }
}

```

---

**Note:** To compile Java code that has a reference to classes in the
`javax.jnlp` package, include
`<your JDK path>/jre/lib/javaws.jar`
in your classpath.
At runtime, the Java Runtime Environment software automatically makes these
classes available to RIAs.

---

[Download source code](examplesIndex.html#AppletJNLPAPI) for the *Text Editor Applet* example to experiment further.

[« Previous](jnlpAPI.html)
•
[Trail](../TOC.html)
•
[Next »](cookies.html)

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

**Previous page:** JNLP API
  
**Next page:** Cookies




A browser with JavaScript enabled is required for this page to operate properly.