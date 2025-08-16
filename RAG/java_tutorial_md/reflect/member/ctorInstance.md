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

Creating New Class Instances

[Troubleshooting](ctorTrouble.html)

[Home Page](../../index.html)
>
[The Reflection API](../index.html)
>
[Members](index.html)

[« Previous](ctorModifiers.html) • [Trail](../TOC.html) • [Next »](ctorTrouble.html)

# Creating New Class Instances

There are two reflective methods for creating instances of classes:
[`java.lang.reflect.Constructor.newInstance()`](http://download.oracle.com/javase/7/docs/api/java/lang/reflect/Constructor.html#newInstance(java.lang.Object...))
and
[`Class.newInstance()`](http://download.oracle.com/javase/7/docs/api/java/lang/Class.html#newInstance()). The former is preferred and is thus used in these examples because:

* [`Class.newInstance()`](http://download.oracle.com/javase/7/docs/api/java/lang/Class.html#newInstance())
  can only invoke the zero-argument constructor, while
  [`Constructor.newInstance()`](http://download.oracle.com/javase/7/docs/api/java/lang/reflect/Constructor.html#newInstance(java.lang.Object...))
  may invoke any constructor, regardless of the number of parameters.* [`Class.newInstance()`](http://download.oracle.com/javase/7/docs/api/java/lang/Class.html#newInstance())
    throws any exception thrown by the constructor, regardless of whether it is
    checked or unchecked.
    [`InvocationTargetException`](http://download.oracle.com/javase/7/docs/api/java/lang/reflect/InvocationTargetException.html).* [`Class.newInstance()`](http://download.oracle.com/javase/7/docs/api/java/lang/Class.html#newInstance())
      requires that the constructor be visible;
      [`Constructor.newInstance()`](http://download.oracle.com/javase/7/docs/api/java/lang/reflect/Constructor.html#newInstance(java.lang.Object...))
      may invoke `private` constructors under certain circumstances.

Sometimes it may be desirable to retrieve internal state from an object
which is only set after construction. Consider a scenario where it is
necessary to obtain the internal character set used by
[`java.io.Console`](http://download.oracle.com/javase/7/docs/api/java/io/Console.html). (The `Console` character set is stored in an private field and is
not necessarily the same as the Java virtual machine default character set
returned by
[`java.nio.charset.Charset.defaultCharset()`](http://download.oracle.com/javase/7/docs/api/java/nio/charset/Charset.html#defaultCharset())). The
[`ConsoleCharset`](example/ConsoleCharset.java)
example shows how this might be achieved:

```


import java.io.Console;
import java.nio.charset.Charset;
import java.lang.reflect.Constructor;
import java.lang.reflect.Field;
import java.lang.reflect.InvocationTargetException;
import static java.lang.System.out;

public class ConsoleCharset {
    public static void main(String... args) {
	Constructor[] ctors = Console.class.getDeclaredConstructors();
	Constructor ctor = null;
	for (int i = 0; i < ctors.length; i++) {
	    ctor = ctors[i];
	    if (ctor.getGenericParameterTypes().length == 0)
		break;
	}

	try {
	    ctor.setAccessible(true);
 	    Console c = (Console)ctor.newInstance();
	    Field f = c.getClass().getDeclaredField("cs");
	    f.setAccessible(true);
	    out.format("Console charset         :  %s%n", f.get(c));
	    out.format("Charset.defaultCharset():  %s%n",
		       Charset.defaultCharset());

        // production code should handle these exceptions more gracefully
	} catch (InstantiationException x) {
	    x.printStackTrace();
 	} catch (InvocationTargetException x) {
 	    x.printStackTrace();
	} catch (IllegalAccessException x) {
	    x.printStackTrace();
	} catch (NoSuchFieldException x) {
	    x.printStackTrace();
	}
    }
}

```

---

**Note:** [`Class.newInstance()`](http://download.oracle.com/javase/7/docs/api/java/lang/Class.html#newInstance())
will only succeed if the constructor is has zero arguments and is already
accessible. Otherwise, it is necessary to use
[`Constructor.newInstance()`](http://download.oracle.com/javase/7/docs/api/java/lang/reflect/Constructor.html#newInstance(java.lang.Object...))
as in the above example.

---

Example output for a Unix system:

```

$ java ConsoleCharset
Console charset          :  ISO-8859-1
Charset.defaultCharset() :  ISO-8859-1

```

Example output for a Windows system:

```

C:\> java ConsoleCharset
Console charset          :  IBM437
Charset.defaultCharset() :  windows-1252

```

Another common application of
[`Constructor.newInstance()`](http://download.oracle.com/javase/7/docs/api/java/lang/reflect/Constructor.html#newInstance(java.lang.Object...))
is to invoke constructors which take arguments. The
[`RestoreAliases`](example/RestoreAliases.java)
example finds a specific single-argument constructor and invokes it:

```


import java.lang.reflect.Constructor;
import java.lang.reflect.Field;
import java.lang.reflect.InvocationTargetException;
import java.util.HashMap;
import java.util.Map;
import java.util.Set;
import static java.lang.System.out;

class EmailAliases {
    private Set<String> aliases;
    private EmailAliases(HashMap<String, String> h) {
	aliases = h.keySet();
    }

    public void printKeys() {
	out.format("Mail keys:%n");
	for (String k : aliases)
	    out.format("  %s%n", k);
    }
}

public class RestoreAliases {

    private static Map<String, String> defaultAliases = new HashMap<String, String>();
    static {
	defaultAliases.put("Duke", "duke@i-love-java");
	defaultAliases.put("Fang", "fang@evil-jealous-twin");
    }

    public static void main(String... args) {
	try {
	    Constructor ctor = EmailAliases.class.getDeclaredConstructor(HashMap.class);
	    ctor.setAccessible(true);
	    EmailAliases email = (EmailAliases)ctor.newInstance(defaultAliases);
	    email.printKeys();

        // production code should handle these exceptions more gracefully
	} catch (InstantiationException x) {
	    x.printStackTrace();
	} catch (IllegalAccessException x) {
	    x.printStackTrace();
	} catch (InvocationTargetException x) {
	    x.printStackTrace();
	} catch (NoSuchMethodException x) {
	    x.printStackTrace();
	}
    }
}

```

This example uses
[`Class.getDeclaredConstructor()`](http://download.oracle.com/javase/7/docs/api/java/lang/Class.html#getDeclaredConstructor(java.lang.Class...))
to find the constructor with a single argument of type
[`java.util.HashMap`](http://download.oracle.com/javase/7/docs/api/java/util/HashMap.html). Note that it is sufficient to pass `HashMap.class` since the
parameter to any `get*Constructor()` method requires a class only
for type purposes. Due to
[type erasure](http://java.sun.com/docs/books/jls/third_edition/html/typesValues.html#4.6), the following expression evaluates to `true`:

```

HashMap.class == defaultAliases.getClass()

```

The example then creates a new instance of the class using this constructor
with
[`Constructor.newInstance()`](http://download.oracle.com/javase/7/docs/api/java/lang/reflect/Constructor.html#newInstance(java.lang.Object...)).

```

$ java RestoreAliases
Mail keys:
  Duke
  Fang

```

[« Previous](ctorModifiers.html)
•
[Trail](../TOC.html)
•
[Next »](ctorTrouble.html)

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

**Previous page:** Retrieving and Parsing Constructor Modifiers
  
**Next page:** Troubleshooting




A browser with JavaScript enabled is required for this page to operate properly.