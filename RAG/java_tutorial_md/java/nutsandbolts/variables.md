[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** Learning the Java Language
  
**Lesson:** Language Basics

[Language Basics](index.html)

Variables

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

[The for Statement](for.html)

[Branching Statements](branch.html)

[Summary of Control Flow Statements](flowsummary.html)

[Questions and Exercises](QandE/questions_flow.html)

[Home Page](../../index.html)
>
[Learning the Java Language](../index.html)
>
[Language Basics](index.html)

[« Previous](index.html) • [Trail](../TOC.html) • [Next »](datatypes.html)

# Variables

As you learned in the previous lesson, an object stores its state in *fields*.
> `int cadence = 0;  
> int speed = 0;  
> int gear = 1;`

The
[What Is an Object?](../concepts/object.html)
discussion introduced you to fields, but you probably
have still a few questions, such as: What are the rules and conventions for naming a field?
Besides `int`, what other data types are there?
Do fields have to be initialized when they are declared? Are fields assigned
a default value if they are not explicitly initialized?
We'll explore the answers to such questions in this lesson, but before we do, there are a few technical distinctions you must first become aware of. In the
Java programming language, the terms "field" and "variable" are both used;
this is a common source of confusion among new developers, since both often seem to refer to the same thing.

The Java programming language defines the following kinds of variables:

* **Instance Variables (Non-Static Fields)** Technically speaking, objects store their individual states in "non-static fields", that is, fields
  declared without the
  `static` keyword. Non-static fields are also known as
  *instance variables* because their values are unique to each *instance* of a class (to each object, in other words); the `currentSpeed` of one bicycle is independent from the `currentSpeed` of another.

  * **Class Variables (Static Fields)** A *class variable* is any field declared with the
    `static` modifier; this tells the compiler that there is exactly one copy of this variable in existence, regardless of how many times the class has been instantiated.
    A field defining the number
    of gears for a particular kind of bicycle could be marked as `static` since conceptually the same number of gears
    will apply to all instances. The code `static int numGears = 6;` would create such a static field.
    Additionally, the keyword `final` could be added to indicate that the number of gears will
    never change.

    * **Local Variables** Similar to how an object stores its state in fields, a method will often store its temporary state in *local variables*.
      The syntax for declaring a local variable is similar to declaring a field (for example, `int count = 0;`).
      There is no special keyword designating a variable as local; that determination
      comes entirely from the location in which the variable is declared — which is between the opening and closing braces of a method. As such, local
      variables are only visible to the methods in which they are declared; they are not accessible from the rest of the class.

      * **Parameters** You've already seen examples of parameters, both in the `Bicycle` class and in
        the `main` method of the "Hello World!" application. Recall that the signature for the `main` method is `public static void main(String[] args)`. Here, the `args` variable is the
        parameter to this method. The important thing to remember is that parameters are always classified as "variables"
        not "fields". This applies to other parameter-accepting constructs as well (such as constructors and exception handlers) that you'll learn about later in the tutorial.

Having said that, the remainder of this tutorial uses the following
general guidelines when discussing fields and variables. If we are talking
about "fields in general" (excluding local variables and parameters), we may simply say "fields". If the discussion applies to "all of the above", we may simply say "variables". If the context calls for a distinction, we will use specific terms (static field, local variables, etc.) as appropriate.
You may also occasionally see the term "member" used as well.
A type's fields, methods, and nested types are collectively called
its *members*.

### Naming

Every programming language has its own set of rules and conventions for the kinds of names that you're allowed to use, and the Java programming language is no different.
The rules and conventions for naming your variables can be summarized as follows:

* Variable names are case-sensitive. A variable's name can be any legal identifier — an unlimited-length sequence of Unicode letters and digits,
  beginning with a letter, the dollar sign "`$`", or the underscore character "`_`". The convention, however, is to always
  begin your variable names with a letter, not "`$`" or "`_`". Additionally, the dollar sign character, by convention, is never used at all.
  You may find some situations where auto-generated names will contain
  the dollar sign, but your variable names should always
  avoid using it. A similar convention exists for the underscore character; while it's technically legal to begin your variable's name with "`_`", this practice is discouraged. White space is not permitted.

  * Subsequent characters may be letters, digits, dollar signs, or underscore characters. Conventions (and common sense) apply to this rule as well. When choosing a name for your variables, use full words instead of cryptic abbreviations.
    Doing so will make your code easier to read and understand.
    In many cases it will also make your code self-documenting;
    fields named `cadence`, `speed`, and `gear`, for example, are much more intuitive than abbreviated versions, such as `s`, `c`, and `g`.
    Also keep in mind that the name you choose must not be a
    [keyword or reserved word](_keywords.html).

    * If the name you choose consists of only one word, spell that word in all
      lowercase letters. If it consists of more than one word, capitalize the first
      letter of each subsequent word. The names `gearRatio` and
      `currentGear` are prime examples of this convention. If your variable
      stores a constant value, such as `static final int NUM_GEARS = 6`,
      the convention changes slightly, capitalizing every letter and separating subsequent words with the underscore character. By convention, the underscore character is never used elsewhere.

[« Previous](index.html)
•
[Trail](../TOC.html)
•
[Next »](datatypes.html)

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

**Previous page:** Language Basics
  
**Next page:** Primitive Data Types




A browser with JavaScript enabled is required for this page to operate properly.