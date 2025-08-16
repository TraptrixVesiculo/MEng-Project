[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** The Reflection API
  
**Lesson:** Members
  
**Section:** Methods

[Members](index.html)

[Fields](field.html)

[Obtaining Field Types](fieldTypes.html)

[Retrieving and Parsing Field Modifiers](fieldModifiers.html)

[Getting and Setting Field Values](fieldValues.html)

[Troubleshooting](fieldTrouble.html)

[Methods](method.html)

Obtaining Method Type Information

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

[« Previous](method.html) • [Trail](../TOC.html) • [Next »](methodModifiers.html)

# Obtaining Method Type Information

A method declaration includes the name, modifiers, parameters, return type,
and list of throwable exceptions. The
[`java.lang.reflect.Method`](http://download.oracle.com/javase/7/docs/api/java/lang/reflect/Method.html)
class provides a way to obtain this information.

The
[`MethodSpy`](example/MethodSpy.java)
example illustrates how to enumerate all of the declared methods in a given
class and retrieve the return, parameter, and exception types for all the
methods of the given name.

```


import java.lang.reflect.Method;
import java.lang.reflect.Type;
import static java.lang.System.out;

public class MethodSpy {
    private static final String  fmt = "%24s: %s%n";

    // for the morbidly curious
    <E extends RuntimeException> void genericThrow() throws E {}

    public static void main(String... args) {
	try {
	    Class<?> c = Class.forName(args[0]);
	    Method[] allMethods = c.getDeclaredMethods();
	    for (Method m : allMethods) {
		if (!m.getName().equals(args[1])) {
		    continue;
		}
		out.format("%s%n", m.toGenericString());

		out.format(fmt, "ReturnType", m.getReturnType());
		out.format(fmt, "GenericReturnType", m.getGenericReturnType());

		Class<?>[] pType  = m.getParameterTypes();
		Type[] gpType = m.getGenericParameterTypes();
		for (int i = 0; i < pType.length; i++) {
		    out.format(fmt,"ParameterType", pType[i]);
		    out.format(fmt,"GenericParameterType", gpType[i]);
		}

		Class<?>[] xType  = m.getExceptionTypes();
		Type[] gxType = m.getGenericExceptionTypes();
		for (int i = 0; i < xType.length; i++) {
		    out.format(fmt,"ExceptionType", xType[i]);
		    out.format(fmt,"GenericExceptionType", gxType[i]);
		}
	    }

        // production code should handle these exceptions more gracefully
	} catch (ClassNotFoundException x) {
	    x.printStackTrace();
	}
    }
}

```

Here is the output for
[`Class.getConstructor()`](http://download.oracle.com/javase/7/docs/api/java/lang/Class.html#getConstructor(java.lang.Class...))
which is an example of a method with parameterized types and a variable number
of parameters.

```

$ java MethodSpy java.lang.Class getConstructor
public java.lang.reflect.Constructor<T> java.lang.Class.getConstructor(java.lang.Class<?>[]) throws java.lang.NoSuchMethodException,java.lang.SecurityException
              ReturnType: class java.lang.reflect.Constructor
       GenericReturnType: java.lang.reflect.Constructor<T>
           ParameterType: class [Ljava.lang.Class;
    GenericParameterType: java.lang.Class<?>[]
           ExceptionType: class java.lang.NoSuchMethodException
    GenericExceptionType: class java.lang.NoSuchMethodException
           ExceptionType: class java.lang.SecurityException
    GenericExceptionType: class java.lang.SecurityException

```

This is the actual declaration of the method in source code:

```

public Constructor<T> getConstructor(Class<?>... parameterTypes)

```

First note that the return and parameter types are generic.
[`Method.getGenericReturnType()`](http://download.oracle.com/javase/7/docs/api/java/lang/reflect/Method.html#getGenericReturnType())
will consult the
[Signature Attribute](http://java.sun.com/docs/books/vmspec/2nd-edition/ClassFileFormat-Java5.pdf)
in the class file if it's present. If the attribute isn't available, it falls
back on
[`Method.getReturnType()`](http://download.oracle.com/javase/7/docs/api/java/lang/reflect/Method.html#getReturnType())
which was not changed by the introduction of generics. The other methods with
name `getGenericFoo()` for some value of *Foo* in
reflection are implemented similarly.

Next, notice that the last (and only) parameter,
`parameterType`, is of variable arity (has a variable number of
parameters) of type `java.lang.Class`. It is represented as a
single-dimension array of type `java.lang.Class`. This can be
distinguished from a parameter that is explicitly an array of
`java.lang.Class` by invoking
[`Method.isVarArgs()`](http://download.oracle.com/javase/7/docs/api/java/lang/reflect/Method.html#isVarArgs()). The syntax for the returned values of `Method.get*Types()` is
described in
[`Class.getName()`](http://download.oracle.com/javase/7/docs/api/java/lang/Class.html#getName()).

The following example illustrates a method with a generic return type.

```

$ java MethodSpy java.lang.Class cast
public T java.lang.Class.cast(java.lang.Object)
              ReturnType: class java.lang.Object
       GenericReturnType: T
           ParameterType: class java.lang.Object
    GenericParameterType: class java.lang.Object

```

The generic return type for the method
[`Class.cast()`](http://download.oracle.com/javase/7/docs/api/java/lang/Class.html#cast(java.lang.Object))
is reported as `java.lang.Object` because generics are implemented
via *type erasure* which removes all information regarding generic types
during compilation. The erasure of `T` is defined by the
declaration of
[`Class`](http://download.oracle.com/javase/7/docs/api/java/lang/Class.html):

```

public final class Class<T> implements ...

```

Thus `T` is replaced by the upper bound of the type variable, in
this case, `java.lang.Object`.

The last example illustrates the output for a method with multiple
overloads.

```

$ java MethodSpy java.io.PrintStream format
public java.io.PrintStream java.io.PrintStream.format(java.util.Locale,java.lang.String,java.lang.Object[])
              ReturnType: class java.io.PrintStream
       GenericReturnType: class java.io.PrintStream
           ParameterType: class java.util.Locale
    GenericParameterType: class java.util.Locale
           ParameterType: class java.lang.String
    GenericParameterType: class java.lang.String
           ParameterType: class [Ljava.lang.Object;
    GenericParameterType: class [Ljava.lang.Object;
public java.io.PrintStream java.io.PrintStream.format(java.lang.String,java.lang.Object[])
              ReturnType: class java.io.PrintStream
       GenericReturnType: class java.io.PrintStream
           ParameterType: class java.lang.String
    GenericParameterType: class java.lang.String
           ParameterType: class [Ljava.lang.Object;
    GenericParameterType: class [Ljava.lang.Object;

```

If multiple overloads of the same method name are discovered, they are all
returned by
[`Class.getDeclaredMethods()`](http://download.oracle.com/javase/7/docs/api/java/lang/Class.html#getDeclaredMethods()).
Since `format()` has two overloads (with with a
[`Locale`](http://download.oracle.com/javase/7/docs/api/java/util/Locale.html)
and one without), both are shown by `MethodSpy`.

---

**Note:** [`Method.getGenericExceptionTypes()`](http://download.oracle.com/javase/7/docs/api/java/lang/reflect/Method.html#getGenericExceptionTypes())
exists because it is actually possible to declare a method with a generic
exception type. However this is rarely used since it is not possible to
catch a generic exception type.

---

[« Previous](method.html)
•
[Trail](../TOC.html)
•
[Next »](methodModifiers.html)

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

**Previous page:** Methods
  
**Next page:** Retrieving and Parsing Method Modifiers




A browser with JavaScript enabled is required for this page to operate properly.