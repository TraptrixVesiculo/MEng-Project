[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** The Reflection API
  
**Lesson:** Classes
  
**Section:** Sealing Packages in Extensions

[Classes](index.html)

[Retrieving Class Objects](classNew.html)

Examining Class Modifiers and Types

[Discovering Class Members](classMembers.html)

[Troubleshooting](classTrouble.html)

[Home Page](../../index.html)
>
[The Reflection API](../index.html)
>
[Classes](index.html)

[« Previous](classNew.html) • [Trail](../TOC.html) • [Next »](classMembers.html)

# Examining Class Modifiers and Types

A class may be declared with one or more modifiers which affect its runtime
behavior:

* Access modifiers: `public`, `protected`, and
  `private`* Modifier requiring override: `abstract`* Modifier restricting to one instance: `static`* Modifier prohibiting value modification: `final`* Modifier forcing strict floating point behavior: `strictfp`* Annotations

Not all modifiers are allowed on all classes, for example an interface cannot
be `final` and an enum cannot be `abstract`.
[`java.lang.reflect.Modifier`](http://download.oracle.com/javase/7/docs/api/java/lang/reflect/Modifier.html)
contains declarations for all possible modifiers. It also contains methods
which may be used to decode the set of modifiers returned by
[`Class.getModifiers()`](http://download.oracle.com/javase/7/docs/api/java/lang/Class.html#getModifiers()).

The
[`ClassDeclarationSpy`](example/ClassDeclarationSpy.java)
example shows how to obtain the declaration components of a class including the
modifiers, generic type parameters, implemented interfaces, and the inheritance
path. Since
[`Class`](http://download.oracle.com/javase/7/docs/api/java/lang/Class.html)
implements the
[`java.lang.reflect.AnnotatedElement`](http://download.oracle.com/javase/7/docs/api/java/lang/reflect/AnnotatedElement.html)
interface it is also possible to query the runtime annotations.

```


import java.lang.annotation.Annotation;
import java.lang.reflect.Modifier;
import java.lang.reflect.Type;
import java.lang.reflect.TypeVariable;
import java.util.Arrays;
import java.util.ArrayList;
import java.util.List;
import static java.lang.System.out;

public class ClassDeclarationSpy {
    public static void main(String... args) {
	try {
	    Class<?> c = Class.forName(args[0]);
	    out.format("Class:%n  %s%n%n", c.getCanonicalName());
	    out.format("Modifiers:%n  %s%n%n",
		       Modifier.toString(c.getModifiers()));

	    out.format("Type Parameters:%n");
	    TypeVariable[] tv = c.getTypeParameters();
	    if (tv.length != 0) {
		out.format("  ");
		for (TypeVariable t : tv)
		    out.format("%s ", t.getName());
		out.format("%n%n");
	    } else {
		out.format("  -- No Type Parameters --%n%n");
	    }

	    out.format("Implemented Interfaces:%n");
	    Type[] intfs = c.getGenericInterfaces();
	    if (intfs.length != 0) {
		for (Type intf : intfs)
		    out.format("  %s%n", intf.toString());
		out.format("%n");
	    } else {
		out.format("  -- No Implemented Interfaces --%n%n");
	    }

	    out.format("Inheritance Path:%n");
	    List<Class> l = new ArrayList<Class>();
	    printAncestor(c, l);
	    if (l.size() != 0) {
		for (Class<?> cl : l)
		    out.format("  %s%n", cl.getCanonicalName());
		out.format("%n");
	    } else {
		out.format("  -- No Super Classes --%n%n");
	    }

	    out.format("Annotations:%n");
	    Annotation[] ann = c.getAnnotations();
	    if (ann.length != 0) {
		for (Annotation a : ann)
		    out.format("  %s%n", a.toString());
		out.format("%n");
	    } else {
		out.format("  -- No Annotations --%n%n");
	    }

        // production code should handle this exception more gracefully
	} catch (ClassNotFoundException x) {
	    x.printStackTrace();
	}
    }

    private static void printAncestor(Class<?> c, List<Class> l) {
	Class<?> ancestor = c.getSuperclass();
 	if (ancestor != null) {
	    l.add(ancestor);
	    printAncestor(ancestor, l);
 	}
    }
}

```

A few samples of the output follows. User input is in italics.

```

$ java ClassDeclarationSpy java.util.concurrent.ConcurrentNavigableMap
Class:
  java.util.concurrent.ConcurrentNavigableMap

Modifiers:
  public abstract interface

Type Parameters:
  K V

Implemented Interfaces:
  java.util.concurrent.ConcurrentMap<K, V>
  java.util.NavigableMap<K, V>

Inheritance Path:
  -- No Super Classes --

Annotations:
  -- No Annotations --

```

This is the actual declaration for
[`java.util.concurrent.ConcurrentNavigableMap`](http://download.oracle.com/javase/7/docs/api/java/util/concurrent/ConcurrentNavigableMap.html)
in the source code:

```

public interface ConcurrentNavigableMap<K,V>
    extends ConcurrentMap, NavigableMap<K,V>

```

Note that since this is an interface, it is implicitly `abstract`.
The compiler adds this modifier for every interface. Also, this declaration
contains two generic type parameters, `K` and `V`. The
example code simply prints the names of these parameters, but is it possible to
retrieve additional information about them using methods in
[`java.lang.reflect.TypeVariable`](http://download.oracle.com/javase/7/docs/api/java/lang/reflect/TypeVariable.html).
Interfaces may also implement other interfaces as shown above.

```

$ java ClassDeclarationSpy "[Ljava.lang.String;"
Class:
  java.lang.String[]

Modifiers:
  public abstract final

Type Parameters:
  -- No Type Parameters --

Implemented Interfaces:
  interface java.lang.Cloneable
  interface java.io.Serializable

Inheritance Path:
  java.lang.Object

Annotations:
  -- No Annotations --

```

Since arrays are runtime objects, all of the type information is defined by the
Java virtual machine. In particular, arrays implement
[`Cloneable`](http://download.oracle.com/javase/7/docs/api/java/lang/Cloneable.html)
and
[`java.io.Serializable`](http://download.oracle.com/javase/7/docs/api/java/io/Serializable.html)
and their direct superclass is always
[`Object`](http://download.oracle.com/javase/7/docs/api/java/lang/Object.html).

```

$ java ClassDeclarationSpy java.io.InterruptedIOException
Class:
  java.io.InterruptedIOException

Modifiers:
  public

Type Parameters:
  -- No Type Parameters --

Implemented Interfaces:
  -- No Implemented Interfaces --

Inheritance Path:
  java.io.IOException
  java.lang.Exception
  java.lang.Throwable
  java.lang.Object

Annotations:
  -- No Annotations --

```

From the inheritance path, it may be deduced that
[`java.io.InterruptedIOException`](http://download.oracle.com/javase/7/docs/api/java/io/InterruptedIOException.html)
is a checked exception because
[`RuntimeException`](http://download.oracle.com/javase/7/docs/api/java/lang/RuntimeException.html)
is not present.

```

$ java ClassDeclarationSpy java.security.Identity
Class:
  java.security.Identity

Modifiers:
  public abstract

Type Parameters:
  -- No Type Parameters --

Implemented Interfaces:
  interface java.security.Principal
  interface java.io.Serializable

Inheritance Path:
  java.lang.Object

Annotations:
  @java.lang.Deprecated()

```

This output shows that
[`java.security.Identity`](http://download.oracle.com/javase/7/docs/api/java/security/Identity.html), a deprecated API, possesses the annotation
[`java.lang.Deprecated`](http://download.oracle.com/javase/7/docs/api/java/lang/Deprecated.html). This may be used by reflective code to detect deprecated APIs.

---

**Note:** Not all annotations are available via reflection. Only those which
have a
[`java.lang.annotation.RetentionPolicy`](http://download.oracle.com/javase/7/docs/api/java/lang/annotation/RetentionPolicy.html)
of
[`RUNTIME`](http://download.oracle.com/javase/7/docs/api/java/lang/annotation/RetentionPolicy.html#RUNTIME)
are accessible. Of the three annotations pre-defined in the language
[`@Deprecated`](http://download.oracle.com/javase/7/docs/api/java/lang/Deprecated.html),
[`@Override`](http://download.oracle.com/javase/7/docs/api/java/lang/Override.html), and
[`@SuppressWarnings`](http://download.oracle.com/javase/7/docs/api/java/lang/SuppressWarnings.html)
only
[`@Deprecated`](http://download.oracle.com/javase/7/docs/api/java/lang/Deprecated.html)
is available at runtime.

---

[« Previous](classNew.html)
•
[Trail](../TOC.html)
•
[Next »](classMembers.html)

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

**Previous page:** Retrieving Class Objects
  
**Next page:** Discovering Class Members




A browser with JavaScript enabled is required for this page to operate properly.