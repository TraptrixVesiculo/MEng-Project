[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** Creating a GUI with JFC/Swing
  
**Lesson:** Drag and Drop and Data Transfer

[Home Page](../../../index.html)
>
[Creating a GUI with JFC/Swing](../../index.html)
>
[Drag and Drop and Data Transfer](index.html)

[« Previous](../../examples/components/index.html) • [Trail](../../TOC.html) • [Next »](../../examples/misc/index.html)

# Drag and Drop and Data Transfer: Examples

The [table](#table) that follows
lists every example in the Drag and Drop and Data Transfer lesson,
with links to required files and to where each example is discussed.
The first column of the table has links
to JNLP files
that let you run the examples using
JavaTM Web Start.

---

**NOTE:** Release 6.0 is required to run all applets and
Java Web Start examples. Most examples will run on an earlier
release but you must compile and run them locally.

---

To run an example using Java Web Start,
click the *[Launch]* link in the first column of the
[table](#table).
The first time you run an example,
there will be a delay
while Java Web Start downloads the JAR file
containing the class files for this lesson's examples.
Afterward, the examples should execute more quickly.

#### Compiling and Running the Examples Locally

> The second column in the table below has links to zip files for each
> demo that you can open and run in the NetBeans IDE. Refer to
> [Running Tutorial Examples in NetBeans IDE](../../../information/examples.html) for more information.
>
> If you download an individual example,
> take care to have all the necessary files
> in the proper hierarchy when you compile and run it.
> All of the examples in the Swing tutorial are placed in
> a package. For example, the components examples are placed
> in a `components` package.
> See the following image for the complete structure.
> Note that any examples using images expect their image files
> to be in a directory named `images`
> that is in the same directory as the example's src files.
>
> You can find out which files each example needs by consulting the
> following table or by looking at the comments at the beginning of
> each source file.

#### Table of Examples

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Example** | **Zip File   *(contains all files necessary for the example plus NetBeans IDE project metadata)*** | **Source Files *(first file has the main method, except for examples that run only as applets)*** | **Image & Other Files** | **Where Described** |
| BasicDnD [*[Launch]*](http://download.oracle.com/javase/tutorialJWS/uiswing/dnd/ex6/BasicDnD.jnlp) [Basic DnD Project](../zipfiles/dnd-BasicDnDProject.zip) | [`BasicDnD.java`](BasicDnDProject/src/dnd/BasicDnD.java) | |  | [Demo - BasicDnD](../../dnd/basicdemo.html) |
| ChooseDropActionDemo [*[Launch]*](http://download.oracle.com/javase/tutorialJWS/uiswing/dnd/ex6/ChooseDropActionDemo.jnlp) [Choose Drop Action Demo](../zipfiles/dnd-ChooseDropActionDemoProject.zip) | [`ChooseDropActionDemo.java`](ChooseDropActionDemoProject/src/dnd/ChooseDropActionDemo.java) | |  | [Demo - ChooseDropAction](../../dnd/dropactiondemo.html) |
| DropDemo [*[Launch]*](http://download.oracle.com/javase/tutorialJWS/uiswing/dnd/ex6/DropDemo.jnlp) [Drop Demo Project](../zipfiles/dnd-DropDemoProject.zip) | [`DropDemo.java`](DropDemoProject/src/dnd/DropDemo.java)  [`ListTransferHandler.java`](DropDemoProject/src/dnd/ListTransferHandler.java) | |  | [Demo - Drop List](../../dnd/dropmodedemo.html) |
| FillViewportHeightDemo [*[Launch]*](http://download.oracle.com/javase/tutorialJWS/uiswing/dnd/ex6/FillViewportHeightDemo.jnlp) [Fill Viewport Height Demo Project](../zipfiles/dnd-FillViewportHeightDemoProject.zip) | [`FillViewportHeightDemo.java`](FillViewportHeightDemoProject/src/dnd/FillViewportHeightDemo.java) | |  | [Empty Table Drop](../../dnd/emptytable.html) |
| ListCutPaste [*[Launch]*](http://download.oracle.com/javase/tutorialJWS/uiswing/dnd/ex6/ListCutPaste.jnlp) [List Cut Paste Project](../zipfiles/dnd-ListCutPasteProject.zip) | [`ListCutPaste.java`](ListCutPasteProject/src/dnd/ListCutPaste.java)  [`ListTransferHandler.java`](ListCutPasteProject/src/dnd/ListTransferHandler.java)  [`TransferActionListener.java`](ListCutPasteProject/src/dnd/TransferActionListener.java) | |  | [CCP in a non-Text Component](../../dnd/listpaste.html) |
| LocationSensitiveDemo [*[Launch]*](http://download.oracle.com/javase/tutorialJWS/uiswing/dnd/ex6/LocationSensitiveDemo.jnlp) [Location Sensitive Demo Project](../zipfiles/dnd-LocationSensitiveDemoProject.zip) | [`LocationSensitiveDemo.java`](LocationSensitiveDemoProject/src/dnd/LocationSensitiveDemo.java) | |  | [Demo - LocationSensitiveDemo](../../dnd/locsensitivedemo.html) |
| TextCutPaste [*[Launch]*](http://download.oracle.com/javase/tutorialJWS/uiswing/dnd/ex6/TextCutPaste.jnlp) [Text Cut Paste Project](../zipfiles/dnd-TextCutPasteProject.zip) | [`TextCutPaste.java`](TextCutPasteProject/src/dnd/TextCutPaste.java)  [`TextTransferHandler.java`](TextCutPasteProject/src/dnd/TextTransferHandler.java) | |  | [CCP in a Text Component](../../dnd/textpaste.html) |
| TopLevelTransferHandlerDemo [TopLevel TransferHandler Demo Project](../zipfiles/dnd-TopLevelTransferHandlerDemoProject.zip) | [`TopLevelTransferHandlerDemo.java`](TopLevelTransferHandlerDemoProject/src/dnd/TopLevelTransferHandlerDemo.java) | |  | [Top-Level Drop](../../dnd/toplevel.html) |