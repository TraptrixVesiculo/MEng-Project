[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** Learning the Java Language
  
**Lesson:** Language Basics

[Language Basics](index.html)

[Variables](variables.html)

[Primitive Data Types](datatypes.html)

[Arrays](arrays.html)

[Summary of Variables](variablesummary.html)

[Questions and Exercises](QandE/questions_variables.html)

Operators

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

[The for Statement](for.html)

[Branching Statements](branch.html)

[Summary of Control Flow Statements](flowsummary.html)

[Questions and Exercises](QandE/questions_flow.html)

[Home Page](../../index.html)
>
[Learning the Java Language](../index.html)
>
[Language Basics](index.html)

[« Previous](QandE/questions_variables.html) • [Trail](../TOC.html) • [Next »](op1.html)

# Operators

Now that you've learned how to declare and initialize variables, you
probably want to know how to *do something* with them.
Learning the operators of the Java programming
language is a good place to start.
Operators are special symbols that perform specific operations on one, two,
or three *operands*, and then return a result.

As we explore the operators of the Java programming language, it may be helpful for you to know ahead of time which operators have
the highest precedence.
The operators in the following table are listed according to precedence order. The closer to the top of the table an operator appears, the higher its precedence. Operators with higher precedence are evaluated before operators with relatively lower precedence. Operators on the same line have equal precedence. When operators of equal precedence appear in the same expression, a rule must govern which is evaluated first. All binary operators except for the assignment operators are evaluated from left to right; assignment operators are evaluated right to left.

**Operator Precedence**

| Operators | Precedence |
| postfix | `expr++ expr--` |
| unary | `++expr --expr +expr -expr ~ !` |
| multiplicative | `* / %` |
| additive | `+ -` |
| shift | `<< >> >>>` |
| relational | `< > <= >= instanceof` |
| equality | `== !=` |
| bitwise AND | `&` |
| bitwise exclusive OR | `^` |
| bitwise inclusive OR | `|` |
| logical AND | `&&` |
| logical OR | `||` |
| ternary | `? :` |
| assignment | `= += -= *= /= %= &= ^= |= <<= >>= >>>=` |

In general-purpose programming, certain operators
tend to appear more frequently than others; for example, the assignment operator "`=`"
is far more common than the unsigned right shift operator "`>>>`". With that in
mind, the following discussion focuses first on the operators that
you're most likely to use on a regular basis, and
ends focusing on those that are less common.
Each discussion is accompanied by sample code
that you can compile and run. Studying its output will help reinforce what you've
just learned.

[« Previous](QandE/questions_variables.html)
•
[Trail](../TOC.html)
•
[Next »](op1.html)

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

**Previous page:** Questions and Exercises: Variables
  
**Next page:** Assignment, Arithmetic, and Unary Operators




A browser with JavaScript enabled is required for this page to operate properly.