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

Getting and Setting Fields with Enum Types

[Troubleshooting](enumTrouble.html)

[Home Page](../../index.html)
>
[The Reflection API](../index.html)
>
[Arrays and Enumerated Types](index.html)

[« Previous](enumMembers.html) • [Trail](../TOC.html) • [Next »](enumTrouble.html)

# Getting and Setting Fields with Enum Types

Fields which store enums are set and retrieved as any other reference type,
using
[`Field.set()`](http://download.oracle.com/javase/7/docs/api/java/lang/reflect/Field.html#set(java.lang.Object, java.lang.Object))
and
[`Field.get()`](http://download.oracle.com/javase/7/docs/api/java/lang/reflect/Field.html#get(java.lang.Object)). For more information on accessing fields, see the [Fields](../member/field.html) section of this trail.

Consider application which needs to dynamically modify the trace level in a
server application which normally does not allow this change during runtime.
Assume the instance of the server object is available. The
[`SetTrace`](example/SetTrace.java)
example shows how code can translate the
[`String`](http://download.oracle.com/javase/7/docs/api/java/lang/String.html)
representation of an enum into an enum type and retrieve and set the value of a
field storing an enum.

```


import java.lang.reflect.Field;
import static java.lang.System.out;

enum TraceLevel { OFF, LOW, MEDIUM, HIGH, DEBUG }

class MyServer {
    private TraceLevel level = TraceLevel.OFF;
}

public class SetTrace {
    public static void main(String... args) {
	TraceLevel newLevel = TraceLevel.valueOf(args[0]);

	try {
	    MyServer svr = new MyServer();
	    Class<?> c = svr.getClass();
	    Field f = c.getDeclaredField("level");
	    f.setAccessible(true);
	    TraceLevel oldLevel = (TraceLevel)f.get(svr);
	    out.format("Original trace level:  %s%n", oldLevel);

	    if (oldLevel != newLevel) {
 		f.set(svr, newLevel);
		out.format("    New  trace level:  %s%n", f.get(svr));
	    }

        // production code should handle these exceptions more gracefully
	} catch (IllegalArgumentException x) {
	    x.printStackTrace();
	} catch (IllegalAccessException x) {
	    x.printStackTrace();
	} catch (NoSuchFieldException x) {
	    x.printStackTrace();
	}
    }
}

```

Since the enum constants are singletons, the `==` and
`!=` operators may be used to compare enum constants of the same
type.

```

$ java SetTrace OFF
Original trace level:  OFF
$ java SetTrace DEBUG
Original trace level:  OFF
    New  trace level:  DEBUG

```

[« Previous](enumMembers.html)
•
[Trail](../TOC.html)
•
[Next »](enumTrouble.html)

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

**Previous page:** Examining Enums
  
**Next page:** Troubleshooting




A browser with JavaScript enabled is required for this page to operate properly.