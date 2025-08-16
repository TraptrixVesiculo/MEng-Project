[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** The Reflection API
  
**Lesson:** Members
  
**Section:** Fields

[Members](index.html)

[Fields](field.html)

[Obtaining Field Types](fieldTypes.html)

[Retrieving and Parsing Field Modifiers](fieldModifiers.html)

Getting and Setting Field Values

[Troubleshooting](fieldTrouble.html)

[Methods](method.html)

[Obtaining Method Type Information](methodType.html)

[Retrieving and Parsing Method Modifiers](methodModifiers.html)

[Invoking Methods](methodInvocation.html)

[Troubleshooting](methodTrouble.html)

[Constructors](ctor.html)

[Finding Constructors](ctorLocation.html)

[Retrieving and Parsing Constructor Modifiers](ctorModifiers.html)

[Creating New Class Instances](ctorInstance.html)

[Troubleshooting](ctorTrouble.html)

[Home Page](../../index.html)
>
[The Reflection API](../index.html)
>
[Members](index.html)

[« Previous](fieldModifiers.html) • [Trail](../TOC.html) • [Next »](fieldTrouble.html)

# Getting and Setting Field Values

Given an instance of a class, it is possible to use reflection to set the
values of fields in that class. This is typically done only in special
circumstances when setting the values in the usual way is not possible.
Because such access usually violates the design intentions of the class, it
should be used with the utmost discretion.

The
[`Book`](example/Book.java)
class illustrates how to set the values for long, array, and enum field types.
Methods for getting and setting other primitive types are described in
[`Field`](http://download.oracle.com/javase/7/docs/api/java/lang/reflect/Field.html#method_summary).

```


import java.lang.reflect.Field;
import java.util.Arrays;
import static java.lang.System.out;

enum Tweedle { DEE, DUM }

public class Book {
    public long chapters = 0;
    public String[] characters = { "Alice", "White Rabbit" };
    public Tweedle twin = Tweedle.DEE;

    public static void main(String... args) {
	Book book = new Book();
	String fmt = "%6S:  %-12s = %s%n";

	try {
	    Class<?> c = book.getClass();

	    Field chap = c.getDeclaredField("chapters");
	    out.format(fmt, "before", "chapters", book.chapters);
  	    chap.setLong(book, 12);
	    out.format(fmt, "after", "chapters", chap.getLong(book));

	    Field chars = c.getDeclaredField("characters");
	    out.format(fmt, "before", "characters",
		       Arrays.asList(book.characters));
	    String[] newChars = { "Queen", "King" };
	    chars.set(book, newChars);
	    out.format(fmt, "after", "characters",
		       Arrays.asList(book.characters));

	    Field t = c.getDeclaredField("twin");
	    out.format(fmt, "before", "twin", book.twin);
	    t.set(book, Tweedle.DUM);
	    out.format(fmt, "after", "twin", t.get(book));

        // production code should handle these exceptions more gracefully
	} catch (NoSuchFieldException x) {
	    x.printStackTrace();
	} catch (IllegalAccessException x) {
	    x.printStackTrace();
	}
    }
}

```

This is the corresponding output:

```

$ java Book
BEFORE:  chapters     = 0
 AFTER:  chapters     = 12
BEFORE:  characters   = [Alice, White Rabbit]
 AFTER:  characters   = [Queen, King]
BEFORE:  twin         = DEE
 AFTER:  twin         = DUM

```

---

**Note:** Setting a field's value via reflection has a certain amount of performance
overhead because various operations must occur such as validating access
permissions. From the runtime's point of view, the effects are the same, and
the operation is as atomic as if the value was changed in the class code
directly.

Use of reflection can cause some runtime optimizations to be lost. For
example, the following code is highly likely be optimized by a Java virtual
machine:

```

int x = 1;
x = 2;
x = 3;

```

Equivalent code using `Field.set*()` may not.

---

[« Previous](fieldModifiers.html)
•
[Trail](../TOC.html)
•
[Next »](fieldTrouble.html)

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

**Previous page:** Retrieving and Parsing Field Modifiers
  
**Next page:** Troubleshooting




A browser with JavaScript enabled is required for this page to operate properly.