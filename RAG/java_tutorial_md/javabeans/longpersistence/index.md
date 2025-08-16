[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)

**Trail:** JavaBeans(TM)

[Home Page](../../index.html)
>
[JavaBeans(TM)](../index.html)

[« Previous](../persistence/index.html) • [Trail](../TOC.html) • [Next »](../introspection/index.html)

# Lesson: Long Term Persistence

*Long-term persistence* is a model that enables beans to be saved in XML
format.

Information on the XML format and on how to implement long-term persistence
for non-beans can be found in
[XML Schema](http://java.sun.com/products/jfc/tsc/articles/persistence3/
)and
[Using XMLEncoder](http://java.sun.com/products/jfc/tsc/articles/persistence4/
).

## Encoder and Decoder

The
[`XMLEncoder`](http://download.oracle.com/javase/7/docs/api/java/beans/XMLEncoder.html
)class is assigned to write output files for textual
representation of `Serializable` objects. The following code fragment is an example of
writing a Java bean and its properties in XML format:

```

     XMLEncoder encoder = new XMLEncoder(
                new BufferedOutputStream(
                        new FileOutputStream( "Beanarchive.xml" ) ) );

        encoder.writeObject( object );
        encoder.close(); 

```

The
[`XMLDecoder`](http://download.oracle.com/javase/7/docs/api/java/beans/XMLDecoder.html
)class reads an XML document that was created with XMLEncoder:

```

      XMLDecoder decoder = new XMLDecoder(
                new BufferedInputStream(
                        new FileInputStream( "Beanarchive.xml" ) ) );

        Object object = decoder.readObject();
        decoder.close();

```

## What's in XML?

An XML bean archive has its own specific syntax, which includes the
following tags to represent each bean element:

* an XML preamble to describe a version of XML and type of encoding* a `<java>` tag to embody all object elements of the bean* an `<object>` tag to represent a set of method calls
      needed to reconstruct an object from its serialized form

      ```

      	<object class="javax.swing.JButton" method="new">
                   <string>Ok</string>
              </object>
      	
      ```

      or statements

      ```

      	<object class="javax.swing.JButton">
                   <void method="setText">
                   <string>Cancel</string>
                   </void>
              </object>
      	
      ```

      * tags to define appropriate primitive types:
        + `<boolean>`+ `<byte>`+ `<char>`+ `<short>`+ `<int>`+ `<long>`+ `<float>`+ `<double>`

        ```

        		<int>5555</int>
        		
        ```

        * a **<`class`>** tag to represent an instance of Class.

          ```

          	<class>java.swing.JFrame</class>
          	
          ```

          * an **<`array`>** tag to define an array

            ```

            	<array class="java.lang.String" length="5">
                    </array>
            	
            ```

The following code represents an XML archive that will
be generated for the [`SimpleBean`](../writingbean/index.html)
component:

```

<?xml version="1.0" encoding="UTF-8" ?>
<java>
  <object class="javax.swing.JFrame">
    <void method="add">
      <object class="java.awt.BorderLayout" field="CENTER"/>
      <object class="SimpleBean"/>
    </void>
    <void property="defaultCloseOperation">
      <object class="javax.swing.WindowConstants" field="DISPOSE_ON_CLOSE"/>
    </void>
    <void method="pack"/>
    <void property="visible">
      <boolean>true</boolean>
    </void>
  </object>
</java>

```

[« Previous](../persistence/index.html)
•
[Trail](../TOC.html)
•
[Next »](../introspection/index.html)

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

**Previous page:** Previous Lesson
  
**Next page:** Introspection




A browser with JavaScript enabled is required for this page to operate properly.