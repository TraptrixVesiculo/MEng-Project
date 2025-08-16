[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** Deployment
  
**Lesson:** Applets
  
**Section:** Getting Started With Applets

[Applets](index.html)

[Getting Started With Applets](getStarted.html)

[Defining an Applet Subclass](subclass.html)

[Methods for Milestones](appletMethods.html)

[Life Cycle of an Applet](lifeCycle.html)

[Applet's Execution Environment](appletExecutionEnv.html)

Developing an Applet

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

[Displaying a Customized Loading Progress Indicator](customProgressIndicatorForApplet.html)

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

[« Previous](appletExecutionEnv.html) • [Trail](../TOC.html) • [Next »](deployingApplet.html)

# Developing an Applet

An application designed using
[component-based architecture](../index.html#componentBasedArch) can be
developed into an applet.
Consider the example of an applet with a Swing-based graphical user interface (GUI).
With component-based design,
the GUI can be built with smaller building blocks or components.
The following general steps are used to create an applet GUI:

* Create a class `MyTopJPanel` that is a subclass of
  `javax.swing.JPanel`.
  Lay out your applet's GUI components in the constructor of the `MyTopJPanel` class.
* Create a class called `MyApplet` that is a subclass
  of `javax.swing.JApplet`.
* In the `init` method of `MyApplet`, instantiate
  `MyTopJPanel` and set it as the applet's content pane.

The following sections explore these steps in greater detail by using the
Dynamic Tree Demo applet.
If you are not familiar with Swing, see
[Creating a GUI with JFC/Swing](../../uiswing/index.html) to learn more about using Swing GUI components.



A browser with JavaScript enabled is required for this page to operate properly.

---

**Note:** If you don't see the applet running, make sure that you have at least the Java 2 Platform, Standard Edition (J2SE) 1.4.2 release on your client. If not, [download](http://java.sun.com/javase/downloads/index.jsp) and install the latest release of the Java SE Development Kit (JDK). 

---

---

**Note:** If you don't see the example running, you might need to enable the JavaScript interpreter in your browser so that the Deployment Toolkit script can function properly.

---

## Creating the Top `JPanel` Class

Create a class that is a subclass of `JPanel`.
This top `JPanel` acts
as a container for all your other UI components. In the following example, the
`DynamicTreePanel` class is the topmost `JPanel`.
The constructor of the
`DynamicTreePanel` class invokes other methods to create and lay out
the UI controls properly.

```

public class DynamicTreePanel extends JPanel implements ActionListener {
    private int newNodeSuffix = 1;
    private static String ADD_COMMAND = "add";
    private static String REMOVE_COMMAND = "remove";
    private static String CLEAR_COMMAND = "clear";
    
    private DynamicTree treePanel;

    public DynamicTreePanel() {
        super(new BorderLayout());
        
        //Create the components.
        treePanel = new DynamicTree();
        populateTree(treePanel);

        JButton addButton = new JButton("Add");
        addButton.setActionCommand(ADD_COMMAND);
        addButton.addActionListener(this);
        
        JButton removeButton = new JButton("Remove");
        ....
        
        JButton clearButton = new JButton("Clear");
        ...
        
        //Lay everything out.
        treePanel.setPreferredSize(new Dimension(300, 150));
        add(treePanel, BorderLayout.CENTER);

        JPanel panel = new JPanel(new GridLayout(0,3));
        panel.add(addButton);
        panel.add(removeButton); 
        panel.add(clearButton);
        add(panel, BorderLayout.SOUTH);
    }
    ....
}

```

## Creating the Applet

For an applet that has a Swing-based GUI, create a class that is a subclass of
`javax.swing.JApplet`. An applet that does not contain a Swing-based
GUI can extend the `java.applet.Applet` class.

Override the applet's `init` method to instantiate
your top `JPanel` class
and create the applet's GUI. The `init` method of the
`DynamicTreeApplet` class
invokes the `createGUI` method in the AWT Event Dispatcher thread.

```

package appletComponentArch;

import javax.swing.JApplet;
import javax.swing.SwingUtilities;

public class DynamicTreeApplet extends JApplet {
    //Called when this applet is loaded into the browser.
    public void init() {
        //Execute a job on the event-dispatching thread; creating this applet's GUI.
        try {
            SwingUtilities.invokeAndWait(new Runnable() {
                public void run() {
                    createGUI();
                }
            });
        } catch (Exception e) { 
            System.err.println("createGUI didn't complete successfully");
        }
    }
    
    private void createGUI() {
        //Create and set up the content pane.
        DynamicTreePanel newContentPane = new DynamicTreePanel();
        newContentPane.setOpaque(true); 
        setContentPane(newContentPane);        
    }        
}

```

## Benefits of Separating Core Functionality From the Final Deployment Mechanism

Another way to create an applet is to just remove the layer of abstraction
(separate top `JPanel`) and lay out all the controls in the
applet's `init` method itself.
The downside to creating the GUI directly in the applet is that it will now be more
difficult to deploy your functionality as a Java Web Start application, if you choose to do so later.

In the Dynamic Tree Demo example, the core functionality resides in the
`DynamicTreePanel` class. It is now trivial to drop the
`DynamicTreePanel` class
into a `JFrame` and deploy as a Java Web Start application.

Hence, to preserve portability and keep deployment options open,
follow component-based design as described on this page.

[Download source code](examplesIndex.html#ComponentArchDynamicTreeDemo) for the *Dynamic Tree Demo Applet* example to experiment further.

[« Previous](appletExecutionEnv.html)
•
[Trail](../TOC.html)
•
[Next »](deployingApplet.html)

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

**Previous page:** Applet's Execution Environment
  
**Next page:** Deploying an Applet




A browser with JavaScript enabled is required for this page to operate properly.