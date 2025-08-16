[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** The Reflection API
  
**Lesson:** Arrays and Enumerated Types
  
**Section:** Arrays

[Arrays and Enumerated Types](index.html)

[Arrays](array.html)

Identifying Array Types

[Creating New Arrays](arrayInstance.html)

[Getting and Setting Arrays and Their Components](arraySetGet.html)

[Troubleshooting](arrayTrouble.html)

[Enumerated Types](enum.html)

[Examining Enums](enumMembers.html)

[Getting and Setting Fields with Enum Types](enumSetGet.html)

[Troubleshooting](enumTrouble.html)

[Home Page](../../index.html)
>
[The Reflection API](../index.html)
>
[Arrays and Enumerated Types](index.html)

[« Previous](array.html) • [Trail](../TOC.html) • [Next »](arrayInstance.html)

# Identifying Array Types

Array types may be identified by invoking
[`Class.isArray()`](http://download.oracle.com/javase/7/docs/api/java/lang/Class.html#isArray()). To obtain a
[`Class`](http://download.oracle.com/javase/7/docs/api/java/lang/Class.html)
use one of the methods described in [Retrieving Class Objects](../class/classNew.html) section of
this trail.

The
[`ArrayFind`](example/ArrayFind.java)
example identifies the fields in the named class that are of array type and
reports the component type for each of them.

```


import java.lang.reflect.Field;
import java.lang.reflect.Type;
import static java.lang.System.out;

public class ArrayFind {
    public static void main(String... args) {
	boolean found = false;
 	try {
	    Class<?> cls = Class.forName(args[0]);
	    Field[] flds = cls.getDeclaredFields();
	    for (Field f : flds) {
 		Class<?> c = f.getType();
		if (c.isArray()) {
		    found = true;
		    out.format("%s%n"
                               + "           Field: %s%n"
			       + "            Type: %s%n"
			       + "  Component Type: %s%n",
			       f, f.getName(), c, c.getComponentType());
		}
	    }
	    if (!found) {
		out.format("No array fields%n");
	    }

        // production code should handle this exception more gracefully
 	} catch (ClassNotFoundException x) {
	    x.printStackTrace();
	}
    }
}

```

The syntax for the returned value of `Class.get*Type()` is
described in
[`Class.getName()`](http://download.oracle.com/javase/7/docs/api/java/lang/Class.html#getName()). The number of '`[`' characters at the beginning of the type name
indicates the number of dimensions (i.e. depth of nesting) of the array.

Samples of the output follows. User input is in italics. An array of primitive type `byte`:

```

$ java ArrayFind java.nio.ByteBuffer
final byte[] java.nio.ByteBuffer.hb
           Field: hb
            Type: class [B
  Component Type: byte

```

An array of reference type
[`StackTraceElement`](http://download.oracle.com/javase/7/docs/api/java/lang/StackTraceElement.html):

```

$ java ArrayFind java.lang.Throwable
private java.lang.StackTraceElement[] java.lang.Throwable.stackTrace
           Field: stackTrace
            Type: class [Ljava.lang.StackTraceElement;
  Component Type: class java.lang.StackTraceElement

```

`predefined` is a one-dimensional array of reference type
[`java.awt.Cursor`](http://download.oracle.com/javase/7/docs/api/java/awt/Cursor.html)
and `cursorProperties` is a two-dimensional array of reference type
[`String`](http://download.oracle.com/javase/7/docs/api/java/lang/String.html):

```

$ java ArrayFind java.awt.Cursor
protected static java.awt.Cursor[] java.awt.Cursor.predefined
           Field: predefined
            Type: class [Ljava.awt.Cursor;
  Component Type: class java.awt.Cursor
static final java.lang.String[][] java.awt.Cursor.cursorProperties
           Field: cursorProperties
            Type: class [[Ljava.lang.String;
  Component Type: class [Ljava.lang.String;

```

[« Previous](array.html)
•
[Trail](../TOC.html)
•
[Next »](arrayInstance.html)

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

**Previous page:** Arrays
  
**Next page:** Creating New Arrays




A browser with JavaScript enabled is required for this page to operate properly.