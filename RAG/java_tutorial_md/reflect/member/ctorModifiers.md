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

Retrieving and Parsing Constructor Modifiers

[Creating New Class Instances](ctorInstance.html)

[Troubleshooting](ctorTrouble.html)

[Home Page](../../index.html)
>
[The Reflection API](../index.html)
>
[Members](index.html)

[« Previous](ctorLocation.html) • [Trail](../TOC.html) • [Next »](ctorInstance.html)

# Retrieving and Parsing Constructor Modifiers

Because of the role of constructors in the language, fewer modifiers are
meaningful than for methods:

* Access modifiers: `public`, `protected`, and
  `private`* Annotations

The
[`ConstructorAccess`](example/ConstructorAccess.java)
example searches for constructors in a given class with the specified access
modifier. It also displays whether the constructor is synthetic
(compiler-generated) or of variable arity.

```


import java.lang.reflect.Constructor;
import java.lang.reflect.Modifier;
import java.lang.reflect.Type;
import static java.lang.System.out;

public class ConstructorAccess {
    public static void main(String... args) {
	try {
	    Class<?> c = Class.forName(args[0]);
	    Constructor[] allConstructors = c.getDeclaredConstructors();
	    for (Constructor ctor : allConstructors) {
		int searchMod = modifierFromString(args[1]);
		int mods = accessModifiers(ctor.getModifiers());
		if (searchMod == mods) {
		    out.format("%s%n", ctor.toGenericString());
		    out.format("  [ synthetic=%-5b var_args=%-5b ]%n",
			       ctor.isSynthetic(), ctor.isVarArgs());
		}
	    }

        // production code should handle this exception more gracefully
	} catch (ClassNotFoundException x) {
	    x.printStackTrace();
	}
    }

    private static int accessModifiers(int m) {
	return m & (Modifier.PUBLIC | Modifier.PRIVATE | Modifier.PROTECTED);
    }

    private static int modifierFromString(String s) {
	if ("public".equals(s))               return Modifier.PUBLIC;
	else if ("protected".equals(s))       return Modifier.PROTECTED;
	else if ("private".equals(s))         return Modifier.PRIVATE;
	else if ("package-private".equals(s)) return 0;
	else return -1;
    }
}

```

There is not an explicit
[`Modifier`](http://download.oracle.com/javase/7/docs/api/java/lang/reflect/Modifier.html)
constant which corresponds to "package-private" access, so it is necessary to
check for the absence of all three access modifiers to identify a
package-private constructor.

This output shows the private constructors in
[`java.io.File`](http://download.oracle.com/javase/7/docs/api/java/io/File.html):

```

$ java ConstructorAccess java.io.File private
private java.io.File(java.lang.String,int)
  [ synthetic=false var_args=false ]
private java.io.File(java.lang.String,java.io.File)
  [ synthetic=false var_args=false ]

```

Synthetic constructors are rare; however the
[`SyntheticConstructor`](example/SyntheticConstructor.java)
example illustrates a typical situation where this may occur:

```


public class SyntheticConstructor {
    private SyntheticConstructor() {}
    class Inner {
	// Compiler will generate a synthetic constructor since
	// SyntheticConstructor() is private.
	Inner() { new SyntheticConstructor(); }
    }
}

```

```

$ java ConstructorAccess SyntheticConstructor package-private
SyntheticConstructor(SyntheticConstructor$1)
  [ synthetic=true  var_args=false ]

```

Since the inner class's constructor references the private constructor of
the enclosing class, the compiler must generate a package-private constructor.
The parameter type `SyntheticConstructor$1` is arbitrary and
dependent on the compiler implementation. Code which depends on the presence
of any synthetic or non-public class members may not be portable.

Constructors implement
[`java.lang.reflect.AnnotatedElement`](http://download.oracle.com/javase/7/docs/api/java/lang/reflect/AnnotatedElement.html), which provides methods to retrieve runtime annotations with
[`java.lang.annotation.RetentionPolicy.RUNTIME`](http://download.oracle.com/javase/7/docs/api/java/lang/annotation/RetentionPolicy.html#RUNTIME). For an example of obtaining annotations see the [Examining Class Modifiers and Types](../class/classModifiers.html)
section.

[« Previous](ctorLocation.html)
•
[Trail](../TOC.html)
•
[Next »](ctorInstance.html)

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

**Previous page:** Finding Constructors
  
**Next page:** Creating New Class Instances




A browser with JavaScript enabled is required for this page to operate properly.