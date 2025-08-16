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

[Invoking Methods](methodInvocation.html)

Troubleshooting

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

[« Previous](methodInvocation.html) • [Trail](../TOC.html) • [Next »](ctor.html)

# Troubleshooting

This section contains examples of problems developers might encounter when
using reflection to locate, invoke, or get information about methods.

## NoSuchMethodException Due to Type Erasure

The
[`MethodTrouble`](example/MethodTrouble.java)
example illustrates what happens when type erasure is not taken into
consideration by code which searches for a particular method in a class.

```


import java.lang.reflect.Method;

public class MethodTrouble<T>  {
    public void lookup(T t) {}
    public void find(Integer i) {}

    public static void main(String... args) {
	try {
	    String mName = args[0];
	    Class cArg = Class.forName(args[1]);
	    Class<?> c = (new MethodTrouble<Integer>()).getClass();
	    Method m = c.getMethod(mName, cArg);
	    System.out.format("Found:%n  %s%n", m.toGenericString());

        // production code should handle these exceptions more gracefully
	} catch (NoSuchMethodException x) {
	    x.printStackTrace();
	} catch (ClassNotFoundException x) {
	    x.printStackTrace();
	}
    }
}

```

```

$ java MethodTrouble lookup java.lang.Integer
java.lang.NoSuchMethodException: MethodTrouble.lookup(java.lang.Integer)
        at java.lang.Class.getMethod(Class.java:1605)
        at MethodTrouble.main(MethodTrouble.java:12)
$ java MethodTrouble lookup java.lang.Object
Found:
  public void MethodTrouble.lookup(T)

```

