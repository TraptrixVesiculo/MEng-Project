[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** Learning the Java Language
  
**Lesson:** Language Basics
  
**Section:** Variables

[Language Basics](index.html)

[Variables](variables.html)

Primitive Data Types

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

[The for Statement](for.html)

[Branching Statements](branch.html)

[Summary of Control Flow Statements](flowsummary.html)

[Questions and Exercises](QandE/questions_flow.html)

[Home Page](../../index.html)
>
[Learning the Java Language](../index.html)
>
[Language Basics](index.html)

[« Previous](variables.html) • [Trail](../TOC.html) • [Next »](arrays.html)

# Primitive Data Types

The Java programming language is statically-typed,
which means that all variables must first be declared before they can be used.
This involves stating the variable's type and name, as you've already seen:

```

int gear = 1;

```

Doing so tells your program that a field named "gear" exists, holds
numerical data, and has an initial value of "1". A variable's data type determines the
values it may contain, plus the operations that may be performed on it.
In addition to `int`, the Java programming language supports seven other *primitive
data types*. A primitive type is predefined by the language and is named by a reserved keyword. Primitive values do not share state with other primitive values.
The eight primitive data types supported by the Java programming language are:

* **byte**: The `byte` data type is an 8-bit signed two's complement integer. It has a minimum
  value of -128 and a maximum value of 127 (inclusive). The `byte` data type can be useful for saving memory
  in large
  [arrays](arrays.html), where the memory savings actually matters. They can also be used in place of
  `int` where their limits help to clarify your code; the fact that a variable's range is limited can
  serve as a form of documentation.
* **short**: The `short` data type is a 16-bit signed two's complement integer. It has a
  minimum value of -32,768 and a maximum value of 32,767 (inclusive). As with `byte`, the same guidelines apply:
  you can use a `short` to save memory in large arrays, in situations where the memory savings actually matters.
* **int**: The `int` data type is a 32-bit signed two's complement integer. It has a minimum value of
  -2,147,483,648 and a maximum value of 2,147,483,647 (inclusive). For integral values, this data type is generally
  the default choice unless there is a reason (like the above) to choose something else. This data type will most likely
  be large enough for the numbers your program will use, but if you need a wider range of values, use `long` instead.
* **long**: The `long` data type is a 64-bit signed two's complement integer. It has a minimum value of
  -9,223,372,036,854,775,808 and a maximum value of 9,223,372,036,854,775,807 (inclusive). Use this data type when you need a
  range of values wider than those provided by `int`.
* **float**: The `float` data type is a single-precision 32-bit IEEE 754 floating point.
  Its range of values is beyond the scope of this discussion, but is specified in section
  [4.2.3](http://java.sun.com/docs/books/jls/third_edition/html/typesValues.html#4.2.3)
  of the Java Language Specification. As with the recommendations for `byte` and `short`, use a `float` (instead of `double`) if you need to save memory in large arrays
  of floating point numbers. This data type should never be used for precise values, such as currency. For that, you will need to
  use the
  [java.math.BigDecimal](http://download.oracle.com/javase/7/docs/api/java/math/BigDecimal.html)
  class instead.
  [Numbers and Strings](../data/index.html)
  covers `BigDecimal` and
  other useful classes provided by the Java platform.
* **double**: The `double` data type is a double-precision 64-bit IEEE 754 floating point.
  Its range of values is beyond the scope of this discussion, but is specified in section
  [4.2.3](http://java.sun.com/docs/books/jls/third_edition/html/typesValues.html#4.2.3)
  of the Java Language Specification. For decimal values, this data type is
  generally the default choice. As mentioned above, this data type should never be used for precise values, such as currency.
* **boolean**: The `boolean` data type has only two possible values: `true` and
  `false`. Use this data type for simple flags that track true/false conditions. This data type represents one bit of information, but its "size" isn't something that's precisely defined.
* **char**: The `char` data type is a single 16-bit Unicode character. It has a minimum value of
  `'\u0000'` (or 0) and a maximum value of `'\uffff'` (or 65,535 inclusive).

In addition to the eight primitive data types listed above, the Java programming language also provides
special support for character strings via the
[java.lang.String](http://download.oracle.com/javase/7/docs/api/java/lang/String.html)
class. Enclosing your character string
within double quotes will automatically create a new `String` object; for example, `String s = "this is a string";`.
`String` objects are *immutable*, which means that once created, their
values cannot be changed. The `String` class is not technically a primitive data type, but considering the special
support given to it by the language, you'll probably tend to think of it as such. You'll learn more about the `String`
class in
[Simple Data Objects](../data/index.html)

### Default Values

It's not always necessary to assign a value when a field is declared. Fields that are declared but not initialized will be
set to a reasonable default by the compiler. Generally speaking, this default will be zero or `null`, depending on the
data type. Relying on such default values, however, is generally considered bad programming style.

The following chart summarizes the default values for the above data types.

| **Data Type** | **Default Value (for fields)** |
| --- | --- |
| byte | 0 |
| short | 0 |
| int | 0 |
| long | 0L |
| float | 0.0f |
| double | 0.0d |
| char | '\u0000' |
| String (or any object) | null |
| boolean | false |

Local variables are slightly different; the compiler never assigns a default value to an uninitialized local variable.
If you cannot initialize your
local variable where it is declared, make sure to assign it a value before you attempt to use it. Accessing an uninitialized local variable will result in a compile-time error.

### Literals

You may have noticed that the `new` keyword isn't used when initializing a variable of a primitive type. Primitive
types are special data types built into the language; they are not objects created
from a class. A *literal* is
the source code representation of a fixed value;
literals are represented
directly in your code without requiring computation.
As shown below,
it's possible to
assign a literal to a variable of a primitive type:

```

     boolean result = true;
     char capitalC = 'C';
     byte b = 100;
     short s = 10000;
     int i = 100000;

```

The integral types (`byte`, `short`, `int`, and `long`) can be expressed using decimal, octal, hexadecimal, or binary number systems. (You can create binary literals in Java SE 7 and later.) Decimal is the number system you already use every day;
it's based on 10 digits, numbered 0 through 9.
The octal number system is base 8, consisting of the digits 0 through 7. The hexadecimal system is base 16,
whose digits are the numbers 0 through 9 and the letters A through F. The binary system is base 2, whose digits are the numbers 0 and 1.
For general-purpose programming, the decimal system is likely to be the only number system you'll ever use.
However, if you need octal, hexadecimal, or binary numbers, the following example shows
the correct syntax. The prefix `0` indicates octal, `0x` indicates hexadecimal, and `0b` indicates binary:

```

     int decVal = 26; 	   // The number 26, in decimal
     int octVal = 032; 	   // The number 26, in octal
     int hexVal = 0x1a;	   // The number 26, in hexadecimal
     int binVal = 0b11010; // The number 26, in binary

```

The floating point types (`float` and `double`) can also be expressed using E or e (for scientific notation),
F or f (32-bit float literal) and D or d (64-bit double literal; this is the default and by convention is omitted).

```

     double d1 = 123.4;
     double d2 = 1.234e2; // same value as d1, but in scientific notation
     float f1  = 123.4f;

```

Literals of types `char` and `String` may contain any Unicode
(UTF-16) characters. If your editor and file system allow it, you can
use such characters directly in your code. If not, you can use
a "Unicode escape" such as `'\u0108'` (capital C with circumflex), or
`"S\u00ED se\u00F1or"` (Sí Señor in Spanish). Always use 'single quotes' for `char` literals
and "double quotes" for `String` literals.
Unicode escape sequences may be used
elsewhere in a program (such as in field names, for example), not just in `char` or `String` literals.

The Java programming language also supports a few special escape sequences for `char` and `String` literals: `\b` (backspace),
`\t` (tab), `\n` (line feed), `\f` (form feed), `\r` (carriage return), `\"` (double quote), `\'` (single quote), and `\\` (backslash).

There's also a special `null` literal that can be
used as a value for any reference type. `null` may be assigned to any variable, except
variables of primitive types. There's little you can do with a `null`
value beyond testing for its presence. Therefore, `null` is often
used in programs as a marker to indicate that some object is unavailable.

Finally, there's also a special kind of literal called a *class literal*, formed
by taking a type name and appending "`.class"`; for example, `String.class`.
This refers to the object (of type `Class`) that represents the type itself.

### Using Underscore Characters in Numeric Literals

In Java SE 7 and later, any number of underscore characters (`_`) can appear anywhere between digits in a numerical literal. This feature enables you, for example. to separate groups of digits in numeric literals, which can improve the readability of your code.

For instance, if your code contains numbers with many digits, you can use an underscore character to separate digits in groups of three, similar to how you would use a punctuation mark like a comma, or a space, as a separator.

The following example shows other ways you can use the underscore in numeric literals:

```
long creditCardNumber = 1234_5678_9012_3456L;
long socialSecurityNumber = 999_99_9999L;
float pi = 	3.14_15F;
long hexBytes = 0xFF_EC_DE_5E;
long hexWords = 0xCAFE_BABE;
long maxLong = 0x7fff_ffff_ffff_ffffL;
byte nybbles = 0b0010_0101;
long bytes = 0b11010010_01101001_10010100_10010010;
```

You can place underscores only between digits; you cannot place underscores in the following places:

* At the beginning or end of a number
* Adjacent to a decimal point in a floating point literal
* Prior to an `F` or `L` suffix
* In positions where a string of digits is expected

The following examples demonstrate valid and invalid underscore placements in numeric literals:

```

float pi1 = 3_.1415F;      // Invalid; cannot put underscores adjacent to a decimal point
float pi2 = 3._1415F;      // Invalid; cannot put underscores adjacent to a decimal point
long socialSecurityNumber1
  = 999_99_9999_L;         // Invalid; cannot put underscores prior to an L suffix

int x1 = _52;              // This is an identifier, not a numeric literal
int x2 = 5_2;              // OK (decimal literal)
int x3 = 52_;              // Invalid; cannot put underscores at the end of a literal
int x4 = 5_______2;        // OK (decimal literal)

int x5 = 0_x52;            // Invalid; cannot put underscores in the 0x radix prefix
int x6 = 0x_52;            // Invalid; cannot put underscores at the beginning of a number
int x7 = 0x5_2;            // OK (hexadecimal literal)
int x8 = 0x52_;            // Invalid; cannot put underscores at the end of a number

int x9 = 0_52;             // OK (octal literal)
int x10 = 05_2;            // OK (octal literal)
int x11 = 052_;            // Invalid; cannot put underscores at the end of a number
```

[« Previous](variables.html)
•
[Trail](../TOC.html)
•
[Next »](arrays.html)

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

**Previous page:** Variables
  
**Next page:** Arrays




A browser with JavaScript enabled is required for this page to operate properly.