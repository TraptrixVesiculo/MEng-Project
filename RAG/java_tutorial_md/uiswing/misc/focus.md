[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** Creating a GUI With JFC/Swing
  
**Lesson:** Using Other Swing Features

[Using Other Swing Features](index.html)

[How to Integrate with the Desktop Class](desktop.html)

[How to Create Translucent and Shaped Windows](trans_shaped_windows.html)

[How to Decorate Components with JLayer](jlayer.html)

[How to Use Actions](action.html)

[How to Use Swing Timers](timer.html)

[How to Support Assistive Technologies](access.html)

How to Use the Focus Subsystem

[How to Use Key Bindings](keybinding.html)

[How to Use Modality in Dialogs](modality.html)

[How to Print Tables](printtable.html)

[How to Print Text](printtext.html)

[How to Create a Splash Screen](splashscreen.html)

[How to Use the System Tray](systemtray.html)

[Solving Common Problems Using Other Swing Features](problems.html)

[Home Page](../../index.html)
>
[Creating a GUI With JFC/Swing](../index.html)
>
[Using Other Swing Features](index.html)

[« Previous](access.html) • [Trail](../TOC.html) • [Next »](keybinding.html)

# How to Use the Focus Subsystem

Many components — even those primarily operated
with the mouse, such as buttons — can be operated
with the keyboard.
For a key press to affect a component,
the component must have the keyboard focus.

From the user's point of view,
the component with the keyboard focus is generally
prominent — with a dotted or black border, for example.
The window containing the component is also more prominent
than other windows onscreen.
These visual cues let the user know
to which component any typing will relate.
Only one component at a time in the window
system can have the keyboard focus.

Exactly how a window gains the focus
depends on the windowing system.
There is no foolproof way, across all platforms,
to ensure that a window gains the focus.
On some operating systems, such as Microsoft Windows,
the front window usually becomes the focused window.
In these cases, the
[`Window.toFront`](http://download.oracle.com/javase/7/docs/api/java/awt/Window.html#toFront()) method moves the window to the front, thereby giving it
the focus.
However, on other operating systems, such as Solaris™ Operating System, the window manager may choose
the focused window based on cursor position, and in
these cases the behavior of the `Window.toFront` method is different.

A component generally gains the focus when the user clicks it, or
when the user tabs between components, or otherwise
interacts with a component.
A component can also be given the focus programmatically,
such as when its containing frame or dialog-box is made visible.
This code snippet shows how to give a particular
component the focus every time the window gains the focus:

```

//Make textField get the focus whenever frame is activated.
frame.addWindowFocusListener(new WindowAdapter() {
    public void windowGainedFocus(WindowEvent e) {
        textField.requestFocusInWindow();
    }
});

```

If you want to ensure that a particular component gains
the focus the first time a window is activated, you can
call the
[`requestFocusInWindow`](http://download.oracle.com/javase/7/docs/api/java/awt/Component.html#requestFocusInWindow()) method on the component after the component
has been realized, but before the frame is displayed.
The following sample code shows how this operation can be done:

```

    //...Where initialization occurs...
    JFrame frame = new JFrame("Test");
    JPanel panel = new JPanel(new BorderLayout());

    //...Create a variety of components here...

    //Create the component that will have the initial focus.
    JButton button = new JButton("I am first");
    panel.add(button);
    frame.getContentPane().add(panel);  //Add it to the panel

    frame.pack();  //Realize the components.
    //This button will have the initial focus.
    button.requestFocusInWindow(); 
    frame.setVisible(true); //Display the window.

```

Alternatively, you can apply a custom `FocusTraversalPolicy` to the frame
and call the `getDefaultComponent` method to determine which
component will gain the focus.

---

**Version note:** This section describes the focus architecture
implemented in JDK 1.4. Prior to the 1.4 release,
`JComponent` methods, such as
`setNextFocusableComponent`,
`getNextFocusableComponent`,
`requestDefaultFocus`, and
`isManagingFocus`, were used to
manage the keyboard focus.
These methods are now deprecated.
Another method, `requestFocus`, is discouraged
because it tries to give the focus to the component's window,
which is not always possible. As of JDK 1.4,
you should instead use the `requestFocusInWindow` method,
which does not attempt to make the component's window
focused. The method returns a boolean value indicating whether
the method succeeded.

---

The rest of this section covers the following topics:

* [Introduction to the Focus Subsystem](#intro)* [Validating Input](#inputVerification)* [Making a Custom Component Focusable](#focusable)* [Customizing Focus Traversal](#customFocusTraversal)* [Tracking Focus Changes to Multiple Components](#trackingFocus)* [Timing Focus Transfers](#transferTiming)* [The Focus API](#api)* [Focus Examples](#eg)

## Introduction to the Focus Subsystem
> The focus subsystem is designed to do the right
> thing as invisibly as possible. In most cases it
> behaves in a reasonable manner, and if it does not
> you can tweak its behavior in various ways.
> Some common scenarios might include:
>
> * The ordering is right but the first component
>   with the focus is not set. As shown in a code
>   snippet in the preceding section, you can use the `requestFocusInWindow` method
>   to set the focus on a component when the window becomes
>   visible.* The ordering is wrong. To fix this issue,
>     you can change the containment hierarchy,
>     you can change the order that the components
>     are added to their containers, or you can create a custom
>     focus traversal policy. For more details see
>     [Customizing Focus Traversal](#customFocusTraversal).* A component must to be prevented from losing focus,
>       or you need to check a value in a component before it
>       loses focus.
>       [Input verification](#inputVerification)
>       is a solution to this problem.* A custom component is not getting the focus.
>         To fix this issue, you need to make sure that it
>         satisfies all the requirements outlined in
>         [Making a Custom Component Focusable](#focusable).
>
> The `FocusConceptsDemo` example illustrates a few concepts.
>
> ![The FocusConceptsDemo example](../../figures/uiswing/misc/FocusConceptsDemo.png)
>
> ---
>
> **Try this:**
>
> 1. Click the Launch button
>    to run FocusConceptsDemo using
>    [Java™ Web Start](http://java.sun.com/products/javawebstart/index.jsp)
>    ([download JDK 6](http://java.sun.com/javase/downloads/index.jsp)).
>    Alternatively, to compile and run the example yourself,
>    consult the
>    [example index](../examples/misc/index.html#FocusConceptsDemo).
>
>    [![Launches the FocusConceptsDemo application](../../images/jws-launch-button.png)](http://download.oracle.com/javase/tutorialJWS/uiswing/misc/ex6/FocusConceptsDemo.jnlp)
> 2. If necessary, click the window to give it the focus.- Move the focus from component to component using the Tab key.
>        
>       You will notice that when the focus moves into the text area,
>      it stays in the text area.- Move the focus out of the text area using Control-Tab.- Move the focus in the opposite direction using Shift-Tab.- Move the focus out of the text area in the opposite direction using
>            Control-Shift-Tab.
>
> ---
>
> The
> `KeyboardFocusManager`
> is a critical element of the focus subsystem.
> It manages state and initiates changes.
> The keyboard manager tracks the *focus owner* —
> the component that receives typing from the keyboard.
> The *focused window* is the window that contains
> the focus owner.
>
> ---
>
> **JWindow and focus:** To use a `JWindow` component in your GUI,
> you should know that the `JWindow` component's owning frame must
> be visible in order for any components in the window to get the focus.
> By default, if you do not specify an owning frame for
> a `JWindow` component, an invisible owning frame is
> created for it. The result is that components in the
> `JWindow` component might not be able to get the focus.
> The solution is either to specify a
> visible owning frame when creating the
> [`JWindow`](http://download.oracle.com/javase/7/docs/api/javax/swing/JWindow.html) component, or to use an undecorated
> [`JFrame`](../components/frame.html) component instead.
>
> ---
>
> A *focus cycle* (or *focus traversal cycle*)
> is a set of components that share a common ancestor in the
> containment hierarchy.
> The *focus cycle root* is the
> container that is the root for a particular
> focus traversal cycle. By default, every
> `JWindow` and `JInternalFrame` component
> can be a focus cycle root. A focus cycle root can itself
> contain one or more focus cycle roots.
> The following Swing objects can be focus cycle roots:
> `JApplet`, `JDesktopPane`, `JDialog`,
> `JEditorPane`, `JFrame`, `JInternalFrame`,
> and `JWindow`.
> While it might appear that `JTable`
> and `JTree` objects are focus cycle roots, they
> are not.
>
> A *focus traversal policy* determines the order in which
> a group of components are navigated. Swing provides
> the
> [`LayoutFocusTraversalPolicy`](http://download.oracle.com/javase/7/docs/api/javax/swing/LayoutFocusTraversalPolicy.html) class, which
> decides the order of navigation based on layout
> manager-dependent factors, such as size,
> location, and orientation of components. Within a focus
> cycle, components can be navigated in a forward or
> backward direction. In a hierarchy of focus cycle
> roots, upwards traversal takes the focus out of the
> current cycle into the parent cycle.
> In most Look and Feel models,
> components are navigated using the
> Tab and Shift-Tab keys. These keys are the default
> *focus traversal keys* and can be changed
> programmatically. For example, you can add Enter
> as a forward focus traversal key with the following
> four lines of code:
>
> ```
>
> Set forwardKeys = getFocusTraversalKeys(
>     KeyboardFocusManager.FORWARD_TRAVERSAL_KEYS);
> Set newForwardKeys = new HashSet(forwardKeys);
> newForwardKeys.add(KeyStroke.getKeyStroke(KeyEvent.VK_ENTER, 0));
> setFocusTraversalKeys(KeyboardFocusManager.FORWARD_TRAVERSAL_KEYS,
>     newForwardKeys);
>
> ```
>
> Tab shifts the focus in
> the forward direction. Shift-Tab moves the
> focus in the backward direction.
> For example, in FocusConceptsDemo, the first
> button has the initial focus. Tabbing moves
> the focus through the buttons into the text area.
> Additional tabbing moves the cursor within
> the text area but not out of the text area
> because, inside a text area, Tab is *not*
> a focus traversal key.
> However, Control-Tab moves the focus out of the
> text area and into the first text field.
> Likewise, Control-Shift-Tab moves
> the focus out of the text area and into the previous
> component. The Control key is used by convention
> to move the focus out of any component that treats Tab
> in a special way, such as `JTable`.
>
> You have just received a brief introduction to the focus architecture.
> If you want more details, see the specification for the
> [Focus Subsystem](http://download.oracle.com/javase/7/docs/api/java/awt/doc-files/FocusSpec.html).

## Validating Input
> A common requirement of GUI design is a component
> that restricts the user's input — for example, a text field
> that allows only numeric input in decimal format (money,
> for example) or a text field that allows only 5 digits
> for a zip code.
> Release 1.4 provides a handy, easy-to-use
> [formatted text field](../components/formattedtextfield.html) component that allows input to be restricted to a variety of
> localizable formats. You can also specify a
> [custom formatter](../components/formattedtextfield.html) for the text field, which can perform special checking
> such as determining whether values are not only formatted
> correctly, but also reasonable.
>
> You can use an input verifier as an alternative to a custom formatter,
> or when you have a component that is not a text field.
> An input verifier allows you to
> reject specific values, such as a properly formatted but
> invalid zip code, or values outside of a desired range,
> for example a body temperature higher than 110°F.
> To use an input verifier, you create a subclass of
> [`InputVerifier`](http://download.oracle.com/javase/7/docs/api/javax/swing/InputVerifier.html) (a class introduced in JDK 1.3), create an instance of
> your subclass, and set the instance as the input verifier
> for one or more components.
>
> A component's input verifier is consulted whenever the
> component is about to lose the focus. If the component's
> value is not acceptable, the input verifier can take
> appropriate action, such as refusing to yield the focus
> on the component or replacing the user's input with the
> last valid value and then allowing the focus to transfer
> to the next component. However, `InputVerifier`
> is not called when the focus is transferred to another toplevel component.
>
> The following two examples show
> mortgage calculators. One uses formatted
> text fields and the other uses input verification with
> standard text fields.
>
> ![The InputVerificationDemo and example, which demonstrates](../../figures/uiswing/misc/InputVerificationDemo.png)
>
> ---
>
> **Try this:**
>
> 1. Click the Launch button
>    to run the FormattedTextFieldDemo using
>    [Java™ Web Start](http://java.sun.com/products/javawebstart/index.jsp)
>    ([download JDK 6](http://java.sun.com/javase/downloads/index.jsp)).
>    Alternatively, to compile and run the example yourself,
>    consult the
>    [example index](../examples/components/index.html#FormattedTextFieldDemo).
>
>    [![Launches the FormattedTextFieldDemo application](../../images/jws-launch-button.png)](http://download.oracle.com/javase/tutorialJWS/uiswing/components/ex6/FormattedTextFieldDemo.jnlp)
> 2. Click the Launch button
>    to run the InputVerificationDemo using
>    [Java™ Web Start](http://java.sun.com/products/javawebstart/index.jsp)
>    ([download JDK 6](http://java.sun.com/javase/downloads/index.jsp)).
>    Alternatively, to compile and run the example yourself,
>    consult the
>    [example index](../examples/misc/index.html#InputVerificationDemo).
>
>    [![Launches the InputVerificationDemo application](../../images/jws-launch-button.png)](http://download.oracle.com/javase/tutorialJWS/uiswing/misc/ex6/InputVerificationDemo.jnlp)
> 3. Compare the two mortgage calculators side by side.
>    You will see that the input verification demo
>    specifies valid input values
>    in the associated label for each editable text field.
>    Try entering badly formatted values in both
>    examples to observe behavior. Then try entering a properly
>    formatted, but unacceptable value.
>
> ---
>
> You can find the code for the Input Verification demo in
> [`InputVerificationDemo.java`](../examples/misc/InputVerificationDemoProject/src/misc/InputVerificationDemo.java). Here is the code for the `InputVerifier`
> subclass, `MyVerifier`:
>
> ```
>
> class MyVerifier extends InputVerifier
>                  implements ActionListener {
>     double MIN_AMOUNT = 10000.0;
>     double MAX_AMOUNT = 10000000.0;
>     double MIN_RATE = 0.0;
>     int MIN_PERIOD = 1;
>     int MAX_PERIOD = 40;
>
>    public boolean shouldYieldFocus(JComponent input) {
>         boolean inputOK = verify(input);
>         makeItPretty(input);
>         updatePayment();
>
>         if (inputOK) {
>             return true;
>         } else {
>             Toolkit.getDefaultToolkit().beep();
>             return false;
>         }
>     }
>
>     protected void updatePayment() {
>         double amount = DEFAULT_AMOUNT;
>         double rate = DEFAULT_RATE;
>         int numPeriods = DEFAULT_PERIOD;
>         double payment = 0.0;
>
>         //Parse the values.
>         try {
>             amount = moneyFormat.parse(amountField.getText()).
>                               doubleValue();
>         } catch (ParseException pe) {pe.printStackTrace();}
>         try {
>             rate = percentFormat.parse(rateField.getText()).
>                                  doubleValue();
>         } catch (ParseException pe) {pe.printStackTrace();}
>         try {
>             numPeriods = decimalFormat.parse(numPeriodsField.getText()).
>                               intValue();
>         } catch (ParseException pe) {pe.printStackTrace();}
>
>         //Calculate the result and update the GUI.
>         payment = computePayment(amount, rate, numPeriods);
>         paymentField.setText(paymentFormat.format(payment));
>     }
>
>     //This method checks input, but should cause no side effects.
>     public boolean verify(JComponent input) {
>         return checkField(input, false);
>     }
>
>     protected void makeItPretty(JComponent input) {
>         checkField(input, true);
>     }
>
>     protected boolean checkField(JComponent input, boolean changeIt) {
>         if (input == amountField) {
>             return checkAmountField(changeIt);
>         } else if (input == rateField) {
>             return checkRateField(changeIt);
>         } else if (input == numPeriodsField) {
>             return checkNumPeriodsField(changeIt);
>         } else {
>             return true; //should not happen
>         }
>     }
>
>     //Checks that the amount field is valid.  If it is valid,
>     //it returns true; otherwise, returns false.  If the
>     //change argument is true, this method sets the
>     //value to the minimum or maximum value if necessary and (even if not) sets it to the
>     //parsed number so that it looks good -- no letters,
>     //for example.
>     protected boolean checkAmountField(boolean change) {
>         boolean wasValid = true;
>         double amount = DEFAULT_AMOUNT;
>
>         //Parse the value.
>         try {
>             amount = moneyFormat.parse(amountField.getText()).
>                               doubleValue();
>         } catch (ParseException pe) {
>             pe.printStackTrace();
> 	    wasValid = false;
>         }
>
>         //Value was invalid.
>         if ((amount < MIN_AMOUNT) || (amount > MAX_AMOUNT)) {
>             wasValid = false;
>             if (change) {
>                 if (amount < MIN_AMOUNT) {
>                     amount = MIN_AMOUNT;
>                 } else { // amount is greater than MAX_AMOUNT
>                     amount = MAX_AMOUNT;
>                 }
>             }
>         }
>
>         //Whether value was valid or not, format it nicely.
>         if (change) {
>             amountField.setText(moneyFormat.format(amount));
>             amountField.selectAll();
>         }
>
>         return wasValid;
>     }
>
>     //Checks that the rate field is valid.  If it is valid,
>     //it returns true; otherwise, returns false.  If the
>     //change argument is true, this method reigns in the
>     //value if necessary and (even if not) sets it to the
>     //parsed number so that it looks good -- no letters,
>     //for example.
>     protected boolean checkRateField(boolean change) {
>         ...//Similar to checkAmountField...
>     }
>
>     //Checks that the numPeriods field is valid.  If it is valid,
>     //it returns true; otherwise, returns false.  If the
>     //change argument is true, this method reigns in the
>     //value if necessary and (even if not) sets it to the
>     //parsed number so that it looks good -- no letters,
>     //for example.
>     protected boolean checkNumPeriodsField(boolean change) {
>         ...//Similar to checkAmountField...
>     }
>
>     public void actionPerformed(ActionEvent e) {
>         JTextField source = (JTextField)e.getSource();
>         shouldYieldFocus(source); //ignore return value
>         source.selectAll();
>     }
> }
>
> ```
>
> Note that the `verify` method is implemented to
> detect invalid values but does nothing else.
> The `verify` method exists only to determine
> whether the input is valid — it should never bring
> up a dialog-box or cause any other side effects.
> The `shouldYieldFocus` method calls `verify`
> and, if a values is invalid, sets it to the minimum or maximum value. The
> `shouldYieldFocus` method is allowed to cause side
> effects, in this case, it always formats the text field and
> may also change its value. In our example,
> the `shouldYieldFocus` method
> always returns true so that the transfer
> of the focus is never actually prevented. This is just one way
> verification can be implemented. Find another version
> of this demo called
> [`InputVerificationDialogDemo`](../examples/misc/index.html#InputVerificationDialogDemo)
> that puts up a dialog-box when user input is invalid and requires
> the user to enter a legal value.
>
> The input verifier is installed using the
> `setInputVerifier` method of the `JComponent` class.
> For example, the `InputVerificationDemo` has the following code:
>
> ```
>
> private MyVerifier verifier = new MyVerifier();
> ...
> amountField.setInputVerifier(verifier);
>
> ```

## Making a Custom Component Focusable
> For a component to gain the focus,
> it must satisfy three requirements: it must be visible, enabled,
> and focusable. An input map may also be given.
> For more information about input map, read
> [How to Use Key Bindings](../misc/keybinding.html).
>
> The [TrackFocusDemo](#trackfocusdemo)
> example defines the simple component `Picture`.
> Its constructor is shown below:
>
> ```
>
> public Picture(Image image) {
>     this.image = image;
>     setFocusable(true);
>     addMouseListener(this);
>     addFocusListener(this);
> }
>
> ```
>
> The call to the `setFocusable(true)` method makes the
> component focusable. If you explicitly give your component
> key bindings in its `WHEN_FOCUSED` input map,
> you do not need to call the `setFocusable` method.
>
> To visually show changes in the focus
> (by drawing a red border only when the component has
> the focus), `Picture` has a
> [focus listener](../events/focuslistener.html).
>
> To gain the focus when the user clicks on the picture,
> the component has a
> [mouse listener](../events/mouselistener.html). The listener's `mouseClicked` method requests
> for the focus to be transferred to the picture. Here is the code:
>
> ```
>
> public void mouseClicked(MouseEvent e) {
>     //Since the user clicked on us, let us get focus!
>     requestFocusInWindow();
> }
>
> ```
>
> See [Tracking Focus Changes to Multiple
> Components](#trackingFocus) for more discussion of the TrackFocusDemo example.

## Customizing Focus Traversal
> The focus subsystem determines a default order that is
> applied when using the focus traversal keys (such as Tab) to navigate.
> The policy of a Swing application is determined by
> [`LayoutFocusTraversalPolicy`](http://download.oracle.com/javase/7/docs/api/javax/swing/LayoutFocusTraversalPolicy.html) . You can set a focus traversal policy on any
> `Container` by using the
> [`setFocusCycleRoot`](http://download.oracle.com/javase/7/docs/api/java/awt/Container.html#setFocusCycleRoot(boolean)) method.
> However, if the container is
> not a focus cycle root, it may have no apparent effect.
> Alternatively you can pass focus traversal policy providers to the
> `FocusTraversalPolicy` methods instead of focus cycle roots.
> Use the
> [`isFocusTraversalPolicyProvider()`](http://download.oracle.com/javase/7/docs/api/java/awt/Container.html#isFocusTraversalPolicyProvider()) method to determine whether a `Container` is a focus traversal policy provider.
> Use the
> [`setFocusTraversalPolicyProvider()`](http://download.oracle.com/javase/7/docs/api/java/awt/Container.html#setFocusTraversalPolicyProvider(boolean)) method to set a container for providing focus traversal policy.
>
> The `FocusTraversalDemo` example
> demonstrates how to customize focus behavior.
>
> ![The Focus Traversal Demo, which demonstrates a custom FocusTraversalPolicy.](../../figures/uiswing/misc/FocusTraversalDemo.png)
>
> ---
>
> **Try this:**
>
> 1. Click the Launch button
>    to run FocusTraversalDemo using
>    [Java™ Web Start](http://java.sun.com/products/javawebstart/index.jsp)
>    ([download JDK 6](http://java.sun.com/javase/downloads/index.jsp)).
>    Alternatively, to compile and run the example yourself,
>    consult the
>    [example index](../examples/misc/index.html#FocusTraversalDemo).
>
>    [![Launches the FocusTraversalDemo application](../../images/jws-launch-button.png)](http://download.oracle.com/javase/tutorialJWS/uiswing/misc/ex6/FocusTraversalDemo.jnlp)
> 2. Click the window, if necessary, to give it the focus.- Note the focus order as you tab through
>      the components. The focus order was determined by
>      the order that the components were added to the content pane.
>      Note also that the check box never gets the focus; we
>      removed it from the focus cycle.- To move the focus out of the table, use Control-Tab or
>        Control-Shift-Tab.- Click the **Custom FocusTraversalPolicy** check box.
>          This box installs a custom focus traversal policy on the frame.- Try tabbing through the components again. Note that
>            the focus order is now in left-to-right, top-down
>            order.
>
> ---
>
> You can find the demo's code in
> [`FocusTraversalDemo.java`](../examples/misc/FocusTraversalDemoProject/src/misc/FocusTraversalDemo.java).
>
> The check box was removed from the focus cycle
> with this line of code:
>
> ```
>
> togglePolicy.setFocusable(false);
>
> ```
>
> Here is the application's custom `FocusTraversalPolicy`:
>
> ```
>
>     ...
>     JTextField tf1 = new JTextField("Field 1");
>     JTextField tf2 = new JTextField("A Bigger Field 2");
>     JTextField tf3 = new JTextField("Field 3");
>     JTextField tf4 = new JTextField("A Bigger Field 4");
>     JTextField tf5 = new JTextField("Field 5");
>     JTextField tf6 = new JTextField("A Bigger Field 6");
>     JTable table = new JTable(4,3);
>     ...
>     public FocusTraversalDemo() {
>         super(new BorderLayout());
>
>         JTextField tf1 = new JTextField("Field 1");
>         JTextField tf2 = new JTextField("A Bigger Field 2");
>         JTextField tf3 = new JTextField("Field 3");
>         JTextField tf4 = new JTextField("A Bigger Field 4");
>         JTextField tf5 = new JTextField("Field 5");
>         JTextField tf6 = new JTextField("A Bigger Field 6");
>         JTable table = new JTable(4,3);
>         togglePolicy = new JCheckBox("Custom FocusTraversalPolicy");
>         togglePolicy.setActionCommand("toggle");
>         togglePolicy.addActionListener(this);
>         togglePolicy.setFocusable(false);  //Remove it from the focus cycle.
>         //Note that HTML is allowed and will break this run of text
>         //across two lines.
>         label = new JLabel("Use Tab (or Shift-Tab) to navigate from component to component.
>
> Control-Tab 
> 	(or Control-Shift-Tab) allows you to break out of the JTable.
>
> ");
>
>         JPanel leftTextPanel = new JPanel(new GridLayout(3,2));
>         leftTextPanel.add(tf1, BorderLayout.PAGE_START);
>         leftTextPanel.add(tf3, BorderLayout.CENTER);
>         leftTextPanel.add(tf5, BorderLayout.PAGE_END);
>         leftTextPanel.setBorder(BorderFactory.createEmptyBorder(0,0,5,5));
>         JPanel rightTextPanel = new JPanel(new GridLayout(3,2));
>         rightTextPanel.add(tf2, BorderLayout.PAGE_START);
>         rightTextPanel.add(tf4, BorderLayout.CENTER);
>         rightTextPanel.add(tf6, BorderLayout.PAGE_END);
>         rightTextPanel.setBorder(BorderFactory.createEmptyBorder(0,0,5,5));
>         JPanel tablePanel = new JPanel(new GridLayout(0,1));
>         tablePanel.add(table, BorderLayout.CENTER);
>         tablePanel.setBorder(BorderFactory.createEtchedBorder());
>         JPanel bottomPanel = new JPanel(new GridLayout(2,1));
>         bottomPanel.add(togglePolicy, BorderLayout.PAGE_START);
>         bottomPanel.add(label, BorderLayout.PAGE_END);
>
>         add(leftTextPanel, BorderLayout.LINE_START);
>         add(rightTextPanel, BorderLayout.CENTER);
>         add(tablePanel, BorderLayout.LINE_END);
>         add(bottomPanel, BorderLayout.PAGE_END);
>         setBorder(BorderFactory.createEmptyBorder(20,20,20,20));
>         Vector order = new Vector(7);
>         order.add(tf1);
>         order.add(tf2);
>         order.add(tf3);
>         order.add(tf4);
>         order.add(tf5);
>         order.add(tf6);
>         order.add(table);
>         newPolicy = new MyOwnFocusTraversalPolicy(order);
>     }
>
> ```
>
> To use a custom `FocusTraversalPolicy`,
> implement the following code on any focus cycle root.
>
> ```
>
>     MyOwnFocusTraversalPolicy newPolicy = new MyOwnFocusTraversalPolicy();
>     frame.setFocusTraversalPolicy(newPolicy);
>
> ```
>
> You can remove the custom focus traversal policy
> by setting the `FocusTraversalPolicy` to
> `null`, which will restore the default policy.

## Tracking Focus Changes to Multiple Components
> In some situations an application may need to track which component has
> the focus. This information might be used to dynamically update menus
> or perhaps a status bar. If you need to track
> the focus only on specific components, it may make sense to implement a
> [focus event listener](../events/focuslistener.html).
>
> If a focus listener is not appropriate, you can instead
> register a `PropertyChangeListener` on the
> `KeyboardFocusManager`. The property change
> listener is notified of every change
> involving the focus, including changes to the
> focus owner, the focused window,
> and the default focus traversal policy. See the
> [KeyboardFocusManager
> Properties](#properties) table for a complete list.
>
> The
> following example demonstrates tracking the focus owner
> by installing a property change listener on the
> keyboard focus manager.
>
> ![The TrackFocusDemo example, which demonstrates tracking the focus owner.](../../figures/uiswing/misc/TrackFocusDemo.png)
>
> ---
>
> **Try this:**
>
> 1. Click the Launch button
>    to run TrackFocusDemo using
>    [Java™ Web Start](http://java.sun.com/products/javawebstart/index.jsp)
>    ([download JDK 6](http://java.sun.com/javase/downloads/index.jsp)).
>    Alternatively, to compile and run the example yourself,
>    consult the
>    [example index](../examples/misc/index.html#TrackFocusDemo).
>
>    [![Launches the TrackFocusDemo application](../../images/jws-launch-button.png)](http://download.oracle.com/javase/tutorialJWS/uiswing/misc/ex6/TrackFocusDemo.jnlp)
> 2. If necessary, click the window to give it the focus.- The window shows six images, each of which is displayed by
>      a `Picture` component. The `Picture`
>      that has the focus is indicated with a red
>      border. A label at the bottom of the window
>      describes the `Picture` that has the focus.- Move the focus to another `Picture` by using Tab
>        or Shift-Tab, or by clicking an image.
>        Because a property change listener has been
>        registered on the keyboard focus manager,
>        the change in focus is detected and the label is
>        updated appropriately.
>
> ---
>
> You can view the demo's code in
> [`TrackFocusDemo.java`](../examples/misc/TrackFocusDemoProject/src/misc/TrackFocusDemo.java). The custom component used for drawing the images can be found in
> [`Picture.java`](../examples/misc/TrackFocusDemoProject/src/misc/Picture.java). Here is the code that defines and installs the
> property change listener:
>
> ```
>
> KeyboardFocusManager focusManager =
>     KeyboardFocusManager.getCurrentKeyboardFocusManager();
> focusManager.addPropertyChangeListener(
>     new PropertyChangeListener() {
>         public void propertyChange(PropertyChangeEvent e) {
>             String prop = e.getPropertyName();
>             if (("focusOwner".equals(prop)) &&
>                   ((e.getNewValue()) instanceof Picture)) {
>                 Component comp = (Component)e.getNewValue();
>                 String name = comp.getName();
>                 Integer num = new Integer(name);
>                 int index = num.intValue();
>                 if (index < 0 || index > comments.length) {
>                     index = 0;
>                 }
>                 info.setText(comments[index]);
>             }
>         }
>     }
> );
>
> ```
>
> The custom component, `Picture`,
> is responsible for drawing the image. All six
> components are defined in this manner:
>
> ```
>
> pic1 = new Picture(createImageIcon("images/" +
>             mayaString + ".gif", mayaString).getImage());
> pic1.setName("1");
>
> ```

## Timing Focus Transfers
> Focus transfers are asynchronous. This quality can lead to some odd
> timing-related problems and assumptions, especially during automatic
> transfers of the focus. For example, imagine an
> application with a window containing a Start button,
> a Cancel button and a text field.
> The components are added in this order:
>
> 1. Start button- Text field- Cancel button
>
> When the application is launched, the
> `LayoutFocusTraversalPolicy`
> determines the focus traversal policy —
> in this case, it is the order that the components
> were added to their container.
> In this example, the desired behavior is that the
> Start button has the initial focus, and when the
> Start button is clicked, it is disabled, and then the Cancel
> button receives the focus.
> The correct way to
> implement this behavior would be to add the components
> to the container in the desired order or to
> create a custom focus traversal policy.
> If, for some reason, that is not possible,
> then you can implement this behavior
> with the following code snippet:
>
> ```
>
> public void actionPerformed(ActionEvent e) {
>     //This works.
>     start.setEnabled(false);
>     cancel.requestFocusInWindow();
> }
>
> ```
>
> As desired, the focus goes from the Start button to the
> Cancel button, rather than to the text field.
> But a different result would occur if the same methods were
> called in the opposite order as follows:
>
> ```
>
> public void actionPerformed(ActionEvent e) {
>     //This does not work.
>     cancel.requestFocusInWindow();
>     start.setEnabled(false);
> }
>
> ```
>
> In this case, the focus is requested on the Cancel button before
> it has left the Start button.
> The call to the `requestFocusInWindow` method
> initiates the focus transfer, but it does not immediately move the focus
> to the Cancel button.
> When the Start button is disabled, the focus is
> transferred to the next component (so there is always a component
> with the focus) and, in this case, it would then move the focus to the
> text field, *not* to the Cancel button.
>
> There are several situations in which you need to make focus requests after all other changes that
> might affect the focus applies to:
>
> * Hiding the focus owner.* Making the focus owner non-focusable.* Calling the `removeNotify` method on the focus owner.* Doing any of the above operations to the container of the focus owner,
>         or causing changes to the focus policy so that the container no
>         longer accepts the component as the focus owner.* Disposing of the top-level window that contains the focus owner.

### The Focus API

> The following tables list the commonly used
> constructors and methods related to focus.
> The focus API falls into four categories:
>
> * [Useful Methods for Components](#focusMethods)* [Creating and Using a Custom
>     FocusTraversalPolicy](#focustraversal)* [Input Verification API](#inputverificationapi)* [KeyboardFocusManager Properties](#properties)
>
> For more detailed information about the focus architecture,
> see the specification for the
> [Focus Subsystem](http://download.oracle.com/javase/7/docs/api/java/awt/doc-files/FocusSpec.html). You may also find
> [How to Write a Focus Listener](../events/focuslistener.html) useful.
>
> Useful Methods for Components
>
> *All of this API was introduced in JDK 1.4.*
>
> | Method (in `Component`) | Purpose |
> | --- | --- |
> | [isFocusOwner()](http://download.oracle.com/javase/7/docs/api/java/awt/Component.html#isFocusOwner()) | Returns `true` if the component is the focus owner. This method, introduced in JDK 1.4, renders obsolete `hasFocus`. |
> | [setRequestFocusEnabled(boolean)](http://download.oracle.com/javase/7/docs/api/javax/swing/JComponent.html#setRequestFocusEnabled(boolean))  [isRequestFocusEnabled()](http://download.oracle.com/javase/7/docs/api/javax/swing/JComponent.html#isRequestFocusEnabled()) (*in `JComponent`)* | Sets or checks on whether this component should get the focus. Setting the `setRequestFocusEnabled` to `false` typically prevents mouse clicks from giving the component the focus, while still allowing keyboard navigation to give the component the focus. This method applies only to components that receive mouse events. For example, you can use this method on a `JButton`, but not on a `JPanel`. If you write a custom component it is up to you to honor this property. This method is recommended over the `setFocusable` method and will allow your program to work better for users employing [assistive technologies](access.html). |
> | [setFocusable(boolean)](http://download.oracle.com/javase/7/docs/api/java/awt/Component.html#setFocusable(boolean))  [isFocusable()](http://download.oracle.com/javase/7/docs/api/java/awt/Component.html#isFocusable()) | Sets or gets the focusable state of the component. A component must be focusable in order to gain the focus. When a component has been removed from the focus cycle with `setFocusable(false)`, it can no longer be navigated with the keyboard. The `setRequestFocusEnabled` method is recommended so that your program can be run by users employing [assistive technologies](access.html). |
> | [requestFocusInWindow()](http://download.oracle.com/javase/7/docs/api/java/awt/Component.html#requestFocusInWindow()) | Requests that this component should get the focus. The component's window must be the current focused window. For this request to be granted a subclass of `JComponent` must be visible, enabled, and focusable, and have an input map for this request to be granted. It should not be assumed that the component has the focus until it fires a `FOCUS_GAINED` event. This method is preferred to the `requestFocus` method, which is platform-dependent. |
> | [setFocusTraversalKeys(int, Set)](http://download.oracle.com/javase/7/docs/api/java/awt/Container.html#setFocusTraversalKeys(int, java.util.Set))  [getFocusTraversalKeys(int)](http://download.oracle.com/javase/7/docs/api/java/awt/Container.html#getFocusTraversalKeys(int))  [areFocusTraversalKeysSet(int)](http://download.oracle.com/javase/7/docs/api/java/awt/Container.html#areFocusTraversalKeysSet(int)) (*in `java.awt.Container`*) | Sets or gets the focus traversal keys for a particular direction or determines whether any focus traversal keys have been explicitly set on this container. If no focus traversal keys have been set, they are inherited from an ancestor or from the keyboard focus manager. Focus traversal keys can be set for the following directions: `KeyboardFocusManager.FORWARD_TRAVERSAL_KEYS`, `KeyboardFocusManager.BACKWARD_TRAVERSAL_KEYS` `KeyboardFocusManager.UP_CYCLE_TRAVERSAL_KEYS`, or `KeyboardFocusManager.DOWN_CYCLE_TRAVERSAL_KEYS`. If you set the `UP_CYCLE_TRAVERSAL_KEYS` or the `DOWN_CYCLE_TRAVERSAL_KEYS`, you must also invoke [`setImplicitDownCycleTraversal(false)`](http://download.oracle.com/javase/7/docs/api/javax/swing/SortingFocusTraversalPolicy.html#setImplicitDownCycleTraversal(boolean)) on the focus traversal policy. |
>
> Creating and Using a Custom
> FocusTraversalPolicy
>
> | Class or Method | Purpose |
> | --- | --- |
> | [LayoutFocusTraversalPolicy](http://download.oracle.com/javase/7/docs/api/javax/swing/LayoutFocusTraversalPolicy.html) | The class that, by default, determines the focus traversal policy for Swing components. |
> | [getComponentAfter(Container, Component)](http://download.oracle.com/javase/7/docs/api/javax/swing/LayoutFocusTraversalPolicy.html#getComponentAfter(java.awt.Container, java.awt.Component)) | Given the component that is passed as input, returns the component that should next have the focus. |
> | [getComponentBefore(Container, Component)](http://download.oracle.com/javase/7/docs/api/javax/swing/LayoutFocusTraversalPolicy.html#getComponentBefore(java.awt.Container, java.awt.Component)) | Given the component that is passed as input, returns the component that should have the focus before this component. The method is used for backward tabbing. |
> | [getDefaultComponent(Container)](http://download.oracle.com/javase/7/docs/api/javax/swing/SortingFocusTraversalPolicy.html#getDefaultComponent(java.awt.Container)) (*in `javax.swing.SortingFocusTraversalPolicy`)* | Returns the component that should have the default focus. |
> | [getFirstComponent(Container)](http://download.oracle.com/javase/7/docs/api/javax/swing/LayoutFocusTraversalPolicy.html#getFirstComponent(java.awt.Container)) | Returns the first component in the traversal cycle. |
> | [getInitialComponent(Container)](http://download.oracle.com/javase/7/docs/api/javax/swing/InternalFrameFocusTraversalPolicy.html#getInitialComponent(java.awt.Container)) | Returns the component that should receive the focus when a window is made visible for the first time. |
> | [getLastComponent(Container)](http://download.oracle.com/javase/7/docs/api/javax/swing/LayoutFocusTraversalPolicy.html#getLastComponent(java.awt.Container)) | Returns the last component in the traversal cycle. |
> | [setFocusTraversalPolicy(FocusTraversalPolicy)](http://download.oracle.com/javase/7/docs/api/java/awt/Container.html#setFocusTraversalPolicy(java.awt.FocusTraversalPolicy))  [getFocusTraversalPolicy(FocusTraversalPolicy)](http://download.oracle.com/javase/7/docs/api/java/awt/Container.html#getFocusTraversalPolicy()) (*in `java.awt.Container`*) | Sets or gets the focus traversal policy or determines if a policy has been set. Note that setting a focus traversal policy on a container that is not the focus cycle root may have no apparent effect. A value of `null` means that a policy has not been explicitly set. If no policy has been set, a policy is inherited from the parent focus cycle root. |
> | [isFocusCycleRoot()](http://download.oracle.com/javase/7/docs/api/java/awt/Container.html#isFocusCycleRoot())  [setFocusCycleRoot(boolean)](http://download.oracle.com/javase/7/docs/api/java/awt/Container.html#setFocusCycleRoot(boolean)) (*in `java.awt.Container`*) | Checks or sets whether a container is the root of a focus traversal cycle. |
> | [isFocusTraversalPolicyProvider()](http://download.oracle.com/javase/7/docs/api/java/awt/Container.html#isFocusTraversalPolicyProvider())  [setFocusTraversalPolicyProvider(boolean)](http://download.oracle.com/javase/7/docs/api/java/awt/Container.html#setFocusTraversalPolicyProvider(boolean)) (*in `java.awt.Container`*) | Checks or sets whether a container will be used to provide focus traversal policy. |
>
> Input Verification API
>
> *All of this API was introduced in JDK 1.3.*
>
> | Class or Method | Purpose |
> | --- | --- |
> | [InputVerifier](http://download.oracle.com/javase/7/docs/api/javax/swing/InputVerifier.html) | Abstract class that allows input validation via the focus mechanism. When an attempt is made to shift the focus from a component containing an input verifier, the focus is not relinquished until the verifier is satisfied. |
> | [shouldYieldFocus(JComponent)](http://download.oracle.com/javase/7/docs/api/javax/swing/InputVerifier.html#shouldYieldFocus(javax.swing.JComponent)) *(in `InputVerifier`)* | When a component has an input verifier, this method is called by the system to determine whether the focus can leave this component. This method may cause side effects, such as bringing up a dialog-box. If this method returns `false`, the focus remains on the component passed in to the method. |
> | [verify(JComponent)](http://download.oracle.com/javase/7/docs/api/javax/swing/InputVerifier.html#verify(javax.swing.JComponent)) *(in `InputVerifier`)* | You need to override this method to check that the component's input is valid. It should return `true` if valid, otherwise return `false`. This method should not cause any side effects, such as bringing up a dialog-box. This method is called by `shouldYieldFocus`. |
> | [setInputVerifier(inputVerifier)](http://download.oracle.com/javase/7/docs/api/javax/swing/JComponent.html#setInputVerifier(javax.swing.InputVerifier))  [getInputVerifier()](http://download.oracle.com/javase/7/docs/api/javax/swing/JComponent.html#getInputVerifier()) *(in `JComponent`)* | Sets or gets the input verifier assigned to the component. By default, components have no input verifier. |
> | [setVerifyInputWhenFocusTarget(boolean)](http://download.oracle.com/javase/7/docs/api/javax/swing/JComponent.html#setVerifyInputWhenFocusTarget(boolean))  [getVerifyInputWhenFocusTarget()](http://download.oracle.com/javase/7/docs/api/javax/swing/JComponent.html#getVerifyInputWhenFocusTarget()) *(in `JComponent`)* | Sets or gets whether the input verifier for the current focus owner is called before this component requests the focus. The default is `true`. This method should be set to `false` for components, such as a Cancel button or a scroll bar, that should receive the focus even if input is invalid. |
>
> KeyboardFocusManager Properties
>
> This table defines the bound properties for
> [`KeyboardFocusManager`](http://download.oracle.com/javase/7/docs/api/java/awt/KeyboardFocusManager.html). A listener can be registered for these properties by calling
> [`addPropertyChangeListener`](http://download.oracle.com/javase/7/docs/api/java/awt/KeyboardFocusManager.html#addPropertyChangeListener(java.beans.PropertyChangeListener)).
>
> *All of this API was introduced in JDK 1.4.*
>
> | Property | Purpose |
> | --- | --- |
> | focusOwner | The component that currently receives key events. |
> | permanentFocusOwner | The component that most recently received a permanent `FOCUS_GAINED` event. Typically the same as `focusOwner`, unless a temporary focus change is currently in effect. |
> | focusedWindow | The window that is or that contains the focus owner. |
> | activeWindow | The component must always be either a `Frame` or a `Dialog`. The active window is either the focused window, or the first frame or dialog-box that is an owner of the focused window. |
> | defaultFocusTraversalPolicy | The default focus traversal policy, which can be set by the `setFocusTraversalPolicy` method of the `Container` class. |
> | forwardDefaultFocusTraversalKeys | The set of default focus keys for a forward traversal. For multi-line text components, these keys default to Control-Tab. For all other components, these keys default to Tab and Control-Tab. |
> | backwardDefaultFocusTraversalKeys | The set of default focus keys for a backward traversal. For multi-line text components these keys default to Control-Shift-Tab. For all other components these keys default to Shift-Tab and Control-Shift-Tab. |
> | upCycleDefaultFocusTraversalKeys | The set of default focus keys for an up cycle. These keys are null, by default, for Swing components. If you set these keys on the `KeyboardFocusManager`, or if you set the `downCycleFocusTraversalKeys` on a focus cycle root, you must also invoke the [`setImplicitDownCycleTraversal(false)`](http://download.oracle.com/javase/7/docs/api/javax/swing/SortingFocusTraversalPolicy.html#setImplicitDownCycleTraversal(boolean)) method on the focus traversal policy. |
> | downCycleDefaultFocusTraversalKeys | The set of default focus keys for a down cycle. These keys are null, by default, for Swing components. If you set these keys on the `KeyboardFocusManager`, or if you set the `upCycleFocusTraversalKeys` on a focus cycle root, you must also invoke the [`setImplicitDownCycleTraversal(false)`](http://download.oracle.com/javase/7/docs/api/javax/swing/SortingFocusTraversalPolicy.html#setImplicitDownCycleTraversal(boolean)) method on the focus traversal policy. |
> | currentFocusCycleRoot | The container that is the current focus cycle root. |

### Examples that Use Focus

> The following table lists examples that
> manipulate the focus:
>
> | Example | Where Described | Notes |
> | --- | --- | --- |
> | [`FocusConceptsDemo`](../examples/misc/index.html#FocusConceptsDemo) | This section | Demonstrates basic default focus behavior. |
> | [`FocusTraversalDemo`](../examples/misc/index.html#FocusTraversalDemo) | This section | Demonstrates how to override the default focus order. |
> | [`TrackFocusDemo`](../examples/misc/index.html#TrackFocusDemo) | This section | Demonstrates how to use a `PropertyChangeListener` to track the focus owner. Also implements a custom focusable component. |
> | [`InputVerificationDemo`](../examples/misc/index.html#InputVerificationDemo) | This section | Demonstrates how to implement an `InputVerifier` to validate user input. |
> | [`InputVerificationDialogDemo`](../examples/misc/index.html#InputVerificationDialogDemo) | This section | Demonstrates how to implement an `InputVerifier` that puts up a dialog-box when user input is invalid. |
> | [`FocusEventDemo`](../examples/events/index.html#FocusEventDemo) [How to Write a Focus Listener](../events/focuslistener.html) | Reports all focus events that occur on several components to demonstrate the circumstances under which focus events are fired. | |

[« Previous](access.html)
•
[Trail](../TOC.html)
•
[Next »](keybinding.html)

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

**Previous page:** How to Support Assistive Technologies
  
**Next page:** How to Use Key Bindings




A browser with JavaScript enabled is required for this page to operate properly.