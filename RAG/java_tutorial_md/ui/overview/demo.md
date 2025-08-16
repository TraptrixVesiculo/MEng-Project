[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** Graphical User Interfaces
  
**Lesson:** A Brief Introduction to the Swing Package

[A Brief Introduction to the Swing Package](index.html)

[What is Swing?](intro.html)

A Swing Demo

[Home Page](../../index.html)
>
[Graphical User Interfaces](../index.html)
>
[A Brief Introduction to the Swing Package](index.html)

[« Previous](intro.html) • [Trail](../TOC.html) • [Next »](../features/index.html)

# A Swing Demo

Here is an example of an application, PasswordStore,
that illustrates some of Swing's rich feature set.
PasswordStore allows the user to manage login information
for various hosts. It also generates passwords, evaluates
the effectiveness of a password, and allows you to store notes
about a particular host or assign an icon to represent the host.

Click the launch button to run PasswordStore using Java Web
Start. [Requires release 6.0.]

[![Launches the PasswordStore application](../../images/jws-launch-button.png)](http://download.oracle.com/javase/tutorialJWS/ui/PasswordStore.jnlp)

The following highlights some of the specific features
of the PasswordStore application:

**Host Info**: > At program launch, the list of hosts is displayed in a Swing list > component. Using the View menu, the view can be toggled between the > table and the list. > > In both views, the **Host/Account Filter** text field can be > used to dynamically restrict the entries to those where the host or > account name contains the typed string. > **List View**: > The Swing list component can be customized to include visual data. > As shown in the following figure, an optional miniature icon to > the left of the host name represents the host. > The graphic to the right uses color and proportional > fill to reflect the strength of the password > (Red = poor, yellow = fair, green = good). > The bar changes dynamically as the user enters/modifies the > password in the text field below. > The user has typed the text "oo" in the filter text field, > which matches two entries: Heirl**oo**m Seeds and > Pacific Z**oo** Shop. ![This is a picture of the PasswordStore demo.](../../figures/ui/ui-FilteredPasswordStore.png) Host Info (List View) and Filter Text Field **Table View**: > The Swing table component allows the user to rearrange the columns > by dragging the column header. Also, a column can be sorted > by clicking the column header. If the column you click on isn't > highlighted as the primary sorted column, it will become the > primary sorted column in ascending order. Clicking on the > primary sorted column toggles the sort order. For example, if > column 1 isn't selected, clicking on it will make it the selected > column and the data is sorted in ascending order. Clicking column > 1 again will sort the data in descending order. Clicking on column > 2 will make column 2 the primary column in ascending order. > > ![This is a picture of the PasswordStore demo in the table view.](../../figures/ui/ui-WindowsTableView.png) > > Host Info (Table View) **Details/Notes Tabbed Pane**: > The tabbed pane below the host info > allows the user to choose between > the Details panel and the Notes text pane, keeping the > overall footprint of the window smaller and less overwhelming. > **Details Panel**: > The icon area on the left can be assigned an image by either > dragging an image (jpg, png, gif, or tif) to the area > or by clicking the image well and bringing up a file browser. > > The text fields (used to enter or modify the host > name, login, and password) support cut/copy, paste, > drag, drop, undo, and redo. > > As the user enters or modifies the password, the 2D bar > chart dynamically displays the distribution of the password. > If the list view is currently displayed, the corresponding > colored bar in the list also changes dynamically. **Notes Text Pane**: > This is the text component where the user can save notes about the > selected host. If the text pane contains a URI, > Swing's text component provides the ability to click on > the URI and a browser window automatically opens to that > location. **Wizzy 2D Graphics**: > PasswordStore uses customized graphics in several ways to enhance > the UI: In the list view, images are used to represent each host; > a colored bar, the *Strength Visualizer*, > represents the effectiveness of a password; > and a dynamic bar chart, the *Password Visualizer*, > displays the distribution of a password. > When you add an image, whether by dragging and dropping it into the > image well (in the Details panel) or by clicking the well and > bringing up the file browser, a mini-icon is automatically generated > for the list view. > > --- > > **Note:** This demo is meant to be illustrative only and not meant to > be used for real analysis of passwords. > > --- > > ![This picture of PasswordStore shows the whizzy graphics used.](../../figures/ui/ui-WindowsPasswordStore2.png) > > 2D Graphics Used **Multiple Look and Feels**: > This provides the ability to switch between three look and feels using > the View menu: Java (called Metal), Motif/CDE, and the native > look and feel: Windows on Microsoft Windows, Aqua on Mac OS X, > and so on. **Undo and Redo**: > Undo and redo works on text, as you would expect, > but it also works on actions. For example, you can generate > a password using the Account > Generate Password menu, and > if you don't like the new password you can undo it using > Edit > Undo or the control-Z shortcut. Similarly, > you can redo the undo using Edit > Redo, or the control-Y shortcut.

The PasswordStore demo has a reasonable level of complexity for
a small Swing application and shows a sampling of Swing's capabilities.
The
[`source code`](PasswordStore-1.0-src.zip) is available for download, but it is outside the scope of this chapter to
discuss the implementation in detail. For more information on
the architecture and implementation of this application, see the blog entries,
[Architecting Applications 1: the model](http://weblogs.java.net/blog/zixle/archive/2006/01/architecting_ap.html) and
[Architecting Applications 2: the Application class](http://weblogs.java.net/blog/zixle/archive/2006/01/architecting_ap_1.html) on
[java.net](http://java.net).

---

**NOTE:** If PasswordStore were a production application,
it would most likely encrypt the password database; however,
due to legal restrictions on distributing information of that
nature, it is not included here.

---

---

**NOTE:** The dice, flower, pill, and pocketwatch images used in the demo
are courtesy of
<http://www.freeimages.co.uk>.
The polar bear and cubs image by Steve Amstrup and the
mountain image are courtesy of
<http://www.fws.gov>.
The spiral galaxy image is courtesy of
<http://grin.hq.nasa.gov>.

---

[« Previous](intro.html)
•
[Trail](../TOC.html)
•
[Next »](../features/index.html)

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

**Previous page:** What is Swing?
  
**Next page:** Swing Features




A browser with JavaScript enabled is required for this page to operate properly.