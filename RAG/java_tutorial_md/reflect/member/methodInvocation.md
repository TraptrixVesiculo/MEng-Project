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

[Obtaining Method Type Information](methodType.html)

[Retrieving and Parsing Method Modifiers](methodModifiers.html)

Invoking Methods

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

[« Previous](methodModifiers.html) • [Trail](../TOC.html) • [Next »](methodTrouble.html)

# Invoking Methods

Reflection provides a means for invoking methods on a class. Typically, this
would only be necessary if it is not possible to cast an instance of the class
to the desired type in non-reflective code. Methods are invoked with
[`java.lang.reflect.Method.invoke()`](http://download.oracle.com/javase/7/docs/api/java/lang/reflect/Method.html#invoke(java.lang.Object, java.lang.Object...)).
The first argument is the object instance on which this particular method is to
be invoked. (If the method is `static`, the first argument should
be `null`.) Subsequent arguments are the method's parameters. If
the underlying method throws an exception, it will be wrapped by an
[`java.lang.reflect.InvocationTargetException`](http://download.oracle.com/javase/7/docs/api/java/lang/reflect/InvocationTargetException.html). The method's original exception may be retrieved using the exception
chaining mechanism's
[`InvocationTargetException.getCause()`](http://download.oracle.com/javase/7/docs/api/java/lang/reflect/InvocationTargetException.html#getCause())
method.

## Finding and Invoking a Method with a Specific Declaration

Consider a test suite which uses reflection to invoke private test methods
in a given class. The
[`Deet`](example/Deet.java)
example searches for `public` methods in a class which begin with
the string "`test`", have a boolean return type, and a single
[`Locale`](http://download.oracle.com/javase/7/docs/api/java/util/Locale.html)
parameter. It then invokes each matching method.

```


import java.lang.reflect.InvocationTargetException;
import java.lang.reflect.Method;
import java.lang.reflect.Type;
import java.util.Locale;
import static java.lang.System.out;
import static java.lang.System.err;

public class Deet<T> {
    private boolean testDeet(Locale l) {
	// getISO3Language() may throw a MissingResourceException
	out.format("Locale = %s, ISO Language Code = %s%n", l.getDisplayName(), l.getISO3Language());
	return true;
    }

    private int testFoo(Locale l) { return 0; }
    private boolean testBar() { return true; }

    public static void main(String... args) {
	if (args.length != 4) {
	    err.format("Usage: java Deet <classname> <langauge> <country> <variant>%n");
	    return;
	}

	try {
	    Class<?> c = Class.forName(args[0]);
	    Object t = c.newInstance();

	    Method[] allMethods = c.getDeclaredMethods();
	    for (Method m : allMethods) {
		String mname = m.getName();
		if (!mname.startsWith("test")
		    || (m.getGenericReturnType() != boolean.class)) {
		    continue;
		}
 		Type[] pType = m.getGenericParameterTypes();
 		if ((pType.length != 1)
		    || Locale.class.isAssignableFrom(pType[0].getClass())) {
 		    continue;
 		}

		out.format("invoking %s()%n", mname);
		try {
		    m.setAccessible(true);
		    Object o = m.invoke(t, new Locale(args[1], args[2], args[3]));
		    out.format("%s() returned %b%n", mname, (Boolean) o);

		// Handle any exceptions thrown by method to be invoked.
		} catch (InvocationTargetException x) {
		    Throwable cause = x.getCause();
		    err.format("invocation of %s failed: %s%n",
			       mname, cause.getMessage());
		}
	    }

        // production code should handle these exceptions more gracefully
	} catch (ClassNotFoundException x) {
	    x.printStackTrace();
	} catch (InstantiationException x) {
	    x.printStackTrace();
	} catch (IllegalAccessException x) {
	    x.printStackTrace();
	}
    }
}

```

`Deet` invokes
[`getDeclaredMethods()`](http://download.oracle.com/javase/7/docs/api/java/lang/Class.html#getDeclaredMethods())
which will return all methods explicitly declared in the class. Also,
[`Class.isAssignableFrom()`](http://download.oracle.com/javase/7/docs/api/java/lang/Class.html#isAssignableFrom(java.lang.Class))
is used to determine whether the parameters of the located method are
compatible with the desired invocation. Technically the code could have tested
whether the following statement is `true` since
[`Locale`](http://download.oracle.com/javase/7/docs/api/java/util/Locale.html)
is `final`:

```

Locale.class == pType[0].getClass()

```

However,
[`Class.isAssignableFrom()`](http://download.oracle.com/javase/7/docs/api/java/lang/Class.html#isAssignableFrom(java.lang.Class))
is more general.

```

$ java Deet Deet ja JP JP
invoking testDeet()
Locale = Japanese (Japan,JP), ISO Language Code = jpn
testDeet() returned true
$ java Deet Deet xx XX XX
invoking testDeet()
invocation of testDeet failed: Couldn't find 3-letter language code for xx

```

First, note that only `testDeet()` meets the declaration
restrictions enforced by the code. Next, when `testDeet()` is
passed an invalid argument it throws an unchecked
[`java.util.MissingResourceException`](http://download.oracle.com/javase/7/docs/api/java/util/MissingResourceException.html). In reflection, there is no distinction in the handling of checked versus
unchecked exceptions. They are all wrapped in an
[`InvocationTargetException`](http://download.oracle.com/javase/7/docs/api/java/lang/reflect/InvocationTargetException.html)

## Invoking Methods with a Variable Number of Arguments

[`Method.invoke()`](http://download.oracle.com/javase/7/docs/api/java/lang/reflect/Method.html#invoke(java.lang.Object, java.lang.Object...))
may be used to pass a variable number of arguments to a method. The key
concept to understand is that methods of variable arity are implemented as if
the variable arguments are packed in an array.

The
[`InvokeMain`](example/InvokeMain.java)
example illustrates how to invoke the `main()` entry point in any
class and pass a set of arguments determined at runtime.

```


import java.lang.reflect.InvocationTargetException;
import java.lang.reflect.Method;
import java.util.Arrays;

public class InvokeMain {
    public static void main(String... args) {
	try {
	    Class<?> c = Class.forName(args[0]);
	    Class[] argTypes = new Class[] { String[].class };
	    Method main = c.getDeclaredMethod("main", argTypes);
  	    String[] mainArgs = Arrays.copyOfRange(args, 1, args.length);
	    System.out.format("invoking %s.main()%n", c.getName());
	    main.invoke(null, (Object)mainArgs);

        // production code should handle these exceptions more gracefully
	} catch (ClassNotFoundException x) {
	    x.printStackTrace();
	} catch (NoSuchMethodException x) {
	    x.printStackTrace();
	} catch (IllegalAccessException x) {
	    x.printStackTrace();
	} catch (InvocationTargetException x) {
	    x.printStackTrace();
	}
    }
}

```

First, to find the `main()` method the code searches for a class
with the name "main" with a single parameter that is an array of
[`String`](http://download.oracle.com/javase/7/docs/api/java/lang/String.html)
Since `main()` is `static`, `null` is the
first argument to
[`Method.invoke()`](http://download.oracle.com/javase/7/docs/api/java/lang/reflect/Method.html#invoke(java.lang.Object, java.lang.Object...)). The second argument is the array of arguments to be passed.

```

$ java InvokeMain Deet Deet ja JP JP
invoking Deet.main()
invoking testDeet()
Locale = Japanese (Japan,JP), ISO Language Code = jpn
testDeet() returned true

```

[« Previous](methodModifiers.html)
•
[Trail](../TOC.html)
•
[Next »](methodTrouble.html)

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

**Previous page:** Retrieving and Parsing Method Modifiers
  
**Next page:** Troubleshooting




A browser with JavaScript enabled is required for this page to operate properly.