[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** Java Naming and Directory Interface(TM).
  
**Lesson:** Java Objects in the Directory

[Java Objects in the Directory](index.html)

[Storing and Reading Objects](store.html)

Serializable Objects

[Home Page](../../index.html)
>
[Java Naming and Directory Interface(TM).](../index.html)
>
[Java Objects in the Directory](index.html)

[« Previous](store.html) • [Trail](../TOC.html) • [Next »](../newstuff/index.html)

# Serializable Objects

To *serialize* an object means to convert its state to a byte
stream so that the byte stream can be reverted back into a
copy of the object. A Java object is *serializable* if its
class or any of its superclasses implements either the java.io.Serializable
interface or its subinterface, java.io.Externalizable.
*Deserialization* is the process of converting the serialized
form of an object back into a copy of the object.

For example, the java.awt.Button class implements the Serializable
interface, so you can serialize a java.awt.Button object
and store that serialized state in a file.
Later, you can read back the serialized state and deserialize
into a java.awt.Button object.

The Java platform specifies a default way by which serializable objects
are serialized.
A (Java) class can override this default
serialization and define its own way of serializing objects of that
class. The
[Object Serialization Specification](http://download.oracle.com/javase/7/docs/technotes/guides/serialization/index.html) describes object serialization in detail.

When an object is serialized, information that identifies its class is
recorded in the serialized stream. However, the class's definition
("class file") itself is not recorded. It is the responsibility of the
system that is deserializing the object to determine how to locate and
load the necessary class files. For example, a Java application
might include in its classpath a JAR file that contains the class files
of the serialized object(s) or load the class definitions by using
information stored in the directory, as explained later
in this lesson.
#### Binding a Serializable Object
You can store a serializable object in the directory
if the underlying service provider supports that action, as does
Sun's LDAP service provider.

The following example invokes
[`Context.bind`](http://download.oracle.com/javase/7/docs/api/javax/naming/Context.html#bind(javax.naming.Name, java.lang.Object)) to bind an AWT button to the name "cn=Button".
To associate attributes with the new binding, you use
[`DirContext.bind`](http://download.oracle.com/javase/7/docs/api/javax/naming/directory/DirContext.html#bind(javax.naming.Name, java.lang.Object, javax.naming.directory.Attributes)).
To overwrite an existing binding, use
[`Context.rebind`](http://download.oracle.com/javase/7/docs/api/javax/naming/Context.html#rebind(javax.naming.Name, java.lang.Object)) and
[`DirContext.rebind`](http://download.oracle.com/javase/7/docs/api/javax/naming/directory/DirContext.html#rebind(javax.naming.Name, java.lang.Object, javax.naming.directory.Attributes)).
> ```
>
> // Create the object to be bound
> Button b = new Button("Push me");
>
> // Perform the bind
> ctx.bind("cn=Button", b);
>
> ```

You can then read the object back using
[`Context.lookup`](http://download.oracle.com/javase/7/docs/api/javax/naming/Context.html#lookup(javax.naming.Name)), as follows.
> ```
>
> // Check that it is bound
> Button b2 = (Button)ctx.lookup("cn=Button");
> System.out.println(b2);
>
> ```

Running [this example](examples/SerObj.java) produces the following output.
> ```
>
> # java SerObj
> java.awt.Button[button0,0,0,0x0,invalid,label=Push me]
>
> ```

#### Specifying a Codebase
> ---
>
> **Note:**
> The procedures described here are for binding a serializable
> object in
> a directory service that follows the schema defined in
> [RFC 2713](http://ietf.org/rfc/rfc2713.txt).
> These procedures might not be generally applicable to other naming and
> directory services that support binding a serializable object with a
> specified codebase.
>
> ---

When a serialized object is bound in the directory as shown in the previous example,
applications that read the serialized object from the directory must
have access to the class definitions necessary to deserialize the object.

Alternatively, you can record a *codebase* with the serialized
object in the directory, either when you bind the object or subsequently
by adding an attribute by using
[`DirContext.modifyAttributes`](http://download.oracle.com/javase/7/docs/api/javax/naming/directory/DirContext.html#modifyAttributes(javax.naming.Name, int, javax.naming.directory.Attributes)).
You can use any attribute to record this codebase and have your application
read that attribute from the directory and use it appropriately.
Or you can use the "javaCodebase" attribute specified in .
In the latter case, Sun's LDAP service provider will automatically
use the attribute to load the class definitions as needed.
"javaCodebase" should contain the URL of a codebase directory
or a JAR file.
If the codebase contains more than one URL,
then each URL must be separated
by a space character.

The following example resembles the one for binding a
java.awt.Button. It differs in that
it uses a user-defined Serializable class,
[Flower](examples/Flower.java), and
supplies a "javaCodebase" attribute
that contains the location
of Flower's class definition.
Here's the code that does the binding.
> ```
>
> String codebase = ...;
>
> // Create the object to be bound
> Flower f = new Flower("rose", "pink");
>
> // Perform the bind and specify the codebase
> ctx.bind("cn=Flower", f, new BasicAttributes("javaCodebase", codebase));
>
> ```

When you run
[this example](examples/SerObjWithCodebase.java), you must supply
the URL of the location at which the class file Flower.class was installed.
For example, if Flower.class was installed at the Web server
web1, in the directory example/classes,
then you would run this example as follows.
> ```
>
> # java SerObjWithCodebase http://web1/example/classes/
> pink rose
>
> ```

Afterward, you may remove Flower.class from your classpath
and run any program that looks up or lists this object without directly
referencing the Flower class.
If your program references Flower directly, then
you must make its class file available for compilation and execution.

[« Previous](store.html)
•
[Trail](../TOC.html)
•
[Next »](../newstuff/index.html)

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

**Previous page:** Storing and Reading Objects
  
**Next page:** New features in JDK 5.0 and JDK 6




A browser with JavaScript enabled is required for this page to operate properly.