[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** Java API for XML Processing (JAXP)
  
**Lesson:** Simple API for XML

[Simple API for XML](index.html)

[When to Use SAX](when.html)

[Parsing an XML File Using SAX](parsing.html)

Implementing SAX Validation

[Handling Lexical Events](events.html)

[Using the DTDHandler and EntityResolver](using.html)

[Further Information](info.html)

[Home Page](../../index.html)
>
[Java API for XML Processing (JAXP)](../index.html)
>
[Simple API for XML](index.html)

[« Previous](parsing.html) • [Trail](../TOC.html) • [Next »](events.html)

# Implementing SAX Validation

The sample program SAXLocalNameCount uses the non-validating parser by default, but it can
also activate validation. Activating validation allows the application to tell whether the XML
document contains the right tags or whether those tags are in the right
sequence. In other words, it can tell you whether the document is *valid*. If
validation is not activated, however, it can only tell whether or not
the document is well-formed, as was shown in the previous section when you
deleted the closing tag from an XML element. For validation to be possible,
the XML document needs to be associated to a DTD or an XML
schema. Both options are possible with the SAXLocalNameCount program.

## Choosing the Parser Implementation

If no other factory class is specified, the default SAXParserFactory class is
used. To use a parser from a different manufacturer, you can change the
value of the environment variable that points to it. You can do that
from the command line:

```
java -Djavax.xml.parsers.SAXParserFactory=yourFactoryHere [...]
```

The factory name you specify must be a fully qualified class name
(all package prefixes included). For more information, see the documentation in the newInstance() method
of the SAXParserFactory class.

## Using the Validating Parser

Up until this point, this lesson has concentrated on the non-validating parser. This
section examines the validating parser to find out what happens when you use
it to parse the sample program.

Two things must be understood about the validating parser:

* A schema or DTD is required.
* Because the schema or DTD is present, the ContentHandler.ignorableWhitespace() method is invoked whenever possible.

## Ignorable White Space

When a DTD is present, the parser will no longer call the
characters() method on white space that it knows to be irrelevant. From
the standpoint of an application that is interested in processing only the XML data,
that is a good thing because the application is never bothered with white
space that exists purely to make the XML file readable.

On the other hand, if you are writing an application that filters
an XML data file and if you want to output an equally readable
version of the file, then that white space would no longer be irrelevant:
it would be essential. To get those characters, you would add the ignorableWhitespace
method to your application. To process any (generally) ignorable white space that the parser
sees, you would need to add something like the following code to implement
the ignorableWhitespace event handler.

```
public void ignorableWhitespace (char buf[], int start, int length)
throws SAXException
{
emit("IGNORABLE");
}
```

This code simply generates a message to let you know that ignorable white
space was seen. However, not all parsers are created equal. The SAX specification
does not require that this method be invoked. The Java XML implementation does
so whenever the DTD makes it possible.

## Configuring the Factory

The SAXParserFactory needs to be set up such that it uses a validating
parser instead of the default non-validating parser. The following code from the SAXLocalNameCount
example's main() method shows how to configure the factory so that it
implements the validating parser.

```
    static public void main(String[] args) throws Exception {
        String filename = null;
        boolean dtdValidate = false;
        boolean xsdValidate = false;
        String schemaSource = null;

        for (int i = 0; i < args.length; i++) {
            if (args[i].equals("-dtd")) {
                dtdValidate = true;
            } else if (args[i].equals("-xsd")) {
                xsdValidate = true;
            } else if (args[i].equals("-xsdss")) {
                if (i == args.length - 1) {
                    usage();
                }
                xsdValidate = true;
                schemaSource = args[++i];
            } else if (args[i].equals("-usage")) {
                usage();
            } else if (args[i].equals("-help")) {
                usage();
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
        SAXParserFactory spf = SAXParserFactory.newInstance();
        spf.setNamespaceAware(true);
        spf.setValidating(dtdValidate || xsdValidate);
        SAXParser saxParser = spf.newSAXParser();
        [...]
```

Here, the SAXLocalNameCount program is configured to take additional arguments when it is
started, which tell it to implement no validation, DTD validation, XML Schema Definition
(XSD) validation, or XSD validation against a specific schema source file. (Descriptions of
these options, -dtd, -xsd, and -xsdss are also added to the usage() method, but
are not shown here.) Then, the factory is configured so that it will
produce the appropriate validating parser when newSAXParser is invoked. As seen in
[Setting up the Parser](parsing.html#gclmt
), you
can also use setNamespaceAware(true) to configure the factory to return a namespace-aware parser. Sun's
implementation supports any combination of configuration options. (If a combination is not supported
by a particular implementation, it is required to generate a factory configuration error).

## Validating with XML Schema

Although a full treatment of XML Schema is beyond the scope of
this tutorial, this section shows you the steps you take to validate an
XML document using an existing schema written in the XML Schema language. To
learn more about XML Schema, you can review the online tutorial, *XML Schema Part 0: Primer*, at
[http://www.w3.org/TR/xmlschema-0/](http://www.w3.org/TR/xmlschema-0/
).

---

**Note -** There are multiple schema-definition languages, including RELAX NG, Schematron, and the W3C "XML
Schema" standard. (Even a DTD qualifies as a "schema," although it is the
only one that does not use XML syntax to describe schema constraints.) However,
"XML Schema" presents us with a terminology challenge. Although the phrase "XML Schema
schema" would be precise, we will use the phrase "XML Schema definition" to
avoid the appearance of redundancy.

