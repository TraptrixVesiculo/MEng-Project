[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** The Reflection API
  
**Lesson:** Classes
  
**Section:** Sealing Packages in Extensions

[Classes](index.html)

[Retrieving Class Objects](classNew.html)

[Examining Class Modifiers and Types](classModifiers.html)

Discovering Class Members

[Troubleshooting](classTrouble.html)

[Home Page](../../index.html)
>
[The Reflection API](../index.html)
>
[Classes](index.html)

[« Previous](classModifiers.html) • [Trail](../TOC.html) • [Next »](classTrouble.html)

# Discovering Class Members

There are two categories of methods provided in
[`Class`](http://download.oracle.com/javase/7/docs/api/java/lang/Class.html)
for accessing fields, methods, and constructors: methods which enumerate these
members and methods which search for particular members. Also there are
distinct methods for accessing members declared directly on the class versus
methods which search the superinterfaces and superclasses for inherited
members. The following tables provide a summary of all the member-locating
methods and their characteristics.

  

Class Methods for Locating Fields

| [`Class`](http://download.oracle.com/javase/7/docs/api/java/lang/Class.html) API List of members? Inherited members? Private members? |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | [`getDeclaredField()`](http://download.oracle.com/javase/7/docs/api/java/lang/Class.html#getDeclaredField(java.lang.String)) no no yes|  |  |  |  |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | [`getField()`](http://download.oracle.com/javase/7/docs/api/java/lang/Class.html#getField(java.lang.String)) no yes no|  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | | [`getDeclaredFields()`](http://download.oracle.com/javase/7/docs/api/java/lang/Class.html#getDeclaredFields()) yes no yes|  |  |  |  | | --- | --- | --- | --- | | [`getFields()`](http://download.oracle.com/javase/7/docs/api/java/lang/Class.html#getFields()) yes yes no | | | | | | | | | | | | | | | | | | | |

  


Class Methods for Locating Methods

| [`Class`](http://download.oracle.com/javase/7/docs/api/java/lang/Class.html) API List of members? Inherited members? Private members?|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | [`getDeclaredMethod()`](http://download.oracle.com/javase/7/docs/api/java/lang/Class.html#getDeclaredMethod(java.lang.String, java.lang.Class...)) no no yes|  |  |  |  |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | [`getMethod()`](http://download.oracle.com/javase/7/docs/api/java/lang/Class.html#getMethod(java.lang.String, java.lang.Class...)) no yes no|  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | | [`getDeclaredMethods()`](http://download.oracle.com/javase/7/docs/api/java/lang/Class.html#getDeclaredMethods()) yes no yes|  |  |  |  | | --- | --- | --- | --- | | [`getMethods()`](http://download.oracle.com/javase/7/docs/api/java/lang/Class.html#getMethods()) yes yes no | | | | | | | | | | | | | | | | | | | |

  


Class Methods for Locating Constructors

| [`Class`](http://download.oracle.com/javase/7/docs/api/java/lang/Class.html) API List of members? Inherited members? Private members?|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | [`getDeclaredConstructor()`](http://download.oracle.com/javase/7/docs/api/java/lang/Class.html#getDeclaredConstructor(java.lang.Class...)) no N/A1 yes|  |  |  |  |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | [`getConstructor()`](http://download.oracle.com/javase/7/docs/api/java/lang/Class.html#getConstructor(java.lang.Class...)) no N/A1 no|  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | | [`getDeclaredConstructors()`](http://download.oracle.com/javase/7/docs/api/java/lang/Class.html#getDeclaredConstructors()) yes N/A1 yes|  |  |  |  | | --- | --- | --- | --- | | [`getConstructors()`](http://download.oracle.com/javase/7/docs/api/java/lang/Class.html#getConstructors()) yes N/A1 no | | | | | | | | | | | | | | | | | | | |

1 Constructors are not inherited.

Given a class name and an indication of which members are of
interest, the
[`ClassSpy`](example/ClassSpy.java)
example uses the `get*s()` methods to determine the list of all
public elements, including any which are inherited.

```


import java.lang.reflect.Constructor;
import java.lang.reflect.Field;
import java.lang.reflect.Method;
import java.lang.reflect.Member;
import static java.lang.System.out;

enum ClassMember { CONSTRUCTOR, FIELD, METHOD, CLASS, ALL }

public class ClassSpy {
    public static void main(String... args) {
	try {
	    Class<?> c = Class.forName(args[0]);
	    out.format("Class:%n  %s%n%n", c.getCanonicalName());

	    Package p = c.getPackage();
	    out.format("Package:%n  %s%n%n",
		       (p != null ? p.getName() : "-- No Package --"));

	    for (int i = 1; i < args.length; i++) {
		switch (ClassMember.valueOf(args[i])) {
		case CONSTRUCTOR:
		    printMembers(c.getConstructors(), "Constructor");
		    break;
		case FIELD:
		    printMembers(c.getFields(), "Fields");
		    break;
		case METHOD:
		    printMembers(c.getMethods(), "Methods");
		    break;
		case CLASS:
		    printClasses(c);
		    break;
		case ALL:
		    printMembers(c.getConstructors(), "Constuctors");
		    printMembers(c.getFields(), "Fields");
		    printMembers(c.getMethods(), "Methods");
		    printClasses(c);
		    break;
		default:
		    assert false;
		}
	    }

        // production code should handle these exceptions more gracefully
	} catch (ClassNotFoundException x) {
	    x.printStackTrace();
	}
    }

    private static void printMembers(Member[] mbrs, String s) {
	out.format("%s:%n", s);
	for (Member mbr : mbrs) {
	    if (mbr instanceof Field)
		out.format("  %s%n", ((Field)mbr).toGenericString());
	    else if (mbr instanceof Constructor)
		out.format("  %s%n", ((Constructor)mbr).toGenericString());
	    else if (mbr instanceof Method)
		out.format("  %s%n", ((Method)mbr).toGenericString());
	}
	if (mbrs.length == 0)
	    out.format("  -- No %s --%n", s);
	out.format("%n");
    }

    private static void printClasses(Class<?> c) {
	out.format("Classes:%n");
	Class<?>[] clss = c.getClasses();
	for (Class<?> cls : clss)
	    out.format("  %s%n", cls.getCanonicalName());
	if (clss.length == 0)
	    out.format("  -- No member interfaces, classes, or enums --%n");
	out.format("%n");
    }
}

```

This example is relatively compact; however the `printMembers()`
method is slightly awkward due to the fact that the
[`java.lang.reflect.Member`](http://download.oracle.com/javase/7/docs/api/java/lang/reflect/Member.html)
interface has existed since the earliest implementations of reflection and it
could not be modified to include the more useful
`getGenericString()` method when generics were introduced. The only
alternatives are to test and cast as shown, replace this method with
`printConstructors()`, `printFields()`, and
`printMethods()`, or to be satisfied with the relatively spare
results of
[`Member.getName()`](http://download.oracle.com/javase/7/docs/api/java/lang/reflect/Member.html#getName()).

Samples of the output and their interpretation follows. User input is in
italics.

```

$ java ClassSpy java.lang.ClassCastException CONSTRUCTOR
Class:
  java.lang.ClassCastException

Package:
  java.lang

Constructor:
  public java.lang.ClassCastException()
  public java.lang.ClassCastException(java.lang.String)

```

Since constructors are not inherited, the exception chaining mechanism
constructors (those with a
[`Throwable`](http://download.oracle.com/javase/7/docs/api/java/lang/Throwable.html)
parameter) which are defined in the immediate super class
[`RuntimeException`](http://download.oracle.com/javase/7/docs/api/java/lang/RuntimeException.html)
and other super classes are not found.

```

$ java ClassSpy java.nio.channels.ReadableByteChannel METHOD
Class:
  java.nio.channels.ReadableByteChannel

Package:
  java.nio.channels

Methods:
  public abstract int java.nio.channels.ReadableByteChannel.read(java.nio.ByteBuffer) throws java.io.IOException
  public abstract void java.nio.channels.Channel.close() throws java.io.IOException
  public abstract boolean java.nio.channels.Channel.isOpen()

```

The interface
[`java.nio.channels.ReadableByteChannel`](http://download.oracle.com/javase/7/docs/api/java/nio/channels/ReadableByteChannel.html)
defines
[`read()`](http://download.oracle.com/javase/7/docs/api/java/nio/channels/ReadableByteChannel.html#read(java.nio.ByteBuffer)). The remaining methods are inherited from a super interface. This code could
easily be modified to list only those methods that are actually declared in the
class by replacing `get*s()` with `getDeclared*s()`.

```

$ java ClassSpy ClassMember FIELD METHOD
Class:
  ClassMember

Package:
  -- No Package --

Fields:
  public static final ClassMember ClassMember.CONSTRUCTOR
  public static final ClassMember ClassMember.FIELD
  public static final ClassMember ClassMember.METHOD
  public static final ClassMember ClassMember.CLASS
  public static final ClassMember ClassMember.ALL

Methods:
  public static ClassMember ClassMember.valueOf(java.lang.String)
  public static ClassMember[] ClassMember.values()
  public final int java.lang.Enum.hashCode()
  public final int java.lang.Enum.compareTo(E)
  public int java.lang.Enum.compareTo(java.lang.Object)
  public final java.lang.String java.lang.Enum.name()
  public final boolean java.lang.Enum.equals(java.lang.Object)
  public java.lang.String java.lang.Enum.toString()
  public static <T> T java.lang.Enum.valueOf(java.lang.Class<T>,java.lang.String)
  public final java.lang.Class<E> java.lang.Enum.getDeclaringClass()
  public final int java.lang.Enum.ordinal()
  public final native java.lang.Class<?> java.lang.Object.getClass()
  public final native void java.lang.Object.wait(long) throws java.lang.InterruptedException
  public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException
  public final void java.lang.Object.wait() throws java.lang.InterruptedException
  public final native void java.lang.Object.notify()
  public final native void java.lang.Object.notifyAll()

```

In the fields portion of these results, enum constants are listed. While
these are technically fields, it might be useful to distinguish them from other
fields. This example could be modified to use
[`java.lang.reflect.Field.isEnumConstant()`](http://download.oracle.com/javase/7/docs/api/java/lang/reflect/Field.html#isEnumConstant())
for this purpose. The
[`EnumSpy`](../special/example/EnumSpy.java)
example in a later section of this trail, [Examining Enums](../special/enumMembers.html), contains a possible
implementation.

In the methods section of the output, observe that the method name includes
the name of the declaring class. Thus, the `toString()`
method is implemented by
[`Enum`](http://download.oracle.com/javase/7/docs/api/java/lang/Enum.html#toString()), not inherited from
[`Object`](http://download.oracle.com/javase/7/docs/api/java/lang/Object.html). The code could be amended to make this more obvious by using
[`Field.getDeclaringClass()`](http://download.oracle.com/javase/7/docs/api/java/lang/reflect/Field.html#getDeclaringClass()). The following fragment illustrates part of a potential solution.

```

if (mbr instanceof Field) {
    Field f = (Field)mbr;
    out.format("  %s%n", f.toGenericString());
    out.format("  -- declared in: %s%n", f.getDeclaringClass());
}

```

[« Previous](classModifiers.html)
•
[Trail](../TOC.html)
•
[Next »](classTrouble.html)

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

**Previous page:** Examining Class Modifiers and Types
  
**Next page:** Troubleshooting




A browser with JavaScript enabled is required for this page to operate properly.