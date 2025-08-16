[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** Learning the Java Language
  
**Lesson:** Numbers and Strings
  
**Section:** Strings

[Numbers and Strings](index.html)

[Numbers](numbers.html)

[The Numbers Classes](numberclasses.html)

[Formatting Numeric Print Output](numberformat.html)

[Beyond Basic Arithmetic](beyondmath.html)

[Summary of Numbers](numbersummary.html)

[Questions and Exercises](QandE/numbers-questions.html)

[Characters](characters.html)

[Strings](strings.html)

Converting Between Numbers and Strings

[Manipulating Characters in a String](manipstrings.html)

[Comparing Strings and Portions of Strings](comparestrings.html)

[The StringBuilder Class](buffers.html)

[Summary of Characters and Strings](stringsummary.html)

[Questions and Exercises](QandE/characters-questions.html)

[Home Page](../../index.html)
>
[Learning the Java Language](../index.html)
>
[Numbers and Strings](index.html)

[« Previous](strings.html) • [Trail](../TOC.html) • [Next »](manipstrings.html)

# Converting Between Numbers and Strings

### Converting Strings to Numbers

Frequently, a program ends up with numeric data in a string object—a value
entered by the user, for example.

The `Number` subclasses that wrap primitive numeric types (
[`Byte`](http://download.oracle.com/javase/7/docs/api/java/lang/Byte.html),
[`Integer`](http://download.oracle.com/javase/7/docs/api/java/lang/Integer.html),
[`Double`](http://download.oracle.com/javase/7/docs/api/java/lang/Double.html),
[`Float`](http://download.oracle.com/javase/7/docs/api/java/lang/Float.html),
[`Long`](http://download.oracle.com/javase/7/docs/api/java/lang/Long.html), and
[`Short`](http://download.oracle.com/javase/7/docs/api/java/lang/Short.html))
each provide a class method named `valueOf` that converts a string to an object of that type. Here is an example,
[`ValueOfDemo`](examples/ValueOfDemo.java)
, that gets two strings from the command line, converts them to numbers, and performs arithmetic operations on the values:

```


public class ValueOfDemo {
    public static void main(String[] args) {

	    //this program requires two arguments on the command line  
        if (args.length == 2) {
			//convert strings to numbers
            float a = (Float.valueOf(args[0]) ).floatValue();  
            float b = (Float.valueOf(args[1]) ).floatValue();

            //do some arithmetic
            System.out.println("a + b = " + (a + b) );
            System.out.println("a - b = " + (a - b) );
            System.out.println("a * b = " + (a * b) );
            System.out.println("a / b = " + (a / b) );
            System.out.println("a % b = " + (a % b) );
        } else {
           System.out.println("This program requires two command-line arguments.");
        }
    }
}

```

The following is the output from the program when you use `4.5` and `87.2` for the command-line arguments:

```

a + b = 91.7
a - b = -82.7
a * b = 392.4
a / b = 0.0516055
a % b = 4.5

```

---

**Note:** Each of the `Number` subclasses that wrap primitive numeric types also provides a
`parseXXXX()` method (for example, `parseFloat()`) that can be used to
convert strings to primitive numbers. Since a primitive type is returned instead of an object, the
`parseFloat()` method is more direct than the `valueOf()` method. For example, in the
`ValueOfDemo` program, we could use:

```

float a = Float.parseFloat(args[0]);
float b = Float.parseFloat(args[1]);

```

---

### Converting Numbers to Strings

Sometimes you need to convert a number to a string because you need to
operate on the value in its string form. There are several easy ways
to convert a number to a string:

```

int i;
String s1 = "" + i; //Concatenate "i" with an empty string;
                    //conversion is handled for you.

```

or

```

String s2 = String.valueOf(i);  //The valueOf class method.

```

Each of the `Number` subclasses includes a class method, `toString()`,
that will convert its primitive type to a string. For example:

```

int i;
double d;
String s3 = Integer.toString(i); 
String s4 = Double.toString(d); 

```

The
[`ToStringDemo`](examples/ToStringDemo.java) example uses the `toString` method to convert a number to a string.
The program then uses some string methods to compute the number of digits
before and after the decimal point:

```


public class ToStringDemo {
    
    public static void main(String[] args) {
        double d = 858.48;
        String s = Double.toString(d);
        
        int dot = s.indexOf('.');
        
        System.out.println(dot + " digits before decimal point.");
        System.out.println( (s.length() - dot - 1) + 
		" digits after decimal point.");
    }
}

```

The output of this program is:

```

3 digits before decimal point.
2 digits after decimal point.

```

[« Previous](strings.html)
•
[Trail](../TOC.html)
•
[Next »](manipstrings.html)

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

**Previous page:** Strings
  
**Next page:** Manipulating Characters in a String




A browser with JavaScript enabled is required for this page to operate properly.