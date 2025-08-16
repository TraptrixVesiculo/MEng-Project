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

Retrieving and Parsing Method Modifiers

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

[« Previous](methodType.html) • [Trail](../TOC.html) • [Next »](methodInvocation.html)

# Retrieving and Parsing Method Modifiers

There a several modifiers that may be part of a method declaration:

* Access modifiers: `public`, `protected`, and
  `private`* Modifier restricting to one instance: `static`* Modifier prohibiting value modification: `final`* Modifier requiring override: `abstract`* Modifier preventing reentrancy: `synchronized`* Modifier indicating implementation in another programming language:
            `native`* Modifier forcing strict floating point behavior: `strictfp`* Annotations

The
[`MethodModifierSpy`](example/MethodModifierSpy.java)
example lists the modifiers of a method with a given name. It also displays
whether the method is synthetic (compiler-generated), of variable arity, or a
bridge method (compiler-generated to support generic interfaces).

```


import java.lang.reflect.Method;
import java.lang.reflect.Modifier;
import static java.lang.System.out;

public class MethodModifierSpy {

    private static int count;
    private static synchronized void inc() { count++; }
    private static synchronized int cnt() { return count; }

    public static void main(String... args) {
	try {
	    Class<?> c = Class.forName(args[0]);
	    Method[] allMethods = c.getDeclaredMethods();
	    for (Method m : allMethods) {
		if (!m.getName().equals(args[1])) {
		    continue;
		}
		out.format("%s%n", m.toGenericString());
		out.format("  Modifiers:  %s%n",
			   Modifier.toString(m.getModifiers()));
		out.format("  [ synthetic=%-5b var_args=%-5b bridge=%-5b ]%n",
			   m.isSynthetic(), m.isVarArgs(), m.isBridge());
		inc();
	    }
	    out.format("%d matching overload%s found%n", cnt(),
		       (cnt() == 1 ? "" : "s"));

        // production code should handle this exception more gracefully
	} catch (ClassNotFoundException x) {
	    x.printStackTrace();
	}
    }
}

```

A few examples of the output
[`MethodMdifierSpy`](example/MethodModifierSpy.java)
produces follow.

```

$ java MethodModifierSpy java.lang.Object wait
public final native void java.lang.Object.wait(long) throws java.lang.InterruptedException
  Modifiers:  public final native
  [ synthetic=false var_args=false bridge=false ]
public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException
  Modifiers:  public final
  [ synthetic=false var_args=false bridge=false ]
public final void java.lang.Object.wait() throws java.lang.InterruptedException
  Modifiers:  public final
  [ synthetic=false var_args=false bridge=false ]
3 matching overloads found
$ java MethodModifierSpy java.lang.StrictMath toRadians
public static double java.lang.StrictMath.toRadians(double)
  Modifiers:  public static strictfp
  [ synthetic=false var_args=false bridge=false ]
1 matching overload found
$ java MethodModifierSpy MethodModifierSpy inc
private synchronized void MethodModifierSpy.inc()
  Modifiers:  private synchronized
  [ synthetic=false var_args=false bridge=false ]
1 matching overload found
$ java MethodModifierSpy java.lang.Class getConstructor
public java.lang.reflect.Constructor<T> java.lang.Class.getConstructor(java.lang.Class<T>[]) throws java.lang.NoSuchMethodException,java.lang.SecurityException
  Modifiers:  public transient
  [ synthetic=false var_args=true  bridge=false ]
1 matching overload found
$ java MethodModifierSpy java.lang.String compareTo
public int java.lang.String.compareTo(java.lang.String)
  Modifiers:  public
  [ synthetic=false var_args=false bridge=false ]
public int java.lang.String.compareTo(java.lang.Object)
  Modifiers:  public volatile
  [ synthetic=true  var_args=false bridge=true  ]
2 matching overloads found

```

Note that
[`Method.isVarArgs()`](http://download.oracle.com/javase/7/docs/api/java/lang/reflect/Method.html#isVarArgs())
returns `true` for
[`Class.getConstructor()`](http://download.oracle.com/javase/7/docs/api/java/lang/Class.html#getConstructor(java.lang.Class...)). This indicates that the method declaration looks like this:

```

public Constructor<T> getConstructor(Class<?>... parameterTypes)

```

not like this:

```

public Constructor<T> getConstructor(Class<?> [] parameterTypes)

```

Notice that the output for
[`String.compareTo()`](http://download.oracle.com/javase/7/docs/api/java/lang/String.html#compareTo(java.lang.String))
contains two methods. The method declared in `String.java`:

```

public int compareTo(String anotherString);

```

and a second *synthetic* or compiler-generated *bridge* method.
This occurs because
[`String`](http://download.oracle.com/javase/7/docs/api/java/lang/String.html)
implements the parameterized interface
[`Comparable`](http://download.oracle.com/javase/7/docs/api/java/lang/Comparable.html).
During type erasure, the argument type of the inherited method
[`Comparable.compareTo()`](http://download.oracle.com/javase/7/docs/api/java/lang/Comparable.html#compareTo(T))
is changed from `java.lang.Object` to `java.lang.String`.
Since the parameter types for the `compareTo` methods in
`Comparable` and `String` no longer match after erasure,
overriding can not occur. In all other circumstances, this would produce a
compile-time error because the interface is not implemented. The addition of
the bridge method avoids this problem.

[`Method`](http://download.oracle.com/javase/7/docs/api/java/lang/reflect/Method.html)
implements
[`java.lang.reflect.AnnotatedElement`](http://download.oracle.com/javase/7/docs/api/java/lang/reflect/AnnotatedElement.html). Thus any runtime annotations with
[`java.lang.annotation.RetentionPolicy.RUNTIME`](http://download.oracle.com/javase/7/docs/api/java/lang/annotation/RetentionPolicy.html#RUNTIME)
may be retrieved. For an example of obtaining annotations see the section [Examining Class Modifiers and Types](../class/classModifiers.html).

[« Previous](methodType.html)
•
[Trail](../TOC.html)
•
[Next »](methodInvocation.html)

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

**Previous page:** Obtaining Method Type Information
  
**Next page:** Invoking Methods




A browser with JavaScript enabled is required for this page to operate properly.