[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** Java API for XML Processing (JAXP)
  
**Lesson:** Extensible Stylesheet Language Transformations

[Extensible Stylesheet Language Transformations](index.html)

[Introducing XSL, XSLT, and XPath](intro.html)

[How XPath Works](xpath.html)

[Writing Out a DOM as an XML File](writingDom.html)

[Generating XML from an Arbitrary Data Structure](generatingXML.html)

Transforming XML Data with XSLT

[Home Page](../../index.html)
>
[Java API for XML Processing (JAXP)](../index.html)
>
[Extensible Stylesheet Language Transformations](index.html)

[« Previous](generatingXML.html) • [Trail](../TOC.html) • [Next »](../stax/index.html)

# Transforming XML Data with XSLT

The Extensible Stylesheet Language Transformations (XSLT) APIs can be used for many purposes.
For example, with a sufficiently intelligent stylesheet, you could generate PDF or PostScript
output from the XML data. But generally, XSLT is used to generate formatted
HTML output, or to create an alternative XML representation of the data.

In this section, an XSLT transform is used to translate XML input
data to HTML output.

---

**Note -** The
[XSLT specification](http://www.w3.org/TR/xslt20/) is large and complex, so this tutorial can only scratch the
surface. It will give you a little background so you can understand
simple XSLT processing tasks, but it does not examine in detail how to
write an XSLT transform, rather concentrating on how to use JAXP's XSLT transform
API. For a more thorough grounding in XSLT, consult a good reference manual,
such as Michael Kay's *XSLT 2.0 and XPath 2.0: Programmer's Reference* (Wrox, 2008).

---



## Defining a Simple Document Type

Start by defining a very simple document type that can be used
for writing articles. Our article documents will contain these structure tags:

* <TITLE>: The title of the article
* <SECT>: A section, consisting of a heading and a body
* <PARA>: A paragraph
* <LIST>: A list
* <ITEM>: An entry in a list
* <NOTE>: An aside, that is offset from the main text

The slightly unusual aspect of this structure is that we will not
create a separate element tag for a section heading. Such elements are commonly
created to distinguish the heading text (and any tags it contains) from the
body of the section (that is, any structure elements underneath the heading).

Instead, we will allow the heading to merge seamlessly into the body of
a section. That arrangement adds some complexity to the stylesheet, but it will
give us a chance to explore XSLT's template-selection mechanisms. It also matches our
intuitive expectations about document structure, where the text of a heading is followed
directly by structure elements, an arrangement that can simplify outline-oriented editing.

---

**Note -** This kind of structure is not easily validated, because XML's mixed-content model allows
text anywhere in a section, whereas we want to confine text and inline
elements so that they appear only before the first structure element in the
body of the section. The assertion-based validator can do it, but most other
schema mechanisms cannot. So we will dispense with defining a DTD for the
document type.

---

In this structure, sections can be nested. The depth of the nesting will
determine what kind of HTML formatting to use for the section heading (for
example, h1 or h2). Using a plain SECT tag (instead of numbered
sections) is also useful with outline-oriented editing, because it lets you move sections
around at will without having to worry about changing the numbering for any
of the affected sections.

For lists, we will use a type attribute to specify whether the
list entries are unordered (bulleted), alpha (enumerated with lowercase letters), ALPHA (enumerated with uppercase
letters), or numbered.

We will also allow for some inline tags that change the appearance
of the text.

* <B>: Bold
* <I>: Italics
* <U>: Underline
* <DEF>: Definition
* <LINK>: Link to a URL

---

**Note -** An inline tag does not generate a line break, so a style
change caused by an inline tag does not affect the flow of text
on the page (although it will affect the appearance of that text). A
structure tag, on the other hand, demarcates a new segment of text, so
at a minimum it always generates a line break in addition to other
format changes.

---

The <DEF> tag will be used for terms that are defined in the
text. Such terms will be displayed in italics, the way they ordinarily are
in a document. But using a special tag in the XML will
allow an index program to find such definitions and add them to an
index, along with keywords in headings. In the preceding Note, for example, the
definitions of inline tags and structure tags could have been marked with <DEF>
tags for future indexing.

Finally, the LINK tag serves two purposes. First, it will let us create
a link to a URL without having to put the URL in
twice; so we can code <link>http//...</link> instead of <a href="http//...">http//...</a>. Of course, we will
also want to allow a form that looks like <link target="...">...name...</link>. That leads to
the second reason for the <link> tag. It will give us an opportunity
to play with conditional expressions in XSLT.

---

**Note -** Although the article structure is exceedingly simple (consisting of only eleven tags), it
raises enough interesting problems to give us a good view of XSLT's basic
capabilities. But we will still leave large areas of the specification untouched. In
[What Else Can XSLT Do?](#ggyut), we will point out the major features we skipped.

---



## Creating a Test Document

Here, you will create a simple test document using nested <SECT> elements,
a few <PARA> elements, a <NOTE> element, a <LINK>, and a <LIST type="unordered">.
The idea is to create a document with one of everything so that
we can explore the more interesting translation mechanisms.

---

**Note -** The code discussed in this section is in article1.xml, which is found in
the xslt/data directory after you unzip [XSLT examples](../examples/xslt_samples.zip) into the *install-dir*/jaxp-1\_4\_2-*release-date*/samples directory.

---

To make the test document, create a file called article.xml and enter the
following XML data.

```
<?xml version="1.0"?>
<ARTICLE>
   <TITLE>A Sample Article</TITLE>
   <SECT>The First Major Section
      <PARA>This section will introduce a subsection.</PARA>
      <SECT>The Subsection Heading
         <PARA>This is the text of the subsection.
         </PARA>
      </SECT>
   </SECT>
</ARTICLE>
```

Note that in the XML file, the subsection is totally contained within the
major section. (In HTML, on the other hand, headings do not contain
the body of a section). The result is an outline structure that is
harder to edit in plain text form, like this, but is much easier
to edit with an outline-oriented editor.

Someday, given a tree-oriented XML editor that understands inline tags such as <B>
and <I>, it should be possible to edit an article of this kind
in outline form, without requiring a complicated stylesheet. (Such an editor would allow
the writer to focus on the structure of the article, leaving layout until
much later in the process). In such an editor, the article fragment would
look something like this:

```
<ARTICLE> 
   <TITLE>A Sample Article 
   <SECT>The First Major Section 
      <PARA>This section will introduce a subsection.
      <SECT>The Subheading 
         <PARA>This is the text of the subsection. Note that ...
```

---

**Note -** At the moment, tree-structured editors exist, but they treat inline tags such as
<B> and <I> in the same way that they treat structure tags, and
that can make the "outline" a bit difficult to read.

---



## Writing an XSLT Transform

Now it is time to begin writing an XSLT transform that will
convert the XML article and render it in HTML.

---

**Note -** The code discussed in this section is in article1a.xsl, which is found in
the xslt/data directory after you unzip [XSLT examples](../examples/xslt_samples.zip) into the *install-dir*/jaxp-1\_4\_2-*release-date*/samples directory.

---

Start by creating a normal XML document:

```
<?xml version="1.0" encoding="ISO-8859-1"?>
```

Then add the following highlighted lines to create an XSL stylesheet:

```
<?xml version="1.0" encoding="ISO-8859-1"?>
<xsl:stylesheet 
 xmlns:xsl="http://www.w3.org/1999/XSL/Transform" 
 version="1.0"
 >

</xsl:stylesheet>
```

Now set it up to produce HTML-compatible output.

```
<xsl:stylesheet 
   [...]

   >
   <xsl:output method="html"/>

   [...]

</xsl:stylesheet>
```

We will get into the detailed reasons for that entry later in
this section. For now, note that if you want to output anything other
than well-formed XML, then you will need an <xsl:output> tag like the one shown,
specifying either text or html. (The default value is xml).

---

**Note -** When you specify XML output, you can add the indent attribute to produce
nicely indented XML output. The specification looks like this: <xsl:output method="xml" indent="yes"/>.

---



## Processing the Basic Structure Elements

You will start filling in the stylesheet by processing the elements that go
into creating a table of contents: the root element, the title element, and
headings. You will also process the PARA element defined in the test document.

---

**Note -** If on first reading you skipped the section that discusses the XPath addressing
mechanisms,
[How XPath Works](xpath.html), now is a good time to go back and review that
section.

---

Begin by adding the main instruction that processes the root element:

```
 <xsl:template match="/">
      <html><body>
         <xsl:apply-templates/>
      </body></html>
   </xsl:template>

</xsl:stylesheet>
```

The new XSL commands are shown in bold. (Note that they are
defined in the xsl namespace). The instruction <xsl:apply-templates> processes the children of the
current node. In this case, the current node is the root node.

Despite its simplicity, this example illustrates a number of important ideas, so it
is worth understanding thoroughly. The first concept is that a stylesheet contains a
number of templates, defined with the <xsl:template> tag. Each template contains a
match attribute, which uses the XPath addressing mechanisms described in
[How XPath Works](xpath.html) to select the
elements that the template will be applied to.

Within the template, tags that do not start with the xsl: namespace prefix
are simply copied. The newlines and whitespace that follow them are also copied,
and that helps to make the resulting output readable.

---

**Note -** When a newline is not present, whitespace is generally ignored. To include whitespace
in the output in such cases, or to include other text, you can
use the <xsl:text> tag. Basically, an XSLT stylesheet expects to process tags. So
everything it sees needs to be either an <xsl:..> tag, some other
tag, or whitespace.

---

In this case, the non-XSL tags are HTML tags. So when the
root tag is matched, XSLT outputs the HTML start tags, processes any templates
that apply to children of the root, and then outputs the HTML end
tags.

## Process the <TITLE> Element

Next, add a template to process the article title:

```
 <xsl:template match="/ARTICLE/TITLE">
 <h1 align="center"> <xsl:apply-templates/> </h1>
 </xsl:template>

</xsl:stylesheet>
```

In this case, you specify a complete path to the TITLE element
and output some HTML to make the text of the title into a
large, centered heading. In this case, the apply-templates tag ensures that if the title
contains any inline tags such as italics, links, or underlining, they also will
be processed.

More importantly, the apply-templates instruction causes the text of the title to be
processed. Like the DOM data model, the XSLT data model is based on
the concept of text nodes contained in element nodes (which, in turn, can
be contained in other element nodes, and so on). That hierarchical structure constitutes
the source tree. There is also a result tree, which contains the output.

XSLT works by transforming the source tree into the result tree. To visualize
the result of XSLT operations, it is helpful to understand the structure of
those trees, and their contents. (For more on this subject, see
[XSLT/XPath Data Model](xpath.html#gchlm)).

## Process Headings

To continue processing the basic structure elements, add a template to process the
top-level headings:

```
 <xsl:template match="/ARTICLE/SECT">
 <h2> <xsl:apply-templates
 select="text()|B|I|U|DEF|LINK"/> </h2>
 <xsl:apply-templates select="SECT|PARA|LIST|NOTE"/>
 </xsl:template>

</xsl:stylesheet>
```

Here, you specify the path to the topmost SECT elements. But this time,
you apply templates in two stages using the select attribute. For the first
stage, you select text nodes, as well as inline tags such as bold
and italics, using the XPath text() function. (The vertical pipe (|) is used
to match multiple items: text or a bold tag or an italics tag,
etc). In the second stage, you select the other structure elements contained in
the file, for sections, paragraphs, lists, and notes.

Using the select attribute lets you put the text and inline elements between
the <h2>...</h2> tags, while making sure that all the structure tags in the
section are processed afterward. In other words, you make sure that the nesting
of the headings in the XML document is not reflected in the HTML
formatting, a distinction that is important for HTML output.

In general, using the select clause lets you apply all templates to a
subset of the information available in the current context. As another example, this
template selects all attributes of the current node:

```
<xsl:apply-templates select="@*"/></attributes>
```

Next, add the virtually identical template to process subheadings that are nested one
level deeper:

```
 <xsl:template match="/ARTICLE/SECT/SECT">
 <h3> <xsl:apply-templates
 select="text()|B|I|U|DEF|LINK"/> </h3>
 <xsl:apply-templates select="SECT|PARA|LIST|NOTE"/>
 </xsl:template>

</xsl:stylesheet>
```

## Generate a Runtime Message

You could add templates for deeper headings, too, but at some point you
must stop, if only because HTML goes down only to five levels.
For this example, you will stop at two levels of section headings. But
if the XML input happens to contain a third level, you will want
to deliver an error message to the user. This section shows you how
to do that.

---

**Note -** We could continue processing SECT elements that are further down, by selecting them
with the expression /SECT/SECT//SECT. The // selects any SECT elements, at any depth,
as defined by the XPath addressing mechanism. But instead we will take the
opportunity to play with messaging.

---

Add the following template to generate an error when a section is
encountered that is nested too deep:

```
 <xsl:template match="/ARTICLE/SECT/SECT/SECT">
 <xsl:message terminate="yes">
 Error: Sections can only be nested 2 deep.
 </xsl:message>
 </xsl:template>

</xsl:stylesheet>
```

The terminate="yes" clause causes the transformation process to stop after the message is
generated. Without it, processing could still go on, with everything in that section
being ignored.

As an additional exercise, you could expand the stylesheet to handle sections nested
up to four sections deep, generating <h2>...<h5> tags. Generate an error on any
section nested five levels deep.

Finally, finish the stylesheet by adding a template to process the PARA
tag:

```
 <xsl:template match="PARA">
 <p><xsl:apply-templates/></p>
 </xsl:template>
</xsl:stylesheet>
```

## Writing the Basic Program

Now you will modify the program that uses XSLT to echo an
XML file unchanged, changing it so that it uses your stylesheet.

---

**Note -** The code discussed in this section is in Stylizer.java, which is found in
the xslt directory after you unzip [XSLT examples](../examples/xslt_samples.zip) into the *install-dir*/jaxp-1\_4\_2-*release-date*/samples directory. The result
is stylizer1a.html, found in xslt/data.

---

The Stylizer example is adapted from TransformationApp02, which parses an XML file
and writes to System.out. The main differences between the two programs are described
below.

Firstly, Stylizer uses the stylesheet when creating the Transformer object.

```
...
import javax.xml.transform.dom.DOMSource; 
import javax.xml.transform.stream.StreamSource; 
import javax.xml.transform.stream.StreamResult; 
... 
public class Stylizer 
{
  ...
  public static void main (String argv[])
  {
    ...
    try {
      File stylesheet = new File(argv[0]);
 File datafile = new File(argv[1]);

      DocumentBuilder builder =
        factory.newDocumentBuilder();
      document = builder.parse(datafile);
      ...
      StreamSource stylesource = 
 new StreamSource(stylesheet); 
      Transformer transformer =
        Factory.newTransformer(stylesource);
```

This code uses the file to create a StreamSource object and then passes
the source object to the factory class to get the transformer.

---

**Note -** You can simplify the code somewhat by eliminating the DOMSource class. Instead
of creating a DOMSource object for the XML file, create a StreamSource object
for it, as well as for the stylesheet.

---



### Running the Stylizer Sample

1. **Navigate to the samples directory.**

   ```
   % cd install-dir/jaxp-1_4_2-release-date/samples.
   ```
2. **[Download the XSLT examples by clicking this link](../examples/xslt_samples.zip) and unzip them into the *install-dir*/jaxp-1\_4\_2-*release-date*/samples directory.**
3. **Navigate to the xslt directory.**

   ```
   cd xslt
   ```
4. **Compile the Stylizer sample.**

   Type the following command:

   ```
   % javac Stylizer.java
   ```
5. **Run the Stylizer sample on article1.xml using the stylesheet article1a.xsl.**

   ```
   % java Stylizer data/article1a.xsl  data/article1.xml
   ```

   You will see the following output:

   ```
   <html>
   <body>

   <h1 align="center">A Sample Article</h1>
   <h2>The First Major Section

      </h2>
   <p>This section will introduce a subsection.</p>
   <h3>The Subsection Heading

         </h3>
   <p>This is the text of the subsection.

            </p>

   </body>
   </html>
   ```

   At this point, there is quite a bit of excess whitespace in
   the output. In the next section, you will see how to eliminate most
   of it.

## Trimming the Whitespace

Recall that when you look at the structure of a DOM, there
are many text nodes that contain nothing but ignorable whitespace. Most of the
excess whitespace in the output comes from these nodes. Fortunately, XSL gives you a
way to eliminate them. (For more about the node structure, see
[XSLT/XPath Data Model](xpath.html#gchlm)).

---

**Note -** The stylesheet discussed in this section is in article1b.xsl, which is found
in the xslt/data directory after you unzip [XSLT examples](../examples/xslt_samples.zip) into the *install-dir*/jaxp-1\_4\_2-*release-date*/samples directory. The result
is stylizer1b.html, found in xslt/data.

---

To remove some of the excess whitespace, add the following highlighted line to
the stylesheet.

```
<xsl:stylesheet ...
   >
   <xsl:output method="html"/> 
   <xsl:strip-space elements="SECT"/>

[...]
```

This instruction tells XSL to remove any text nodes under SECT elements that
contain nothing but whitespace. Nodes that contain text other than whitespace will not
be affected, nor will other kinds of nodes.

### Running the Stylizer Sample with Trimmed Whitespace

1. **Navigate to the samples directory.**

   ```
   % cd install-dir/jaxp-1_4_2-release-date/samples.
   ```
2. **[Download the XSLT examples by clicking this link](../examples/xslt_samples.zip) and unzip them into the *install-dir*/jaxp-1\_4\_2-*release-date*/samples directory.**
3. **Navigate to the xslt directory.**

   ```
   cd xslt
   ```
4. **Compile the Stylizer sample.**

   Type the following command:

   ```
   % javac Stylizer.java
   ```
5. **Run the Stylizer sample on article1.xml using the stylesheet article1b.xsl.**

   ```
   % java Stylizer data/article1b.xsl  data/article1.xml
   ```

   You will see the following output:

   ```
   <html>
   <body>

   <h1 align="center">A Sample Article</h1>

   <h2>The First Major Section
      </h2>
   <p>This section will introduce a subsection.</p>
   <h3>The Subsection Heading
         </h3>
   <p>This is the text of the subsection.
         </p>

   </body>
   </html>
   ```

   That is quite an improvement. There are still newline characters and whitespace after
   the headings, but those come from the way the XML is written:

   ```
   <SECT>The First Major Section
   ____<PARA>This section will introduce a subsection.</PARA>
   ^^^^
   ```

   Here, you can see that the section heading ends with a newline
   and indentation space, before the PARA entry starts. That is not a big
   worry, because the browsers that will process the HTML compress and ignore the
   excess space routinely. But there is still one more formatting tool at our
   disposal.

## Removing the Last Whitespace

---

**Note -** The stylesheet discussed in this section is in article1c.xsl, which is found
in the xslt/data directory after you unzip [XSLT examples](../examples/xslt_samples.zip) into the *install-dir*/jaxp-1\_4\_2-*release-date*/samples directory. The result
is stylizer1c.html, found in xslt/data.

---

That last little bit of whitespace is disposed of by adding the
following to the stylesheet:

```
   <xsl:template match="text()">
 <xsl:value-of select="normalize-space()"/>
 </xsl:template>

</xsl:stylesheet>
```

Running Stylizer with this stylesheet will remove all remaining whitespace.

### Running the Stylizer Sample with All Whitespace Trimmed

1. **Navigate to the samples directory.**

   ```
   % cd install-dir/jaxp-1_4_2-release-date/samples.
   ```
2. **[Download the XSLT examples by clicking this link](../examples/xslt_samples.zip) and unzip them into the *install-dir*/jaxp-1\_4\_2-*release-date*/samples directory.**
3. **Navigate to the xslt directory.**

   ```
   cd xslt
   ```
4. **Compile the Stylizer sample.**

   Type the following command:

   ```
   % javac Stylizer.java
   ```
5. **Run the Stylizer sample on article1.xml using the stylesheet article1c.xsl.**

   ```
   % java Stylizer data/article1c.xsl  data/article1.xml
   ```

   The output now looks like this:

   ```
   <html>
   <body>
   <h1 align="center">A Sample Article</h1>
   <h2>The First Major Section</h2>
   <p>This section will introduce a subsection.</p>
   <h3>The Subsection Heading</h3>
   <p>This is the text of the subsection.</p>
   </body>
   </html>
   ```

   That is quite a bit better. Of course, it would be nicer
   if it were indented, but that turns out to be somewhat harder than
   expected. Here are some possible avenues of attack, along with the difficulties:

   Indent option
   :   Unfortunately, the indent="yes" option that can be applied to XML output is not available for HTML output. Even if that option were available, it would not help, because HTML elements are rarely nested! Although HTML source is frequently indented to show the implied structure, the HTML tags themselves are not nested in a way that creates a real structure.

   Indent variables
   :   The <xsl:text> function lets you add any text you want, including whitespace. So it could conceivably be used to output indentation space. The problem is to vary the amount of indentation space. XSLT variables seem like a good idea, but they do not work here. The reason is that when you assign a value to a variable in a template, the value is known only within that template (statically, at compile time). Even if the variable is defined globally, the assigned value is not stored in a way that lets it be dynamically known by other templates at runtime. When <apply-templates/> invokes other templates, those templates are unaware of any variable settings made elsewhere.

   Parameterized templates
   :   Using a parameterized template is another way to modify a template's behavior. But determining the amount of indentation space to pass as the parameter remains the crux of the problem.

   At the moment, then, there does not appear to be any good
   way to control the indentation of HTML formatted output. That would be inconvenient
   if you needed to display or edit the HTML as plain text. But
   it is not a problem if you do your editing on the XML
   form, using the HTML version only for display in a browser. (When you
   view stylizer1c.html, for example, you see the results you expect).

## Processing the Remaining Structure Elements

In this section, you will process the LIST and NOTE elements, which
add more structure to an article.

---

**Note -** The sample document described in this section is article2.xml, and the stylesheet
used to manipulate it is article2.xsl. The result is stylizer2.html. These files
are found in the xslt/data directory after you unzip [XSLT examples](../examples/xslt_samples.zip) into the *install-dir*/jaxp-1\_4\_2-*release-date*/samples directory.

---

Start by adding some test data to the sample document:

```
<?xml version="1.0"?>
<ARTICLE>
  <TITLE>A Sample Article</TITLE>
  <SECT>The First Major Section
    ...
  </SECT>
  <SECT>The Second Major Section
    <PARA>This section adds a LIST and a NOTE.
    <PARA>Here is the LIST:
      <LIST type="ordered">
        <ITEM>Pears</ITEM>
        <ITEM>Grapes</ITEM>
      </LIST>
    </PARA>
    <PARA>And here is the NOTE:
      <NOTE>Don't forget to go to the hardware store 
        on your way to the grocery!
      </NOTE>
    </PARA>
  </SECT> 
</ARTICLE>  
```

---

**Note -** Although the list and note in the XML file are contained in their
respective paragraphs, it really makes no difference whether they are contained or not;
the generated HTML will be the same either way. But having them contained
will make them easier to deal with in an outline-oriented editor.

---



## Modify <PARA> Handling

Next, modify the PARA template to account for the fact that we are
now allowing some of the structure elements to be embedded with a paragraph:

```
<xsl:template match="PARA">
   <p> <xsl:apply-templates select="text()|B|I|U|DEF|LINK"/>
 </p>
 <xsl:apply-templates select="PARA|LIST|NOTE"/>
</xsl:template>
```

This modification uses the same technique you used for section headings. The only
difference is that SECT elements are not expected within a paragraph. (However, a
paragraph could easily exist inside another paragraph-for example, as quoted material).

## Process <LIST> and <ITEM> Elements

Now you're ready to add a template to process LIST elements:

```
   <xsl:template match="LIST">
      <xsl:if test="@type='ordered'"> 
         <ol>
         <xsl:apply-templates/>
         </ol>
      </xsl:if>
      <xsl:if test="@type='unordered'">
         <ul>
         <xsl:apply-templates/>
         </ul>
      </xsl:if>
   </xsl:template>

</xsl:stylesheet>
```

The <xsl:if> tag uses the test="" attribute to specify a Boolean condition. In
this case, the value of the type attribute is tested, and the list
that is generated changes depending on whether the value is ordered or unordered.

Note two important things in this example:

* There is no else clause, nor is there a return or exit statement, so it takes two <xsl:if> tags to cover the two options. (Or the <xsl:choose> tag could have been used, which provides case-statement functionality).
* Single quotes are required around the attribute values. Otherwise, the XSLT processor attempts to interpret the word ordered as an XPath function instead of as a string.

Now finish LIST processing by handling ITEM elements:

```
 <xsl:template match="ITEM">
 <li><xsl:apply-templates/>
 </li>
 </xsl:template>

</xsl:stylesheet>
```

## Ordering Templates in a Stylesheet

By now, you should have the idea that templates are independent of
one another, so it does not generally matter where they occur in a
file. So from this point on, we will show only the template you
need to add. (For the sake of comparison, they're always added at the
end of the example stylesheet).

Order does make a difference when two templates can apply to the
same node. In that case, the one that is defined last is the
one that is found and processed. For example, to change the ordering of
an indented list to use lowercase alphabetics, you could specify a template pattern
that looks like this: //LIST//LIST. In that template, you would use the HTML option
to generate an alphabetic enumeration, instead of a numeric one.

But such an element could also be identified by the pattern //LIST.
To make sure that the proper processing is done, the template that specifies
//LIST would have to appear before the template that specifies //LIST//LIST.

## Process <NOTE> Elements

The last remaining structure element is the NOTE element. Add the following template
to handle that.

```
 <xsl:template match="NOTE">
 <blockquote><b>Note:</b><br/>
 <xsl:apply-templates/>
 </p></blockquote>
 </xsl:template>

</xsl:stylesheet>
```

This code brings up an interesting issue that results from the inclusion of
the <br/> tag. For the file to be well-formed XML, the tag must
be specified in the stylesheet as <br/>, but that tag is not recognized
by many browsers. And although most browsers recognize the sequence <br></br>, they all
treat it like a paragraph break instead of a single line break.

In other words, the transformation must generate a <br> tag, but the stylesheet
must specify <br/>. That brings us to the major reason for that special
output tag we added early in the stylesheet:

```
<xsl:stylesheet ... >
   <xsl:output method="html"/>
   [...]
</xsl:stylesheet>
```

That output specification converts empty tags such as <br/> to their HTML form,
<br>, on output. That conversion is important, because most browsers do not recognize
the empty tags. Here is a list of the affected tags:

```
area      frame   isindex
base      hr      link
basefont  img     meta
br        input   param
col
```

To summarize, by default XSLT produces well-formed XML on output. And because an
XSL stylesheet is well-formed XML to start with, you cannot easily put a
tag such as <br> in the middle of it. The <xsl:output method="html"/> tag
solves the problem so that you can code <br/> in the stylesheet
but get <br> in the output.

The other major reason for specifying <xsl:output method="html"/> is that, as with the
specification <xsl:output method="text"/>, generated text is not escaped. For example, if the stylesheet includes
the < entity reference, it will appear as the < character in
the generated text. When XML is generated, on the other hand, the <
entity reference in the stylesheet would be unchanged, so it would appear as
< in the generated text.

---

**Note -** If you actually want < to be generated as part of the HTML
output, you will need to encode it as &lt;. That sequence becomes <
on output, because only the & is converted to an & character.

---



### Running the Stylizer Sample With LIST and NOTE Elements Defined

1. **Navigate to the samples directory.**

   ```
   % cd install-dir/jaxp-1_4_2-release-date/samples.
   ```
2. **[Download the XSLT examples by clicking this link](../examples/xslt_samples.zip) and unzip them into the *install-dir*/jaxp-1\_4\_2-*release-date*/samples directory.**
3. **Navigate to the xslt directory.**

   ```
   cd xslt
   ```
4. **Compile the Stylizer sample.**

   Type the following command:

   ```
   % javac Stylizer.java
   ```
5. **Run the Stylizer sample on article2.xml using the stylesheet article2.xsl.**

   ```
   % java Stylizer data/article2.xsl  data/article2.xml
   ```

   Here is the HTML that is generated for the second section when
   you run the program now:

   ```
   ...
   <h2>The Second Major Section</h2>
   <p>This section adds a LIST and a NOTE.</p>
   <p>Here is the LIST:</p>
   <ol>
   <li>Pears</li>
   <li>Grapes</li>
   </ol>
   <p>And here is the NOTE:</p>
   <blockquote>
   <b>Note:</b>
   <br>Do not forget to go to the hardware store on your way to the grocery!
   </blockquote>
   ```

## Process Inline (Content) Elements

The only remaining tags in the ARTICLE type are the inline tags-the ones
that do not create a line break in the output, but instead are
integrated into the stream of text they are part of.

Inline elements are different from structure elements in that inline elements are part
of the content of a tag. If you think of an element
as a node in a document tree, then each node has both content
and structure. The content is composed of the text and inline tags it
contains. The structure consists of the other elements (structure elements) under the tag.

---

**Note -** The sample document described in this section is article3.xml, and the stylesheet
used to manipulate it is article3.xsl. The result is stylizer3.html.

---

Start by adding one more bit of test data to the sample
document:

```
<?xml version="1.0"?>
<ARTICLE>
   <TITLE>A Sample Article</TITLE>
   <SECT>The First Major Section
      [...]
   </SECT>
   <SECT>The Second Major Section
      [...]
   </SECT> 
   <SECT>The <I>Third</I> Major Section
 <PARA>In addition to the inline tag in the heading, 
 this section defines the term <DEF>inline</DEF>,
 which literally means "no line break". It also 
 adds a simple link to the main page for the Java
 platform (<LINK>http://java.sun.com</LINK>), 
 as well as a link to the 
 <LINK target="http://java.sun.com/xml">XML</LINK>
 page.
 </PARA>
 </SECT> 
</ARTICLE>
```

Now process the inline <DEF> elements in paragraphs, renaming them to HTML italics
tags:

```
<xsl:template match="DEF">
 <i> <xsl:apply-templates/> </i> 
</xsl:template>
```

Next, comment out the text-node normalization. It has served its purpose, and now
you are to the point that you need to preserve important spaces:

```
<!--   <xsl:template match="text()">
      <xsl:value-of select="normalize-space()"/>
   </xsl:template>
-->
```

This modification keeps us from losing spaces before tags such as <I>
and <DEF>. (Try the program without this modification to see the result).

Now process basic inline HTML elements such as <B>, <I>, and <U>
for bold, italics, and underlining.

```
<xsl:template match="B|I|U">
 <xsl:element name="{name()}">
 <xsl:apply-templates/>
 </xsl:element> 
</xsl:template>
```

The <xsl:element> tag lets you compute the element you want to generate. Here,
you generate the appropriate inline tag using the name of the current element.
In particular, note the use of curly braces ({}) in the name=".." expression.
Those curly braces cause the text inside the quotes to be processed as
an XPath expression instead of being interpreted as a literal string. Here, they
cause the XPath name() function to return the name of the current node.

Curly braces are recognized anywhere that an attribute value template can occur. (Attribute
value templates are defined in section 7.6.2 of the XSLT specification, and they
appear several places in the template definitions). In such expressions, curly braces can
also be used to refer to the value of an attribute, {@foo}, or
to the content of an element {foo}.

---

**Note -** You can also generate attributes using <xsl:attribute>. For more information, see section 7.1.3
of the XSLT Specification.

---

The last remaining element is the LINK tag. The easiest way to process
that tag will be to set up a named template that we
can drive with a parameter:

```
<xsl:template name="htmLink">
 <xsl:param name="dest" select="UNDEFINED"/> 
 <xsl:element name="a">
 <xsl:attribute name="href">
 <xsl:value-of select=""/>
 </xsl:attribute>
 <xsl:apply-templates/> 
 </xsl:element> 
</xsl:template>
```

The major difference in this template is that, instead of specifying a match
clause, you give the template a name using the name="" clause. So this
template gets executed only when you invoke it.

Within the template, you also specify a parameter named dest using the <xsl:param>
tag. For a bit of error checking, you use the select clause to
give that parameter a default value of UNDEFINED. To reference the variable
in the <xsl:value-of> tag, you specify .

---

**Note -** Recall that an entry in quotes is interpreted as an expression unless it
is further enclosed in single quotes. That is why the single quotes were
needed earlier in "@type='ordered'" to make sure that ordered was interpreted as a
string.

---

The <xsl:element> tag generates an element. Previously, you have been able to simply
specify the element we want by coding something like <html>. But here you
are dynamically generating the content of the HTML anchor (<a>) in the body
of the <xsl:element> tag. And you are dynamically generating the href attribute of the
anchor using the <xsl:attribute> tag.

The last important part of the template is the <apply-templates> tag, which
inserts the text from the text node under the LINK element. Without
it, there would be no text in the generated HTML link.

Next, add the template for the LINK tag, and call the named template
from within it:

```
<xsl:template match="LINK">
 <xsl:if test="@target">
 <!--Target attribute specified.-->
 <xsl:call-template name="htmLink">
 <xsl:with-param name="dest" select="@target"/> 
 </xsl:call-template>
 </xsl:if>
</xsl:template>
<xsl:template name="htmLink">

[...]
```

The test="@target" clause returns true if the target attribute exists in the LINK
tag. So this <xsl-if> tag generates HTML links when the text of the
link and the target defined for it are different.

The <xsl:call-template> tag invokes the named template, whereas <xsl:with-param> specifies a parameter using the
name clause and specifies its value using the select clause.

As the very last step in the stylesheet construction process, add the
<xsl-if> tag to process LINK tags that do not have a target attribute.

```
<xsl:template match="LINK">
   <xsl:if test="@target">
      [...]
   </xsl:if>

   <xsl:if test="not(@target)">
 <xsl:call-template name="htmLink">
 <xsl:with-param name="dest">
 <xsl:apply-templates/>
 </xsl:with-param>
 </xsl:call-template>
 </xsl:if>
</xsl:template>
```

The not(...) clause inverts the previous test (remember, there is no else clause).
So this part of the template is interpreted when the target attribute is
not specified. This time, the parameter value comes not from a select clause,
but from the contents of the <xsl:with-param> element.

---

**Note -** Just to make it explicit: Parameters and variables (which are discussed in a
few moments in [What Else Can XSLT Do?](#ggyut) can have their value specified either by a select
clause, which lets you use XPath expressions, or by the content of the
element, which lets you use XSLT tags.

---

In this case, the content of the parameter is generated by the
<xsl:apply-templates/> tag, which inserts the contents of the text node under the
LINK element.

### Running the Stylizer Sample With Inline Elements Defined

1. **Navigate to the samples directory.**

   ```
   % cd install-dir/jaxp-1_4_2-release-date/samples.
   ```
2. **[Download the XSLT examples by clicking this link](../examples/xslt_samples.zip) and unzip them into the *install-dir*/jaxp-1\_4\_2-*release-date*/samples directory.**
3. **Navigate to the xslt directory.**

   ```
   cd xslt
   ```
4. **Compile the Stylizer sample.**

   Type the following command:

   ```
   % javac Stylizer.java
   ```
5. **Run the Stylizer sample on article3.xml using the stylesheet article3.xsl.**

   ```
   % java Stylizer data/article3.xsl  data/article3.xml
   ```

   When you run the program now, the results should look something like this:

   ```
   [...]
   <h2>The <I>Third</I> Major Section
         </h2>
   <p>In addition to the inline tag in the heading, this section
         defines the term <i>inline</i>, which literally means
         "no line break". It also adds a simple link to the
         main page for the Java platform (<a href="http://java.
         sun.com">http://java.sun.com</a>), 
         as well as a link to the 
         <a href="http://java.sun.com/xml">XML</a> page.
      </p>
   ```

   Good work! You have now converted a rather complex XML file to
   HTML. (As simple as it appears at first, it certainly provides a lot
   of opportunity for exploration).

## Printing the HTML

You have now converted an XML file to HTML. One day, someone
will produce an HTML-aware printing engine that you will be able to find
and use through the Java Printing Service API. At that point, you will
have ability to print an arbitrary XML file by generating HTML. All you
will have to do is to set up a stylesheet and use your
browser.

## What Else Can XSLT Do?

As lengthy as this section has been, it has only scratched the
surface of XSLT's capabilities. Many additional possibilities await you in the XSLT specification. Here
are a few things to look for:

import (Section 2.6.2) and include (section 2.6.1)
:   rt (Section 2.6.2) and include (section 2.6.1) Use these statements to modularize and combine XSLT stylesheets. The include statement simply inserts any definitions from the included file. The import statement lets you override definitions in the imported file with definitions in your own stylesheet.

for-each loops (section 8)
:   Loop over a collection of items and process each one in turn.

choose (case statement) for conditional processing (section 9.2)
:   Branch to one of multiple processing paths depending on an input value.

Generating numbers (section 7.7)
:   Dynamically generate numbered sections, numbered elements, and numeric literals. XSLT provides three numbering modes:

    * Single: Numbers items under a single heading, like an ordered list in HTML
    * Multiple: Produces multilevel numbering such as "A.1.3"
    * Any: Consecutively numbers items wherever they appear, as with footnotes in a lesson.

Formatting numbers (section 12.3)
:   Control enumeration formatting so that you get numerics (format="1"), uppercase alphabetics (format="A"), lowercase alphabetics (format="a"), or compound numbers, like "A.1," as well as numbers and currency amounts suited for a specific international locale.

Sorting output (section 10)
:   Produce output in a desired sorting order.

Mode-based templates (section 5.7)
:   Process an element multiple times, each time in a different "mode." You add a mode attribute to templates and then specify <apply-templates mode="..."> to apply only the templates with a matching mode. Combine with the <apply-templates select="..."> attribute to apply mode-based processing to a subset of the input data.

Variables (section 11)
:   Variables are something like method parameters, in that they let you control a template's behavior. But they are not as valuable as you might think. The value of a variable is known only within the scope of the current template or <xsl:if> tag (for example) in which it is defined. You cannot pass a value from one template to another, or even from an enclosed part of a template to another part of the same template.

    These statements are true even for a "global" variable. You can change its value in a template, but the change applies only to that template. And when the expression used to define the global variable is evaluated, that evaluation takes place in the context of the structure's root node. In other words, global variables are essentially runtime constants. Those constants can be useful for changing the behavior of a template, especially when coupled with include and import statements. But variables are not a general-purpose data-management mechanism.

## The Trouble with Variables

It is tempting to create a single template and set a variable
for the destination of the link, rather than go to the trouble of
setting up a parameterized template and calling it two different ways. The idea
is to set the variable to a default value (say, the text of
the LINK tag) and then, if the target attribute exists, set the destination
variable to the value of the target attribute.

That would be a good idea-if it worked. But again, the issue
is that variables are known only in the scope within which they are
defined. So when you code an <xsl:if> tag to change the value of
the variable, the value is known only within the context of the <xsl:if>
tag. Once </xsl:if> is encountered, any change to the variable's setting is lost.

A similarly tempting idea is the possibility of replacing the text()|B|I|U|DEF|LINK specification
with a variable (). But because the value of the variable is determined
by where it is defined, the value of a global inline variable consists
of text nodes, <B> nodes, and so on, that happen to exist at
the root level. In other words, the value of such a variable, in
this case, is null.

[« Previous](generatingXML.html)
•
[Trail](../TOC.html)
•
[Next »](../stax/index.html)

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

**Previous page:** Generating XML from an Arbitrary Data Structure
  
**Next page:** Streaming API for XML




A browser with JavaScript enabled is required for this page to operate properly.