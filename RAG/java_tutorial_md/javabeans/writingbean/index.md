[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)

**Trail:** JavaBeans(TM)

[Home Page](../../index.html)
>
[JavaBeans(TM)](../index.html)

[« Previous](../nb/index.html) • [Trail](../TOC.html) • [Next »](../properties/index.html)

# Lesson: Writing a Simple Bean

In this section you will learn more about beans by performing the following
actions:

* Creating a simple bean
* Compiling the bean
* Generating a Java Archive (JAR) file
* Loading the bean into the GUI Builder of the NetBeans IDE
* Inspecting the bean's properties and events

Your bean will be named `SimpleBean`.
Here are the steps to create it:

1. **Write the `SimpleBean` code**. Put it in a file
   named `SimpleBean.java`, in the directory
   of your choice. Here's the code:

   ```

   import java.awt.Color;
   import java.beans.XMLDecoder;
   import javax.swing.JLabel;
   import java.io.Serializable;

   public class SimpleBean extends JLabel 
                           implements Serializable {
       public SimpleBean() {
           setText( "Hello world!" );
           setOpaque( true );
           setBackground( Color.RED );
           setForeground( Color.YELLOW );
           setVerticalAlignment( CENTER );
           setHorizontalAlignment( CENTER );
       } 
   }

   ```

   `SimpleBean` extends the
   [`javax.swing.JLabel`](http://download.oracle.com/javase/7/docs/api/javax/swing/JLabel.html
   ) graphic component and inherits its properties, which makes the
   SimpleBean a visual component.
   `SimpleBean` also implements the
   [`java.io.Serializable`](http://download.oracle.com/javase/7/docs/api/java/io/Serializable.html
   ) interface. Your bean may implement either the `Serializable` or
   the `Externalizable` interface.
2. **Create a manifest, the JAR file, and the class file SimpleBean.class**. Use
   the Apache Ant tool to create these files. Apache Ant is a Java-based build tool
   that enables you to generate XML-based configurations files as follows:

   ```

    <?xml version="1.0" encoding="ISO-8859-1"?>

    <project default="build">

     <dirname property="basedir" file="${ant.file}"/>

     <property name="beanname" value="SimpleBean"/>
     <property name="jarfile" value="${basedir}/${beanname}.jar"/>

     <target name="build" depends="compile">
         <jar destfile="${jarfile}" basedir="${basedir}" includes="*.class">
             <manifest>
                 <section name="${beanname}.class">
                    <attribute name="Java-Bean" value="true"/>
                 </section>
             </manifest>
         </jar>
     </target>

     <target name="compile">
         <javac destdir="${basedir}">
             <src location="${basedir}"/>
         </javac>
     </target>

     <target name="clean">
         <delete file="${jarfile}">
             <fileset dir="${basedir}" includes="*.class"/>
         </delete>
     </target>

   </project> 

   ```

   It is recommended to save an XML script in the `build.xml` file,
   because Ant recognizes this file name automatically.
3. **Load the JAR file**. Use the NetBeans IDE GUI Builder to load the jar file as follows:

   1. Start NetBeans.
   2. From the File menu select "New Project" to create a new
      application for your bean. You can use "Open Project" to add your bean to an
      existing application.
   3. Create a new application using the New Project Wizard.
   4. Select a newly created project in the List of Projects, expand the
      Source Packages node, and select the Default Package element.
   5. Click the right mouse button and select New|JFrameForm from the
      pop-up menu.
   6. Select the newly created Form node in the Project Tree. A blank form
      opens in the GUI Builder view of an Editor tab.
   7. Open the Palette Manager for Swing/AWT components by selecting
      Palette Manager in the Tools menu.
   8. In the Palette Manager window select the beans components in the
      Palette tree and press the "Add from JAR" button.
   9. Specify a location for your SimpleBean JAR file and follow the Add
      from JAR Wizard instructions.
   10. Select the Palette and Properties options from the Windows menu.
   11. Expand the beans group in the Palette window. The SimpleBean object
       appears. Drag the SimpleBean object to the GUI Builder panel.

   The following figure represents the SimpleBean object loaded in the GUI Builder panel:

   ![This figure represents the SimpleBean object loaded in the GUI Builder panel, 
   ](../../figures/javabeans/nb-simplebean.gif
   )
4. **Inspect Properties and Events**. The `SimpleBean` properties will appear in the
   Properties window. For example, you can change a background property by
   selecting another color. To preview your form, use the Preview Design button of
   the GUI Builder toolbar. To inspect events associated with the SimpleBean
   object, switch to the Events tab of the Properties window. You will learn more
   about bean properties and events in the lessons that follow.

[« Previous](../nb/index.html)
•
[Trail](../TOC.html)
•
[Next »](../properties/index.html)

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
  
**Next page:** Properties




A browser with JavaScript enabled is required for this page to operate properly.