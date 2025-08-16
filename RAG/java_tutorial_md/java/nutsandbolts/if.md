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

The if-then and if-then-else Statements

[The switch Statement](switch.html)

[The while and do-while Statements](while.html)

[The for Statement](for.html)

[Branching Statements](branch.html)

[Summary of Control Flow Statements](flowsummary.html)

[Questions and Exercises](QandE/questions_flow.html)

[Home Page](../../index.html)
>
[Learning the Java Language](../index.html)
>
[Language Basics](index.html)

[« Previous](flow.html) • [Trail](../TOC.html) • [Next »](switch.html)

# The if-then and if-then-else Statements

### The `if-then` Statement

The `if-then` statement is the most basic of
all the control flow statements. It tells your program to execute a certain
section of code *only if* a particular test evaluates to `true`.
For example, the `Bicycle` class could allow the brakes to
decrease the bicycle's speed *only if* the bicycle is already in motion. One possible
implementation of the `applyBrakes` method could be as follows:

```

void applyBrakes(){
     if (isMoving){  // the "if" clause: bicycle must be moving
          currentSpeed--; // the "then" clause: decrease current speed
     }
}

```

If this test evaluates to `false` (meaning that the bicycle is not in motion),
control jumps to the end of the `if-then` statement.

In addition, the opening and closing braces are optional, provided
that the "then" clause contains only one statement:

```

void applyBrakes(){
     if (isMoving) currentSpeed--; // same as above, but without braces 
}

```

Deciding when to omit the braces is a matter of personal taste.
Omitting them can make the code more brittle. If a second statement
is later added to the "then" clause, a common mistake would be forgetting
to add the newly required braces. The compiler cannot catch this sort
of error; you'll just get the wrong results.

### The `if-then-else` Statement

The `if-then-else` statement provides a secondary path of execution when an
"if" clause evaluates to `false`. You could use an `if-then-else`
statement in the `applyBrakes` method to take some action if the brakes are applied
when the bicycle is not in motion. In this case, the action is to simply print an error message
stating that the bicycle has already stopped.

```

void applyBrakes(){
     if (isMoving) {
          currentSpeed--;
     } else {
          System.err.println("The bicycle has already stopped!");
     } 
}

```

The following program,
[`IfElseDemo`](examples/IfElseDemo.java), assigns a grade based on the
value of a test score: an A for a score of 90% or above, a B for
a score of 80% or above, and so on.

```


class IfElseDemo {
    public static void main(String[] args) {

        int testscore = 76;
        char grade;

        if (testscore >= 90) {
            grade = 'A';
        } else if (testscore >= 80) {
            grade = 'B';
        } else if (testscore >= 70) {
            grade = 'C';
        } else if (testscore >= 60) {
            grade = 'D';
        } else {
            grade = 'F';
        }
        System.out.println("Grade = " + grade);
    }
}

```

The output from the program is:

```

    Grade = C

```

You may have noticed that the value of `testscore` can satisfy more than
one expression in the compound statement: `76 >= 70` and
`76 >= 60`. However,
once a condition is satisfied, the
appropriate statements are executed `(grade = 'C';)` and
the remaining conditions are not evaluated.

[« Previous](flow.html)
•
[Trail](../TOC.html)
•
[Next »](switch.html)

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

**Previous page:** Control Flow Statements
  
**Next page:** The switch Statement




A browser with JavaScript enabled is required for this page to operate properly.