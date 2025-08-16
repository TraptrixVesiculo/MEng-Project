[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** Learning the Java Language
  
**Lesson:** Language Basics
  
**Section:** Operators

[Language Basics](index.html)

[Variables](variables.html)

[Primitive Data Types](datatypes.html)

[Arrays](arrays.html)

[Summary of Variables](variablesummary.html)

[Questions and Exercises](QandE/questions_variables.html)

[Operators](operators.html)

[Assignment, Arithmetic, and Unary Operators](op1.html)

[Equality, Relational, and Conditional Operators](op2.html)

Bitwise and Bit Shift Operators

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

[« Previous](op2.html) • [Trail](../TOC.html) • [Next »](opsummary.html)

# Bitwise and Bit Shift Operators

The Java programming language also provides operators that perform bitwise and bit shift operations on integral types.
The operators discussed in this section are less commonly used.
Therefore, their coverage is brief; the intent is to simply make you aware that these operators exist.

The unary bitwise complement operator "`~`" inverts a bit pattern; it can be applied to any of the
integral types, making every "0" a "1" and every "1" a "0". For example, a `byte` contains 8 bits; applying
this operator to a value whose bit pattern is "00000000" would change its pattern to "11111111".

The signed left shift operator "`<<`" shifts a bit pattern to the left,
and the signed right shift operator "`>>`" shifts a bit pattern to the
right. The bit pattern is given by the left-hand operand, and the
number of positions to shift by the right-hand operand.
The unsigned right shift operator "`>>>`"
shifts a zero into the leftmost position, while the leftmost
position after `">>"` depends on sign extension.

The bitwise `&` operator performs a bitwise AND operation.

The bitwise `^` operator performs a bitwise exclusive OR operation.

The bitwise `|` operator performs a bitwise inclusive OR operation.

The following program,
[`BitDemo`](examples/BitDemo.java), uses the bitwise AND operator to print the number "2" to standard output.

```


class BitDemo {
     public static void main(String[] args) {
          int bitmask = 0x000F;
	  int val = 0x2222;
	  System.out.println(val & bitmask);  // prints "2"
     }
}

```

[« Previous](op2.html)
•
[Trail](../TOC.html)
•
[Next »](opsummary.html)

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

**Previous page:** Equality, Relational, and Conditional Operators
  
**Next page:** Summary of Operators




A browser with JavaScript enabled is required for this page to operate properly.