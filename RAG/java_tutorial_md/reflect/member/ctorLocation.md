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

Finding Constructors

[Retrieving and Parsing Constructor Modifiers](ctorModifiers.html)

[Creating New Class Instances](ctorInstance.html)

[Troubleshooting](ctorTrouble.html)

[Home Page](../../index.html)
>
[The Reflection API](../index.html)
>
[Members](index.html)

[« Previous](ctor.html) • [Trail](../TOC.html) • [Next »](ctorModifiers.html)

# Finding Constructors

A constructor declaration includes the name, modifiers, parameters, and list of
throwable exceptions. The
[`java.lang.reflect.Constructor`](http://download.oracle.com/javase/7/docs/api/java/lang/reflect/Constructor.html)
class provides a way to obtain this information.

The
[`ConstructorSift`](example/ConstructorSift.java)
example illustrates how to search a class's declared constructors for one which
has a parameter of a given type.

```


import java.lang.reflect.Constructor;
import java.lang.reflect.Type;
import static java.lang.System.out;

public class ConstructorSift {
    public static void main(String... args) {
	try {
	    Class<?> cArg = Class.forName(args[1]);

	    Class<?> c = Class.forName(args[0]);
	    Constructor[] allConstructors = c.getDeclaredConstructors();
	    for (Constructor ctor : allConstructors) {
		Class<?>[] pType  = ctor.getParameterTypes();
		for (int i = 0; i < pType.length; i++) {
		    if (pType[i].equals(cArg)) {
			out.format("%s%n", ctor.toGenericString());

			Type[] gpType = ctor.getGenericParameterTypes();
			for (int j = 0; j < gpType.length; j++) {
			    char ch = (pType[j].equals(cArg) ? '*' : ' ');
			    out.format("%7c%s[%d]: %s%n", ch,
				       "GenericParameterType", j, gpType[j]);
			}
			break;
		    }
		}
	    }

        // production code should handle this exception more gracefully
	} catch (ClassNotFoundException x) {
	    x.printStackTrace();
	}
    }
}

```

[`Method.getGenericParameterTypes()`](http://download.oracle.com/javase/7/docs/api/java/lang/reflect/Method.html#getGenericParameterTypes())
will consult the
[Signature Attribute](http://java.sun.com/docs/books/vmspec/2nd-edition/ClassFileFormat-Java5.pdf)
in the class file if it's present. If the attribute isn't available, it falls
back on
[`Method.getParameterType()`](http://download.oracle.com/javase/7/docs/api/java/lang/reflect/Method.html#getParameterType())
which was not changed by the introduction of generics. The other methods with
name `getGenericFoo()` for some value of *Foo* in
reflection are implemented similarly.
The syntax for the returned values of `Method.get*Types()` is
described in
[`Class.getName()`](http://download.oracle.com/javase/7/docs/api/java/lang/Class.html#getName()).

Here is the output for all constructors in
[`java.util.Formatter`](http://download.oracle.com/javase/7/docs/api/java/util/Formatter.html)
which have a
[`Locale`](http://download.oracle.com/javase/7/docs/api/java/util/Locale.html)
argument.

```

$ java ConstructorSift java.util.Formatter java.util.Locale
public
java.util.Formatter(java.io.OutputStream,java.lang.String,java.util.Locale)
throws java.io.UnsupportedEncodingException
       GenericParameterType[0]: class java.io.OutputStream
       GenericParameterType[1]: class java.lang.String
      *GenericParameterType[2]: class java.util.Locale
public java.util.Formatter(java.lang.String,java.lang.String,java.util.Locale)
throws java.io.FileNotFoundException,java.io.UnsupportedEncodingException
       GenericParameterType[0]: class java.lang.String
       GenericParameterType[1]: class java.lang.String
      *GenericParameterType[2]: class java.util.Locale
public java.util.Formatter(java.lang.Appendable,java.util.Locale)
       GenericParameterType[0]: interface java.lang.Appendable
      *GenericParameterType[1]: class java.util.Locale
public java.util.Formatter(java.util.Locale)
      *GenericParameterType[0]: class java.util.Locale
public java.util.Formatter(java.io.File,java.lang.String,java.util.Locale)
throws java.io.FileNotFoundException,java.io.UnsupportedEncodingException
       GenericParameterType[0]: class java.io.File
       GenericParameterType[1]: class java.lang.String
      *GenericParameterType[2]: class java.util.Locale

```

The next example output illustrates how to search for a parameter of type
`char[]` in
[`String`](http://download.oracle.com/javase/7/docs/api/java/lang/String.html).

```

$ java ConstructorSift java.lang.String "[C"
java.lang.String(int,int,char[])
       GenericParameterType[0]: int
       GenericParameterType[1]: int
      *GenericParameterType[2]: class [C
public java.lang.String(char[],int,int)
      *GenericParameterType[0]: class [C
       GenericParameterType[1]: int
       GenericParameterType[2]: int
public java.lang.String(char[])
      *GenericParameterType[0]: class [C

```

The syntax for expressing arrays of reference and primitive types
acceptable to
[`Class.forName()`](http://download.oracle.com/javase/7/docs/api/java/lang/Class.html#forName(java.lang.String))
is described in
[`Class.getName()`](http://download.oracle.com/javase/7/docs/api/java/lang/Class.html#getName()). Note that the first listed constructor is `package-private`, not
`public`. It is returned because the example code uses
[`Class.getDeclaredConstructors()`](http://download.oracle.com/javase/7/docs/api/java/lang/Class.html#getDeclaredConstructors())
rather than
[`Class.getConstructors()`](http://download.oracle.com/javase/7/docs/api/java/lang/Class.html#getConstructors()), which returns only `public` constructors.

This example shows that searching for arguments of variable arity (which
have a variable number of parameters) requires use of array syntax:

```

$ java ConstructorSift java.lang.ProcessBuilder "[Ljava.lang.String;"
public java.lang.ProcessBuilder(java.lang.String[])
      *GenericParameterType[0]: class [Ljava.lang.String;

```

This is the actual declaration of the
[`ProcessBuilder`](http://download.oracle.com/javase/7/docs/api/java/lang/ProcessBuilder.html#ProcessBuilder(java.lang.String...))
constructor in source code:

```

public ProcessBuilder(String... command)

```

The parameter is represented as a single-dimension array of type
`java.lang.String`. This can be distinguished from a parameter that
is explicitly an array of `java.lang.String` by invoking
[`Constructor.isVarArgs()`](http://download.oracle.com/javase/7/docs/api/java/lang/reflect/Constructor.html#isVarArgs()).

The final example reports the output for a constructor which has been
declared with a generic parameter type:

```

$ java ConstructorSift java.util.HashMap java.util.Map
public java.util.HashMap(java.util.Map<? extends K, ? extends V>)
      *GenericParameterType[0]: java.util.Map<? extends K, ? extends V>

```

Exception types may be retrieved for constructors in a similar way as for
methods. See the
[`MethodSpy`](example/MethodSpy.java)
example described in [Obtaining Method Type
Information](methodType.html) section for further details.

[« Previous](ctor.html)
•
[Trail](../TOC.html)
•
[Next »](ctorModifiers.html)

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

**Previous page:** Constructors
  
**Next page:** Retrieving and Parsing Constructor Modifiers




A browser with JavaScript enabled is required for this page to operate properly.