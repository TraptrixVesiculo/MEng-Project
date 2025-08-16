[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** Creating a GUI With JFC/Swing
  
**Lesson:** Using Swing Components
  
**Section:** How to Use Various Components

[Using Swing Components](index.html)

[Using Top-Level Containers](toplevel.html)

[The JComponent Class](jcomponent.html)

[Using Text Components](text.html)

[Text Component Features](generaltext.html)

[The Text Component API](textapi.html)

[How to Use Various Components](componentlist.html)

[How to Make Applets](applet.html)

[How to Use Buttons, Check Boxes, and Radio Buttons](button.html)

[How to Use the ButtonGroup Component](buttongroup.html)

[How to Use Color Choosers](colorchooser.html)

[How to Use Combo Boxes](combobox.html)

[How to Make Dialogs](dialog.html)

[How to Use Editor Panes and Text Panes](editorpane.html)

[How to Use File Choosers](filechooser.html)

[How to Use Formatted Text Fields](formattedtextfield.html)

[How to Make Frames (Main Windows)](frame.html)

[How to Use Internal Frames](internalframe.html)

[How to Use Labels](label.html)

[How to Use Layered Panes](layeredpane.html)

[How to Use Lists](list.html)

[How to Use Menus](menu.html)

[How to Use Panels](panel.html)

[How to Use Password Fields](passwordfield.html)

[How to Use Progress Bars](progress.html)

[How to Use Root Panes](rootpane.html)

[How to Use Scroll Panes](scrollpane.html)

[How to Use Separators](separator.html)

[How to Use Sliders](slider.html)

How to Use Spinners

[How to Use Split Panes](splitpane.html)

[How to Use Tabbed Panes](tabbedpane.html)

[How to Use Tables](table.html)

[How to Use Text Areas](textarea.html)

[How to Use Text Fields](textfield.html)

[How to Use Tool Bars](toolbar.html)

[How to Use Tool Tips](tooltip.html)

[How to Use Trees](tree.html)

[How to Use HTML in Swing Components](html.html)

[How to Use Models](model.html)

[How to Use Icons](icon.html)

[How to Use Borders](border.html)

[Solving Common Component Problems](problems.html)

[Home Page](../../index.html)
>
[Creating a GUI With JFC/Swing](../index.html)
>
[Using Swing Components](index.html)

[« Previous](slider.html) • [Trail](../TOC.html) • [Next »](splitpane.html)

# How to Use Spinners

Spinners are similar to
[combo boxes](combobox.html) and
[lists](list.html) in that they let the user choose from a range of values.
Like editable combo boxes, spinners allow
the user to type in a value.
Unlike combo boxes, spinners do not have a drop-down list
that can cover up other components.
Because spinners do not display possible values —
only the current value is visible —
they are often used instead of
combo boxes or lists
when the set of possible values is extremely large.
However, spinners should only be used
when the possible values and their sequence
are obvious.

A spinner is a compound component with three
subcomponents: two small buttons and an
*editor*.
The editor can be any `JComponent`,
but by default it is implemented
as a panel that contains a
[formatted text field](formattedtextfield.html).
The spinner's possible and current values
are managed by its *model*.

Here is a picture of an application named `SpinnerDemo`
that has three spinners used to specify dates:

![SpinnerDemo shows 3 kinds of spinners](../../figures/uiswing/components/SpinnerDemo.png)

The code for the main class can be found in
[`SpinnerDemo.java`](../examples/components/SpinnerDemoProject/src/components/SpinnerDemo.java).
The Month spinner displays the name
of the first month in the user's locale.
The possible values for this spinner
are specified using
an array of strings.
The Year spinner displays one value of a range of integers,
initialized to the current year.
The Another Date spinner displays one value
in a range of `Date` objects
(initially the current date)
in a custom format
that shows just a month and year.

---

**Try this:**

1. Click the Launch button
   to run SpinnerDemo using
   [Java™ Web Start](http://java.sun.com/products/javawebstart/index.jsp ) 
   ([download JDK 6](http://java.sun.com/javase/downloads/index.jsp)).
   Alternatively, to compile and run the example yourself,
   consult the [example index](../examples/components/index.html#SpinnerDemo).

[![Launches the SpinnerDemo Application](../../images/jws-launch-button.png)](http://download.oracle.com/javase/tutorialJWS/uiswing/components/ex6/SpinnerDemo.jnlp)

2. With the Month spinner, use the arrow buttons
   or keys to
   cycle forward and backward through the possible values.
     
   Note that the lowest value is the first month of the year
   (for example, January)
   and the highest is the last (for example, December).
   The exact values depend on your locale.
   Also note that the values do not cycle — you cannot
   use the up arrow button or key to go
   from December directly to January —
   because the standard spinner models do not support cycling.- Type in a valid month name for your locale —
     for example, July.
       
     Note that the spinner automatically completes the month name.- Moving on to the Year spinner,
       try typing a year over 100 years ago —
       for example, 1800 —
       and then click on another spinner or press the Tab key
       to move the focus out of the spinner.
         
       Because this program restricts the spinner's model
       to numbers within 100 years of the current year,
       1800 is invalid.
       When the focus moves out of the spinner,
       the displayed text changes back to the last valid value.- Moving to the Another Date spinner,
         use the arrow buttons or keys to change the date.
           
         Note that by default the first part of the date —
         in this case, the month number — changes.
         You can change which part of the date changes either by
         clicking the mouse or using the arrow keys
         to move to another part of the date.

---

To create a spinner, first
create its model
and then pass the model into the
[JSpinner](http://download.oracle.com/javase/7/docs/api/javax/swing/JSpinner.html) constructor.
For example:

```

String[] monthStrings = getMonthStrings(); //get month names
SpinnerListModel monthModel = new SpinnerListModel(monthStrings);
JSpinner spinner = new JSpinner(monthModel);

```

The rest of this section covers the following topics:

* [Using Standard Spinner Models and Editors](#standard)* [Specifying Spinner Formatting](#format)* [Creating Custom Spinner Models and Editors](#model)* [Detecting Spinner Value Changes](#change)* [The Spinner API](#api)* [Examples That Use Spinners](#eg)

### Using Standard Spinner Models and Editors

> The Swing API provides three spinner models:
>
> [SpinnerListModel](http://download.oracle.com/javase/7/docs/api/javax/swing/SpinnerListModel.html)
> :   The `SpinnerListModel` is a model whose values are
>     defined by an array of objects or a `List` object.
>     The Month spinner in the `SpinnerDemo` example
>     uses this model,
>     initialized with an array derived from the value
>     returned by the `getMonths`
>     method of the `java.text.DateFormatSymbols` class.
>     See
>     [`SpinnerDemo.java`](../examples/components/SpinnerDemoProject/src/components/SpinnerDemo.java) for details.
>
> [SpinnerNumberModel](http://download.oracle.com/javase/7/docs/api/javax/swing/SpinnerNumberModel.html)
> :   The `SpinnerNumberModel` supports sequences of numbers
>     which can be expressed as `double` objects,
>     `int` objects,
>     or `Number` objects.
>     You can specify the minimum and maximum allowable values,
>     as well as the *step size* —
>     the amount of each increment or decrement.
>     The Year spinner uses this model,
>     created with the following code:
>
>     ```
>
>     SpinnerModel model =
>             new SpinnerNumberModel(currentYear, //initial value
>                                    currentYear - 100, //min
>                                    currentYear + 100, //max
>                                    1);                //step
>
>     ```
>
> [SpinnerDateModel](http://download.oracle.com/javase/7/docs/api/javax/swing/SpinnerDateModel.html)
> :   The `SpinnerDateModel` supports sequences of `Date` objects.
>     You can specify the minimum and maximum dates,
>     as well as the field
>     (such as `Calendar.YEAR`)
>     to increment or decrement.
>     Note, however, that some types of look and feel
>     ignore the specified field,
>     and instead change the field
>     that appears selected.
>     The Another Date spinner uses this model, created with the following code:
>
>     ```
>
>     Date initDate = calendar.getTime();
>     calendar.add(Calendar.YEAR, -100);
>     Date earliestDate = calendar.getTime();
>     calendar.add(Calendar.YEAR, 200);
>     Date latestDate = calendar.getTime();
>     model = new SpinnerDateModel(initDate,
>                                  earliestDate,
>                                  latestDate,
>                                  Calendar.YEAR);
>
>     ```
>
> When you set the spinner's model,
> the spinner's editor is automatically set.
> The Swing API provides an editor class
> corresponding to each of the three model classes listed above.
> These classes —
> [JSpinner.ListEditor](http://download.oracle.com/javase/7/docs/api/javax/swing/JSpinner.ListEditor.html),
> [JSpinner.NumberEditor](http://download.oracle.com/javase/7/docs/api/javax/swing/JSpinner.NumberEditor.html), and
> [JSpinner.DateEditor](http://download.oracle.com/javase/7/docs/api/javax/swing/JSpinner.DateEditor.html) —
> are all subclasses of the
> [JSpinner.DefaultEditor](http://download.oracle.com/javase/7/docs/api/javax/swing/JSpinner.DefaultEditor.html) class that feature editable formatted text fields.
> If you use a model that does not have an editor associated with it,
> the editor is by default
> a `JSpinner.DefaultEditor` instance
> with a non-editable formatted text field.

### Specifying Spinner Formatting

> To change the formatting
> used in a standard spinner editor,
> you can create and set the editor yourself.
>
> The `JSpinner.NumberEditor`
> and `JSpinner.DateEditor` classes
> have constructors that allow you to
> create an editor that formats its data in a particular way.
> For example, the following code
> sets up the Another Date spinner
> so that instead of using the default date format,
> which is long and includes the time,
> it shows just a month and year
> in a compact way.
>
> ```
>
> spinner.setEditor(new JSpinner.DateEditor(spinner, "MM/yyyy"));
>
> ```
>
> ---
>
> **Note:** You can play with date formats by
> running `ComboBoxDemo2` example.
> Click the Launch button
> to run ComboBoxDemo2 using
> [Java™ Web Start](http://java.sun.com/products/javawebstart/index.jsp ) 
> ([download JDK 6](http://java.sun.com/javase/downloads/index.jsp)).
> Alternatively, to compile and run the example yourself,
> consult the [example index](../examples/components/index.html#ComboBoxDemo2).
>
> [![Launches the ComboBoxDemo2 Application](../../images/jws-launch-button.png)](http://download.oracle.com/javase/tutorialJWS/uiswing/components/ex6/ComboBoxDemo2.jnlp)
>
> For information about format strings, see the
> [Formatting](../../i18n/format/index.html) lesson of the Internationalization trail.
>
> ---
>
> To change the formatting
> when using a default editor,
> you can obtain the editor's formatted text field
> and invoke methods on it.
> You can call those methods using the
> `getTextField` method
> defined in the `JSpinner.DefaultEditor` class.
> Note that the Swing-provided editors are not
> formatted text fields.
> Instead, they are the `JPanel` instances
> that contain
> a formatted text field.
> Here is an example of getting and invoking methods on
> the editor's formatted text field:
>
> ```
>
> //Tweak the spinner's formatted text field.
> ftf = getTextField(spinner);
> if (ftf != null ) {
>     ftf.setColumns(8); //specify more width than we need
>     ftf.setHorizontalAlignment(JTextField.RIGHT);
> }
> ...
>
> public JFormattedTextField getTextField(JSpinner spinner) {
>     JComponent editor = spinner.getEditor();
>     if (editor instanceof JSpinner.DefaultEditor) {
>         return ((JSpinner.DefaultEditor)editor).getTextField();
>     } else {
>         System.err.println("Unexpected editor type: "
>                            + spinner.getEditor().getClass()
>                            + " isn't a descendant of DefaultEditor");
>         return null;
>     }
> }
>
> ```

### Creating Custom Spinner Models and Editors

> If the existing spinner models or editors do not meet your needs,
> you can create your own.
>
> The easiest route to creating a custom spinner model
> is to create a subclass
> of an existing `AbstractSpinnerModel` subclass
> that already does most of what you need.
> An alternative is to implement your own class
> by extending
> [`AbstractSpinnerModel`](http://download.oracle.com/javase/7/docs/api/javax/swing/AbstractSpinnerModel.html) class,
> which implements the event notifications
> required for all spinner models.
>
> The following subclass of `SpinnerListModel`
> implements a spinner model
> that cycles through an array of objects.
> It also lets you specify a second spinner model
> that will be updated whenever the cycle begins again.
> For example, if the array of objects is a list of months,
> the linked model could be for a spinner that displays the year.
> When the month flips over from December to January the year is incremented.
> Similarly, when the month flips back from January to December
> the year is decremented.
>
> ```
>
> public class CyclingSpinnerListModel extends SpinnerListModel {
>     Object firstValue, lastValue;
>     SpinnerModel linkedModel = null;
>
>     public CyclingSpinnerListModel(Object[] values) {
>         super(values);
>         firstValue = values[0];
>         lastValue = values[values.length - 1];
>     }
>
>     public void setLinkedModel(SpinnerModel linkedModel) {
>         this.linkedModel = linkedModel;
>     }
>
>     public Object getNextValue() {
>         Object value = super.getNextValue();
>         if (value == null) {
>             value = firstValue;
>             if (linkedModel != null) {
>                 linkedModel.setValue(linkedModel.getNextValue());
>             }
>         }
>         return value;
>     }
>
>     public Object getPreviousValue() {
>         Object value = super.getPreviousValue();
>         if (value == null) {
>             value = lastValue;
>             if (linkedModel != null) {
>                 linkedModel.setValue(linkedModel.getPreviousValue());
>             }
>         }
>         return value;
>     }
> }
>
> ```
>
> The `CyclingSpinnerListModel` model
> is used for the Month spinner in the `SpinnerDemo2` example,
> an example that is almost identical to the `SpinnerDemo`.
> Click the Launch button
> to run SpinnerDemo2 using
> [Java™ Web Start](http://java.sun.com/products/javawebstart/index.jsp ) 
> ([download JDK 6](http://java.sun.com/javase/downloads/index.jsp)).
> Alternatively, to compile and run the example yourself,
> consult the [example index](../examples/components/index.html#SpinnerDemo2).
>
> [![Launches the SpinnerDemo2 Application](../../images/jws-launch-button.png)](http://download.oracle.com/javase/tutorialJWS/uiswing/components/ex6/SpinnerDemo2.jnlp)
>
> As we mentioned before, if you implement a spinner model
> that does not descend from
> `SpinnerListModel`,
> `SpinnerNumberModel`, or
> `SpinnerDateModel`,
> then the spinner's default editor is
> a non-editable instance of `JSpinner.DefaultEditor`.
> As you have already seen,
> you can set a spinner's editor
> by invoking the `setEditor` method on the spinner
> after the spinner's model property has been set.
> An alternative to using `setEditor` is to
> create a subclass of the `JSpinner` class
> and override its `createEditor` method
> so that it returns a particular kind of editor
> whenever the spinner model is of a certain type.
>
> In theory at least, you can use any `JComponent` instance
> as an editor.
> Possibilities include using a
> subclass of a standard component
> such as `JLabel`,
> or a component you have implemented from scratch,
> or a subclass of
> `JSpinner.DefaultEditor`.
> The only requirements
> are that the editor must
> be updated to reflect changes in the spinner's value,
> and it must have a reasonable preferred size.
> The editor should generally also
> set its tool tip text
> to whatever tool tip text has been specified
> for the spinner.
> An example of implementing an editor is provided in the next section.

### Detecting Spinner Value Changes

> You can detect that a spinner's value has changed
> by registering a change listener on
> either the spinner or its model.
> Here is an example of implementing such a change listener.
> This example is from `SpinnerDemo3`,
> which is based on `SpinnerDemo`
> and uses a change listener
> to change the color of some text
> to match the value of the Another Date spinner.
> Click the Launch button
> to run SpinnerDemo3 using
> [Java™ Web Start](http://java.sun.com/products/javawebstart/index.jsp ) 
> ([download JDK 6](http://java.sun.com/javase/downloads/index.jsp)).
> Alternatively, to compile and run the example yourself,
> consult the [example index](../examples/components/index.html#SpinnerDemo3).
>
> [![Launches the SpinnerDemo3 Application](../../images/jws-launch-button.png)](http://download.oracle.com/javase/tutorialJWS/uiswing/components/ex6/SpinnerDemo3.jnlp)
>
> ```
>
> public class SpinnerDemo3 extends JPanel
>                           implements ChangeListener {
>     protected Calendar calendar;
>     protected JSpinner dateSpinner;
>     ...
>     public SpinnerDemo3() {
>         ...
>         SpinnerDateModel dateModel = ...;
>         ...
>         setSeasonalColor(dateModel.getDate()); //initialize color
>
>         //Listen for changes on the date spinner.
>         dateSpinner.addChangeListener(this);
>         ...
>     }
>
>     public void stateChanged(ChangeEvent e) {
>         SpinnerModel dateModel = dateSpinner.getModel();
>         if (dateModel instanceof SpinnerDateModel) {
>             setSeasonalColor(((SpinnerDateModel)dateModel).getDate());
>         }
>     }
>
>     protected void setSeasonalColor(Date date) {
>         calendar.setTime(date);
>         int month = calendar.get(Calendar.MONTH);
>         JFormattedTextField ftf = getTextField(dateSpinner);
>         if (ftf == null) return;
>
>         //Set the color to match northern hemisphere seasonal conventions.
>         switch (month) {
>             case 2:  //March
>             case 3:  //April
>             case 4:  //May
>                      ftf.setForeground(SPRING_COLOR);
>                      break;
>             ...
>             default: //December, January, February
>                      ftf.setForeground(WINTER_COLOR);
>         }
>     }
>     ...
> }
>
> ```
>
> The following example implements an editor
> which has a change listener
> so that it can reflect the spinner's current value.
> This particular editor
> displays a solid color of gray,
> ranging anywhere from white to black.
> Click the Launch button
> to run SpinnerDemo4 using
> [Java™ Web Start](http://java.sun.com/products/javawebstart/index.jsp ) 
> ([download JDK 6](http://java.sun.com/javase/downloads/index.jsp)).
> Alternatively, to compile and run the example yourself,
> consult the [example index](../examples/components/index.html#SpinnerDemo4).
>
> [![Launches the SpinnerDemo4 Application](../../images/jws-launch-button.png)](http://download.oracle.com/javase/tutorialJWS/uiswing/components/ex6/SpinnerDemo4.jnlp)
>
> ```
>
> ...//Where the components are created:
> JSpinner spinner = new JSpinner(new GrayModel(170));
> spinner.setEditor(new GrayEditor(spinner));
>
> class GrayModel extends SpinnerNumberModel {
>     ...
> }
>
> class GrayEditor extends JLabel
>                  implements ChangeListener {
>     public GrayEditor(JSpinner spinner) {
>         setOpaque(true);
>         ...
>         //Get info from the model.
>         GrayModel myModel = (GrayModel)(spinner.getModel());
>         setBackground(myModel.getColor());
>         spinner.addChangeListener(this);
>         ...
>         updateToolTipText(spinner);
>     }
>
>     protected void updateToolTipText(JSpinner spinner) {
>         String toolTipText = spinner.getToolTipText();
>         if (toolTipText != null) {
>             //JSpinner has tool tip text.  Use it.
>             if (!toolTipText.equals(getToolTipText())) {
>                 setToolTipText(toolTipText);
>             }
>         } else {
>             //Define our own tool tip text.
>             GrayModel myModel = (GrayModel)(spinner.getModel());
>             int rgb = myModel.getIntValue();
>             setToolTipText("(" + rgb + "," + rgb + "," + rgb + ")");
>         }
>     }
>
>     public void stateChanged(ChangeEvent e) {
>             JSpinner mySpinner = (JSpinner)(e.getSource());
>             GrayModel myModel = (GrayModel)(mySpinner.getModel());
>             setBackground(myModel.getColor());
>             updateToolTipText(mySpinner);
>     }
> }
>
> ```

### The Spinner API

> The following tables list some of the commonly used API
> for using spinners.
> If you need to deal directly with the editor's formatted text field,
> you should also see
> [The FormattedTextField API](formattedtextfield.html#api).
> Other methods you might use
> are listed in the API tables in
> [The JComponent Class](jcomponent.html#api).
>
> * [Classes Related to Spinners](#newclassesapi)* [Useful JSpinner Constructors and Methods](#jspinnerapi)* [Useful Editor Constructors and Methods](#editorapi)* [SpinnerListModel Methods](#listapi)* [SpinnerDateModel Methods](#dateapi)* [SpinnerNumberModel Methods](#numberapi)
>
> **Classes Related to Spinners**
>
> | Class or Interface | Purpose |
> | [JSpinner](http://download.oracle.com/javase/7/docs/api/javax/swing/JSpinner.html) | A single-line input field that allows the user to select a number or object value from an ordered sequence. |
> | [SpinnerModel](http://download.oracle.com/javase/7/docs/api/javax/swing/SpinnerModel.html) | The interface implemented by all spinner models. |
> | [AbstractSpinnerModel](http://download.oracle.com/javase/7/docs/api/javax/swing/AbstractSpinnerModel.html) | The usual superclass for spinner model implementations. |
> | [SpinnerListModel](http://download.oracle.com/javase/7/docs/api/javax/swing/SpinnerListModel.html) | A subclass of `AbstractSpinnerModel` whose values are defined by an array or a `List`. |
> | [SpinnerDateModel](http://download.oracle.com/javase/7/docs/api/javax/swing/SpinnerDateModel.html) | A subclass of `AbstractSpinnerModel` that supports sequences of `Date` instances. |
> | [SpinnerNumberModel](http://download.oracle.com/javase/7/docs/api/javax/swing/SpinnerNumberModel.html) | A subclass of `AbstractSpinnerModel` that supports sequences of numbers. |
> | [JSpinner.DefaultEditor](http://download.oracle.com/javase/7/docs/api/javax/swing/JSpinner.DefaultEditor.html) | Implements an uneditable component that displays the spinner's value. Subclasses of this class are generally more specialized (and editable). |
> | [JSpinner.ListEditor](http://download.oracle.com/javase/7/docs/api/javax/swing/JSpinner.ListEditor.html) | A subclass of `JSpinner.DefaultEditor` whose values are defined by an array or a `List`. |
> | [JSpinner.DateEditor](http://download.oracle.com/javase/7/docs/api/javax/swing/JSpinner.DateEditor.html) | A subclass of `JSpinner.DefaultEditor` that supports sequences of `Date` instances. |
> | [JSpinner.NumberEditor](http://download.oracle.com/javase/7/docs/api/javax/swing/JSpinner.NumberEditor.html) | A subclass of `JSpinner.DefaultEditor` that supports sequences of numbers. |
>
> **Useful JSpinner Constructors and Methods**
>
> | Constructor or Method | Purpose |
> | [JSpinner()](http://download.oracle.com/javase/7/docs/api/javax/swing/JSpinner.html#JSpinner())   [JSpinner(SpinnerModel)](http://download.oracle.com/javase/7/docs/api/javax/swing/JSpinner.html#JSpinner(javax.swing.SpinnerModel)) | Creates a new `JSpinner`. The no-argument constructor creates a spinner with an integer `SpinnerNumberModel` with an initial value of 0 and no minimum or maximum limits. The optional parameter on the second constructor allows you to specify your own `SpinnerModel`. |
> | [void setValue(java.lang.Object)](http://download.oracle.com/javase/7/docs/api/javax/swing/JSpinner.html#setValue(java.lang.Object))   [Object getValue()](http://download.oracle.com/javase/7/docs/api/javax/swing/JSpinner.html#getValue()) | Sets or gets the currently displayed element of the sequence. |
> | [Object getNextValue()](http://download.oracle.com/javase/7/docs/api/javax/swing/JSpinner.html#getNextValue())   [Object getPreviousValue()](http://download.oracle.com/javase/7/docs/api/javax/swing/JSpinner.html#getPreviousValue()) | Gets the object in the sequence that comes before or after the object returned by the `getValue` method. |
> | [SpinnerModel getModel()](http://download.oracle.com/javase/7/docs/api/javax/swing/JSpinner.html#getModel())  [void setModel(SpinnerModel)](http://download.oracle.com/javase/7/docs/api/javax/swing/JSpinner.html#setModel(javax.swing.SpinnerModel)) | Gets or sets the spinner's model. |
> | [JComponent getEditor()](http://download.oracle.com/javase/7/docs/api/javax/swing/JSpinner.html#getEditor())  [void setEditor(JComponent)](http://download.oracle.com/javase/7/docs/api/javax/swing/JSpinner.html#setEditor(javax.swing.JComponent)) | Gets or sets the spinner's editor, which is often an object of type `JSpinner.DefaultEditor`. |
> | [protected JComponent createEditor(SpinnerModel)](http://download.oracle.com/javase/7/docs/api/javax/swing/JSpinner.html#createEditor(javax.swing.SpinnerModel)) | Called by the `JSpinner` constructors to create the spinner's editor. Override this method to associate an editor with a particular type of model. |
>
> **Useful Editor Constructors and Methods**
>
> | Constructor or Method | Purpose |
> | [JSpinner.NumberEditor(JSpinner, String)](http://download.oracle.com/javase/7/docs/api/javax/swing/JSpinner.NumberEditor.html#JSpinner.NumberEditor(javax.swing.JSpinner, java.lang.String)) | Creates a `JSpinner.NumberEditor` instance that displays and allows editing of the number value of the specified spinner. The string argument specifies the format to use to display the number. See the API documentation for [DecimalFormat](http://download.oracle.com/javase/7/docs/api/java/text/DecimalFormat.html) for information about decimal format strings. |
> | [JSpinner.DateEditor(JSpinner, String)](http://download.oracle.com/javase/7/docs/api/javax/swing/JSpinner.DateEditor.html#JSpinner.DateEditor(javax.swing.JSpinner, java.lang.String)) | Creates a `JSpinner.DateEditor` instance that displays and allows editing of the `Date` value of the specified spinner. The string argument specifies the format to use to display the date. See the API documentation for [SimpleDateFormat](http://download.oracle.com/javase/7/docs/api/java/text/SimpleDateFormat.html) for information about date format strings. |
> | [JFormattedTextField getTextField()](http://download.oracle.com/javase/7/docs/api/javax/swing/JSpinner.DefaultEditor.html#getTextField())  *(defined in `JSpinner.DefaultEditor`)* | Gets the formatted text field that provides the main GUI for this editor. |
>
> **SpinnerListModel Methods**
>
> | Method | Purpose |
> | [void setList(List)](http://download.oracle.com/javase/7/docs/api/javax/swing/SpinnerListModel.html#setList(java.util.List))   [List getList()](http://download.oracle.com/javase/7/docs/api/javax/swing/SpinnerListModel.html#getList()) | Sets or gets the `List` that defines the sequence for this model. |
>
> **SpinnerDateModel Methods**
>
> | Method | Purpose |
> ||  |  |
> | --- | --- |
> | [void setValue(Object)](http://download.oracle.com/javase/7/docs/api/javax/swing/SpinnerDateModel.html#setValue(java.lang.Object))   [Date getDate()](http://download.oracle.com/javase/7/docs/api/javax/swing/SpinnerDateModel.html#getDate())   [Object getValue()](http://download.oracle.com/javase/7/docs/api/javax/swing/SpinnerDateModel.html#getValue()) | Sets or gets the current `Date` for this sequence. |
> | [void setStart(Comparable)](http://download.oracle.com/javase/7/docs/api/javax/swing/SpinnerDateModel.html#setStart(java.lang.Comparable))   [Comparable getStart()](http://download.oracle.com/javase/7/docs/api/javax/swing/SpinnerDateModel.html#getStart()) | Sets or gets the first `Date` in this sequence. Use `null` to specify that the spinner has no lower limit. |
> | [void setEnd(Comparable)](http://download.oracle.com/javase/7/docs/api/javax/swing/SpinnerDateModel.html#setEnd(java.lang.Comparable))   [Comparable getEnd()](http://download.oracle.com/javase/7/docs/api/javax/swing/SpinnerDateModel.html#getEnd()) | Sets or gets the last `Date` in this sequence. Use `null` to specify that the spinner has no upper limit. |
> | [void setCalendarField(int)](http://download.oracle.com/javase/7/docs/api/javax/swing/SpinnerDateModel.html#setCalendarField(int))   [int getCalendarField()](http://download.oracle.com/javase/7/docs/api/javax/swing/SpinnerDateModel.html#getCalendarField()) | Sets or gets the size of the date value increment used by the `getNextValue` and `getPreviousValue` methods. This property is *not* used when the user explicitly increases or decreases the value; instead, the selected part of the formatted text field is incremented or decremented. The specified parameter must be one of the following constants, defined in `Calendar`: `ERA`, `YEAR`, `MONTH`, `WEEK_OF_YEAR`, `WEEK_OF_MONTH`, `DAY_OF_MONTH`, `DAY_OF_YEAR`, `DAY_OF_WEEK`, `DAY_OF_WEEK_IN_MONTH`, `AM_PM`, `HOUR_OF_DAY`, `MINUTE`, `SECOND`, `MILLISECOND`. |
>
> **SpinnerNumberModel Methods**
>
> | Method | Purpose |
> ||  |  |
> | --- | --- |
> | [void setValue(Object)](http://download.oracle.com/javase/7/docs/api/javax/swing/SpinnerNumberModel.html#setValue(java.lang.Object))   [Number getNumber()](http://download.oracle.com/javase/7/docs/api/javax/swing/SpinnerNumberModel.html#getNumber()) | Sets or gets the current value for this sequence. |
> | [void setMaximum(Comparable)](http://download.oracle.com/javase/7/docs/api/javax/swing/SpinnerNumberModel.html#setMaximum(java.lang.Comparable))   [Comparable getMaximum()](http://download.oracle.com/javase/7/docs/api/javax/swing/SpinnerNumberModel.html#getMaximum()) | Sets or gets the upper bound for numbers in this sequence. If the maximum is `null`, there is no upper bound. |
> | [void setMinimum(Comparable)](http://download.oracle.com/javase/7/docs/api/javax/swing/SpinnerNumberModel.html#setMinimum(java.lang.Comparable))   [Comparable getMinimum()](http://download.oracle.com/javase/7/docs/api/javax/swing/SpinnerNumberModel.html#getMinimum()) | Sets or gets the lower bound for numbers in this sequence. If the minimum is `null`, there is no lower bound. |
> | [void setStepSize(Number)](http://download.oracle.com/javase/7/docs/api/javax/swing/SpinnerNumberModel.html#setStepSize(java.lang.Number))   [Number getStepSize()](http://download.oracle.com/javase/7/docs/api/javax/swing/SpinnerNumberModel.html#getStepSize()) | Sets or gets the increment used by `getNextValue` and `getPreviousValue` methods. |

### Examples That Use Spinners

> This table lists examples that use spinners
> and points to where those examples are described.
>
> | Example | Where Described | Notes |
> | --- | --- | --- |
> | [`SpinnerDemo`](../examples/components/index.html#SpinnerDemo) | This section | Uses all three standard spinner model classes. Contains the code to use a custom spinner model, but the code is turned off by default. |
> | [`SpinnerDemo2`](../examples/components/index.html#SpinnerDemo2) | This section | A `SpinnerDemo` subclass that uses the custom spinner model for its Months spinner. |
> | [`SpinnerDemo3`](../examples/components/index.html#SpinnerDemo3) | This section | Based on SpinnerDemo, this application shows how to listen for changes in a spinner's value. |
> | [`SpinnerDemo4`](../examples/components/index.html#SpinnerDemo4) | This section | Implements a custom model and a custom editor for a spinner that displays shades of gray. |

[« Previous](slider.html)
•
[Trail](../TOC.html)
•
[Next »](splitpane.html)

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

**Previous page:** How to Use Sliders
  
**Next page:** How to Use Split Panes




A browser with JavaScript enabled is required for this page to operate properly.