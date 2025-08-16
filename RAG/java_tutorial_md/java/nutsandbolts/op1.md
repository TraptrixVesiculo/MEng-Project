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

Assignment, Arithmetic, and Unary Operators

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

[« Previous](operators.html) • [Trail](../TOC.html) • [Next »](op2.html)

# Assignment, Arithmetic, and Unary Operators

**The Simple Assignment Operator**

One of the most common operators that you'll encounter
is the simple assignment operator "`=`".
You saw this operator in the Bicycle class; it assigns the
value on its right to the operand on its left:

```

 int cadence = 0;
 int speed = 0;
 int gear = 1;

```

This operator can also be used on objects to assign
*object references*, as discussed in
[Creating Objects](../javaOO/objectcreation.html).

**The Arithmetic Operators**

The Java programming language provides operators that perform
addition, subtraction, multiplication, and division.
There's a good chance you'll recognize them by their counterparts
in basic mathematics.
The only symbol that might look new to you is "`%`", which divides one operand by another and returns
the remainder as its result.

```

+ 	additive operator (also used for String concatenation)
- 	subtraction operator
*	multiplication operator
/ 	division operator
%	remainder operator

```

The following program,
[`ArithmeticDemo`](examples/ArithmeticDemo.java),
tests the arithmetic operators.

```


class ArithmeticDemo {

     public static void main (String[] args){
          
          int result = 1 + 2; // result is now 3
          System.out.println(result);

          result = result - 1; // result is now 2
          System.out.println(result);

          result = result * 2; // result is now 4
          System.out.println(result);

          result = result / 2; // result is now 2
          System.out.println(result);

          result = result + 8; // result is now 10
          result = result % 7; // result is now 3
          System.out.println(result);

     }
}

```

You can also combine the arithmetic operators with the simple assignment operator
to create *compound assignments*.
For example, `x+=1;` and `x=x+1;` both increment the value
of `x` by 1.

The `+` operator can also be used for concatenating (joining)
two strings together, as shown in the following
[`ConcatDemo`](examples/ConcatDemo.java) program:

```


class ConcatDemo {
     public static void main(String[] args){
          String firstString = "This is";
          String secondString = " a concatenated string.";
          String thirdString = firstString+secondString;
          System.out.println(thirdString);
     }
}

```

By the end of this program, the variable `thirdString`
contains "This is a concatenated string.", which gets printed to standard output.

**The Unary Operators**

The unary operators require only one
operand; they perform various operations such as
incrementing/decrementing a value by one,
negating an expression, or inverting the value of a boolean.

```

+ 	Unary plus operator; indicates positive value (numbers are positive without this, however)
- 	Unary minus operator; negates an expression
++  	Increment operator; increments a value by 1
--    	Decrement operator; decrements a value by 1
!     	Logical complement operator; inverts the value of a boolean

```

The following program,
[`UnaryDemo`](examples/UnaryDemo.java), tests the unary operators:

```


class UnaryDemo {

     public static void main(String[] args){
          int result = +1; // result is now 1
          System.out.println(result);
          result--;  // result is now 0
          System.out.println(result);
          result++; // result is now 1 
          System.out.println(result);
          result = -result; // result is now -1
          System.out.println(result);
          boolean success = false;
          System.out.println(success); // false
          System.out.println(!success); // true
     }
}

```

The increment/decrement operators can be applied before (prefix)
or after (postfix) the operand.
The code `result++;` and `++result;` will both
end in `result` being incremented by one. The only difference is that
the prefix version (`++result`) evaluates to the incremented value,
whereas the postfix version (`result++`)
evaluates to the original value. If you are just
performing a simple increment/decrement, it doesn't really matter which version you choose. But if
you use this operator in part of a larger expression, the one that you choose may make a
significant difference.

The following program,
[`PrePostDemo`](examples/PrePostDemo.java), illustrates the prefix/postfix unary increment operator:

```


class PrePostDemo {
     public static void main(String[] args){
          int i = 3;
	  i++;
	  System.out.println(i);	// "4"
	  ++i;			   
	  System.out.println(i);	// "5"
	  System.out.println(++i);	// "6"
	  System.out.println(i++);	// "6"
	  System.out.println(i);	// "7"
     }
}

```

[« Previous](operators.html)
•
[Trail](../TOC.html)
•
[Next »](op2.html)

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

**Previous page:** Operators
  
**Next page:** Equality, Relational, and Conditional Operators




A browser with JavaScript enabled is required for this page to operate properly.