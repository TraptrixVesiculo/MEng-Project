[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** Java API for XML Processing (JAXP)
  
**Lesson:** Document Object Model

[Document Object Model](index.html)

[When to Use DOM](when.html)

Reading XML Data into a DOM

[Validating with XML Schema](validating.html)

[Further Information](info.html)

[Home Page](../../index.html)
>
[Java API for XML Processing (JAXP)](../index.html)
>
[Document Object Model](index.html)

[« Previous](when.html) • [Trail](../TOC.html) • [Next »](validating.html)

# Reading XML Data into a DOM

In this section, you will construct a Document Object Model by reading in
an existing XML file.

---

**Note -** In
[Extensible Stylesheet Language Transformations](../xslt
/index.html
),
you will see how to write out a DOM as an
XML file. (You will also see how to convert an existing data file
into XML with relative ease.)

---

## Creating the Program

The Document Object Model provides APIs that let you create, modify, delete, and
rearrange nodes. Before you try to create a DOM, it is helpful to
understand how a DOM is structured. This series of examples will make
DOM internals visible via a sample program called DOMEcho, which you will find in
the directory *INSTALL\_DIR*/jaxp-*version*/samples/dom after you have installed the JAXP API.

### Create the Skeleton

First, build a simple program to read an XML document into a
DOM and then write it back out again.

Start with the normal basic logic for an application, and check to
make sure that an argument has been supplied on the command line:

```
public class DOMEcho {

    static final String outputEncoding = "UTF-8";

    private static void usage() {
    [...]
    }

    public static void main(String[] args) throws Exception {
        String filename = null;
    
        for (int i = 0; i < args.length; i++) {
        if (...) { 
        [...]
            } else {
                filename = args[i];

                if (i != args.length - 1) {
                    usage();
                }
            }        
    }
        if (filename == null) {
            usage();
        }

    }

}   
```

This code performs all the basic set up operations. All output for
DOMEcho uses UTF-8 encoding. The usage() method that is called if no argument
is specified simply tells you what arguments DOMEcho expects, so the code
is not shown here. A filename string is also declared, which will be
the name of the XML file to be parsed into a DOM by
DOMEcho.

### Import the Required Classes

In this section, all the classes are individually named so you that can
see where each class comes from, in case you want to reference
the API documentation. In the sample file, the import statements are made with
the shorter form, such as javax.xml.parsers.\*.

These are the JAXP APIs used by DOMEcho:

```
package dom;
import javax.xml.parsers.DocumentBuilder; 
import javax.xml.parsers.DocumentBuilderFactory;
```

These classes are for the exceptions that can be thrown when the
XML document is parsed:

```
import org.xml.sax.ErrorHandler;
import org.xml.sax.SAXException; 
import org.xml.sax.SAXParseException;
import org.xml.sax.helpers.*
```

These classes read the sample XML file and manage output:

```
import java.io.File;
import java.io.OutputStreamWriter;
import java.io.Printwriter;
```

Finally, import the W3C definitions for a DOM, DOM exceptions, entities and nodes:

```
import org.w3c.dom.Document;
import org.w3c.dom.DocumentType;
import org.w3c.dom.Entity;
import org.w3c.dom.NamedNodeMap;
import org.w3c.dom.Node;
```

### Handle Errors

Next, add the error-handling logic. The most important point is that a JAXP-conformant
document builder is required to report SAX exceptions when it has trouble parsing
an XML document. The DOM parser does not have to actually use a
SAX parser internally, but because the SAX standard is already there, it makes
sense to use it for reporting errors. As a result, the error-handling code
for DOM applications is very similar to that for SAX applications:

```
    private static class MyErrorHandler implements ErrorHandler {
     
        private PrintWriter out;

        MyErrorHandler(PrintWriter out) {
            this.out = out;
        }

        private String getParseExceptionInfo(SAXParseException spe) {
            String systemId = spe.getSystemId();
            if (systemId == null) {
                systemId = "null";
            }
            String info = "URI=" + systemId +
                " Line=" + spe.getLineNumber() +
                ": " + spe.getMessage();
            return info;
        }

        public void warning(SAXParseException spe) throws SAXException {
            out.println("Warning: " + getParseExceptionInfo(spe));
        }
        
        public void error(SAXParseException spe) throws SAXException {
            String message = "Error: " + getParseExceptionInfo(spe);
            throw new SAXException(message);
        }

        public void fatalError(SAXParseException spe) throws SAXException {
            String message = "Fatal Error: " + getParseExceptionInfo(spe);
            throw new SAXException(message);
        }
    }
```

As you can see, the DomEcho class's error handler generates its output using
PrintWriter instances.

### Instantiate the Factory

Next, add the following code to the main() method, to obtain an instance
of a factory that can give us a document builder.

```
    public static void main(String[] args) throws Exception {
    [...]

        DocumentBuilderFactory dbf = DocumentBuilderFactory.newInstance();

    }
```

### Get a Parser and Parse the File

Now, add the following code to main() to get an instance of a
builder, and use it to parse the specified file.

```
        DocumentBuilderFactory dbf =
            DocumentBuilderFactory.newInstance();

        DocumentBuilder db = dbf.newDocumentBuilder(); Document doc = db.parse(new File(filename));
```

The file being parsed is provided by the filename variable that was declared
at the beginning of the main() method, which is passed to DOMEcho as
an argument when the program is run.

### Configuring the Factory

By default, the factory returns a non-validating parser that knows nothing about name
spaces. To get a validating parser, or one that understands name spaces (or
both), you can configure the factory to set either or both of
those options using the following code.

```
    public static void main(String[] args) throws Exception {
        String filename = null;
        boolean dtdValidate = false;
        boolean xsdValidate = false;
        String schemaSource = null;
        
        for (int i = 0; i < args.length; i++) {
        if (args[i].equals("-dtd"))  { 
            {
                dtdValidate = true;
            } else if (args[i].equals("-xsd")) {
                xsdValidate = true;
            } else if (args[i].equals("-xsdss")) {
                if (i == args.length - 1) {
                    usage();
                }
                xsdValidate = true;
                schemaSource = args[++i];
           
            } else {
                filename = args[i];

                if (i != args.length - 1) {
                    usage();
                }
            }        
    }
        if (filename == null) {
            usage();
        }

        DocumentBuilderFactory dbf =
            DocumentBuilderFactory.newInstance();

        dbf.setNamespaceAware(true);
        dbf.setValidating(dtdValidate || xsdValidate);
            [...]

        DocumentBuilder db = dbf.newDocumentBuilder();
        Document doc = db.parse(new File(filename));


    }
```

As you can see, command line arguments are set up so that
you can inform DOMEcho to perform validation against either a DTD or
an XML Schema, and the factory is configured to be name space aware
and to perform whichever type of validation the user specifies.

---

**Note -** JAXP-conformant parsers are not required to support all combinations of those options, even
though the reference parser does. If you specify an invalid combination of options,
the factory generates a ParserConfigurationException when you attempt to obtain a parser
instance.

---

More information about how to use name spaces and validation is provided in
[Validating with XML Schema](validating.html
), in which the code that is missing from the above extract will
be described.

### Handling Validation Errors

The default response to a validation error, as dictated by the SAX
standard, is to do nothing. The JAXP standard requires throwing SAX exceptions, so
you use exactly the same error-handling mechanisms as you use for a SAX
application. In particular, you use the DocumentBuilder class's setErrorHandler method to supply it
with an object that implements the SAX ErrorHandler interface.

---

**Note -** DocumentBuilder also has a setEntityResolver method you can use.

---

The following code configures the document builder to use the error
handler defined in
[Handle Errors](readingXML.html#gestm
).

```

        DocumentBuilder db = dbf.newDocumentBuilder();
    
        OutputStreamWriter errorWriter =
            new OutputStreamWriter(System.err, outputEncoding);
        db.setErrorHandler(
            new MyErrorHandler(new PrintWriter(errorWriter, true)));
    
        Document doc = db.parse(new File(filename));
```

The code you have seen so far has set up the document
builder, and configured it to perform validation upon request. Error handling is also
in place. However, DOMEcho does not do anything yet. In the next
section, you will see how to display the DOM structure and begin to
explore it. For example, you will see what entity references and CDATA sections
look like in the DOM. And perhaps most importantly, you will see how
text nodes (which contain the actual data) reside under element nodes in a
DOM.

## Displaying the DOM Nodes

To create or manipulate a DOM, it helps to have a clear
idea of how the nodes in a DOM are structured. This section of
the tutorial exposes the internal structure of a DOM, so that you can
see what it contains. The DOMEcho example does this by echoing the
DOM nodes, and then printing them out onscreen, with the appropriate indentation to
make the node hierarchy apparent. The specification of these node types can be
found in the
[DOM Level 2 Core Specification](http://www.w3.org/TR/2000/REC-DOM-Level-2-Core-20001113
), under the specification for Node. [Table 3-1](#gfzpy) below is
adapted from that specification.

Table 3-1 Node Types

| Node | nodeName | nodeValue | Attributes |
| Attr | Name of attribute | Value of attribute | null |
| CDATASection | #cdata-section | Content of the CDATA section | null |
| Comment | #comment | Content of the comment | null |
| Document | #document | null | null |
| DocumentFragment | #documentFragment | null | null |
| DocumentType | Document Type name | null | null |
| Element | Tag name | null | null |
| Entity | Entity name | null | null |
| EntityReference | Name of entity referenced | null | null |
| Notation | Notation name | null | null |
| ProcessingInstruction | Target | Entire content excluding the target | null |
| Text | #text | Content of the text node | null |

The information in this table is extremely useful; you will need it when
working with a DOM, because all these types are intermixed in a
DOM tree.

### Obtaining Node Type Information

The DOM node element type information is obtained by calling the various methods
of the org.w3c.dom.Node class. The node attributes by exposed by DOMEcho are echoed
by the following code.

```
    private void printlnCommon(Node n) {
        out.print(" nodeName=\"" + n.getNodeName() + "\"");

        String val = n.getNamespaceURI();
        if (val != null) {
            out.print(" uri=\"" + val + "\"");
        }

        val = n.getPrefix();
        if (val != null) {
            out.print(" pre=\"" + val + "\"");
        }

        val = n.getLocalName();
        if (val != null) {
            out.print(" local=\"" + val + "\"");
        }

        val = n.getNodeValue();
        if (val != null) {
            out.print(" nodeValue=");
            if (val.trim().equals("")) {
                // Whitespace
                out.print("[WS]");
            } else {
                out.print("\"" + n.getNodeValue() + "\"");
            }
        }
        out.println();
    }
```

Every DOM node has at least a type, a name, and a
value, which might or might not be empty. In the example above, the
Node interface's getNamespaceURI(), getPrefix(), getLocalName(), and getNodeValue() methods return and print the echoed
node's namespace URI, namespace prefix, local qualified name and value. Note that the
trim() method is called on the value returned by getNodeValue() to establish whether
the node's value is empty white space and print a message accordingly.

For the full list of Node methods and the different information they return,
see the API documentation for
[`Node`](http://download.oracle.com/javase/7/docs/api/org/w3c/dom/Node.html
).

Next, a method is defined to set the indentation for the nodes
when they are printed, so that the node hierarchy will be easily visible.

```
    private void outputIndentation() {
        for (int i = 0; i < indent; i++) {
            out.print(basicIndent);
        }
    }
```

The basicIndent constant to define the basic unit of indentation used when DOMEcho
displays the node tree hierarchy, is defined by adding the following highlighted lines
to the DOMEcho constructor class.

```
public class DOMEcho {
    static final String outputEncoding = "UTF-8";

    private PrintWriter out;
    private int indent = 0;
    private final String basicIndent = " ";

    DOMEcho(PrintWriter out) {
        this.out = out;
    }
```

As was the case with the error handler defined in
[Handle Errors](readingXML.html#gestm
), the
DOMEcho program will create its output as PrintWriter instances.

### Lexical Controls

Lexical information is the information you need to reconstruct the original syntax of
an XML document. Preserving lexical information is important in editing applications, where you
want to save a document that is an accurate reflection of the original-complete
with comments, entity references, and any CDATA sections it may have included at
the outset.

Most applications, however, are concerned only with the content of the XML structures.
They can afford to ignore comments, and they do not care whether data
was coded in a CDATA section or as plain text, or whether
it included an entity reference. For such applications, a minimum of lexical information is
desirable, because it simplifies the number and kind of DOM nodes that the
application must be prepared to examine.

The following DocumentBuilderFactory methods give you control over the lexical information you see
in the DOM.

setCoalescing()
:   To convert CDATA nodes to Text nodes and append to an adjacent Text node (if any).

setExpandEntityReferences()
:   To expand entity reference nodes.

setIgnoringComments()
:   To ignore comments.

setIgnoringElementContentWhitespace()
:   To ignore whitespace that is not a significant part of element content.

The default values for all these properties is false, which preserves all the
lexical information necessary to reconstruct the incoming document in its original form. Setting
them to true lets you construct the simplest possible DOM so that the
application can focus on the data's semantic content without having to worry about
lexical syntax details. [Table 3-2](#ggdxy) summarizes the effects of the settings.

Table 3-2 Lexical Control Settings

| API | Preserve Lexical Info | Focus on Content |
| setCoalescing() | False | True |
| setExpandEntityReferences() | False | True |
| setIgnoringComments() | False | True |
| setIgnoringElementContentWhitespace() | False | True |

The implementation of these methods in the main method of the DomEcho
example is shown below.

```
[...]

        dbf.setIgnoringComments(ignoreComments);
        dbf.setIgnoringElementContentWhitespace(ignoreWhitespace);
        dbf.setCoalescing(putCDATAIntoText);
        dbf.setExpandEntityReferences(!createEntityRefs);

[...]
```

The boolean variables ignoreComments, ignoreWhitespace, putCDATAIntoText, and createEntityRefs are declared at the beginning
of the main method code, and they are set by command line arguments
when DomEcho is run.

```
    public static void main(String[] args) throws Exception {
        [...]
        boolean ignoreWhitespace = false;
        boolean ignoreComments = false;
        boolean putCDATAIntoText = false;
        boolean createEntityRefs = false;

        for (int i = 0; i < args.length; i++) {
            if [...] // Validation arguments here
 
            } else if (args[i].equals("-ws")) {
                ignoreWhitespace = true;
            } else if (args[i].startsWith("-co")) {
                ignoreComments = true;
            } else if (args[i].startsWith("-cd")) {
                putCDATAIntoText = true;
            } else if (args[i].startsWith("-e")) {
                createEntityRefs = true;
            [...]
            } else {
                filename = args[i];

                // Must be last arg
                if (i != args.length - 1) {
                    usage();
                }
            }
        }
        [...]
```

## Printing DOM Tree Nodes

The DomEcho application allows you to see the structure of a DOM, and
demonstrates what nodes make up the DOM and how they are arranged. Generally,
the vast majority of nodes in a DOM tree will be Element
and Text nodes.

---

[« Previous](when.html)
•
[Trail](../TOC.html)
•
[Next »](validating.html)

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

**Previous page:** When to Use DOM
  
**Next page:** Validating with XML Schema




A browser with JavaScript enabled is required for this page to operate properly.