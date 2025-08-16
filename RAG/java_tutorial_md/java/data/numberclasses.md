[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** Learning the Java Language
  
**Lesson:** Numbers and Strings
  
**Section:** Numbers

[Numbers and Strings](index.html)

[Numbers](numbers.html)

The Numbers Classes

[Formatting Numeric Print Output](numberformat.html)

[Beyond Basic Arithmetic](beyondmath.html)

[Summary of Numbers](numbersummary.html)

[Questions and Exercises](QandE/numbers-questions.html)

[Characters](characters.html)

[Strings](strings.html)

[Converting Between Numbers and Strings](converting.html)

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

[« Previous](numbers.html) • [Trail](../TOC.html) • [Next »](numberformat.html)

# The Numbers Classes

When working with numbers, most of the time you use the primitive types in your code.
For example:

```

int i = 500;
float gpa = 3.65f;
byte mask = 0xff;

```

There are, however, reasons to use objects in place of primitives, and the
Java platform provides *wrapper* classes for each of the primitive data types. These
classes "wrap" the primitive in an object. Often, the wrapping is done by the compiler—if
you use a primitive where an object is expected, the compiler *boxes* the primitive in its
wrapper class for you. Similarly, if you use a number object when a primitive is expected, the compiler
*unboxes* the object for you.

Here is an example of boxing and unboxing:

```

Integer x, y;
x = 12;
y = 15;
System.out.println(x+y);

```

When `x` and `y` are assigned integer values, the compiler boxes the integers because
`x` and `y` are integer objects. In the `println()` statement, `x`
and `y` are unboxed so that they can be added as integers.

All of the
numeric wrapper classes are subclasses of the abstract class `Number`:

![The class hierarchy of Number.](../../figures/java/objects-numberHierarchy.gif)

---

**Note:** There are four other subclasses of `Number` that are not discussed here. `BigDecimal` and
`BigInteger` are used for high-precision calculations. `AtomicInteger` and
`AtomicLong` are used for multi-threaded applications.

---

There are three reasons that you might use a `Number` object
rather than a primitive:

1. As an argument of a method that expects an object (often used when manipulating collections
   of numbers).

   - To use constants defined by
     the class, such as `MIN_VALUE` and
     `MAX_VALUE`, that provide the upper and lower bounds of the data type.
   - To use class methods for converting values to and from other primitive types,
     for converting to and from strings, and for converting between number systems (decimal, octal,
     hexadecimal, binary).

The following table lists the instance methods that all the subclasses of
the `Number` class implement.

**Methods Implemented by all Subclasses of Number**

| Method | Description |
| `byte byteValue()`  `short shortValue()`  `int intValue()`  `long longValue()`  `float floatValue()`  `double doubleValue()` | Converts the value of this `Number` object to the primitive data type returned. |
| `int compareTo(Byte anotherByte)   int compareTo(Double anotherDouble)   int compareTo(Float anotherFloat)   int compareTo(Integer anotherInteger)   int compareTo(Long anotherLong)   int compareTo(Short anotherShort)` | Compares this `Number` object to the argument. |
| `boolean equals(Object obj)` | Determines whether this number object is equal to the argument.   The methods return `true` if the argument is not `null` and is an object of the same type and with the same numeric value.   There are some extra requirements for `Double` and `Float` objects that are described in the Java API documentation. |

Each `Number` class contains other methods that are useful for converting numbers to and from strings
and for converting between number systems. The following table lists these methods in the `Integer` class.
Methods for the other `Number` subclasses are similar:

**Conversion Methods, `Integer` Class**

| Method | Description |
| `static Integer decode(String s)` | Decodes a string into an integer. Can accept string representations of decimal, octal, or hexadecimal numbers as input. |
| `static int parseInt(String s)` | Returns an integer (decimal only). |
| `static int parseInt(String s, int radix)` | Returns an integer, given a string representation of decimal, binary, octal, or hexadecimal (`radix` equals 10, 2, 8, or 16 respectively) numbers as input. |
| `String toString()` | Returns a `String` object representing the value of this `Integer`. |
| `static String toString(int i)` | Returns a `String` object representing the specified integer. |
| `static Integer valueOf(int i)` | Returns an `Integer` object holding the value of the specified primitive. |
| `static Integer valueOf(String s)` | Returns an `Integer` object holding the value of the specified string representation. |
| `static Integer valueOf(String s, int radix)` | Returns an `Integer` object holding the integer value of the specified string representation, parsed with the value of radix. For example, if s = "333" and radix = 8, the method returns the base-ten integer equivalent of the octal number 333. |

[« Previous](numbers.html)
•
[Trail](../TOC.html)
•
[Next »](numberformat.html)

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

**Previous page:** Numbers
  
**Next page:** Formatting Numeric Print Output




A browser with JavaScript enabled is required for this page to operate properly.