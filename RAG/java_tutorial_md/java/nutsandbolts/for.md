[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** Learning the Java Language
  
**Lesson:** Language Basics
  
**Section:** Control Flow Statements

[Language Basics](index.html)

[Variables](variables.html)

[Primitive Data Types](datatypes.html)

[Arrays](arrays.html)

[Summary of Variables](variablesummary.html)

[Questions and Exercises](QandE/questions_variables.html)

[Operators](operators.html)

[Assignment, Arithmetic, and Unary Operators](op1.html)

[Equality, Relational, and Conditional Operators](op2.html)

[Bitwise and Bit Shift Operators](op3.html)

[Summary of Operators](opsummary.html)

[Questions and Exercises](QandE/questions_operators.html)

[Expressions, Statements, and Blocks](expressions.html)

[Questions and Exercises](QandE/questions_expressions.html)

[Control Flow Statements](flow.html)

[The if-then and if-then-else Statements](if.html)

[The switch Statement](switch.html)

[The while and do-while Statements](while.html)

The for Statement

[Branching Statements](branch.html)

[Summary of Control Flow Statements](flowsummary.html)

[Questions and Exercises](QandE/questions_flow.html)

[Home Page](../../index.html)
>
[Learning the Java Language](../index.html)
>
[Language Basics](index.html)

[« Previous](while.html) • [Trail](../TOC.html) • [Next »](branch.html)

# The for Statement

The `for` statement provides a compact way to iterate over a range of values. Programmers often
refer to it as the "for loop" because of the way in which it repeatedly loops until a particular
condition is satisfied. The general form of the `for` statement can be expressed as follows:

```

for (initialization; termination; increment) {
    statement(s)
}

```

When using this version of the `for` statement, keep in mind that:

* The *initialization* expression initializes the
  loop; it's executed once, as the loop begins.* When the *termination* expression evaluates to `false`, the loop terminates.* The *increment* expression is invoked after each
      iteration through the loop; it is perfectly acceptable for this expression
      to increment *or* decrement a value.

The following program,
[`ForDemo`](examples/ForDemo.java), uses the general form of the `for` statement to
print the numbers 1 through 10 to standard output:

```


class ForDemo {
     public static void main(String[] args){
          for(int i=1; i<11; i++){
               System.out.println("Count is: " + i);
          }
     }
}

```

The output of this program is:

```

Count is: 1
Count is: 2
Count is: 3
Count is: 4
Count is: 5
Count is: 6
Count is: 7
Count is: 8
Count is: 9
Count is: 10

```

Notice how the code declares a variable within the initialization
expression. The scope of this variable extends from its
declaration to the end of the block governed by the `for` statement, so it can be
used in the termination and increment expressions as well. If the variable that controls
a `for` statement is not needed outside of the loop, it's best to declare the
variable in the initialization expression. The names `i`, `j`, and `k`
are often used to control `for` loops; declaring them within the
initialization expression limits their life span and reduces errors.

The three expressions of the `for` loop are optional; an infinite
loop can be created as follows:

```

for ( ; ; ) {    // infinite loop
    
     // your code goes here
}

```

The `for` statement also has another form designed for iteration through
[Collections](../../collections/index.html)
and
[arrays](arrays.html)
This form is sometimes referred to as the *enhanced for* statement, and can be used to make
your loops more compact and easy to read. To demonstrate, consider the following array, which holds the numbers 1 through 10:

```

int[] numbers = {1,2,3,4,5,6,7,8,9,10};

```

The following program,
[`EnhancedForDemo`](examples/EnhancedForDemo.java), uses the enhanced `for` to loop through the array:

```


class EnhancedForDemo {
     public static void main(String[] args){
          int[] numbers = {1,2,3,4,5,6,7,8,9,10};
          for (int item : numbers) {
            System.out.println("Count is: " + item);
          }
     }
}

```

In this example, the variable `item` holds the current value from the
numbers array. The output from this program is the same as before:

```

Count is: 1
Count is: 2
Count is: 3
Count is: 4
Count is: 5
Count is: 6
Count is: 7
Count is: 8
Count is: 9
Count is: 10

```

We recommend using this form of the `for` statement instead of
the general form whenever possible.

[« Previous](while.html)
•
[Trail](../TOC.html)
•
[Next »](branch.html)

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

**Previous page:** The while and do-while Statements
  
**Next page:** Branching Statements




A browser with JavaScript enabled is required for this page to operate properly.