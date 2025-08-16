[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** The Reflection API
  
**Lesson:** Arrays and Enumerated Types
  
**Section:** Enumerated Types

[Arrays and Enumerated Types](index.html)

[Arrays](array.html)

[Identifying Array Types](arrayComponents.html)

[Creating New Arrays](arrayInstance.html)

[Getting and Setting Arrays and Their Components](arraySetGet.html)

[Troubleshooting](arrayTrouble.html)

[Enumerated Types](enum.html)

[Examining Enums](enumMembers.html)

[Getting and Setting Fields with Enum Types](enumSetGet.html)

Troubleshooting

[Home Page](../../index.html)
>
[The Reflection API](../index.html)
>
[Arrays and Enumerated Types](index.html)

[« Previous](enumSetGet.html) • [Trail](../TOC.html) • [Next »](../end.html)

# Troubleshooting

The following examples show problems which may be encountered when using
enumerated types.

#### IllegalArgumentException When Attempting to Instantiate an Enum Type As has been mentioned, instantiation of enum types is forbidden. The [`EnumTrouble`](example/EnumTrouble.java) example attempts this. ``` import java.lang.reflect.Constructor; import java.lang.reflect.InvocationTargetException; import static java.lang.System.out; enum Charge { POSITIVE, NEGATIVE, NEUTRAL; Charge() { out.format("under construction%n"); } } public class EnumTrouble { public static void main(String... args) { try { Class<?> c = Charge.class; Constructor[] ctors = c.getDeclaredConstructors(); for (Constructor ctor : ctors) { out.format("Constructor: %s%n", ctor.toGenericString()); ctor.setAccessible(true); ctor.newInstance(); } // production code should handle these exceptions more gracefully } catch (InstantiationException x) { x.printStackTrace(); } catch (IllegalAccessException x) { x.printStackTrace(); } catch (InvocationTargetException x) { x.printStackTrace(); } } } ``` ``` $ java EnumTrouble Constructor: private Charge() Exception in thread "main" java.lang.IllegalArgumentException: Cannot reflectively create enum objects at java.lang.reflect.Constructor.newInstance(Constructor.java:511) at EnumTrouble.main(EnumTrouble.java:22) ``` --- **Tip:** It is a compile-time error to attempt to explicitly instantiate an enum because that would prevent the defined enum constants from being unique. This restriction is also enforced in reflective code. Code which attempts to instantiate classes using their default constructors should invoke [`Class.isEnum()`](http://download.oracle.com/javase/7/docs/api/java/lang/Class.html#isEnum()) first to determine if the class is an enum. --- IllegalArgumentException when Setting a Field with an Incompatible Enum Type Fields storing enums set with the appropriate enum type. (Actually, fields of *any* type must be set with compatible types.) The [`EnumTroubleToo`](example/EnumTroubleToo.java) example produces the expected error. ``` import java.lang.reflect.Field; enum E0 { A, B } enum E1 { A, B } class ETest { private E0 fld = E0.A; } public class EnumTroubleToo { public static void main(String... args) { try { ETest test = new ETest(); Field f = test.getClass().getDeclaredField("fld"); f.setAccessible(true); f.set(test, E1.A); // IllegalArgumentException // production code should handle these exceptions more gracefully } catch (NoSuchFieldException x) { x.printStackTrace(); } catch (IllegalAccessException x) { x.printStackTrace(); } } } ``` ``` $ java EnumTroubleToo Exception in thread "main" java.lang.IllegalArgumentException: Can not set E0 field ETest.fld to E1 at sun.reflect.UnsafeFieldAccessorImpl.throwSetIllegalArgumentException(UnsafeFieldAccessorImpl.java:146) at sun.reflect.UnsafeFieldAccessorImpl.throwSetIllegalArgumentException(UnsafeFieldAccessorImpl.java:150) at sun.reflect.UnsafeObjectFieldAccessorImpl.set(UnsafeObjectFieldAccessorImpl.java:63) at java.lang.reflect.Field.set(Field.java:657) at EnumTroubleToo.main(EnumTroubleToo.java:16) ``` --- **Tip:**  Strictly speaking, any attempt to set a field of type `X` to a value of type `Y` can only succeed if the following statement holds: ``` X.class.isAssignableFrom(Y.class) == true ``` The code could be modified to perform the following test to verify whether the types are compatible: ``` if (f.getType().isAssignableFrom(E0.class)) // compatible else // expect IllegalArgumentException ``` ---

[« Previous](enumSetGet.html)
•
[Trail](../TOC.html)
•
[Next »](../end.html)

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

**Previous page:** Getting and Setting Fields with Enum Types
  
**Next page:** End of Trail




A browser with JavaScript enabled is required for this page to operate properly.