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

[Examining Class Modifiers and Types](classModifiers.html)

[Discovering Class Members](classMembers.html)

Troubleshooting

[Home Page](../../index.html)
>
[The Reflection API](../index.html)
>
[Classes](index.html)

[« Previous](classMembers.html) • [Trail](../TOC.html) • [Next »](../member/index.html)

# Troubleshooting

The following examples show typical errors which may be encountered when
reflecting on classes.

## Compiler Warning: "Note: ... uses unchecked or unsafe operations"

When a method is invoked, the types of the argument values are checked and
possibly converted.
[`ClassWarning`](example/ClassWarning.java)
invokes
[`getMethod()`](http://download.oracle.com/javase/7/docs/api/java/lang/Class.html#getMethod(java.lang.String, java.lang.Class...))
to cause a typical unchecked conversion warning:

```


import java.lang.reflect.Method;

public class ClassWarning {
    void m() {
	try {
	    Class c = ClassWarning.class;
	    Method m = c.getMethod("m");  // warning

        // production code should handle this exception more gracefully
	} catch (NoSuchMethodException x) {
    	    x.printStackTrace();
    	}
    }
}

```

```

$ javac ClassWarning.java
Note: ClassWarning.java uses unchecked or unsafe operations.
Note: Recompile with -Xlint:unchecked for details.
$ javac -Xlint:unchecked ClassWarning.java
ClassWarning.java:7: warning: [unchecked] unchecked call to getMethod(java.lang.String,java.lang.Class<?>...) as a member of the raw type java.lang.Class
            Method m = c.getMethod("m");  // warning
                                  ^
1 warning

```

Many library methods have been retrofitted with generic declarations including
several in
[`Class`](http://download.oracle.com/javase/7/docs/api/java/lang/Class.html). Since `c` is declared as a *raw* type (has no type
parameters) and the corresponding parameter of
[`getMethod()`](http://download.oracle.com/javase/7/docs/api/java/lang/Class.html#getMethod(java.lang.String, java.lang.Class...))
is a parameterized type, an unchecked conversion occurs. The compiler is
required to generate a warning. (See [*The
Java Language Specification, Third Edition*](http://java.sun.com/docs/books/jls/third_edition/html/j3TOC.html), sections [5.1.9](http://java.sun.com/docs/books/jls/third_edition/html/conversions.html#5.1.9)
and [5.3](http://java.sun.com/docs/books/jls/third_edition/html/conversions.html#5.1.9).)

There are two possible solutions. The more preferable it to modify the
declaration of `c` to include an appropriate generic type. In this
case, the declaration should be:

```

Class<?> c = warn.getClass();

```

Alternatively, the warning could be explicitly suppressed using the predefined
annotation
[`@SuppressWarnings`](http://download.oracle.com/javase/7/docs/api/java/lang/SuppressWarnings.html)
preceding the problematic statement.

```

Class c = ClassWarning.class;
@SuppressWarnings("unchecked")
Method m = c.getMethod("m");  // warning gone

```

---

**Tip:** As a general principle, warnings should not be ignored as they may indicate the
presence of a bug. Parameterized declarations should be used as appropriate.
If that is not possible (perhaps because an application must interact with a
library vendor's code), annotate the offending line using
[`@SuppressWarnings`](http://download.oracle.com/javase/7/docs/api/java/lang/SuppressWarnings.html).

---

## InstantiationException when the Constructor is Not Accessible

[`Class.newInstance()`](http://download.oracle.com/javase/7/docs/api/java/lang/Class.html#newInstance())
will throw an
[`InstantiationException`](http://download.oracle.com/javase/7/docs/api/java/lang/InstantiationException.html)
if an attempt is made to create a new instance of the class and the
zero-argument constructor is not visible. The
[`ClassTrouble`](example/ClassTrouble.java)
example illustrates the resulting stack trace.

```


class Cls {
    private Cls() {}
}

public class ClassTrouble {
    public static void main(String... args) {
	try {
	    Class<?> c = Class.forName("Cls");
	    c.newInstance();  // InstantiationException

        // production code should handle these exceptions more gracefully
	} catch (InstantiationException x) {
	    x.printStackTrace();
	} catch (IllegalAccessException x) {
	    x.printStackTrace();
	} catch (ClassNotFoundException x) {
	    x.printStackTrace();
	}
    }
}

```

```

$ java ClassTrouble
java.lang.IllegalAccessException: Class ClassTrouble can not access a member of
class Cls with modifiers "private"
        at sun.reflect.Reflection.ensureMemberAccess(Reflection.java:65)
        at java.lang.Class.newInstance0(Class.java:349)
        at java.lang.Class.newInstance(Class.java:308)
        at ClassTrouble.main(ClassTrouble.java:9)

```

[`Class.newInstance()`](http://download.oracle.com/javase/7/docs/api/java/lang/Class.html#newInstance())
behaves very much like the `new` keyword and will fail for the same
reasons `new` would fail. The typical solution in reflection is to
take advantage of the
[`java.lang.reflect.AccessibleObject`](http://download.oracle.com/javase/7/docs/api/java/lang/reflect/AccessibleObject.html)
class which provides the ability to suppress access control checks; however,
this approach will not work because
[`java.lang.Class`](http://download.oracle.com/javase/7/docs/api/java/lang/Class.html)
does not extend
[`AccessibleObject`](http://download.oracle.com/javase/7/docs/api/java/lang/reflect/AccessibleObject.html). The only solution is to modify the code to use
[`Constructor.newInstance()`](http://download.oracle.com/javase/7/docs/api/java/lang/reflect/Constructor.html#newInstance(java.lang.Object...))
which does extend
[`AccessibleObject`](http://download.oracle.com/javase/7/docs/api/java/lang/reflect/AccessibleObject.html).

---

**Tip:** In general, it is preferable to use
[`Constructor.newInstance()`](http://download.oracle.com/javase/7/docs/api/java/lang/reflect/Constructor.html#newInstance(java.lang.Object...))
for the reasons described in the
[Creating New Class Instances](../member/ctorInstance.html)
section in the [Members](../member/index.html) lesson.

---

Additional examples of potential problems using
[`Constructor.newInstance()`](http://download.oracle.com/javase/7/docs/api/java/lang/reflect/Constructor.html#newInstance(java.lang.Object...))
may be found in the
[Constructor Troubleshooting](../member/ctorTrouble.html)
section of the [Members](../member/index.html) lesson.

[« Previous](classMembers.html)
•
[Trail](../TOC.html)
•
[Next »](../member/index.html)

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

**Previous page:** Discovering Class Members
  
**Next page:** Members




A browser with JavaScript enabled is required for this page to operate properly.