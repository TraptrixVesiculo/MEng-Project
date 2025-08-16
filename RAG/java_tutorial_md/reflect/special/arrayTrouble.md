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

[Identifying Array Types](arrayComponents.html)

[Creating New Arrays](arrayInstance.html)

[Getting and Setting Arrays and Their Components](arraySetGet.html)

Troubleshooting

[Enumerated Types](enum.html)

[Examining Enums](enumMembers.html)

[Getting and Setting Fields with Enum Types](enumSetGet.html)

[Troubleshooting](enumTrouble.html)

[Home Page](../../index.html)
>
[The Reflection API](../index.html)
>
[Arrays and Enumerated Types](index.html)

[« Previous](arraySetGet.html) • [Trail](../TOC.html) • [Next »](enum.html)

# Troubleshooting

The following examples show typical errors which may occur when operating on
arrays.

### IllegalArgumentException due to Inconvertible Types

The
[`ArrayTroubleAgain`](example/ArrayTroubleAgain.java)
example will generate an
[`IllegalArgumentException`](http://download.oracle.com/javase/7/docs/api/java/lang/IllegalArgumentException.html).
[`Array.setInt()`](http://download.oracle.com/javase/7/docs/api/java/lang/reflect/Array.html#setInt(java.lang.Object, int, int))
is invoked to set a component that is of the reference type
`Integer` with a value of primitive type `int`. In the
non-reflection equivalent `ary[0] = 1`, the compiler would convert
(or *box*) the value `1` to a reference type as `new
Integer(1)` so that its type checking will accept the statement. When
using reflection, type checking only occurs at runtime so there is no
opportunity to box the value.

```


import java.lang.reflect.Array;
import static java.lang.System.err;

public class ArrayTroubleAgain {
    public static void main(String... args) {
	Integer[] ary = new Integer[2];
	try {
	    Array.setInt(ary, 0, 1);  // IllegalArgumentException

        // production code should handle these exceptions more gracefully
	} catch (IllegalArgumentException x) {
	    err.format("Unable to box%n");
	} catch (ArrayIndexOutOfBoundsException x) {
	    x.printStackTrace();
	}
    }
}

```

```

$ java ArrayTroubleAgain
Unable to box

```

To eliminate this exception, the problematic line should be replaced
by the following invocation of
[`Array.set(Object array, int index, Object value)`](http://download.oracle.com/javase/7/docs/api/java/lang/reflect/Array.html#set(java.lang.Object, int, java.lang.Object)):

```

Array.set(ary, 0, new Integer(1));

```

---

**Tip:** When using reflection to set or get an array component, the compiler does not
have an opportunity to perform boxing. It can only convert types that are
related as described by the specification for
[`Class.isAssignableFrom()`](http://download.oracle.com/javase/7/docs/api/java/lang/Class.html#isAssignableFrom(java.lang.Class)). The example is expected to fail because `isAssignableFrom()` will
return `false` in this test which can be used programmatically to
verify whether a particular conversion is possible:

```

Integer.class.isAssignableFrom(int.class) == false

```

Similarly, automatic conversion from primitive to reference type is also
impossible in reflection.

```

int.class.isAssignableFrom(Integer.class) == false

```

---

### ArrayIndexOutOfBoundsException for Empty Arrays

The
[`ArrayTrouble`](example/ArrayTrouble.java)
example illustrates an error which will occur if an attempt is made to access
the elements of an array of zero length:

```


import java.lang.reflect.Array;
import static java.lang.System.out;

public class ArrayTrouble {
    public static void main(String... args) {
        Object o = Array.newInstance(int.class, 0);
        int[] i = (int[])o;
        int[] j = new int[0];
        out.format("i.length = %d, j.length = %d, args.length = %d%n",
                   i.length, j.length, args.length);
        Array.getInt(o, 0);  // ArrayIndexOutOfBoundsException
    }
}

```

```

$ java ArrayTrouble
i.length = 0, j.length = 0, args.length = 0
Exception in thread "main" java.lang.ArrayIndexOutOfBoundsException
        at java.lang.reflect.Array.getInt(Native Method)
        at ArrayTrouble.main(ArrayTrouble.java:11)

```

---

**Tip:** It is possible to have arrays with no elements (empty arrays). There
are only a few cases in common code where they are seen but they can
occur in reflection inadvertently. Of course, it is not possible to
set/get the values of an empty array because an
[`ArrayIndexOutOfBoundsException`](http://download.oracle.com/javase/7/docs/api/java/lang/ArrayIndexOutOfBoundsException.html)
will be thrown.

---

### IllegalArgumentException if Narrowing is Attempted

The
[`ArrayTroubleToo`](example/ArrayTroubleToo.java)
example contains code which fails because it attempts perform an operation
which could potentially lose data:

```


import java.lang.reflect.Array;
import static java.lang.System.out;

public class ArrayTroubleToo {
    public static void main(String... args) {
        Object o = new int[2];
        Array.setShort(o, 0, (short)2);  // widening, succeeds
        Array.setLong(o, 1, 2L);         // narrowing, fails
    }
}

```

```

$ java ArrayTroubleToo
Exception in thread "main" java.lang.IllegalArgumentException: argument type mismatch
        at java.lang.reflect.Array.setLong(Native Method)
        at ArrayTroubleToo.main(ArrayTroubleToo.java:9)

```

---

**Tip:** 
The `Array.set*()` and `Array.get*()` methods will
perform automatic widening conversion but will throw an
[`IllegalArgumentException`](http://download.oracle.com/javase/7/docs/api/java/lang/IllegalArgumentException.html)
if a narrowing conversion is attempted. For complete discussion of
widening and narrowing conversions, see [*The
Java Language Specification, Third Edition*](http://java.sun.com/docs/books/jls/third_edition/html/j3TOC.html), sections [5.1.2](http://java.sun.com/docs/books/jls/third_edition/html/conversions.html#5.1.2)
and [5.1.3](http://java.sun.com/docs/books/jls/third_edition/html/conversions.html#5.1.3) respectively.

---

[« Previous](arraySetGet.html)
•
[Trail](../TOC.html)
•
[Next »](enum.html)

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

**Previous page:** Getting and Setting Arrays and Their Components
  
**Next page:** Enumerated Types




A browser with JavaScript enabled is required for this page to operate properly.