---

To be notified of validation errors in an XML document, the parser
factory must be configured to create a validating parser, as shown in the
preceding section. In addition, the following must be true:

* The appropriate properties must be set on the SAX parser.
* The appropriate error handler must be set.
* The document must be associated with a schema.

## Setting the SAX Parser Properties

It is helpful to start by defining the constants you will use
when setting the properties. The SAXLocalNameCount example sets the following constants.

```
public class SAXLocalNameCount extends DefaultHandler {
    static final String JAXP_SCHEMA_LANGUAGE =
        "http://java.sun.com/xml/jaxp/properties/schemaLanguage";
    static final String W3C_XML_SCHEMA =
        "http://www.w3.org/2001/XMLSchema";
    static final String JAXP_SCHEMA_SOURCE =
        "http://java.sun.com/xml/jaxp/properties/schemaSource";
```

---

**Note -** The parser factory must be configured to generate a parser that is namespace-aware
as well as validating. This was shown in [Configuring the Factory](#gcwtg). More information about
namespaces is provided in
[Document Object Model](../dom
/index.html
) but for now, understand that schema validation is a
namespace-oriented process. Because JAXP-compliant parsers are not namespace-aware by default, it is necessary to
set the property for schema validation to work.

---

Then you must configure the parser to tell it which schema language to
use. In SAXLocalNameCount, validation can be performed either against a DTD or against
an XML Schema. The following code uses the constants defined above to specify
the W3C's XML Schema language as the one to use if the -xsd
option is specified when the program is started.

```
[...]
        if (xsdValidate) {
            saxParser.setProperty(JAXP_SCHEMA_LANGUAGE, W3C_XML_SCHEMA);
        [...]
        }
```

In addition to the error handling described in
[Setting up Error Handling](parsing.html#gcnsr
), there is one
error that can occur when configuring the parser for schema-based validation. If the
parser is not compliant with JAXP version 1.2 or later, and therefore does
not support XML Schema, it can throw a SAXNotRecognizedException. To handle that case, the
setProperty() statement is wrapped in a try/catch block, as shown in the code
below.

```
[...]
        if (xsdValidate) {
            try {
                saxParser.setProperty(JAXP_SCHEMA_LANGUAGE, W3C_XML_SCHEMA);
            } catch (SAXNotRecognizedException x) {
                System.err.println(
                    "Error: JAXP SAXParser property not recognized: "
                    + JAXP_SCHEMA_LANGUAGE);
                System.err.println(
                    "Check to see if parser conforms to JAXP 1.2 spec.");
                System.exit(1);
            }
        }
[...]
```

## Associating a Document with a Schema

To validate the data using an XML Schema definition, it is necessary to
ensure that the XML document is associated with one. There are two
ways to do that.

* By including a schema declaration in the XML document.
* By specifying the schema to use in the application.

---

**Note -** When the application specifies the schema to use, it overrides any schema declaration
in the document.

---

To specify the schema definition in the document, you would create XML such
as this:

```
<documentRoot
xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
xsi:noNamespaceSchemaLocation='YourSchemaDefinition.xsd'
>
```

The first attribute defines the XML namespace (xmlns) prefix, xsi, which stands for
XML Schema instance. The second line specifies the schema to use for elements
in the document that do not have a namespace prefix, namely for the
elements that are typically defined in any simple, uncomplicated XML document.

---

**Note -** More information about namespaces is included in Validating with XML Schema in
[Document Object Model](../dom
/index.html
).
For now, think of these attributes as the "magic incantation" you use to
validate a simple XML file that does not use them. After you have
learned more about namespaces, you will see how to use XML Schema to
validate complex documents that do use them. Those ideas are discussed in Validating
with Multiple Namespaces in
[Document Object Model](../dom
/index.html
).

---

You can also specify the schema file in the application, as is
the case in SAXLocalNameCount.

```
        [...]
        if (schemaSource != null) {
            saxParser.setProperty(JAXP_SCHEMA_SOURCE, new File(schemaSource));
        }

        [...]
```

In the code above, the variable schemaSource relates to a schema source file
that you can point the SAXLocalNameCount application to by starting it with the
-xsdss option and providing the name of the schema source file to be
used.

## Error Handling in the Validating Parser

It is important to recognize that the only reason an exception is
thrown when a file fails validation is as a result of the error-handling
code shown in
[Setting up Error Handling](parsing.html#gcnsr
). That code is reproduced here as a reminder:

```
[...]

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

[...]
```

If these exceptions are not thrown, the validation errors are simply ignored. In
general, a SAX parsing error is a validation error, although it can also
be generated if the file specifies a version of XML that the
parser is not prepared to handle. Remember that your application will not generate a
validation exception unless you supply an error handler such as the one here.

## DTD Warnings

As mentioned earlier, warnings are generated only when the SAX parser is processing
a DTD. Some warnings are generated only by the validating parser. The non-validating
parser's main goal is to operate as rapidly as possible, but it too
generates some warnings.

The XML specification suggests that warnings should be generated as a result of
the following:

* Providing additional declarations for entities, attributes, or notations. (Such declarations are ignored. Only the first is used. Also, note that duplicate definitions of elements always produce a fatal error when validating, as you saw earlier.)
* Referencing an undeclared element type. (A validity error occurs only if the undeclared type is actually used in the XML document. A warning results when the undeclared element is referenced in the DTD.)
* Declaring attributes for undeclared element types.

The Java XML SAX parser also emits warnings in other cases:

* No <!DOCTYPE ...> when validating.
* References to an undefined parameter entity when not validating. (When validating, an error results. Although nonvalidating parsers are not required to read parameter entities, the Java XML parser does so. Because it is not a requirement, the Java XML parser generates a warning, rather than an error.)
* Certain cases where the character-encoding declaration does not look right.

## Running the SAX Parser Examples with Validation

In this section, the SAXLocalNameCount sample program used previously will be used again,
except this time it will be run with validation against an XML Schema
or a DTD. The best way to demonstrate the different types of validation
is to modify the code of the XML file being parsed, as well
as the associated schema and DTDs, to break the processing and get the
application to generate exceptions.

## Experimenting with DTD Validation Errors

As stated above, these examples reuse the SAXLocalNameCount program. The locations where you
will find the sample and its associated files are given in
[Running the SAX Parser Example without Validation](parsing.html#gcnrx
).

1. **If you have not already done so, navigate to the samples directory.**

   ```
   % cd install-dir/jaxp-1_4_2-release-date/samples
   ```
2. **If you have not already done so, compile the example class.**

   ```
   % javac sax/*
   ```
3. **Open the file data/rich\_iii.xml in a text editor.**

   This is the same XML file that was processed without validation in
   [To Run the SAXLocalNameCount Example without Validation](parsing.html#gcvwx
   ).
   At the beginning of data/rich\_iii.xml, you will see that the DOCTYPE declaration points
   a validating parser to a DTD file called play.dtd. If DTD validation
   is activated, the structure of the XML file being parsed will be checked
   against the structure provided in play.dtd.
4. **Delete the declaration <!DOCTYPE PLAY SYSTEM "play.dtd"> from the beginning of the file.**

   Do not forget to save the modification, but leave the file open, as
   it will be needed again later.
5. **Run the SAXLocalNameCount program, with DTD validation activated.**

   To do this, you must specify the -dtd option when you run
   the program.

   ```
   % java sax/SAXLocalNameCount -dtd data/rich_iii.xml
   ```

   The result you see will look something like this:

   ```
   Exception in thread "main" org.xml.sax.SAXException: 
   Error: URI=file:install-dir/JAXP_sources/jaxp-1_4_2-release-date
   /samples/data/rich_iii.xml 
   Line=12: Document is invalid: no grammar found.
   ```

   ---

   **Note -** This message was generated by the JAXP 1.4.2 libraries. If you are using
   a different parser, the error message is likely to be somewhat different.

   ---

   This message says that there is no grammar against which the document
   rich\_iii.txt can be validated, so therefore it is automatically invalid. In other words,
   the message is saying that you are trying to validate the document, but
   no DTD has been declared, because no DOCTYPE declaration is present. So now
   you know that a DTD is a requirement for a valid document. That
   makes sense.
6. **Restore the <!DOCTYPE PLAY SYSTEM "play.dtd"> declaration to data/rich\_iii.xml.**

   Again, do not forget to save the file, but leave it open.
7. **Return to data/rich\_iii.xml and modify the tags for the character "KING EDWARD The
   Fourth" in line 26.**

   Change the start and end tags from <PERSONA> and </PERSONA> to <PERSON> and
   </PERSON>. Line 26 should now look like this:

   ```
   26:<PERSON>KING EDWARD The Fourth</PERSON>
   ```

   Again, do not forget to save the modification, and leave the file
   open.
8. **Run the SAXLocalNameCount program, with DTD validation activated.**

   This time, you will see a different error when you run the program:

   ```
   % java sax/SAXLocalNameCount -dtd data/rich_iii.xml
   Exception in thread "main" org.xml.sax.SAXException: 
   Error: URI=file:install-dir/JAXP_sources/jaxp-1_4_2-release-date
   /samples/data/rich_iii.xml 
   Line=26: Element type "PERSON" must be declared.
   ```

   Here you can see that the parser has objected to an element
   that is not included in the DTD data/play.dtd.
9. **In data/rich\_iii.xml correct the tags for "KING EDWARD The Fourth".**

   Return the start and end tags to their original versions, <PERSONA> and </PERSONA>.
10. **In data/rich\_iii.xml, delete <TITLE>Dramatis Personae</TITLE> from line 24.**

    Once more, do not forget to save the modification.
11. **Run the SAXLocalNameCount program, with DTD validation activated.**

    As before, you will see another validation error:

    ```
    java sax/SAXLocalNameCount -dtd data/rich_iii.xml
    Exception in thread "main" org.xml.sax.SAXException: 
    Error: URI=file:install-dir/JAXP_sources/jaxp-1_4_2-release-date
    /samples/data/rich_iii.xml 
    Line=85: The content of element type "PERSONAE" must match "(TITLE,(PERSONA|PGROUP)+)".
    ```

    By deleting the <TITLE> element from line 24, the <PERSONAE> element is rendered
    invalid because it does not contain the sub-elements that the DTD expects of
    a <PERSONAE> element. Note that the error message states that the error
    is in line 85 of data/rich\_iii.xml, even though you deleted the <TITLE> element from
    line 24. This is because the closing tag of the <PERSONAE> element is
    located at line 85 and the parser only throws the exception when it
    reaches the end of the element it parsing.
12. **Open the DTD file, data/play.dtd in a text editor.**

    In the DTD file, you can see the declaration of the <PERSONAE>
    element, as well as all the other elements that can be used in
    XML documents that conform to the play DTD. The declaration of <PERSONAE>
    looks like this.

    ```
    <!ELEMENT PERSONAE (TITLE, (PERSONA | PGROUP)+)>
    ```

    As you can see, the <PERSONAE> element requires a <TITLE> sub-element. The pipe
    (|) key means that either <PERSONA> or <PGROUP> sub-elements can be included in a
    <PERSONAE> element, and the plus (+) key after the (PERSONA | PGROUP) grouping means that at
    least one or more of either of these sub-elements must be included.
13. **Add a question mark (?) key after TITLE in the declaration of <PERSONAE>.**

    Adding a question mark to a sub-element's declaration in a DTD makes the
    presence of one instance of that sub-element optional.

    ```
    <!ELEMENT PERSONAE (TITLE?, (PERSONA | PGROUP)+)>
    ```

    If you were add an asterisk (\*) after the element, you could include
    either zero or multiple instances of that sub-element. However, in this case it
    does not make sense to have more than one title in a
    section of a document.

    Do not forget to save the modification you have made to data/play.dtd.
14. **Run the SAXLocalNameCount program, with DTD validation activated.**

    ```
    % java sax/SAXLocalNameCount -dtd data/rich_iii.xml
    ```

    This time, you should see the proper output of SAXLocalNameCount, with no
    errors.

## Experimenting with Schema Validation Errors

The previous exercise demonstrated using SAXLocalNameCount to validate an XML file against a
DTD. In this exercise you will use SAXLocalNameCount to validate a different
XML file against both the standard XML Schema definition and a custom schema
source file. Again, this type of validation will be demonstrated by breaking the
parsing process by modifying the XML file and the schema, so that the
parser throws errors.

As stated above, these examples reuse the SAXLocalNameCount program. The locations where you
will find the sample and its associated files are given in
[Running the SAX Parser Example without Validation](parsing.html#gcnrx
).

1. **If you have not already done so, navigate to the samples directory.**

   ```
   % cd install-dir/jaxp-1_4_2-release-date/samples
   ```
2. **If you have not already done so, compile the example class.**

   ```
   % javac sax/*
   ```
3. **Open the file data/personal-schema.xml in a text editor.**

   This is a simple XML file that provides the names and contact details
   for the employees of a small company. In this XML file, you will
   see that it has been associated with a schema definition file personal.xsd.

   ```
   <personnel xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
   xsi:noNamespaceSchemaLocation='personal.xsd'>
   ```
4. **Open the file data/personal.xsd in a text editor.**

   This schema defines what kinds of information are required about each employee in
   order for an XML document associated with the schema to be considered valid.
   For example, by examining the schema definition, you can see that each
   person element requires a name, and that each person's name must comprise a
   family name and a given name. Employees can also optionally have email
   addresses and URLs.
5. **In data/personal.xsd, change the minimum number of email addresses required for a person
   element from 0 to 1.**

   The declaration of the email element is now as follows.

   ```
        <xs:element ref="email" minOccurs='1' maxOccurs='unbounded'/>
   ```
6. **In data/personal-schema.xml, delete the email element from the person element one.worker.**

   Worker One now looks like this:

   ```
     <person id="one.worker">
       <name><family>Worker</family> <given>One</given></name>
       <link manager="Big.Boss"/>
     </person>
   ```
7. **Run SAXLocalNameCount against personal-schema.xml, with no schema validation.**

   ```
   % java sax/SAXLocalNameCount data/personal-schema.xml
   ```

   SAXLocalNameCount informs you of the number of times each element occurs in personal-schema.xml.

   ```
   Local Name "email" occurs 5 times
   Local Name "name" occurs 6 times
   Local Name "person" occurs 6 times
   Local Name "family" occurs 6 times
   Local Name "link" occurs 6 times
   Local Name "personnel" occurs 1 times
   Local Name "given" occurs 6 times
   ```

   You see that email only occurs five times, whereas there are six person
   elements in personal-schema.xml. So, because we set the minimum occurrences of the email
   element to 1 per person element, we know that this document is invalid. However,
   because SAXLocalNameCount was not told to validate against a schema, no error is
   reported.
8. **Run SAXLocalNameCount again, this time specifying that the personal—schema.xml document should be validated against
   a the personal.xsd schema definition.**

   As you saw in [Validating with XML Schema](#gcwtl) above, SAXLocalNameCount has an option to enable
   schema validation. Run SAXLocalNameCount with the following command.

   ```
   % java sax/SAXLocalNameCount -xsd data/personal-schema.xml
   ```

   This time, you will see the following error message.

   ```
   Exception in thread "main" org.xml.sax.SAXException: Error: 
   URI=file:install_dir/samples/data/personal-schema.xml 
   Line=19: cvc-complex-type.2.4.a: Invalid content was found starting with 
   element 'link'. 
   One of '{email}' is expected.
   ```
9. **Restore the email element to the person element one.worker.**
10. **Run SAXLocalNameCount a third time, again specifying that the personal—schema.xml document should be validated
    against a the personal.xsd schema definition.**

    ```
    % java sax/SAXLocalNameCount -xsd data/personal-schema.xml
    ```

    This time you will see the correct output, with no errors.
11. **Open personal-schema.xml in a text editor again.**
12. **Delete the declaration of the schema definition personal.xsd from the personnel element.**

    Remove the italicized code from the personnel element.

    ```
      <personnel xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation='personal.xsd'/>
    ```
13. **Run SAXLocalNameCount, again specifying schema validation.**

    ```
    % java sax/SAXLocalNameCount -xsd data/personal-schema.xml
    ```

    Obviously, this will not work, as the schema definition against which to validate
    the XML file has not been declared. You will see the following error.

    ```
    Exception in thread "main" org.xml.sax.SAXException: 
    Error: URI=file:install_dir/samples/data/personal-schema.xml 
    Line=8: cvc-elt.1: Cannot find the declaration of element 'personnel'.
    ```
14. **Run SAXLocalNameCount again, this time passing it the schema definition file at the
    command line.**

    ```
    % java sax/SAXLocalNameCount -xsdss data/personal.xsd  data/personal-schema.xml
    ```

    This time you use the SAXLocalNameCount option that allows you to specify a
    schema definition that is not hard-coded into the application. You should see the
    correct output.

[« Previous](parsing.html)
•
[Trail](../TOC.html)
•
[Next »](events.html)

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

**Previous page:** Parsing an XML File Using SAX
  
**Next page:** Handling Lexical Events




A browser with JavaScript enabled is required for this page to operate properly.