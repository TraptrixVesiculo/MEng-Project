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

Obtaining Field Types

[Retrieving and Parsing Field Modifiers](fieldModifiers.html)

[Getting and Setting Field Values](fieldValues.html)

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

[« Previous](field.html) • [Trail](../TOC.html) • [Next »](fieldModifiers.html)

# Obtaining Field Types

A field may be either of primitive or reference type. There are eight
primitive types: `boolean`, `byte`, `short`,
`int`, `long`, `char`, `float`, and
`double`. A reference type is anything that is a direct or indirect
subclass of
[`java.lang.Object`](http://download.oracle.com/javase/7/docs/api/java/lang/Object.html)
including interfaces, arrays, and enumerated types.

The
[`FieldSpy`](example/FieldSpy.java)
example prints the field's type and generic type given a fully-qualified
binary class name and field name.

```


import java.lang.reflect.Field;
import java.util.List;

public class FieldSpy<T> {
    public boolean[][] b = {{ false, false }, { true, true } };
    public String name  = "Alice";
    public List<Integer> list;
    public T val;

    public static void main(String... args) {
	try {
	    Class<?> c = Class.forName(args[0]);
	    Field f = c.getField(args[1]);
	    System.out.format("Type: %s%n", f.getType());
	    System.out.format("GenericType: %s%n", f.getGenericType());

        // production code should handle these exceptions more gracefully
	} catch (ClassNotFoundException x) {
	    x.printStackTrace();
	} catch (NoSuchFieldException x) {
	    x.printStackTrace();
	}
    }
}

```

Sample output to retrieve the type of the three public fields in this class
(`b`, `name`, and the parameterized type
`list`), follows. User input is in italics.

```

$ java FieldSpy FieldSpy b
Type: class [[Z
GenericType: class [[Z
$ java FieldSpy FieldSpy name
Type: class java.lang.String
GenericType: class java.lang.String
$ java FieldSpy FieldSpy list
Type: interface java.util.List
GenericType: java.util.List<java.lang.Integer>
$ java FieldSpy FieldSpy val
Type: class java.lang.Object
GenericType: T

```

The type for the field `b` is two-dimensional array of
boolean. The syntax for the type name is described in
[`Class.getName()`](http://download.oracle.com/javase/7/docs/api/java/lang/Class.html#getName()).

The type for the field `val` is reported as
`java.lang.Object` because generics are implemented via *type
erasure* which removes all information regarding generic types during
compilation. Thus `T` is replaced by the upper bound of the type
variable, in this case, `java.lang.Object`.

[`Field.getGenericType()`](http://download.oracle.com/javase/7/docs/api/java/lang/reflect/Field.html#getGenericType())
will consult the
[Signature Attribute](http://java.sun.com/docs/books/vmspec/2nd-edition/ClassFileFormat-Java5.pdf)
in the class file if it's present. If the attribute isn't available, it falls
back on
[`Field.getType()`](http://download.oracle.com/javase/7/docs/api/java/lang/reflect/Field.html#getType())
which was not changed by the introduction of generics. The other methods in
reflection with name `getGenericFoo` for some value of
*Foo* are implemented similarly.

[« Previous](field.html)
•
[Trail](../TOC.html)
•
[Next »](fieldModifiers.html)

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

**Previous page:** Fields
  
**Next page:** Retrieving and Parsing Field Modifiers




A browser with JavaScript enabled is required for this page to operate properly.