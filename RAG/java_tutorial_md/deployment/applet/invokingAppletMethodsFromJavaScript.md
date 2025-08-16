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

Invoking Applet Methods From JavaScript Code

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

[« Previous](invokingJavaScriptFromApplet.html) • [Trail](../TOC.html) • [Next »](manipulatingDOMFromApplet.html)

# Invoking Applet Methods From JavaScript Code

JavaScript code on a web page can interact with Java applets embedded on the page.
JavaScript code can perform operations such as the following:

* Invoke methods on Java objects
* Get and set fields in Java objects
* Get and set Java array elements
* Create new instances of Java objects

The
[LiveConnect Specification](http://java.sun.com/javase/6/webnotes/6u10/plugin2/liveconnect/index.html) describes details about how JavaScript code communicates with Java code.

This topic explores JavaScript code to Java applet communication using the Math applet example.
The `MathApplet` class and supporting `Calculator` class provide a
set of public methods and variables. The JavaScript code on the web page invokes and
evaluates these public members to pass data and retrieve calculated results.

## Math Applet and Related Classes

Here is the source code for the
[`MathApplet`](examples/applet_InvokingAppletMethodsFromJavaScript/src/jstojava/MathApplet.java) class. The `getCalculator` method returns a reference to the `Calculator`
helper class.

```

 
package jstojava;
import java.applet.Applet;

public class MathApplet extends Applet{

    public String userName = null;
         
    public String getGreeting() {
        return "Hello " + userName;
    }
    
    public Calculator getCalculator() {
        return new Calculator();
    } 
}

```

The methods in the
[`Calculator`](examples/applet_InvokingAppletMethodsFromJavaScript/src/jstojava/Calculator.java) class let the user set two values, add numbers, and retrieve the numbers in a range.

```


package jstojava;

public class Calculator {
    private int a = 0;
    private int b = 0; // assume b > a
    
    public void setNums(int numA, int numB) {
        a = numA;
        b = numB;
    }
    
    public int add() {
        return a + b;
    }
    
    public int [] getNumInRange() {    
        int x = a;
        int len = (b - a) + 1;
        int [] range = new int [len];
        for (int i = 0; i < len; i++) {
            range[i]= x++;
            System.out.println("i: " + i + " ; range[i]: " + range[i]);
        }
        return range;
    }
}

```

The `getDate` method of the
[`DateHelper`](examples/applet_InvokingAppletMethodsFromJavaScript/src/jstojava/DateHelper.java) class returns the current date.

```


package jstojava;
import java.util.Date;
import java.text.SimpleDateFormat;

public class DateHelper {
    
    public static String label = null;
        
    public String getDate() {
        return label + " " + new SimpleDateFormat().format(new Date());
    }

}

```

## Deploying the Applet

Deploy the applet in a web page,
[`AppletPage.html`](examples/dist/applet_InvokingAppletMethodsFromJavaScript/AppletPage.html) When deploying the applet, make sure that you specify an id for the applet.
The applet id is used later to obtain a reference to the applet object.

```

<script src="http://www.java.com/js/deployJava.js"></script>
<script>
    <!-- applet id can be used to get a reference to the applet object -->
    var attributes = { id:'mathApplet', code:'jstojava.MathApplet',  width:1, height:1} ;
    var parameters = {jnlp_href: 'math-applet.jnlp'} ;
    deployJava.runApplet(attributes, parameters, '1.6');
</script>

```

Next, add some JavaScript code to the
[`AppletPage.html`](examples/dist/applet_InvokingAppletMethodsFromJavaScript/AppletPage.html) web page. The JavaScript code can use the applet id as a
reference to the applet object and invoke the applet's methods.
In the example shown next, the JavaScript
code sets the applet's public member variables, invokes public methods, and
retrieves a reference
to another object referenced by the applet (`Calculator`).
The JavaScript code is
able to handle primitive, array, and object return types. The JavaScript code can
also invoke methods from classes or objects in other packages using the
`Packages` keyword.

```

...
<script language="javascript">
    		function enterNums(){
    			var numA = prompt('Enter number \'a\'?','0');
    var numB = prompt('Enter number \'b\' (should be greater than number \'a\' ?','1');
    			// set applet's public variable
    mathApplet.userName = "John Doe";

    // invoke public applet method
    var greeting = mathApplet.getGreeting();

    // get another class referenced by applet and invoke its methods
    var calculator = mathApplet.getCalculator();
    calculator.setNums(numA, numB);

    // primitive datatype returned by applet
    var sum = calculator.add();

    // array returned by applet
    var numRange = calculator.getNumInRange();

    // "Packages" keyword; check Java console log for this message
    mathApplet.Packages.java.lang.System.out.println("Testing printing to System.out");

    // Set static field using "Packages" keyword; static methods may be similarly invoked
    mathApplet.Packages.jstojava.DateHelper.label = "Today\'s date is: ";

    // Create an instance of a class and invoke method using "Packages" keyword
    var dateHelper = new mathApplet.Packages.jstojava.DateHelper();
    var dateStr = dateHelper.getDate();

    .....
</script>

```

The Math applet displays the following results on the web page
when the number a = 0 and b = 5:

```

Results of JavaScript to Java Communication

Hello John Doe

a = 0 ; b = 5

Sum: 5

Numbers in range array: [ 0, 1, 2, 3, 4, 5 ]

Today's date is: 1/13/09 10:12 AM // shows current date

```

Open
[`AppletPage.html`](examples/dist/applet_InvokingAppletMethodsFromJavaScript/AppletPage.html) in a browser to view the Math applet.

---

**Note:** If you don't see the applet running, you need to install at least the [Java SE Development Kit (JDK) 6 update 10](http://java.sun.com/javase/downloads/index.jsp) release.

---

---

**Note:** If you don't see the example running, you might need to enable the JavaScript interpreter in your browser so that the Deployment Toolkit script can function properly.

---

Check
[security restrictions](security.html#jsNote) placed on applets invoked by JavaScript code.

[Download source code](examplesIndex.html#InvokingAppletMethodsFromJavaScript) for the *Invoking Applet Methods From JavaScript Code* example to experiment further.

[« Previous](invokingJavaScriptFromApplet.html)
•
[Trail](../TOC.html)
•
[Next »](manipulatingDOMFromApplet.html)

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

**Previous page:** Invoking JavaScript Code From an Applet
  
**Next page:** Manipulating DOM of Applet's Web Page




A browser with JavaScript enabled is required for this page to operate properly.