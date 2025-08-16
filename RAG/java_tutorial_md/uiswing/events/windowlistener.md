[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** Creating a GUI With JFC/Swing
  
**Lesson:** Writing Event Listeners
  
**Section:** Implementing Listeners for Commonly Handled Events

[Writing Event Listeners](index.html)

[Introduction to Event Listeners](intro.html)

[General Information about Writing Event Listeners](generalrules.html)

[Listeners Supported by Swing Components](eventsandcomponents.html)

[Implementing Listeners for Commonly Handled Events](handling.html)

[How to Write an Action Listener](actionlistener.html)

[How to Write a Caret Listener](caretlistener.html)

[How to Write a Change Listener](changelistener.html)

[How to Write a Component Listener](componentlistener.html)

[How to Write a Container Listener](containerlistener.html)

[How to Write a Document Listener](documentlistener.html)

[How to Write a Focus Listener](focuslistener.html)

[How to Write an Internal Frame Listener](internalframelistener.html)

[How to Write an Item Listener](itemlistener.html)

[How to Write a Key Listener](keylistener.html)

[How to Write a List Data Listener](listdatalistener.html)

[How to Write a List Selection Listener](listselectionlistener.html)

[How to Write a Mouse Listener](mouselistener.html)

[How to Write a Mouse-Motion Listener](mousemotionlistener.html)

[How to Write a Mouse-Wheel Listener](mousewheellistener.html)

[How to Write a Property Change Listener](propertychangelistener.html)

[How to Write a Table Model Listener](tablemodellistener.html)

[How to Write a Tree Expansion Listener](treeexpansionlistener.html)

[How to Write a Tree Model Listener](treemodellistener.html)

[How to Write a Tree Selection Listener](treeselectionlistener.html)

[How to Write a Tree-Will-Expand Listener](treewillexpandlistener.html)

[How to Write an Undoable Edit Listener](undoableeditlistener.html)

How to Write Window Listeners

[Listener API Table](api.html)

[Solving Common Event-Handling Problems](problems.html)

[Home Page](../../index.html)
>
[Creating a GUI With JFC/Swing](../index.html)
>
[Writing Event Listeners](index.html)

[« Previous](undoableeditlistener.html) • [Trail](../TOC.html) • [Next »](api.html)

# How to Write Window Listeners

This section explains how to implement three kinds
of window-related event handlers:
`WindowListener`, `WindowFocusListener`,
and `WindowStateListener`. All three listeners handle
`WindowEvent` objects. The methods in all
three event handlers are implemented by
the abstract `WindowAdapter` class.

When the appropriate listener has been registered
on a window (such as a
[frame](../components/frame.html) or
[dialog](../components/dialog.html)), window events are fired just after the window activity or state has occurred.
A window is considered as a "focus owner", if this window receives keyboard input.

The following window activities or states can precede a window event:

* Opening a window — Showing a window for the first time.* Closing a window — Removing the window from the screen.* Iconifying a window — Reducing the window to an icon on the desktop.* Deiconifying a window — Restoring the window to its original size.* Focused window — The window which contains the "focus owner".* Activated window (frame or dialog) — This window is either the focused window, or owns the focused window.* Deactivated window — This window has lost the focus.
              For more information about focus, see the
              [AWT Focus Subsystem](http://download.oracle.com/javase/6/docs/api/java/awt/doc-files/FocusSpec.html) specification.* Maximizing the window — Increasing a window's
                size to the maximum allowable size, either in the vertical
                direction, the horizontal direction, or both directions.

                The `WindowListener` interface defines methods that
                handle most window events, such as the events for opening and
                closing the window, activation and deactivation of
                the window, and iconification and deiconification of
                the window.

                The other two window listener interfaces,
                `WindowFocusListener` and
                `WindowStateListener`, were introduced
                in JDK release 1.4. `WindowFocusListener`
                contains methods to detect when the window becomes the focus owner
                or it loses the focus owner status. `WindowStateListener`
                has a single method to detect a change to the state of the window,
                such as when the window is iconified, deiconified,
                maximized, or restored to normal.

                ---

                **Version note:** Prior to JDK release 1.4, focus-gained and focus-lost
                events were inferred by using the `WindowListener`
                methods `windowActivated` and
                `windowDeactivated`. This approach
                did not work with windows that were not frames or dialogs,
                because such windows never received those events.
                To determine a window's iconification, the
                `ComponentListener` methods `componentHidden`
                and `componentShown` were used. As of JDK release 1.4,
                the methods defined in `WindowFocusListener`
                and `WindowStateListener` are preferred.

                ---

                While you can use the `WindowListener`
                methods to detect some window states, such as iconification,
                there are two reasons why a `WindowStateListener`
                might be preferable: it has only one method for you to implement,
                and it provides support for maximization.

                ---

                **Note:** Not all window managers/native platforms support all window states.
                The 1.4 `java.awt.Toolkit` method
                [`isFrameStateSupported(int)`](http://download.oracle.com/javase/7/docs/api/java/awt/Toolkit.html#isFrameStateSupported(int)) can be used to determine whether a particular window
                state is supported by a particular window manager.
                The WindowEventDemo example, described
                later in this section, shows how this method can be used.

                ---

                Window listeners are commonly used to
                implement custom window-closing behavior.
                For example, a window listener is used
                to save data before closing the window,
                or to exit the program when the last window closes.

                A user does not necessarily need to implement a window listener
                to specify what a window should do when the user closes it.
                By default, when the user closes a window the window
                becomes invisible.
                To specify different behavior,
                use the `setDefaultCloseOperation` method of the `JFrame` or `JDialog` classes.
                To implement a window-closing handler, use the
                `setDefaultCloseOperation(WindowConstants.DO_NOTHING_ON_CLOSE)` method
                to enable the window listener to
                provide all window-closing duties. See
                [Responding to Window-Closing Events](../components/frame.html#windowevents) for details on how to use `setDefaultCloseOperation`.

                ---

                **Version note:** As of JDK release 1.4, when the last displayable window
                within the Java virtual machine (VM) is disposed of,
                the VM may terminate. In previous releases, such as
                1.3, the VM remained running even if all windows
                were disposed of. Note, however, that there can be
                a delay before the program exits automatically,
                and that under some circumstances the program might
                keep running. It is quicker and safer to explicitly
                exit the program using `System.exit(int)`. See
                [AWT Threading Issues](http://download.oracle.com/javase/7/docs/api/java/awt/doc-files/AWTThreadIssues.html#Autoshutdown) for more information.

                ---

                Window listeners are also commonly used to stop threads and release resources
                when a window is iconified,
                and to start up again when the window is deiconified.
                This avoids unnecessarily
                using the processor or other resources.
                For example,
                when a window that contains animation is iconified,
                it should stop its animation thread
                and free any large buffers.
                When the window is deiconified,
                it can start the thread again
                and recreate the buffers.

                The following example demonstrates window events.
                A non-editable text area reports all window events
                that are fired by its window.
                This demo implements all methods in the `WindowListener`,
                `WindowFocusListener`, and `WindowStateListener`
                interfaces. You can find the demo's code in
                [`WindowEventDemo.java`](../examples/events/WindowEventDemoProject/src/events/WindowEventDemo.java).

                ![WindowEventDemo.html](../../figures/uiswing/events/WindowEventDemo.png)

                ---

                **Try this:**
                1. Click the Launch button
                   to run WindowEventDemo using
                   [Java™ Web Start](http://java.sun.com/products/javawebstart/index.jsp)
                   ([download JDK 6](http://java.sun.com/javase/downloads/index.jsp)).
                   Alternatively, to compile and run the example yourself,
                   consult the
                   [example index](../examples/events/index.html#WindowEventDemo).

                   [![Launches the WindowEventDemo application](../../images/jws-launch-button.png)](http://download.oracle.com/javase/tutorialJWS/uiswing/events/ex6/WindowEventDemo.jnlp)* When the window appears, several messages are already
                     displayed. One line reports whether your window manager
                     supports MAXIMIZED\_BOTH. If the window manager does not support
                     other window states, this condition is also reported. Next,
                     several lines are displayed, reporting that the window's
                     window listener has received window-opened, activated,
                     and gained-focus events. All the messages displayed
                     in the window are also sent to standard output.* Click another window. The "window lost focus"
                       and "window deactivated" messages will be displayed.
                       If this window is not a frame or a dialog,
                       it will receive the activated or deactivated events.* Click the WindowEventDemo window. You'll see
                         "window activated" and "window gained focus" messages.* Iconify the window, using the window controls.
                           Two iconification messages are displayed, one from the window listener
                           and the other from the window state listener.
                           Unless you are looking at standard output, the messages will not display
                           until the window is deiconified. Window-deactivation and
                           window-lost-focus events are also reported.* De-iconify the window.
                             Two deiconification messages are displayed, one from the window listener
                             and the other from the window state listener.
                             The `windowStateChanged` method in
                             `WindowStateListener` class gives the same information
                             that you get using the `windowIconified` and
                             `windowDeiconified` methods in `WindowListener` class.
                             Window-activation and window-gained-focus events are also
                             reported.* Maximize the window, if your look and feel provides
                               a way to do so. Note that some look and feels running on
                               some window managers, such as the Java look
                               and feel on dtwm, provide a way to maximize the window,
                               but no events are reported. This is because dtwm mimics maximization by
                               resizing the window, but it is not a true maximization event.
                               Some look and feels provide a way to maximize the window in the vertical
                               or horizontal direction *only*. Experiment with your window
                               controls to see what options are available.* Close the window, using the window controls.
                                 A window closing message is displayed. Once the window has
                                 closed, a window closed message is sent to standard output.

                ---

                Here is the demo's window event handling code:

                ```

                public class WindowEventDemo extends JFrame implements WindowListener,
                                                            WindowFocusListener,
                                                            WindowStateListener {
                    ...
                    static WindowEventDemo frame = new WindowEventDemo("WindowEventDemo");
                    JTextArea display;
                    ...

                    private void addComponentsToPane() {
                        display = new JTextArea();
                        display.setEditable(false);
                        JScrollPane scrollPane = new JScrollPane(display);
                        scrollPane.setPreferredSize(new Dimension(500, 450));
                        getContentPane().add(scrollPane, BorderLayout.CENTER);
                        
                        addWindowListener(this);
                        addWindowFocusListener(this);
                        addWindowStateListener(this);
                        
                        checkWM();
                    }
                    
                    public WindowEventDemo(String name) {
                        super(name);
                    }

                    //Some window managers don't support all window states.
                  
                    public void checkWM() {
                        Toolkit tk = frame.getToolkit();
                        if (!(tk.isFrameStateSupported(Frame.ICONIFIED))) {
                            displayMessage(
                                    "Your window manager doesn't support ICONIFIED.");
                        }  else displayMessage(
                                "Your window manager supports ICONIFIED.");
                        if (!(tk.isFrameStateSupported(Frame.MAXIMIZED_VERT))) {
                            displayMessage(
                                    "Your window manager doesn't support MAXIMIZED_VERT.");
                        }  else displayMessage(
                                "Your window manager supports MAXIMIZED_VERT.");
                        if (!(tk.isFrameStateSupported(Frame.MAXIMIZED_HORIZ))) {
                            displayMessage(
                                    "Your window manager doesn't support MAXIMIZED_HORIZ.");
                        } else displayMessage(
                                "Your window manager supports MAXIMIZED_HORIZ.");
                        if (!(tk.isFrameStateSupported(Frame.MAXIMIZED_BOTH))) {
                            displayMessage(
                                    "Your window manager doesn't support MAXIMIZED_BOTH.");
                        } else {
                            displayMessage(
                                    "Your window manager supports MAXIMIZED_BOTH.");
                        }
                    }

                    public void windowClosing(WindowEvent e) {
                        displayMessage("WindowListener method called: windowClosing.");
                        //A pause so user can see the message before
                        //the window actually closes.
                        ActionListener task = new ActionListener() {
                            boolean alreadyDisposed = false;
                            public void actionPerformed(ActionEvent e) {
                                if (frame.isDisplayable()) {
                                    alreadyDisposed = true;
                                    frame.dispose();
                                }
                            }
                        };
                        Timer timer = new Timer(500, task); //fire every half second
                        timer.setInitialDelay(2000);        //first delay 2 seconds
                        timer.setRepeats(false);
                        timer.start();
                    }

                    public void windowClosed(WindowEvent e) {
                        //This will only be seen on standard output.
                        displayMessage("WindowListener method called: windowClosed.");
                    }

                    public void windowOpened(WindowEvent e) {
                        displayMessage("WindowListener method called: windowOpened.");
                    }

                    public void windowIconified(WindowEvent e) {
                        displayMessage("WindowListener method called: windowIconified.");
                    }

                    public void windowDeiconified(WindowEvent e) {
                        displayMessage("WindowListener method called: windowDeiconified.");
                    }

                    public void windowActivated(WindowEvent e) {
                        displayMessage("WindowListener method called: windowActivated.");
                    }

                    public void windowDeactivated(WindowEvent e) {
                        displayMessage("WindowListener method called: windowDeactivated.");
                    }

                    public void windowGainedFocus(WindowEvent e) {
                        displayMessage("WindowFocusListener method called: windowGainedFocus.");
                    }

                    public void windowLostFocus(WindowEvent e) {
                        displayMessage("WindowFocusListener method called: windowLostFocus.");
                    }

                    public void windowStateChanged(WindowEvent e) {
                        displayStateMessage(
                          "WindowStateListener method called: windowStateChanged.", e);
                    }

                    void displayMessage(String msg) {
                        display.append(msg + newline);
                        System.out.println(msg);
                    }

                    void displayStateMessage(String prefix, WindowEvent e) {
                        int state = e.getNewState();
                        int oldState = e.getOldState();
                        String msg = prefix
                                   + newline + space
                                   + "New state: "
                                   + convertStateToString(state)
                                   + newline + space
                                   + "Old state: "
                                   + convertStateToString(oldState);
                        displayMessage(msg);
                    }

                    String convertStateToString(int state) {
                        if (state == Frame.NORMAL) {
                            return "NORMAL";
                        }
                        String strState = " ";
                        if ((state & Frame.ICONIFIED) != 0) {
                            strState += "ICONIFIED";
                        }
                        //MAXIMIZED_BOTH is a concatenation of two bits, so
                        //we need to test for an exact match.
                        if ((state & Frame.MAXIMIZED_BOTH) == Frame.MAXIMIZED_BOTH) {
                            strState += "MAXIMIZED_BOTH";
                        } else {
                            if ((state & Frame.MAXIMIZED_VERT) != 0) {
                                strState += "MAXIMIZED_VERT";
                            }
                            if ((state & Frame.MAXIMIZED_HORIZ) != 0) {
                                strState += "MAXIMIZED_HORIZ";
                            }
                            if (" ".equals(strState)){
                                strState = "UNKNOWN";
                            }
                        }
                        return strState.trim();
                    }
                }

                ```

                ### The Window Listener API

                > The window listener API consists of three window
                > listener interfaces and the `WindowEvent`
                > class. Their methods are listed in the following tables:
                > + [The WindowListener Interface](#windowlistener)+ [The WindowFocusListener Interface](#windowfocuslistener)+ [The WindowStateListener Interface](#windowstatelistener)+ [The WindowEvent Class](#windowevent)The methods from all three interfaces
                > are available through the
                > [`WindowAdapter`](http://download.oracle.com/javase/7/docs/api/java/awt/event/WindowAdapter.html) class.
                >
                > The WindowListener
                > Interface
                >
                > | Method | Purpose |
                > | --- | --- |
                > | [windowOpened(WindowEvent)](http://download.oracle.com/javase/7/docs/api/java/awt/event/WindowListener.html#windowOpened(java.awt.event.WindowEvent)) | Called just after the listened-to window has been shown for the first time. |
                > | [windowClosing(WindowEvent)](http://download.oracle.com/javase/7/docs/api/java/awt/event/WindowListener.html#windowClosing(java.awt.event.WindowEvent)) | Called in response to a user request for the listened-to window to be closed. To actually close the window, the listener should invoke the window's `dispose` or `setVisible(false)` method. |
                > | [windowClosed(WindowEvent)](http://download.oracle.com/javase/7/docs/api/java/awt/event/WindowListener.html#windowClosed(java.awt.event.WindowEvent)) | Called just after the listened-to window has closed. |
                > | [windowIconified(WindowEvent)](http://download.oracle.com/javase/7/docs/api/java/awt/event/WindowListener.html#windowIconified(java.awt.event.WindowEvent))  [windowDeiconified(WindowEvent)](http://download.oracle.com/javase/7/docs/api/java/awt/event/WindowListener.html#windowDeiconified(java.awt.event.WindowEvent)) | Called just after the listened-to window is iconified or deiconified, respectively. |
                > | [windowActivated(WindowEvent)](http://download.oracle.com/javase/7/docs/api/java/awt/event/WindowListener.html#windowActivated(java.awt.event.WindowEvent))  [windowDeactivated(WindowEvent)](http://download.oracle.com/javase/7/docs/api/java/awt/event/WindowListener.html#windowDeactivated(java.awt.event.WindowEvent)) | Called just after the listened-to window is activated or deactivated, respectively. These methods are not sent to windows that are not frames or dialogs. For this reason, we prefer the 1.4 `windowGainedFocus` and `windowLostFocus` methods to determine when a window gains or loses the focus. |
                >
                > The WindowFocusListener
                > Interface
                >
                > | Method | Purpose |
                > | --- | --- |
                > | [windowGainedFocus(WindowEvent)](http://download.oracle.com/javase/7/docs/api/java/awt/event/WindowFocusListener.html#windowGainedFocus(java.awt.event.WindowEvent))  [windowLostFocus(WindowEvent)](http://download.oracle.com/javase/7/docs/api/java/awt/event/WindowFocusListener.html#windowLostFocus(java.awt.event.WindowEvent)) | Called just after the listened-to window gains or loses the focus, respectively. |
                >
                > The WindowStateListener
                > Interface
                >
                > | Method | Purpose |
                > | --- | --- |
                > | [windowStateChanged(WindowEvent)](http://download.oracle.com/javase/7/docs/api/java/awt/event/WindowStateListener.html#windowStateChanged(java.awt.event.WindowEvent)) | Called just after the listened-to window's state is changed by being iconified, deiconified, maximized, or returned to normal. The state is available through the `WindowEvent` as a bitwise mask. The possible values, defined in `java.awt.Frame`, are: + NORMAL. Indicates that no state bits are set.+ ICONIFIED.+ MAXIMIZED\_HORIZ.+ MAXIMIZED\_VERT.+ MAXIMIZED\_BOTH. Concatenates `MAXIMIZED_HORIZ` and           `MAXIMIZED_VERT`. A window manager may support           `MAXIMIZED_BOTH`, while not supporting           `MAXIMIZED_HORIZ` or `MAXIMIZED_VERT`.           The           [`java.awt.Toolkit`](http://download.oracle.com/javase/7/docs/api/java/awt/Toolkit.html) method           [`isFrameStateSupported(int)`](http://download.oracle.com/javase/7/docs/api/java/awt/Toolkit.html#isFrameStateSupported(int)) can be used to determine what states are supported by the window manager. |
                >
                > The WindowEvent
                > Class
                >
                > | Method | Purpose |
                > | --- | --- |
                > | [Window getWindow()](http://download.oracle.com/javase/7/docs/api/java/awt/event/WindowEvent.html#getWindow()) | Returns the window that fired the event. You can use this instead of the `getSource` method. |
                > | [Window getOppositeWindow()](http://download.oracle.com/javase/7/docs/api/java/awt/event/WindowEvent.html#getOppositeWindow()) | Returns the other window involved in this focus or activation change. For a `WINDOW_ACTIVATED` or `WINDOW_GAINED_FOCUS` event, this returns the window that lost activation or the focus. For a `WINDOW_DEACTIVATED` or `WINDOW_LOST_FOCUS` event, this returns the window that gained activation or the focus. For any other type of `WindowEvent` with a Java application in a different VM or context, or with no other window, `null` is returned. This method was introduced in JDK release 1.4. |
                > | [int getOldState()](http://download.oracle.com/javase/7/docs/api/java/awt/event/WindowEvent.html#getOldState())  [int getNewState()](http://download.oracle.com/javase/7/docs/api/java/awt/event/WindowEvent.html#getNewState()) | For `WINDOW_STATE_CHANGED` events, these methods return the previous or new state of the window as a bitwise mask. These methods were introduced in JDK release 1.4. |

                ### Examples that Use Window Listeners
                > The following table lists the
                > examples that use window listeners.
                >
                > | Example | Where Described | Notes |
                > | --- | --- | --- |
                > | [`WindowEventDemo`](../examples/events/index.html#WindowEventDemo) | This section | Reports all window events that occur on one window to demonstrate the circumstances under which window events are fired. |
                > | [`SliderDemo`](../examples/components/index.html#SliderDemo) | [How to Use Sliders](../components/slider.html) | Listens for window iconify and deiconify events, so that it can stop the animation when the window isn't visible. |
                > | [`InternalFrameEventDemo`](../examples/events/index.html#InternalFrameEventDemo) | [How to Write an Internal Frame Listener](internalframelistener.html) | Reports all internal frame events that occur on one internal frame to demonstrate the circumstances under which internal frame events are fired. Internal frame events are similar to window events. |
                > | [`DialogDemo`](../examples/components/index.html#DialogDemo) | [Text Component Features](../components/generaltext.html) | [`CustomDialog.java`](../examples/components/DialogDemoProject/src/components/CustomDialog.java) uses `setDefaultCloseOperation` instead of a window listener to determine what action to take when the user closes the window. |
                > | [`Framework`](../examples/components/index.html#Framework) | — | A demo that allows multiple windows to be created and destroyed. |

[« Previous](undoableeditlistener.html)
•
[Trail](../TOC.html)
•
[Next »](api.html)

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

**Previous page:** How to Write an Undoable Edit Listener
  
**Next page:** Listener API Table




A browser with JavaScript enabled is required for this page to operate properly.