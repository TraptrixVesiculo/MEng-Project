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

[Getting and Setting Field Values](fieldValues.html)

Troubleshooting

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

[« Previous](fieldValues.html) • [Trail](../TOC.html) • [Next »](method.html)

# Troubleshooting

Here are a few common problems encountered by developers with explanations
for why the occur and how to resolve them.

## IllegalArgumentException due to Inconvertible Types

The
[`FieldTrouble`](example/FieldTrouble.java)
example will generate an
[`IllegalArgumentException`](http://download.oracle.com/javase/7/docs/api/java/lang/IllegalArgumentException.html).
[`Field.setInt()`](http://download.oracle.com/javase/7/docs/api/java/lang/reflect/Field.html#setInt(java.lang.Object, int))
is invoked to set a field that is of the reference type `Integer`
with a value of primitive type. In the non-reflection equivalent
`Integer val = 42`, the compiler would convert (or *box*)
the primitive type `42` to a reference type as `new
Integer(42)` so that its type checking will accept the statement. When
using reflection, type checking only occurs at runtime so there is no
opportunity to box the value.

```


import java.lang.reflect.Field;

public class FieldTrouble {
    public Integer val;

    public static void main(String... args) {
	FieldTrouble ft = new FieldTrouble();
	try {
	    Class<?> c = ft.getClass();
	    Field f = c.getDeclaredField("val");
  	    f.setInt(ft, 42);               // IllegalArgumentException

        // production code should handle these exceptions more gracefully
	} catch (NoSuchFieldException x) {
	    x.printStackTrace();
 	} catch (IllegalAccessException x) {
 	    x.printStackTrace();
	}
    }
}

```

```

$ java FieldTrouble
Exception in thread "main" java.lang.IllegalArgumentException: Can not set
java.lang.Object field FieldTrouble.val to (long)42
        at sun.reflect.UnsafeFieldAccessorImpl.throwSetIllegalArgumentException(UnsafeFieldAccessorImpl.java:146)
        at sun.reflect.UnsafeFieldAccessorImpl.throwSetIllegalArgumentException(UnsafeFieldAccessorImpl.java:174)
        at sun.reflect.UnsafeObjectFieldAccessorImpl.setLong(UnsafeObjectFieldAccessorImpl.java:102)
        at java.lang.reflect.Field.setLong(Field.java:831)
        at FieldTrouble.main(FieldTrouble.java:11)

```

To eliminate this exception, the problematic line should be replaced
by the following invocation of
[`Field.set(Object obj, Object value)`](http://download.oracle.com/javase/7/docs/api/java/lang/reflect/Field.html#set(java.lang.Object, java.lang.Object)):

```

f.set(ft, new Integer(43));

```

---

**Tip:** When using reflection to set or get a field, the compiler does not have
an opportunity to perform boxing. It can only convert types that are related
as described by the specification for
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

## NoSuchFieldException for Non-Public Fields

The astute reader may notice that if the
[`FieldSpy`](example/FieldSpy.java)
example shown earlier is used to get information on a non-public field, it
will fail:

```

$ java FieldSpy java.lang.String count
java.lang.NoSuchFieldException: count
        at java.lang.Class.getField(Class.java:1519)
        at FieldSpy.main(FieldSpy.java:12)

```

---

**Tip:** The
[`Class.getField()`](http://download.oracle.com/javase/7/docs/api/java/lang/Class.html#getField(java.lang.String))
and
[`Class.getFields()`](http://download.oracle.com/javase/7/docs/api/java/lang/Class.html#getFields())
methods return the *public* member field(s) of the class, enum, or
interface represented by the `Class` object. To retrieve all fields
declared (but not inherited) in the `Class`, use the
[`Class.getDeclaredFields()`](http://download.oracle.com/javase/7/docs/api/java/lang/Class.html#getDeclaredFields())
method.

---

## IllegalAccessException when Modifying Final Fields

An
[`IllegalAccessException`](http://download.oracle.com/javase/7/docs/api/java/lang/IllegalAccessException.html)
may be thrown if an attempt is made to get or set the value of a
`private` or otherwise inaccessible field or to set the value of a
`final` field (regardless of its access modifiers).

The
[`FieldTroubleToo`](example/FieldTroubleToo.java)
example illustrates the type of stack trace which results from attempting to
set a final field.

```


import java.lang.reflect.Field;

public class FieldTroubleToo {
    public final boolean b = true;

    public static void main(String... args) {
	FieldTroubleToo ft = new FieldTroubleToo();
	try {
	    Class<?> c = ft.getClass();
	    Field f = c.getDeclaredField("b");
// 	    f.setAccessible(true);  // solution
	    f.setBoolean(ft, Boolean.FALSE);   // IllegalAccessException

        // production code should handle these exceptions more gracefully
	} catch (NoSuchFieldException x) {
	    x.printStackTrace();
	} catch (IllegalArgumentException x) {
	    x.printStackTrace();
	} catch (IllegalAccessException x) {
	    x.printStackTrace();
	}
    }
}

```

```

$ java FieldTroubleToo
java.lang.IllegalAccessException: Can not set final boolean field FieldTroubleToo.b to (boolean)false
        at sun.reflect.UnsafeFieldAccessorImpl.throwFinalFieldIllegalAccessException(UnsafeFieldAccessorImpl.java:55)
        at sun.reflect.UnsafeFieldAccessorImpl.throwFinalFieldIllegalAccessException(UnsafeFieldAccessorImpl.java:63)
        at sun.reflect.UnsafeQualifiedBooleanFieldAccessorImpl.setBoolean(UnsafeQualifiedBooleanFieldAccessorImpl.java:78)
        at java.lang.reflect.Field.setBoolean(Field.java:686)
        at FieldTroubleToo.main(FieldTroubleToo.java:12)

```

---

**Tip:** An access restriction exists which prevents `final` fields from
being set after initialization of the class. However, `Field` is
declared to extend
[`AccessibleObject`](http://download.oracle.com/javase/7/docs/api/java/lang/reflect/AccessibleObject.html)
which provides the ability to suppress this check.

If
[`AccessibleObject.setAccessible()`](http://download.oracle.com/javase/7/docs/api/java/lang/reflect/AccessibleObject.html#setAccessible(boolean))
succeeds, then subsequent operations on this field value will not fail do to
this problem. This may have unexpected side-effects; for example, sometimes
the original value will continue to be used by some sections of the application
even though the value has been modified.
[`AccessibleObject.setAccessible()`](http://download.oracle.com/javase/7/docs/api/java/lang/reflect/AccessibleObject.html#setAccessible(boolean))
will only succeed if the operation is allowed by the security context.

---

[« Previous](fieldValues.html)
•
[Trail](../TOC.html)
•
[Next »](method.html)

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

**Previous page:** Getting and Setting Field Values
  
**Next page:** Methods




A browser with JavaScript enabled is required for this page to operate properly.