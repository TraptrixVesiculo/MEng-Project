[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** The Reflection API
  
**Lesson:** Members
  
**Section:** Constructors

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

[Troubleshooting](methodTrouble.html)

[Constructors](ctor.html)

[Finding Constructors](ctorLocation.html)

[Retrieving and Parsing Constructor Modifiers](ctorModifiers.html)

[Creating New Class Instances](ctorInstance.html)

Troubleshooting

[Home Page](../../index.html)
>
[The Reflection API](../index.html)
>
[Members](index.html)

[« Previous](ctorInstance.html) • [Trail](../TOC.html) • [Next »](../special/index.html)

# Troubleshooting

The following problems are sometimes encountered by developers when trying
to invoke constructors via reflection.

## InstantiationException Due to Missing Zero-Argument Constructor

The
[`ConstructorTrouble`](example/ConstructorTrouble.java)
example illustrates what happens when code attempts to create a new instance of
a class using
[`Class.newInstance()`](http://download.oracle.com/javase/7/docs/api/java/lang/Class.html#newInstance())
and there is no accessible zero-argument constructor:

```


public class ConstructorTrouble {
    private ConstructorTrouble(int i) {}

    public static void main(String... args){
	try {
	    Class<?> c = Class.forName("ConstructorTrouble");
	    Object o = c.newInstance();  // InstantiationException

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

```

$ java ConstructorTrouble
java.lang.InstantiationException: ConstructorTrouble
        at java.lang.Class.newInstance0(Class.java:340)
        at java.lang.Class.newInstance(Class.java:308)
        at ConstructorTrouble.main(ConstructorTrouble.java:7)

```

---

**Tip:** There a number of different reasons an
[`InstantiationException`](http://download.oracle.com/javase/7/docs/api/java/lang/InstantiationException.html)
can occur. In this case, the problem is that the presence of the constructor
with an `int` argument prevents the compiler from generating the
default (or zero-argument) constructor and there is no explicit zero-argument
constructor in the code. Remember that
[`Class.newInstance()`](http://download.oracle.com/javase/7/docs/api/java/lang/Class.html#newInstance())
behaves very much like the `new` keyword and will fail whenever
`new` would fail.

---

## Class.newInstance() Throws Unexpected Exception

The
[`ConstructorTroubleToo`](example/ConstructorTroubleToo.java)
example shows an unresolvable problem in
[`Class.newInstance()`](http://download.oracle.com/javase/7/docs/api/java/lang/Class.html#newInstance()). Namely, it propagates any exception — checked or unchecked —
thrown by the constructor.

```


import java.lang.reflect.InvocationTargetException;
import static java.lang.System.err;

public class ConstructorTroubleToo {
    public ConstructorTroubleToo() {
 	throw new RuntimeException("exception in constructor");
    }

    public static void main(String... args) {
	try {
	    Class<?> c = Class.forName("ConstructorTroubleToo");
	    // Method propagetes any exception thrown by the constructor
	    // (including checked exceptions).
	    if (args.length > 0 && args[0].equals("class")) {
		Object o = c.newInstance();
	    } else {
		Object o = c.getConstructor().newInstance();
	    }

        // production code should handle these exceptions more gracefully
	} catch (ClassNotFoundException x) {
	    x.printStackTrace();
	} catch (InstantiationException x) {
	    x.printStackTrace();
	} catch (IllegalAccessException x) {
	    x.printStackTrace();
	} catch (NoSuchMethodException x) {
	    x.printStackTrace();
	} catch (InvocationTargetException x) {
	    x.printStackTrace();
	    err.format("%n%nCaught exception: %s%n", x.getCause());
	}
    }
}

```

```

$ java ConstructorTroubleToo class
Exception in thread "main" java.lang.RuntimeException: exception in constructor
        at ConstructorTroubleToo.<init>(ConstructorTroubleToo.java:6)
        at sun.reflect.NativeConstructorAccessorImpl.newInstance0(Native Method)
        at sun.reflect.NativeConstructorAccessorImpl.newInstance(NativeConstructorAccessorImpl.java:39)
        at sun.reflect.DelegatingConstructorAccessorImpl.newInstance(DelegatingConstructorAccessorImpl.java:27)
        at java.lang.reflect.Constructor.newInstance(Constructor.java:513)
        at java.lang.Class.newInstance0(Class.java:355)
        at java.lang.Class.newInstance(Class.java:308)
        at ConstructorTroubleToo.main(ConstructorTroubleToo.java:15)

```

This situation is unique to reflection. Normally, it is impossible to
write code which ignores a checked exception because it would not compile. It
is possible to wrap any exception thrown by a constructor by using
[`Constructor.newInstance()`](http://download.oracle.com/javase/7/docs/api/java/lang/reflect/Constructor.html#newInstance(java.lang.Object...))
rather than
[`Class.newInstance()`](http://download.oracle.com/javase/7/docs/api/java/lang/Class.html#newInstance()).

```

$ java ConstructorTroubleToo
java.lang.reflect.InvocationTargetException
        at sun.reflect.NativeConstructorAccessorImpl.newInstance0(Native Method)
        at sun.reflect.NativeConstructorAccessorImpl.newInstance(NativeConstructorAccessorImpl.java:39)
        at sun.reflect.DelegatingConstructorAccessorImpl.newInstance(DelegatingConstructorAccessorImpl.java:27)
        at java.lang.reflect.Constructor.newInstance(Constructor.java:513)
        at ConstructorTroubleToo.main(ConstructorTroubleToo.java:17)
Caused by: java.lang.RuntimeException: exception in constructor
        at ConstructorTroubleToo.<init>(ConstructorTroubleToo.java:6)
        ... 5 more


Caught exception: java.lang.RuntimeException: exception in constructor

```

If an
[`InvocationTargetException`](http://download.oracle.com/javase/7/docs/api/java/lang/reflect/InvocationTargetException.html)
is thrown, the method was invoked. Diagnosis of the problem would be the same
as if the constructor was called directly and threw the exception that is
retrieved by
[`InvocationTargetException.getCause()`](http://download.oracle.com/javase/7/docs/api/java/lang/reflect/InvocationTargetException.html#getCause()). This exception does not indicate a problem with the reflection package or
its usage.

---

**Tip:** It is preferable to use
[`Constructor.newInstance()`](http://download.oracle.com/javase/7/docs/api/java/lang/reflect/Constructor.html#newInstance(java.lang.Object...))
over
[`Class.newInstance()`](http://download.oracle.com/javase/7/docs/api/java/lang/Class.html#newInstance())
because the former API permits examination and handling of arbitrary
exceptions thrown by constructors.

---

## Problems Locating or Invoking the Correct Constructor

The
[`ConstructorTroubleAgain`](example/ConstructorTroubleAgain.java)
class illustrates various ways in which incorrect code can fail to locate or
invoke the expected constructor.

```


import java.lang.reflect.InvocationTargetException;
import static java.lang.System.out;

public class ConstructorTroubleAgain {
    public ConstructorTroubleAgain() {}

    public ConstructorTroubleAgain(Integer i) {}

    public ConstructorTroubleAgain(Object o) {
	out.format("Constructor passed Object%n");
    }

    public ConstructorTroubleAgain(String s) {
	out.format("Constructor passed String%n");
    }

    public static void main(String... args){
	String argType = (args.length == 0 ? "" : args[0]);
	try {
	    Class<?> c = Class.forName("ConstructorTroubleAgain");
	    if ("".equals(argType)) {
		// IllegalArgumentException: wrong number of arguments
		Object o = c.getConstructor().newInstance("foo");
	    } else if ("int".equals(argType)) {
		// NoSuchMethodException - looking for int, have Integer
		Object o = c.getConstructor(int.class);
	    } else if ("Object".equals(argType)) {
		// newInstance() does not perform method resolution
		Object o = c.getConstructor(Object.class).newInstance("foo");
	    } else {
		assert false;
	    }

        // production code should handle these exceptions more gracefully
	} catch (ClassNotFoundException x) {
	    x.printStackTrace();
	} catch (NoSuchMethodException x) {
	    x.printStackTrace();
	} catch (InvocationTargetException x) {
	    x.printStackTrace();
	} catch (InstantiationException x) {
	    x.printStackTrace();
	} catch (IllegalAccessException x) {
	    x.printStackTrace();
	}
    }
}

```

```

$ java ConstructorTroubleAgain
Exception in thread "main" java.lang.IllegalArgumentException: wrong number of arguments
        at sun.reflect.NativeConstructorAccessorImpl.newInstance0(Native Method)
        at sun.reflect.NativeConstructorAccessorImpl.newInstance(NativeConstructorAccessorImpl.java:39)
        at sun.reflect.DelegatingConstructorAccessorImpl.newInstance(DelegatingConstructorAccessorImpl.java:27)
        at java.lang.reflect.Constructor.newInstance(Constructor.java:513)
        at ConstructorTroubleAgain.main(ConstructorTroubleAgain.java:23)

```

An
[`IllegalArgumentException`](http://download.oracle.com/javase/7/docs/api/java/lang/IllegalArgumentException.html)
is thrown because the zero-argument constructor was requested and an attempt
was made to pass an argument. The same exception would be thrown if the
constructor was passed an argument of the wrong type.

```

$ java ConstructorTroubleAgain int
java.lang.NoSuchMethodException: ConstructorTroubleAgain.<init>(int)
        at java.lang.Class.getConstructor0(Class.java:2706)
        at java.lang.Class.getConstructor(Class.java:1657)
        at ConstructorTroubleAgain.main(ConstructorTroubleAgain.java:26)

```

This exception may occur if the developer mistakenly believes that
reflection will autobox or unbox types. Boxing (conversion of a primitive to a
reference type) occurs only during compilation. There is no opportunity in
reflection for this operation to occur, so the specific type must be used when
locating a constructor.

```

$ java ConstructorTroubleAgain Object
Constructor passed Object

```

Here, it might be expected that the constructor taking a
[`String`](http://download.oracle.com/javase/7/docs/api/java/lang/String.html)
argument would be invoked since `newInstance()` was invoked
with the more specific `String` type. However it is too
late! The constructor which was found is already the constructor with
an
[`Object`](http://download.oracle.com/javase/7/docs/api/java/lang/Object.html)
argument. `newInstance()` makes no attempt to do method
resolution; it simply operates on the existing constructor object.

---

**Tip:** An important difference between `new` and
[`Constructor.newInstance()`](http://download.oracle.com/javase/7/docs/api/java/lang/reflect/Constructor.html#newInstance(java.lang.Object...))
is that `new` performs method argument type checking, boxing, and
method resolution. None of these occur in reflection, where explicit choices
must be made.

---

## IllegalAccessException When Attempting to Invoke an Inaccessible Constructor

An
[`IllegalAccessException`](http://download.oracle.com/javase/7/docs/api/java/lang/IllegalAccessException.html)
may be thrown if an attempt is made to invoke a private or otherwise
inaccessible constructor. The
[`ConstructorTroubleAccess`](example/ConstructorTroubleAccess.java)
example illustrates the resulting stack trace.

```


import java.lang.reflect.Constructor;
import java.lang.reflect.InvocationTargetException;

class Deny {
    private Deny() {
	System.out.format("Deny constructor%n");
    }
}

public class ConstructorTroubleAccess {
    public static void main(String... args) {
	try {
	    Constructor c = Deny.class.getDeclaredConstructor();
//  	    c.setAccessible(true);   // solution
	    c.newInstance();

        // production code should handle these exceptions more gracefully
	} catch (InvocationTargetException x) {
	    x.printStackTrace();
	} catch (NoSuchMethodException x) {
	    x.printStackTrace();
	} catch (InstantiationException x) {
	    x.printStackTrace();
	} catch (IllegalAccessException x) {
	    x.printStackTrace();
	}
    }
}

```

```

$ java ConstructorTroubleAccess
java.lang.IllegalAccessException: Class ConstructorTroubleAccess can not access a member of class Deny with modifiers "private"
        at sun.reflect.Reflection.ensureMemberAccess(Reflection.java:65)
        at java.lang.reflect.Constructor.newInstance(Constructor.java:505)
        at ConstructorTroubleAccess.main(ConstructorTroubleAccess.java:15)

```

---

**Tip:** An access restriction exists which prevents reflective invocation of
constructors which normally would not be accessible via direct invocation.
(This includes---but is not limited to---private constructors in a separate
class and public constructors in a separate private class.) However,
`Constructor` is declared to extend
[`AccessibleObject`](http://download.oracle.com/javase/7/docs/api/java/lang/reflect/AccessibleObject.html)
which provides the ability to suppress this check via
[`AccessibleObject.setAccessible()`](http://download.oracle.com/javase/7/docs/api/java/lang/reflect/AccessibleObject.html#setAccessible(boolean)).

---

[« Previous](ctorInstance.html)
•
[Trail](../TOC.html)
•
[Next »](../special/index.html)

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

**Previous page:** Creating New Class Instances
  
**Next page:** Arrays and Enumerated Types




A browser with JavaScript enabled is required for this page to operate properly.