[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** The Reflection API
  
**Lesson:** Classes
  
**Section:** Sealing Packages in Extensions

[Classes](index.html)

Retrieving Class Objects

[Examining Class Modifiers and Types](classModifiers.html)

[Discovering Class Members](classMembers.html)

[Troubleshooting](classTrouble.html)

[Home Page](../../index.html)
>
[The Reflection API](../index.html)
>
[Classes](index.html)

[« Previous](index.html) • [Trail](../TOC.html) • [Next »](classModifiers.html)

# Retrieving Class Objects

The entry point for all reflection operations is
[`java.lang.Class`](http://download.oracle.com/javase/7/docs/api/java/lang/Class.html). With the exception of
[`java.lang.reflect.ReflectPermission`](http://download.oracle.com/javase/7/docs/api/java/lang/reflect/ReflectPermission.html), none of the classes in
[`java.lang.reflect`](http://download.oracle.com/javase/7/docs/api/java/lang/reflect/package-summary.html)
have public constructors. To get to these classes, it is necessary to invoke
appropriate methods on
[`Class`](http://download.oracle.com/javase/7/docs/api/java/lang/Class.html). There are several ways to get a
[`Class`](http://download.oracle.com/javase/7/docs/api/java/lang/Class.html)
depending on whether the code has access to an object, the name of class, a
type, or an existing
[`Class`](http://download.oracle.com/javase/7/docs/api/java/lang/Class.html).

## Object.getClass()

If an instance of an object is available, then the simplest way to get its
[`Class`](http://download.oracle.com/javase/7/docs/api/java/lang/Class.html)
is to invoke
[`Object.getClass()`](http://download.oracle.com/javase/7/docs/api/java/lang/Object.html#getClass()). Of course, this only works for reference types which all inherit from
[`Object`](http://download.oracle.com/javase/7/docs/api/java/lang/Object.html). Some examples follow.

```

Class c = "foo".getClass();

```

Returns the
[`Class`](http://download.oracle.com/javase/7/docs/api/java/lang/Class.html)
for
[`String`](http://download.oracle.com/javase/7/docs/api/java/lang/String.html)

```

Class c = System.console().getClass();

```

There is a unique console associated with the virtual machine which is returned
by the `static` method
[`System.console()`](http://download.oracle.com/javase/7/docs/api/java/lang/System.html#console()). The value returned by
[`getClass()`](http://download.oracle.com/javase/7/docs/api/java/lang/Object.html#getClass())
is the
[`Class`](http://download.oracle.com/javase/7/docs/api/java/lang/Class.html)
corresponding to
[`java.io.Console`](http://download.oracle.com/javase/7/docs/api/java/io/Console.html).

```

enum E { A, B }
Class c = A.getClass();

```

`A` is is an instance of the enum `E`; thus
[`getClass()`](http://download.oracle.com/javase/7/docs/api/java/lang/Object.html#getClass())
returns the
[`Class`](http://download.oracle.com/javase/7/docs/api/java/lang/Class.html)
corresponding to the enumeration type `E`.

```

byte[] bytes = new byte[1024];
Class c = bytes.getClass();

```

Since arrays are
[`Objects`](http://download.oracle.com/javase/7/docs/api/java/lang/Object.html), it is also possible to invoke
[`getClass()`](http://download.oracle.com/javase/7/docs/api/java/lang/Object.html#getClass())
on an instance of an array. The returned
[`Class`](http://download.oracle.com/javase/7/docs/api/java/lang/Class.html)
corresponds to an array with component type `byte`.

```

import java.util.HashSet;
import java.util.Set;

Set<String> s = new HashSet<String>();
Class c = s.getClass();

```

In this case,
[`java.util.Set`](http://download.oracle.com/javase/7/docs/api/java/util/Set.html)
is an interface to an object of type
[`java.util.HashSet`](http://download.oracle.com/javase/7/docs/api/java/util/HashSet.html). The value returned by
[`getClass()`](http://download.oracle.com/javase/7/docs/api/java/lang/Object.html#getClass())
is the class corresponding to
[`java.util.HashSet`](http://download.oracle.com/javase/7/docs/api/java/util/HashSet.html).

## The .class Syntax

If the type is available but there is no instance then it is possible to
obtain a
[`Class`](http://download.oracle.com/javase/7/docs/api/java/lang/Class.html)
by appending `".class"` to the name of the type. This is also the
easiest way to obtain the
[`Class`](http://download.oracle.com/javase/7/docs/api/java/lang/Class.html)
for a primitive type.

```

boolean b;
Class c = b.getClass();   // compile-time error

Class c = boolean.class;  // correct

```

Note that the statement `boolean.getClass()` would produce a
compile-time error because a `boolean` is a primitive type and
cannot be dereferenced. The `.class` syntax returns the
[`Class`](http://download.oracle.com/javase/7/docs/api/java/lang/Class.html)
corresponding to the type `boolean`.

```

Class c = java.io.PrintStream.class;

```

The variable `c` will be the
[`Class`](http://download.oracle.com/javase/7/docs/api/java/lang/Class.html)
corresponding to the type
[`java.io.PrintStream`](http://download.oracle.com/javase/7/docs/api/java/io/PrintStream.html).

```

Class c = int[][][].class;

```

The `.class` syntax may be used to retrieve a
[`Class`](http://download.oracle.com/javase/7/docs/api/java/lang/Class.html)
corresponding to a multi-dimensional array of a given type.

## Class.forName()

If the fully-qualified name of a class is available, it is possible to get the
corresponding
[`Class`](http://download.oracle.com/javase/7/docs/api/java/lang/Class.html)
using the static method
[`Class.forName()`](http://download.oracle.com/javase/7/docs/api/java/lang/Class.html#forName(java.lang.String)). This cannot be used for primitive types. The syntax for names of array
classes is described by
[`Class.getName()`](http://download.oracle.com/javase/7/docs/api/java/lang/Class.html#getName()). This syntax is applicable to references and primitive types.

```

Class c = Class.forName("com.duke.MyLocaleServiceProvider");

```

This statement will create a class from the given fully-qualified name.

```

Class cDoubleArray = Class.forName("[D");

Class cStringArray = Class.forName("[[Ljava.lang.String;");

```

The variable `cDoubleArray` will contain the
[`Class`](http://download.oracle.com/javase/7/docs/api/java/lang/Class.html)
corresponding to an array of primitive type `double` (i.e. the same
as `double[].class`). The `cStringArray` variable will
contain the
[`Class`](http://download.oracle.com/javase/7/docs/api/java/lang/Class.html)
corresponding to a two-dimensional array of
[`String`](http://download.oracle.com/javase/7/docs/api/java/lang/String.html)
(i.e. identical to `String[][].class`).

## TYPE Field for Primitive Type Wrappers

The `.class` syntax is a more convenient and the preferred way to
obtain the
[`Class`](http://download.oracle.com/javase/7/docs/api/java/lang/Class.html)
for a primitive type; however there is another way to acquire the
[`Class`](http://download.oracle.com/javase/7/docs/api/java/lang/Class.html). Each of the primitive types and `void` has a wrapper class in
[`java.lang`](http://download.oracle.com/javase/7/docs/api/java/lang/package-summary.html)
that is used for boxing of primitive types to reference types. Each wrapper
class contains a field named `TYPE` which is equal to the
[`Class`](http://download.oracle.com/javase/7/docs/api/java/lang/Class.html)
for the primitive type being wrapped.

```

Class c = Double.TYPE;

```

There is a class
[`java.lang.Double`](http://download.oracle.com/javase/7/docs/api/java/lang/Double.html)
which is used to wrap the primitive type `double` whenever an
[`Object`](http://download.oracle.com/javase/7/docs/api/java/lang/Object.html)
is required. The value of
[`Double.TYPE`](http://download.oracle.com/javase/7/docs/api/java/lang/Double.html#TYPE)
is identical to that of `double.class`.

```

Class c = Void.TYPE;

```

[`Void.TYPE`](http://download.oracle.com/javase/7/docs/api/java/lang/Void.html#TYPE)
is identical to `void.class`.

## Methods that Return Classes

There are several Reflection APIs which return classes but these may only be
accessed if a
[`Class`](http://download.oracle.com/javase/7/docs/api/java/lang/Class.html)
has already been obtained either directly or indirectly.

[`Class.getSuperclass()`](http://download.oracle.com/javase/7/docs/api/java/lang/Class.html#getSuperclass()): Returns the super class for the given class. ``` Class c = javax.swing.JButton.class.getSuperclass(); ``` The super class of [`javax.swing.JButton`](http://download.oracle.com/javase/7/docs/api/javax/swing/JButton.html) is [`javax.swing.AbstractButton`](http://download.oracle.com/javase/7/docs/api/javax/swing/AbstractButton.html).

[`Class.getClasses()`](http://download.oracle.com/javase/7/docs/api/java/lang/Class.html#getClasses()): Returns all the public classes, interfaces, and enums that are members of the class including inherited members. ``` Class<?>[] c = Character.class.getClasses(); ``` [`Character`](http://download.oracle.com/javase/7/docs/api/java/lang/Character.html) contains two member classes [`Character.Subset`](http://download.oracle.com/javase/7/docs/api/java/lang/Character.Subset.html) and [`Character.UnicodeBlock`](http://download.oracle.com/javase/7/docs/api/java/lang/Character.UnicodeBlock.html).

[`Class.getDeclaredClasses()`](http://download.oracle.com/javase/7/docs/api/java/lang/Class.html#getDeclaredClasses()): Returns all of the classes interfaces, and enums that are explicitly declared in this class. ``` Class<?>[] c = Character.class.getDeclaredClasses(); ``` [`Character`](http://download.oracle.com/javase/7/docs/api/java/lang/Character.html) contains two public member classes [`Character.Subset`](http://download.oracle.com/javase/7/docs/api/java/lang/Character.Subset.html) and [`Character.UnicodeBlock`](http://download.oracle.com/javase/7/docs/api/java/lang/Character.UnicodeBlock.html) and one private class `Character.CharacterCache`.

`{` [`Class`](http://download.oracle.com/javase/7/docs/api/java/lang/Class.html#getDeclaringClass())`, java.lang.reflect. {` [`Field`](http://download.oracle.com/javase/7/docs/api/java/lang/reflect/Field.html#getDeclaringClass()), [`Method`](http://download.oracle.com/javase/7/docs/api/java/lang/reflect/Method.html#getDeclaringClass()), [`Constructor`](http://download.oracle.com/javase/7/docs/api/java/lang/reflect/Constructor.html#getDeclaringClass()) `} }.getDeclaringClass()`: Returns the [`Class`](http://download.oracle.com/javase/7/docs/api/java/lang/Class.html) in which these members were declared. [Anonymous classes](http://java.sun.com/docs/books/jls/third_edition/html/expressions.html#252986) will not have a declaring class but will have an enclosing class. ``` import java.lang.reflect.Field; Field f = System.class.getField("out"); Class c = f.getDeclaringClass(); ``` The field [`out is declared in System. ``` public class MyClass { static Object o = new Object() { public void m() {} }; static Class<c> = o.getClass().getEnclosingClass(); } ``` The declaring class of the anonymous class defined by o is null.`](http://download.oracle.com/javase/7/docs/api/java/lang/System.html#out)

[`Class.getEnclosingClass()`](http://download.oracle.com/javase/7/docs/api/java/lang/Class.html#getEnclosingClass()): Returns the immediately enclosing class of the class. ``` Class c = Thread.State.class().getEnclosingClass(); ``` The enclosing class of the enum [`Thread.State`](http://download.oracle.com/javase/7/docs/api/java/lang/Thread.State.html) is [`Thread`](http://download.oracle.com/javase/7/docs/api/java/lang/Thread.html). ``` public class MyClass { static Object o = new Object() { public void m() {} }; static Class<c> = o.getClass().getEnclosingClass(); } ``` The anonymous class defined by `o` is enclosed by `MyClass`.

[« Previous](index.html)
•
[Trail](../TOC.html)
•
[Next »](classModifiers.html)

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

**Previous page:** Classes
  
**Next page:** Examining Class Modifiers and Types




A browser with JavaScript enabled is required for this page to operate properly.