When a method is declared with a generic parameter type, the compiler will
replace the generic type with its upper bound, in this case, the upper bound of
`T` is
[`Object`](http://download.oracle.com/javase/7/docs/api/java/lang/Object.html). Thus, when the code searches for `lookup(Integer)`, no
method is found, despite the fact that the instance of
`MethodTrouble` was created as follows:

```

Class c = (new MethodTrouble()).getClass();

```

Searching for `lookup(Object)` succeeds as expected.

```

$ java MethodTrouble find java.lang.Integer
Found:
  public void MethodTrouble.find(java.lang.Integer)
$ java MethodTrouble find java.lang.Object
java.lang.NoSuchMethodException: MethodTrouble.find(java.lang.Object)
        at java.lang.Class.getMethod(Class.java:1605)
        at MethodTrouble.main(MethodTrouble.java:12)

```

In this case, `find()` has no generic parameters, so
the parameter types searched for by
[`getMethod()`](http://download.oracle.com/javase/7/docs/api/java/lang/Class.html#getMethod(java.lang.String, java.lang.Class...))
must match exactly.

---

**Tip:** Always pass the upper bound of the parameterized type when searching for a
method.

---

## IllegalAccessException when Invoking a Method

An
[`IllegalAccessException`](http://download.oracle.com/javase/7/docs/api/java/lang/IllegalAccessException.html)
is thrown if an attempt is made to invoke a `private` or
otherwise inaccessible method.

The
[`MethodTroubleAgain`](example/MethodTroubleAgain.java)
example shows a typical stack trace which results from trying to invoke a
private method in an another class.

```


import java.lang.reflect.InvocationTargetException;
import java.lang.reflect.Method;

class AnotherClass {
    private void m() {}
}

public class MethodTroubleAgain {
    public static void main(String... args) {
	AnotherClass ac = new AnotherClass();
	try {
	    Class<?> c = ac.getClass();
 	    Method m = c.getDeclaredMethod("m");
//  	    m.setAccessible(true);      // solution
 	    Object o = m.invoke(ac);    // IllegalAccessException

        // production code should handle these exceptions more gracefully
	} catch (NoSuchMethodException x) {
	    x.printStackTrace();
	} catch (InvocationTargetException x) {
	    x.printStackTrace();
	} catch (IllegalAccessException x) {
	    x.printStackTrace();
	}
    }
}

```

The stack trace for the exception thrown follows.

```

$ java MethodTroubleAgain
java.lang.IllegalAccessException: Class MethodTroubleAgain can not access a member of class AnotherClass with modifiers "private"
        at sun.reflect.Reflection.ensureMemberAccess(Reflection.java:65)
        at java.lang.reflect.Method.invoke(Method.java:588)
        at MethodTroubleAgain.main(MethodTroubleAgain.java:15)

```

---

**Tip:** An access restriction exists which prevents reflective invocation of methods
which normally would not be accessible via direct invocation. (This
includes---but is not limited to---`private` methods in a separate
class and public methods in a separate private class.) However,
`Method` is declared to extend
[`AccessibleObject`](http://download.oracle.com/javase/7/docs/api/java/lang/reflect/AccessibleObject.html)
which provides the ability to suppress this check via
[`AccessibleObject.setAccessible()`](http://download.oracle.com/javase/7/docs/api/java/lang/reflect/AccessibleObject.html#setAccessible(boolean)). If it succeeds, then subsequent invocations of this method object will not
fail due to this problem.

---

## IllegalArgumentException from Method.invoke()

[`Method.invoke()`](http://download.oracle.com/javase/7/docs/api/java/lang/reflect/Method.html#invoke(java.lang.Object, java.lang.Object...))
has been retrofitted to be a variable-arity method. This is an enormous
convenience, however it can lead to unexpected behavior. The
[`MethodTroubleToo`](example/MethodTroubleToo.java)
example shows various ways in which
[`Method.invoke()`](http://download.oracle.com/javase/7/docs/api/java/lang/reflect/Method.html#invoke(java.lang.Object, java.lang.Object...))
can produce confusing results.

```


import java.lang.reflect.Method;

public class MethodTroubleToo {
    public void ping() { System.out.format("PONG!%n"); }

    public static void main(String... args) {
	try {
	    MethodTroubleToo mtt = new MethodTroubleToo();
	    Method m = MethodTroubleToo.class.getMethod("ping");

 	    switch(Integer.parseInt(args[0])) {
	    case 0:
  		m.invoke(mtt);                 // works
		break;
	    case 1:
 		m.invoke(mtt, null);           // works (expect compiler warning)
		break;
	    case 2:
		Object arg2 = null;
		m.invoke(mtt, arg2);           // IllegalArgumentException
		break;
	    case 3:
		m.invoke(mtt, new Object[0]);  // works
		break;
	    case 4:
		Object arg4 = new Object[0];
		m.invoke(mtt, arg4);           // IllegalArgumentException
		break;
	    default:
		System.out.format("Test not found%n");
	    }

        // production code should handle these exceptions more gracefully
	} catch (Exception x) {
	    x.printStackTrace();
	}
    }
}

```

```

$ java MethodTroubleToo 0
PONG!

```

Since all of the parameters of
[`Method.invoke()`](http://download.oracle.com/javase/7/docs/api/java/lang/reflect/Method.html#invoke(java.lang.Object, java.lang.Object...))
are optional except for the first, they can be omitted when the method to be
invoked has no parameters.

```

$ java MethodTroubleToo 1
PONG!

```

The code in this case generates this compiler warning because
`null` is ambiguous.

```

$ javac MethodTroubleToo.java
MethodTroubleToo.java:16: warning: non-varargs call of varargs method with inexact argument type for last parameter;
cast to java.lang.Object for a varargs call
cast to java.lang.Object[] for a non-varargs call and to suppress this warning
                m.invoke(mtt, null);           // works (expect compiler warning)
                              ^
1 warning

```

It is not possible to determine whether `null` represents an
empty array of arguments or a first argument of `null`.

```

$ java MethodTroubleToo 2
java.lang.IllegalArgumentException: wrong number of arguments
        at sun.reflect.NativeMethodAccessorImpl.invoke0(Native Method)
        at sun.reflect.NativeMethodAccessorImpl.invoke(NativeMethodAccessorImpl.java:39)
        at sun.reflect.DelegatingMethodAccessorImpl.invoke(DelegatingMethodAccessorImpl.java:25)
        at java.lang.reflect.Method.invoke(Method.java:597)
        at MethodTroubleToo.main(MethodTroubleToo.java:21)

```

This fails despite the fact that the argument is `null`, because
the type is a
[`Object`](http://download.oracle.com/javase/7/docs/api/java/lang/Object.html)
and `ping()` expects no arguments at all.

```

$ java MethodTroubleToo 3
PONG!

```

This works because `new Object[0]` creates an empty array, and
to a varargs method, this is equivalent to not passing any of the optional
arguments.

```

$ java MethodTroubleToo 4
java.lang.IllegalArgumentException: wrong number of arguments
        at sun.reflect.NativeMethodAccessorImpl.invoke0(Native Method)
        at sun.reflect.NativeMethodAccessorImpl.invoke(NativeMethodAccessorImpl.java:39)
        at sun.reflect.DelegatingMethodAccessorImpl.invoke(DelegatingMethodAccessorImpl.java:25)
        at java.lang.reflect.Method.invoke(Method.java:597)
        at MethodTroubleToo.main(MethodTroubleToo.java:28)

```

Unlike the previous example, if the empty array is stored in an
[`Object`](http://download.oracle.com/javase/7/docs/api/java/lang/Object.html), then it is treated as an
[`Object`](http://download.oracle.com/javase/7/docs/api/java/lang/Object.html). This fails for the same reason that case 2 fails, `ping()`
does not expect an argument.

---

**Tip:** When a method `foo(Object... o)` is declared the compiler will put
all of the arguments passed to `foo()` in an array of type
[`Object`](http://download.oracle.com/javase/7/docs/api/java/lang/Object.html). The implementation of `foo()` is the same as if it were declared
`foo(Object[] o)`. Understanding this may help avoid the types of
problems illustrated above.

---

## InvocationTargetException when Invoked Method Fails

An
[`InvocationTargetException`](http://download.oracle.com/javase/7/docs/api/java/lang/reflect/InvocationTargetException.html)
wraps all exceptions (checked and unchecked) produced when a method object
is invoked. The
[`MethodTroubleReturns`](example/MethodTroubleReturns.java)
example shows how to retrieve the original exception thrown by the invoked
method.

```


import java.lang.reflect.InvocationTargetException;
import java.lang.reflect.Method;

public class MethodTroubleReturns {
    private void drinkMe(int liters) {
	if (liters < 0)
	    throw new IllegalArgumentException("I can't drink a negative amount of liquid");
    }

    public static void main(String... args) {
	try {
	    MethodTroubleReturns mtr  = new MethodTroubleReturns();
 	    Class<?> c = mtr.getClass();
   	    Method m = c.getDeclaredMethod("drinkMe", int.class);
	    m.invoke(mtr, -1);

        // production code should handle these exceptions more gracefully
	} catch (InvocationTargetException x) {
	    Throwable cause = x.getCause();
	    System.err.format("drinkMe() failed: %s%n", cause.getMessage());
	} catch (Exception x) {
	    x.printStackTrace();
	}
    }
}

```

```

$ java MethodTroubleReturns
drinkMe() failed: I can't drink a negative amount of liquid

```

---

**Tip:** If an
[`InvocationTargetException`](http://download.oracle.com/javase/7/docs/api/java/lang/reflect/InvocationTargetException.html)
is thrown, the method was invoked. Diagnosis of the problem would be the same
as if the method was called directly and threw the exception that is retrieved
by
[`getCause()`](http://download.oracle.com/javase/7/docs/api/java/lang/reflect/InvocationTargetException.html#getCause()). This exception does not indicate a problem with the reflection package or
its usage.

---

[« Previous](methodInvocation.html)
•
[Trail](../TOC.html)
•
[Next »](ctor.html)

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

**Previous page:** Invoking Methods
  
**Next page:** Constructors




A browser with JavaScript enabled is required for this page to operate properly.