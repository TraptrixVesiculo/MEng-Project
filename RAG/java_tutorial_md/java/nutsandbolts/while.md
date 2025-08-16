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

The while and do-while Statements

[The for Statement](for.html)

[Branching Statements](branch.html)

[Summary of Control Flow Statements](flowsummary.html)

[Questions and Exercises](QandE/questions_flow.html)

[Home Page](../../index.html)
>
[Learning the Java Language](../index.html)
>
[Language Basics](index.html)

[« Previous](switch.html) • [Trail](../TOC.html) • [Next »](for.html)

# The while and do-while Statements

The `while` statement continually executes a block of statements
while a particular condition is `true`.
Its syntax can be expressed as:

```

while (expression) {
     statement(s)
}

```

The `while` statement evaluates *expression*, which must return a
`boolean` value. If the expression evaluates to `true`, the `while`
statement executes the *statement*(s) in the `while` block. The `while`
statement continues testing the expression and executing its block until the expression
evaluates to `false`. Using the `while` statement to print the values
from 1 through 10 can be accomplished as in the following
[`WhileDemo`](examples/WhileDemo.java)
program:

```


class WhileDemo {
     public static void main(String[] args){
          int count = 1;
          while (count < 11) {
               System.out.println("Count is: " + count);
               count++;
          }
     }
}

```

You can implement an infinite loop using the `while` statement
as follows:

```

while (true){
    // your code goes here
}

```

The Java programming language also provides a `do-while`
statement, which can be expressed as follows:

```

do {
     statement(s)
} while (expression);

```

The difference between `do-while` and `while` is
that `do-while` evaluates its expression at the bottom of the loop
instead of the top.
Therefore, the statements within the `do` block are always executed
at least once, as shown in the following
[`DoWhileDemo`](examples/DoWhileDemo.java)
program:

```


class DoWhileDemo {
     public static void main(String[] args){
          int count = 1;
          do {
               System.out.println("Count is: " + count);
               count++;
          } while (count <= 11);
     }
}

```

[« Previous](switch.html)
•
[Trail](../TOC.html)
•
[Next »](for.html)

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

**Previous page:** The switch Statement
  
**Next page:** The for Statement




A browser with JavaScript enabled is required for this page to operate properly.