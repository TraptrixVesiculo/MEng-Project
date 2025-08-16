[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** Learning the Java Language
  
**Lesson:** Numbers and Strings

[Numbers and Strings](index.html)

[Numbers](numbers.html)

[The Numbers Classes](numberclasses.html)

[Formatting Numeric Print Output](numberformat.html)

[Beyond Basic Arithmetic](beyondmath.html)

[Summary of Numbers](numbersummary.html)

[Questions and Exercises](QandE/numbers-questions.html)

Characters

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

[« Previous](QandE/numbers-questions.html) • [Trail](../TOC.html) • [Next »](strings.html)

# Characters

Most of the time, if you are using a single character value, you will
use the primitive `char` type. For example:

```

char ch = 'a'; 
char uniChar = '\u039A'; // Unicode for uppercase Greek omega character
char[] charArray ={ 'a', 'b', 'c', 'd', 'e' }; // an array of chars

```

There are times, however, when you need to use a char as an object—for example, as a
method argument where an object is expected. The Java programming
language provides a *wrapper* class that "wraps" the `char`
in a `Character` object for this purpose. An object of type `Character` contains a single field,
whose type is `char`.
This
[`Character`](http://download.oracle.com/javase/7/docs/api/java/lang/Character.html) class also offers a number of useful class (i.e., static) methods for manipulating characters.

You can create a `Character` object with the `Character` constructor:

```

Character ch = new Character('a');

```

The Java compiler will also create a `Character` object for you under some circumstances.
For example, if you pass a primitive `char` into a
method that expects an object,
the compiler automatically converts the `char` to a `Character` for you.
This feature is called *autoboxing*—or *unboxing*, if the conversion
goes the other way.

Here is an example of boxing,

```

Character ch = 'a'; // the primitive char 'a' is boxed into the Character object ch

```

and here is an example of both boxing and unboxing,

```

Character test(Character c) {...} // method parameter and return type = Character object

char c = test('x'); // primitive 'x' is boxed for method test, return is unboxed to char 'c'

```

---

**Note:** The `Character` class is
immutable, so that once it is created, a `Character` object cannot be changed.

---

The following table lists some of the most useful methods
in the `Character` class, but is not exhaustive.
For a complete listing of all methods in this class (there are more than 50), refer to the
[`java.lang.Character`](http://download.oracle.com/javase/7/docs/api/java/lang/Character.html) API specification.

**Useful Methods in the `Character` Class**

| Method | Description |
| `boolean isLetter(char ch)   boolean isDigit(char ch)` | Determines whether the specified char value is a letter or a digit, respectively. |
| `boolean isWhitespace(char ch)` | Determines whether the specified char value is white space. |
| `boolean isUpperCase(char ch)   boolean isLowerCase(char ch)` | Determines whether the specified char value is uppercase or lowercase, respectively. |
| `char toUpperCase(char ch)   char toLowerCase(char ch)` | Returns the uppercase or lowercase form of the specified char value. |
| `toString(char ch)` | Returns a `String` object representing the specified character value—that is, a one-character string. |

### Escape Sequences

A character preceded by a backslash (\) is an *escape sequence*
and has special meaning to the compiler.
The following table shows the Java escape sequences:

**Escape Sequences**

| Escape Sequence | Description |
| `\t` | Insert a tab in the text at this point. |
| `\b` | Insert a backspace in the text at this point. |
| `\n` | Insert a newline in the text at this point. |
| `\r` | Insert a carriage return in the text at this point. |
| `\f` | Insert a formfeed in the text at this point. |
| `\'` | Insert a single quote character in the text at this point. |
| `\"` | Insert a double quote character in the text at this point. |
| `\\` | Insert a backslash character in the text at this point. |

When an escape sequence is encountered in a print statement, the compiler interprets it accordingly. For example,
if you want to put quotes within quotes you must use the escape sequence, \", on the interior quotes. To
print the sentence

```

She said "Hello!" to me.

```

you would write

```

System.out.println("She said \"Hello!\" to me.");

```

[« Previous](QandE/numbers-questions.html)
•
[Trail](../TOC.html)
•
[Next »](strings.html)

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

**Previous page:** Questions and Exercises: Numbers
  
**Next page:** Strings




A browser with JavaScript enabled is required for this page to operate properly.