[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** Essential Classes
  
**Lesson:** Basic I/O
  
**Section:** I/O Streams

[Basic I/O](index.html)

[I/O Streams](streams.html)

[Byte Streams](bytestreams.html)

[Character Streams](charstreams.html)

[Buffered Streams](buffers.html)

[Scanning and Formatting](scanfor.html)

[Scanning](scanning.html)

[Formatting](formatting.html)

[I/O from the Command Line](cl.html)

[Data Streams](datastreams.html)

Object Streams

[File I/O (Featuring NIO.2)](fileio.html)

[What Is a Path? (And Other File System Facts)](path.html)

[The Path Class](pathClass.html)

[Path Operations](pathOps.html)

[File Operations](fileOps.html)

[Checking a File or Directory](check.html)

[Deleting a File or Directory](delete.html)

[Copying a File or Directory](copy.html)

[Moving a File or Directory](move.html)

[Managing Metadata (File and File Store Attributes)](fileAttr.html)

[Reading, Writing, and Creating Files](file.html)

[Random Access Files](rafs.html)

[Creating and Reading Directories](dirs.html)

[Links, Symbolic or Otherwise](links.html)

[Walking the File Tree](walk.html)

[Finding Files](find.html)

[Watching a Directory for Changes](notification.html)

[Other Useful Methods](misc.html)

[Legacy File I/O Code](legacy.html)

[Summary](summary.html)

[Questions and Exercises](QandE/questions.html)

[Home Page](../../index.html)
>
[Essential Classes](../index.html)
>
[Basic I/O](index.html)

[« Previous](datastreams.html) • [Trail](../TOC.html) • [Next »](fileio.html)

# Object Streams

Just as data streams support I/O of primitive data types, object
streams support I/O of objects. Most, but not all, standard classes
support serialization of their objects. Those that do implement the
marker interface
[`Serializable`](http://download.oracle.com/javase/7/docs/api/java/io/Serializable.html).

The object stream classes are
[`ObjectInputStream`](http://download.oracle.com/javase/7/docs/api/java/io/ObjectInputStream.html)
and
[`ObjectOutputStream`](http://download.oracle.com/javase/7/docs/api/java/io/ObjectOutputStream.html). These classes implement
[`ObjectInput`](http://download.oracle.com/javase/7/docs/api/java/io/ObjectInput.html)
and
[`ObjectOutput`](http://download.oracle.com/javase/7/docs/api/java/io/ObjectOutput.html),
which are subinterfaces of `DataInput` and
`DataOutput`. That means that all the primitive data I/O
methods covered in [Data Streams](datastreams.html) are also
implemented in object streams. So an object stream can contain a
mixture of primitive and object values.
The
[`ObjectStreams`](examples/ObjectStreams.java)
example illustrates this. `ObjectStreams` creates the
same application as `DataStreams`, with a couple of
changes. First, prices are now
[`BigDecimal`](http://download.oracle.com/javase/7/docs/api/java/math/BigDecimal.html)objects, to better represent fractional values. Second, a
[`Calendar`](http://download.oracle.com/javase/7/docs/api/java/util/Calendar.html)
object is written to the data file, indicating an invoice date.

If `readObject()` doesn't return the object type expected,
attempting to cast it to the correct type may throw a
[`ClassNotFoundException`](http://download.oracle.com/javase/7/docs/api/java/lang/ClassNotFoundException.html).
In this simple example, that can't happen, so we don't try to catch
the exception. Instead, we notify the compiler that we're aware of the
issue by adding `ClassNotFoundException` to the
`main` method's `throws` clause.

## Output and Input of Complex Objects

The `writeObject` and `readObject` methods are
simple to use, but they contain some very sophisticated object
management logic. This isn't important for a class like Calendar,
which just encapsulates primitive values. But many objects contain
references to other objects. If `readObject` is to
reconstitute an object from a stream, it has to be able to
reconstitute all of the objects the original object referred to. These
additional objects might have their own references, and so on. In this
situation, `writeObject` traverses the entire web of object
references and writes all objects in that web onto the stream. Thus a
single invocation of `writeObject` can cause a large number
of objects to be written to the stream.

This is demonstrated in the following figure, where
`writeObject` is invoked to write a single object named
**a**. This object contains references to objects
**b** and **c**, while **b** contains references to **d**
and **e**. Invoking `writeobject(a)` writes not just
**a**, but all the objects necessary to reconstitute **a**, so
the other four objects in this web are written also. When **a**
is read back by `readObject`, the other four objects are
read back as well, and all the original object references are
preserved.

![I/O of multiple referred-to objects](../../figures/essential/io-trav.gif)

I/O of multiple referred-to objects

You might wonder what happens if two objects on the same stream both
contain references to a single object. Will they both refer to a
single object when they're read back? The answer is "yes." A stream can
only contain one copy of an object, though it can contain any number
of references to it. Thus if you explicitly write an object to a
stream twice, you're really writing only the reference twice. For
example, if the following code writes an object `ob` twice
to a stream:

```

Object ob = new Object();
out.writeObject(ob);
out.writeObject(ob);

```

Each `writeObject` has to be matched by a
readObject, so the code that reads the stream back will
look something like this:

```

Object ob1 = in.readObject();
Object ob2 = in.readObject();

```

This results in two variables, `ob1` and `ob2`,
that are references to a single object.

However, if a single object is written to two different streams, it is
effectively duplicated — a single program reading both streams back will
see two distinct objects.

[« Previous](datastreams.html)
•
[Trail](../TOC.html)
•
[Next »](fileio.html)

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

**Previous page:** Data Streams
  
**Next page:** File I/O (Featuring NIO.2)




A browser with JavaScript enabled is required for this page to operate properly.