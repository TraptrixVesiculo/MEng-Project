[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** The Reflection API
  
**Lesson:** Members
  
**Section:** Fields

[Members](index.html)

[Fields](field.html)

[Obtaining Field Types](fieldTypes.html)

Retrieving and Parsing Field Modifiers

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

[Troubleshooting](ctorTrouble.html)

[Home Page](../../index.html)
>
[The Reflection API](../index.html)
>
[Members](index.html)

[« Previous](fieldTypes.html) • [Trail](../TOC.html) • [Next »](fieldValues.html)

# Retrieving and Parsing Field Modifiers

There are several modifiers that may be part of a field declaration:

* Access modifiers: `public`, `protected`, and
  `private`* Field-specific modifiers governing runtime behavior:
    `transient` and `volatile`* Modifier restricting to one instance: `static`* Modifier prohibiting value modification: `final`* Annotations

The method
[`Field.getModifiers()`](http://download.oracle.com/javase/7/docs/api/java/lang/reflect/Field.html#getModifiers())
can be used to return the integer representing the set of declared modifiers
for the field. The bits representing the modifiers in this integer are defined
in
[`java.lang.reflect.Modifier`](http://download.oracle.com/javase/7/docs/api/java/lang/reflect/Modifier.html).

The
[`FieldModifierSpy`](example/FieldModifierSpy.java)
example illustrates how to search for fields with a given modifier. It also
determines whether the located field is synthetic (compiler-generated) or is an
enum constant by invoking
[`Field.isSynthetic()`](http://download.oracle.com/javase/7/docs/api/java/lang/reflect/Field.html#isSynthetic())
and
[`Field.isEnumCostant()`](http://download.oracle.com/javase/7/docs/api/java/lang/reflect/Field.html#isEnumConstant())
respectively.

```


import java.lang.reflect.Field;
import java.lang.reflect.Modifier;
import static java.lang.System.out;

enum Spy { BLACK , WHITE }

public class FieldModifierSpy {
    volatile int share;
    int instance;
    class Inner {}

    public static void main(String... args) {
	try {
	    Class<?> c = Class.forName(args[0]);
	    int searchMods = 0x0;
	    for (int i = 1; i < args.length; i++) {
		searchMods |= modifierFromString(args[i]);
	    }

	    Field[] flds = c.getDeclaredFields();
	    out.format("Fields in Class '%s' containing modifiers:  %s%n",
		       c.getName(),
		       Modifier.toString(searchMods));
	    boolean found = false;
	    for (Field f : flds) {
		int foundMods = f.getModifiers();
		// Require all of the requested modifiers to be present
		if ((foundMods & searchMods) == searchMods) {
		    out.format("%-8s [ synthetic=%-5b enum_constant=%-5b ]%n",
			       f.getName(), f.isSynthetic(),
			       f.isEnumConstant());
		    found = true;
		}
	    }

	    if (!found) {
		out.format("No matching fields%n");
	    }

        // production code should handle this exception more gracefully
	} catch (ClassNotFoundException x) {
	    x.printStackTrace();
	}
    }

    private static int modifierFromString(String s) {
	int m = 0x0;
	if ("public".equals(s))           m |= Modifier.PUBLIC;
	else if ("protected".equals(s))   m |= Modifier.PROTECTED;
	else if ("private".equals(s))     m |= Modifier.PRIVATE;
	else if ("static".equals(s))      m |= Modifier.STATIC;
	else if ("final".equals(s))       m |= Modifier.FINAL;
	else if ("transient".equals(s))   m |= Modifier.TRANSIENT;
	else if ("volatile".equals(s))    m |= Modifier.VOLATILE;
	return m;
    }
}

```

Sample output follows:

```

$ java FieldModifierSpy FieldModifierSpy volatile
Fields in Class 'FieldModifierSpy' containing modifiers:  volatile
share    [ synthetic=false enum_constant=false ]
$ java FieldModifierSpy Spy public
Fields in Class 'Spy' containing modifiers:  public
BLACK    [ synthetic=false enum_constant=true  ]
WHITE    [ synthetic=false enum_constant=true  ]
$ java FieldModifierSpy FieldModifierSpy\$Inner final
Fields in Class 'FieldModifierSpy$Inner' containing modifiers:  final
this$0   [ synthetic=true  enum_constant=false ]
$ java FieldModifierSpy Spy private static final
Fields in Class 'Spy' containing modifiers:  private static final
$VALUES  [ synthetic=true  enum_constant=false ]

```

Notice that some fields are reported even though they are not declared in
the original code. This is because the compiler will generate some
*synthetic fields* which are needed during runtime. To test whether a
field is synthetic, the example invokes
[`Field.isSynthetic()`](http://download.oracle.com/javase/7/docs/api/java/lang/reflect/Field.html#isSynthetic()). The set of synthetic fields is compiler-dependent; however commonly used
fields include `this$0` for inner classes (i.e. nested classes
that are not static member classes) to reference the outermost enclosing class
and `$VALUES` used by enums to implement the implicitly defined
static method `values()`. The names of synthetic class members are
not specified and may not be the same in all compiler implementations or
releases. These and other synthetic fields will be included in the array
returned by
[`Class.getDeclaredFields()`](http://download.oracle.com/javase/7/docs/api/java/lang/Class.html#getDeclaredFields())
but not identified by
[`Class.getField()`](http://download.oracle.com/javase/7/docs/api/java/lang/Class.html#getField(java.lang.String))
since synthetic members are not typically `public`.

Because
[`Field`](http://download.oracle.com/javase/7/docs/api/java/lang/reflect/Field.html)
implements the interface
[`java.lang.reflect.AnnotatedElement`](http://download.oracle.com/javase/7/docs/api/java/lang/reflect/AnnotatedElement.html), it is possible to retrieve any runtime annotation with
[`java.lang.annotation.RetentionPolicy.RUNTIME`](http://download.oracle.com/javase/7/docs/api/java/lang/annotation/RetentionPolicy.html#RUNTIME). For an example of obtaining annotations see the section [Examining Class Modifiers and
Types](../class/classModifiers.html).

[« Previous](fieldTypes.html)
•
[Trail](../TOC.html)
•
[Next »](fieldValues.html)

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

**Previous page:** Obtaining Field Types
  
**Next page:** Getting and Setting Field Values




A browser with JavaScript enabled is required for this page to operate properly.