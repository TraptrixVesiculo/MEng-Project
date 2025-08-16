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

How to Use Formatted Text Fields

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

[How to Use Spinners](spinner.html)

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

[« Previous](filechooser.html) • [Trail](../TOC.html) • [Next »](frame.html)

# How to Use Formatted Text Fields

Formatted text fields provide a way for developers to specify
the valid set of characters that can be typed in a text field.
Specifically, the
[`JFormattedTextField`](http://download.oracle.com/javase/7/docs/api/javax/swing/JFormattedTextField.html) class adds a *formatter* and an object *value*
to the features inherited from the `JTextField` class.
The formatter translates
the field's value into the text it displays,
and the text into the field's value.

Using the formatters that Swing provides,
you can set up formatted text fields
to type dates and numbers
in localized formats.
Another kind of formatter
enables you to use a character mask
to specify the set of characters
that can be typed at each position in the field.
For example, you can specify a mask
for typing phone numbers in a particular format,
such as (XX) X-XX-XX-XX-XX.

If the possible values of a formatted text field have an
obvious order,
use a [spinner](spinner.html) instead.
A spinner uses a formatted text field
by default,
but adds two buttons that enable the user
to choose a value in a sequence.

Another alternative or adjunct to using a formatted text field
is installing an
[input verifier](../misc/focus.html#inputVerification) on the field.
A component's input verifier is called
when the component nearly loses the keyboard focus.
The input verifier enables you to
check whether the value of the component is valid
and optionally change it or
stop the focus from being transferred.

This GUI uses formatted text fields
to display numbers in four different formats.

![A snapshot of FormattedTextFieldDemo](../../figures/uiswing/components/FormattedTextFieldDemoMetal.png)

---

**Try this:**

1. Click the Launch button
   to run FormattedTextFieldDemo using
   [Java™ Web Start](http://java.sun.com/products/javawebstart/index.jsp ) 
   ([download JDK 6](http://java.sun.com/javase/downloads/index.jsp)).
   Alternatively, to compile and run the example yourself,
   consult the [example index](../examples/components/index.html#FormattedTextFieldDemo).

[![Launches the FormattedTextFieldDemo Application](../../images/jws-launch-button.png)](http://download.oracle.com/javase/tutorialJWS/uiswing/components/ex6/FormattedTextFieldDemo.jnlp)

2. Experiment with different loan amounts, annual percentage rates (APRs),
   and loan lengths.
     
   Note that as long as the text you type is valid,
   the Month Payment field is updated
   when you press Enter or move the focus
   out of the field that you are editing.- Type invalid text such as "abcd" in the Loan Amount field
     and then press Enter.
       
     The Month Payment field remains the same.
     When you move the focus from the Loan Amount field,
     the text reverts to the field's last valid value.- Type marginally valid text such as "2000abcd" in the Loan Amount field
       and press Enter.
         
       The Monthly Payment field is updated,
       though the Loan Amount field still displays `2000abcd`.
       When you move the focus from the Loan Amount field,
       the text it displays is updated
       to a neatly formatted version of its value,
       for example, "2,000".

---

You can find the entire code for this program in
[`FormattedTextFieldDemo.java`](../examples/components/FormattedTextFieldDemoProject/src/components/FormattedTextFieldDemo.java).
This code creates the first field.

```

amountField = new JFormattedTextField(amountFormat);
amountField.setValue(new Double(amount));
amountField.setColumns(10);
amountField.addPropertyChangeListener("value", this);
...
amountFormat = NumberFormat.getNumberInstance();

```

The constructor used to create the `amountField` object
takes a `java.text.Format` argument.
The `Format` object is used by the field's formatter
to translate the field's value to text and the text to the field's value.

The remaining code
sets up the `amountField` object.
The `setValue` method sets the field's
value property to a floating-point number
represented as a `Double` object.
The `setColumns` method,
inherited from the `JTextField` class,
hints about the preferred size of the field.
The call to the `addPropertyChangeListener` method
registers a listener
for the value property of the field,
so the program can update the Monthly Payment field
whenever the user changes the loan amount.

The rest of this section covers the following topics:

* [Creating and Initializing Formatted Text Fields](#constructors)* [Setting and Getting the Field's Value](#value)* [Specifying Formats](#format)* [Using MaskFormatter](#maskformatter)* [Specifying Formatters and Using Formatter Factories](#factory)

This section does not explain the API inherited from
the `JTextField` class.
That API is described in
[How to Use Text Fields](textfield.html).

### Creating and Initializing Formatted Text Fields

> The following code creates and initializes the remaining three fields
> in the `FormattedTextFieldDemo` example.
>
> ```
>
> rateField = new JFormattedTextField(percentFormat);
> rateField.setValue(new Double(rate));
> rateField.setColumns(10);
> rateField.addPropertyChangeListener("value", this);
>
> numPeriodsField = new JFormattedTextField();
> numPeriodsField.setValue(new Integer(numPeriods));
> numPeriodsField.setColumns(10);
> numPeriodsField.addPropertyChangeListener("value", this);
>
> paymentField = new JFormattedTextField(paymentFormat);
> paymentField.setValue(new Double(payment));
> paymentField.setColumns(10);
> paymentField.setEditable(false);
> paymentField.setForeground(Color.red);
>
> ...
> percentFormat = NumberFormat.getNumberInstance();
> percentFormat.setMinimumFractionDigits(2);
>
> paymentFormat = NumberFormat.getCurrencyInstance();
>
> ```
>
> The code for setting up the `rateField` object
> is almost identical to the code listed previously for other fields.
> The only difference is that the format is slightly different,
> thanks to the code `percentFormat.setMinimumFractionDigits(2)`.
>
> The code
> that creates the `numPeriodsField` object
> does not explicitly set a format or formatter.
> Instead, it sets the value to an `Integer`
> and enables the field to use the default formatter for `Integer` objects.
> The code did not do this in the previous two fields
> because the default formatter is not being used
> for `Double` objects.
> The result was not what was needed.
> How to specify formats and formatters is covered
> later in this section.
>
> The payment field is different from the
> other fields because it is uneditable,
> uses a different color for its text,
> and does not have a property change listener.
> Otherwise, it is identical
> to the other fields.
> We could have chosen to use a
> [text field](textfield.html) or
> [label](label.html) instead.
> Whatever the component,
> we could still use the `paymentFormat` method to parse the
> payment amount into the text to be displayed.

### Setting and Getting the Field's Value

> Keep the following in mind
> when using a formatted text field:
> > ---
> >
> > **A formatted text field's *text*
> > and its *value*
> > are two different properties,
> > and the value often lags behind the text.**
> >
> >
> > ---
>
> The *text* property is defined by the `JTextField` class.
> This property always reflects what the field displays.
> The *value* property, defined by the `JFormattedTextField` class,
> might not reflect the latest text displayed in the field.
> While the user is typing,
> the text property changes,
> but the value property does not change
> until the changes are *committed*.
>
> To be more precise,
> the value of a formatted text field can be set
> by using either the `setValue` method
> or the `commitEdit` method.
> The `setValue` method sets the value
> to the specified argument.
> The argument can technically be any `Object`,
> but the formatter needs to be able to
> convert it into a string.
> Otherwise, the text field does not display any substantive information.
>
> The `commitEdit` method
> sets the value to whatever object
> the formatter determines is represented by the field's text.
> The `commitEdit` method is
> automatically called when either of the following happens:
>
> * When the user presses Enter while the field has the focus.* By default, when the field loses the focus,
>     for example, when the user presses the Tab key to change the focus
>     to another component.
>     You can use the `setFocusLostBehavior` method
>     to specify a different outcome
>     when the field loses the focus.
>
> ---
>
> **Note:** Some formatters might update the value constantly,
> rendering the loss of focus meaningless,
> as the value is always the same as what the text specifies.
>
> ---
>
> When you set the value of a formatted text field,
> the field's text is updated to reflect the value.
> Exactly how the value is represented as text
> depends on the field's formatter.
>
> Note that although the `JFormattedTextField` class
> inherits the `setText` method from
> the `JTextField` class,
> you do not usually call the `setText` method on a formatted text field.
> If you do,
> the field's display changes accordingly
> but the value is not updated
> (unless the field's formatter updates it constantly).
>
> To obtain a formatted text field's current value,
> use the `getValue` method.
> If necessary, you can ensure that the value reflects the text
> by calling the `commitEdit` method
> before `getValue`.
> Because the `getValue` method returns an `Object`,
> you need to cast it to the type used for your field's value.
> For example:
>
> ```
>
> Date enteredDate = (Date)dateField.getValue();
>
> ```
>
> To detect changes in a formatted text field's value,
> you can register a property change listener
> on the formatted text field
> to listen for changes to the "value" property.
> The property change listener is taken
> from the `FormattedTextFieldDemo` example:
>
> ```
>
> //The property change listener is registered on each
> //field using code like this:
> //    someField.addPropertyChangeListener("value", this);
>
> /** Called when a field's "value" property changes. */
> public void propertyChange(PropertyChangeEvent e) {
>     Object source = e.getSource();
>     if (source == amountField) {
>         amount = ((Number)amountField.getValue()).doubleValue();
>     } else if (source == rateField) {
>         rate = ((Number)rateField.getValue()).doubleValue();
>     } else if (source == numPeriodsField) {
>         numPeriods = ((Number)numPeriodsField.getValue()).intValue();
>     }
>
>     double payment = computePayment(amount, rate, numPeriods);
>     paymentField.setValue(new Double(payment));
> }
>
> ```

### Specifying Formats

> The
> [`Format`](http://download.oracle.com/javase/7/docs/api/java/text/Format.html) class provides a way to format
> locale-sensitive information such as dates and numbers.
> Formatters that descend from the
> [`InternationalFormatter`](http://download.oracle.com/javase/7/docs/api/javax/swing/text/InternationalFormatter.html) class, such as the
> [`DateFormatter`](http://download.oracle.com/javase/7/docs/api/javax/swing/text/DateFormatter.html) and
> [`NumberFormatter`](http://download.oracle.com/javase/7/docs/api/javax/swing/text/NumberFormatter.html) classes, use `Format` objects
> to translate between the field's text and value.
> You can obtain a `Format` object
> by calling one of the factory methods in the
> [`DateFormat`](http://download.oracle.com/javase/7/docs/api/java/text/DateFormat.html) or
> [`NumberFormat`](http://download.oracle.com/javase/7/docs/api/java/text/NumberFormat.html) classes, or by using one of the
> [`SimpleDateFormat`](http://download.oracle.com/javase/7/docs/api/java/text/SimpleDateFormat.html) constructors.
>
> ---
>
> **Note:** A third commonly used formatter class,
> `MaskFormatter`,
> does not descend from the `InternationalFormatter` class
> and does not use formats.
> The `MaskFormatter` is discussed in
> [Using MaskFormatter](#maskformatter).
>
> ---
>
> You can customize certain format aspects
> when you create the `Format` object,
> and others through a format-specific API.
> For example,
> [`DecimalFormat`](http://download.oracle.com/javase/7/docs/api/java/text/DecimalFormat.html) objects,
> which inherit from `NumberFormat`
> and are often returned by its factory methods,
> can be customized by using the
> `setMaximumFractionDigits` and
> `setNegativePrefix` methods.
> For information about using `Format` objects,
> see the
> [Formatting](../../i18n/format/index.html) lesson of the Internationalization trail.
>
> The easiest way to associate a customized format
> with a formatted text field
> is to create the field by using
> the `JFormattedTextField` constructor
> that takes a `Format` as an argument.
> You can see this association in the previous code examples that create
> `amountField` and `rateField` objects.

### Using MaskFormatter
> The
> [`MaskFormatter`](http://download.oracle.com/javase/7/docs/api/javax/swing/text/MaskFormatter.html) class implements a formatter
> that specifies exactly which characters are
> valid in each position of the field's text.
> For example, the following code creates a `MaskFormatter`
> that lets the user to type a five-digit zip code:
>
> ```
>
> zipField = new JFormattedTextField(
>                     createFormatter("#####"));
> ...
> protected MaskFormatter createFormatter(String s) {
>     MaskFormatter formatter = null;
>     try {
>         formatter = new MaskFormatter(s);
>     } catch (java.text.ParseException exc) {
>         System.err.println("formatter is bad: " + exc.getMessage());
>         System.exit(-1);
>     }
>     return formatter;
> }
>
> ```
>
> You can try out the results of the preceding code by
> running `TextInputDemo`.
> Click the Launch button
> to run TextInputDemo using
> [Java™ Web Start](http://java.sun.com/products/javawebstart/index.jsp ) 
> ([download JDK 6](http://java.sun.com/javase/downloads/index.jsp)).
> Alternatively, to compile and run the example yourself,
> consult the [example index](../examples/components/index.html#TextInputDemo).
>
> [![Launches the TextInputDemo Application](../../images/jws-launch-button.png)](http://download.oracle.com/javase/tutorialJWS/uiswing/components/ex6/TextInputDemo.jnlp)
>
> The program's GUI is displayed.
>
> ![A snapshot of TextInputDemo](../../figures/uiswing/components/TextInputDemoMetal.png)
>
> The following table shows
> the characters that you can use in the formatting mask:
>
> | Character | Description |
> | --- | --- |
> | # | Any valid number (`Character.isDigit`). |
> | '   *(single quote)* | Escape character, used to escape any of the special formatting characters. |
> | U | Any character (`Character.isLetter`). All lowercase letters are mapped to uppercase. |
> | L | Any character (`Character.isLetter`). All uppercase letters are mapped to lowercase. |
> | A | Any character or number (`Character.isLetter` or `Character.isDigit`). |
> | ? | Any character (`Character.isLetter`). |
> | \* | Anything. |
> | H | Any hex character (0-9, a-f or A-F). |

### Specifying Formatters and Using Formatter Factories

> When specifying formatters,
> keep in mind that each formatter object
> can be used by at most one
> formatted text field at a time.
> Each field should have at least one formatter associated with it,
> of which exactly one is used at any time.
>
> You can specify the formatters to be used by a formatted text field
> in several ways:
>
> * **Use the `JFormattedTextField` constructor
>   that takes a `Format` argument.**
>     
>   A formatter for the field is automatically created
>   that uses the specified format.
>
>   * **Use the `JFormattedTextField` constructor
>     that takes a `JFormattedTextField.AbstractFormatter` argument.**
>       
>     The specified formatter is used for the field.
>
>     * **Set the value of a formatted text field
>       that has no format, formatter, or formatter factory specified.**
>         
>       A formatter is assigned to the field by the default formatter factory,
>       using the type of the field's value as a guide.
>       If the value is a `Date`,
>       the formatter is a `DateFormatter`.
>       If the value is a `Number`,
>       the formatter is a `NumberFormatter`.
>       Other types
>       result in an instance of `DefaultFormatter`.
>
>       * **Make the formatted text field use
>         a formatter factory that returns customized formatter objects.**
>           
>         This is the most flexible approach.
>         It is useful when you want to associate
>         more than one formatter with a field
>         or add a new kind of formatter
>         to be used for multiple fields.
>         An example of the former use
>         is a field that
>         interprets the user typing in a certain way
>         but displays the value (when the user is not typing) in another way.
>         An example of the latter use
>         is several fields
>         with custom class values,
>         for example, `PhoneNumber`.
>         You can set up the fields to use a formatter factory
>         that returns specialized formatters for phone numbers.
>
> You can set a field's formatter factory
> either by creating the field using a constructor
> that takes a formatter factory argument,
> or by calling the `setFormatterFactory` method
> on the field.
> To create a formatter factory,
> you can often use an instance of
> [`DefaultFormatterFactory`](http://download.oracle.com/javase/7/docs/api/javax/swing/text/DefaultFormatterFactory.html) class.
> A `DefaultFormatterFactory` object
> enables you to specify the formatters returned
> when a value is being edited, is not being edited,
> or has a null value.
>
> The following figures show an application
> based on the `FormattedTextFieldDemo` example
> that uses formatter factories
> to set multiple editors for the
> Loan Amount and APR fields.
> While the user is editing the Loan Amount,
> the $ character is not used
> so that the user is not forced to type it.
> Similarly, while the user is editing the APR field,
> the % character is not required.
>
> Click the Launch button
> to run FormatterFactoryDemo using
> [Java™ Web Start](http://java.sun.com/products/javawebstart/index.jsp ) 
> ([download JDK 6](http://java.sun.com/javase/downloads/index.jsp)).
> Alternatively, to compile and run the example yourself,
> consult the [example index](../examples/components/index.html#FormatterFactoryDemo).
>
> [![Launches the FormatterFactoryDemo Application](../../images/jws-launch-button.png)](http://download.oracle.com/javase/tutorialJWS/uiswing/components/ex6/FormatterFactoryDemo.jnlp)
>
> ![FormatterFactoryDemo, with amount field being edited](../../figures/uiswing/components/FormatterFactoryDemoMetal.png)
> ![FormatterFactoryDemo, with no custom editors installed](../../figures/uiswing/components/FormatterFactoryDemo2Metal.png)
>
> The following code that creates the formatters
> and sets them up by
> using instances of the `DefaultFormatterFactory` class:
>
> ```
>
> private double rate = .075;  //7.5 %
> ...
> amountField = new JFormattedTextField(
>                     new DefaultFormatterFactory(
>                         new NumberFormatter(amountDisplayFormat),
>                         new NumberFormatter(amountDisplayFormat),
>                         new NumberFormatter(amountEditFormat)));
> ...
> NumberFormatter percentEditFormatter =
>         new NumberFormatter(percentEditFormat) {
>     public String valueToString(Object o)
>           throws ParseException {
>         Number number = (Number)o;
>         if (number != null) {
>             double d = number.doubleValue() * 100.0;
>             number = new Double(d);
>         }
>         return super.valueToString(number);
>     }
>     public Object stringToValue(String s)
>            throws ParseException {
>         Number number = (Number)super.stringToValue(s);
>         if (number != null) {
>             double d = number.doubleValue() / 100.0;
>             number = new Double(d);
>         }
>         return number;
>     }
> };
> rateField = new JFormattedTextField(
>                      new DefaultFormatterFactory(
>                         new NumberFormatter(percentDisplayFormat),
>                         new NumberFormatter(percentDisplayFormat),
>                         percentEditFormatter));
> ...
> amountDisplayFormat = NumberFormat.getCurrencyInstance();
> amountDisplayFormat.setMinimumFractionDigits(0);
> amountEditFormat = NumberFormat.getNumberInstance();
>
> percentDisplayFormat = NumberFormat.getPercentInstance();
> percentDisplayFormat.setMinimumFractionDigits(2);
> percentEditFormat = NumberFormat.getNumberInstance();
> percentEditFormat.setMinimumFractionDigits(2);
>
> ```
>
> The boldface code highlights the calls to
> `DefaultFormatterFactory` constructors.
> The first argument to the constructor specifies the default formatter
> to use for the formatted text field.
> The second argument specifies the display formatter,
> which is used
> when the field does not have the focus.
> The third argument specifies the edit formatter,
> which is used when the field has the focus.
> The code does not use a fourth argument,
> but if it did,
> the fourth argument would specify the null formatter,
> which is used when the field's value is null.
> Because no null formatter is specified,
> the default formatter is used when the value is null.
>
> The code customizes the formatter
> that uses `percentEditFormat`
> by creating a subclass of the `NumberFormatter` class.
> This subclass overrides the `valueToString`
> and `stringToValue` methods
> of `NumberFormatter`
> so that they convert the displayed number
> to the value actually used in calculations,
> and convert the value to a number.
> Specifically, the displayed number
> is 100 times the actual value.
> The reason is that the percent format
> used by the display formatter
> automatically displays the text
> as 100 times the value,
> so the corresponding editor formatter must display the text at the same value.
> The `FormattedTextFieldDemo` example does not need
> to take care of this conversion
> because this demo uses only one format for both display and editing.
>
> You can find the code for the entire program in
> [`FormatterFactoryDemo.java`](../examples/components/FormatterFactoryDemoProject/src/components/FormatterFactoryDemo.java).

### Formatted Text Field API

> The following tables list some of the commonly used APIs
> for using formatted text fields.
>
> * [Classes Related to Formatted Text Fields](#newclassesapi)* [JFormattedTextField Methods](#formattedtextfieldapi)* [DefaultFormatter Options](#defaultformatterapi)
>
> **Classes Related to Formatted Text Fields**
>
> | Class or Interface | Purpose |
> | [JFormattedTextField](http://download.oracle.com/javase/7/docs/api/javax/swing/JFormattedTextField.html) | Subclass of `JTextField` that supports formatting arbitrary values. |
> | [JFormattedTextField.AbstractFormatter](http://download.oracle.com/javase/7/docs/api/javax/swing/JFormattedTextField.AbstractFormatter.html) The superclass of all formatters for `JFormattedTextField`. A formatter enforces editing policies and navigation policies, handles string-to-object conversions, and manipulates the `JFormattedTextField` as necessary to enforce the desired policy. | |
> | [JFormattedTextField.AbstractFormatterFactory](http://download.oracle.com/javase/7/docs/api/javax/swing/JFormattedTextField.AbstractFormatterFactory.html) | The superclass of all formatter factories. Each `JFormattedTextField` uses a formatter factory to obtain the formatter that best corresponds to the text field's state. |
> | [DefaultFormatterFactory](http://download.oracle.com/javase/7/docs/api/javax/swing/text/DefaultFormatterFactory.html) | The formatter factory normally used. Provides formatters based on details such as the passed-in parameters and focus state. |
> | [DefaultFormatter](http://download.oracle.com/javase/7/docs/api/javax/swing/text/DefaultFormatter.html) | Subclass of `JFormattedTextField.AbstractFormatter` that formats arbitrary objects by using the `toString` method. |
> | [MaskFormatter](http://download.oracle.com/javase/7/docs/api/javax/swing/text/MaskFormatter.html) | Subclass of `DefaultFormatter` that formats and edits strings using a specified character mask. (For example, seven-digit phone numbers can be specified by using "###-####".) |
> | [InternationalFormatter](http://download.oracle.com/javase/7/docs/api/javax/swing/text/InternationalFormatter.html) | Subclass of `DefaultFormatter` that uses an instance of `java.text.Format` to handle conversion to and from a `String`. |
> | [NumberFormatter](http://download.oracle.com/javase/7/docs/api/javax/swing/text/NumberFormatter.html) | Subclass of `InternationalFormatter` that supports number formats by using an instance of `NumberFormat`. |
> | [DateFormatter](http://download.oracle.com/javase/7/docs/api/javax/swing/text/DateFormatter.html) | Subclass of `InternationalFormatter` that supports date formats by using an instance of `DateFormat`. |
>
> **JFormattedTextField Methods**
>
> | Method or Constructor | Purpose |
> | [JFormattedTextField()](http://download.oracle.com/javase/7/docs/api/javax/swing/JFormattedTextField.html#JFormattedTextField())   [JFormattedTextField(Object)](http://download.oracle.com/javase/7/docs/api/javax/swing/JFormattedTextField.html#JFormattedTextField(java.lang.Object))   [JFormattedTextField(Format)](http://download.oracle.com/javase/7/docs/api/javax/swing/JFormattedTextField.html#JFormattedTextField(java.text.Format))   [JFormattedTextField(AbstractFormatter)](http://download.oracle.com/javase/7/docs/api/javax/swing/JFormattedTextField.html#JFormattedTextField(javax.swing.JFormattedTextField.AbstractFormatter))   [JFormattedTextField(AbstractFormatterFactory)](http://download.oracle.com/javase/7/docs/api/javax/swing/JFormattedTextField.html#JFormattedTextField(javax.swing.JFormattedTextField.AbstractFormatterFactory))   [JFormattedTextField(AbstractFormatterFactory, Object)](http://download.oracle.com/javase/7/docs/api/javax/swing/JFormattedTextField.html#JFormattedTextField(javax.swing.JFormattedTextField.AbstractFormatterFactory, java.lang.Object)) | Creates a new formatted text field. The `Object` argument, if present, specifies the initial value of the field and causes an appropriate formatter factory to be created. The `Format` or `AbstractFormatter` argument specifies the format or formatter to be used for the field, and causes an appropriate formatter factory to be created. The `AbstractFormatterFactory` argument specifies the formatter factory to be used, which determines which formatters are used for the field. |
> | [void setValue(Object)](http://download.oracle.com/javase/7/docs/api/javax/swing/JFormattedTextField.html#setValue(java.lang.Object))   [Object getValue()](http://download.oracle.com/javase/7/docs/api/javax/swing/JFormattedTextField.html#getValue()) | Sets or obtains the value of the formatted text field. You must cast the return type based on how the `JFormattedTextField` has been configured. If the formatter has not been set yet, calling `setValue` sets the formatter to one returned by the field's formatter factory. |
> | [void setFormatterFactory(AbstractFormatterFactory)](http://download.oracle.com/javase/7/docs/api/javax/swing/JFormattedTextField.html#setFormatterFactory(javax.swing.JFormattedTextField.AbstractFormatterFactory)) | Sets the object that determines the formatters used for the formatted text field. The object is often an instance of the `DefaultFormatterFactory` class. |
> | [AbstractFormatter getFormatter()](http://download.oracle.com/javase/7/docs/api/javax/swing/JFormattedTextField.html#getFormatter()) | Obtains the formatter of the formatted text field. The formatter is often an instance of the `DefaultFormatter` class. |
> | [void setFocusLostBehavior(int)](http://download.oracle.com/javase/7/docs/api/javax/swing/JFormattedTextField.html#setFocusLostBehavior(int)) | Specifies the outcome of a field losing the focus. Possible values are defined in `JFormattedTextField` as `COMMIT_OR_REVERT` (the default), `COMMIT` (commit if valid, otherwise leave everything the same), `PERSIST` (do nothing), and `REVERT` (change the text to reflect the value). |
> | [void commitEdit()](http://download.oracle.com/javase/7/docs/api/javax/swing/JFormattedTextField.html#commitEdit()) | Sets the value to the object represented by the field's text, as determined by the field's formatter. If the text is invalid, the value remains the same and a [`ParseException`](http://download.oracle.com/javase/7/docs/api/java/text/ParseException.html) is thrown. |
> | [boolean isEditValid()](http://download.oracle.com/javase/7/docs/api/javax/swing/JFormattedTextField.html#isEditValid()) | Returns true if the formatter considers the current text to be valid, as determined by the field's formatter. |
>
> **DefaultFormatter Options**
>
> | Method | Purpose |
> | [void setCommitsOnValidEdit(boolean)](http://download.oracle.com/javase/7/docs/api/javax/swing/text/DefaultFormatter.html#setCommitsOnValidEdit(boolean))   [boolean getCommitsOnValidEdit()](http://download.oracle.com/javase/7/docs/api/javax/swing/text/DefaultFormatter.html#getCommitsOnValidEdit()) | Sets or obtains values when edits are pushed back to the `JFormattedTextField`. If `true`, `commitEdit` is called after every valid edit. This property is `false` by default. |
> | [void setOverwriteMode(boolean)](http://download.oracle.com/javase/7/docs/api/javax/swing/text/DefaultFormatter.html#setOverwriteMode(boolean))   [boolean getOverwriteMode()](http://download.oracle.com/javase/7/docs/api/javax/swing/text/DefaultFormatter.html#getOverwriteMode()) | Sets or obtains the behavior when inserting characters. If `true`, new characters overwrite existing characters in the model as they are inserted. The default value of this property is `true` in `DefaultFormatter` (and thus in `MaskFormatter`) and `false` in `InternationalFormatter` (and thus in `DateFormatter` and `NumberFormatter`). |
> | [void setAllowsInvalid(boolean)](http://download.oracle.com/javase/7/docs/api/javax/swing/text/DefaultFormatter.html#setAllowsInvalid(boolean))   [boolean getAllowsInvalid()](http://download.oracle.com/javase/7/docs/api/javax/swing/text/DefaultFormatter.html#getAllowsInvalid()) | Sets or interprets whether the value being edited is allowed to be invalid for a length of time. It is often convenient to enable the user to type invalid values until the `commitEdit` method is attempted. `DefaultFormatter` initializes this property to `true`. Of the standard Swing formatters, only `MaskFormatter` sets this property to `false`. |

### Examples That Use Formatted Text Fields

> This table lists examples that use formatted text fields
> and points to where those examples are described.
>
> | Example | Where Described | Notes |
> | --- | --- | --- |
> | [FormattedTextFieldDemo](../examples/components/index.html#FormattedTextFieldDemo) | This section | Uses four formatted text fields. |
> | [SpinnerDemo](../examples/components/index.html#SpinnerDemo) | [How to Use Spinners](spinner.html) | Customizes the appearance of the formatted text fields used by two spinners. |
> | [Converter](../examples/components/index.html#Converter) | [Using Models](model.html) | Each `ConversionPanel` pairs a formatted text field with a slider. |
> | [TextInputDemo](../examples/components/index.html#TextInputDemo) | This section | Shows how to use text fields, spinners, and formatted text fields together, and demonstrates how to use `MaskFormatter`. Includes code for selecting the text of the field that has just received the focus. |
> | [FormatterFactoryDemo](../examples/components/index.html#FormatterFactoryDemo) | This section | A variation on FormattedTextFieldDemo that uses formatter factories to specify multiple formatters for two formatted text fields. |

[« Previous](filechooser.html)
•
[Trail](../TOC.html)
•
[Next »](frame.html)

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

**Previous page:** How to Use File Choosers
  
**Next page:** How to Make Frames (Main Windows)




A browser with JavaScript enabled is required for this page to operate properly.