[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../../search.html)

**Trail:** Essential Classes
  
**Lesson:** The Platform Environment

[Home Page](../../../index.html)
>
[Essential Classes](../../index.html)
>
[The Platform Environment](../index.html)

[« Previous](../QandE/questions.html) • [TOC](../../TOC.html)

# Answers to Questions and Exercises: The Platform Environment

### Questions

> Question 1.A programmer installs a
> new library contained in a .jar file. In order to access the
> library from his code, he sets the CLASSPATH environment variable
> to point to the new .jar file. Now he finds that he gets an error
> message when he tries to launch simple applications:
>
> ```
>
> java Hello
> Exception in thread "main" java.lang.NoClassDefFoundError: Hello
>
> ```
>
> In this case, the `Hello` class is compiled into a .class
> file in the current directory — yet the `java`
> command can't seem to find it. What's going wrong?
>
> Answer 1.
> A class is only found if it appears in the class path. By default,
> the class path consists of the current directory. If the CLASSPATH
> environment variable is set, and doesn't include the current
> directory, the launcher can no longer find classes in the current
> directory. The solution is to change the CLASSPATH variable to
> include the current directory. For example, if the CLASSPATH value
> is `c:\java\newLibrary.jar` (Windows) or
> `/home/me/newLibrary.jar` (UNIX or Linux) it needs to
> be changed to `.;c:\java\newLibrary.jar` or
> `.:/home/me/newLibrary.jar`.

  

### Exercises

> Exercise 1.
> Write an application, `PersistentEcho`, with the
> following features:
>
> * If `PersistentEcho` is run with command line
>   arguments, it prints out those arguments. It also saves the
>   string printed out to a property, and saves the property to a
>   file called `PersistentEcho.txt`* If `PersistentEcho` is run with no command line
>     arguments, it looks for an environment variable called
>     PERSISTENTECHO. If that variable exists,
>     `PersistentEcho` prints out its value, and also saves the
>     value in the same way it does for command line arguments.* If `PersistentEcho` is run with no command line
>       arguments, and the PERSISTENTECHO environment variable is not
>       defined, it retrieves the property value from
>       `PersistentEcho.txt` and prints that out.
>
>   
>  Answer 1.
>
> ```
>
>
> import java.util.Properties;
> import java.io.FileInputStream;
> import java.io.FileOutputStream;
> import java.io.IOException;
>
> public class PersistentEcho {
>     public static void main (String[] args) {
>         String argString = "";
>         boolean notProperty = true;
>
>         //Are there arguments? If so retrieve them.
>         if (args.length > 0) {
>             for (String arg: args) {
>                 argString += arg + " ";
>             }
>             argString = argString.trim();
>         }
>         //No arguments, is there an environment variable? If so,
>         //retrieve it.
>         else if ((argString = System.getenv("PERSISTENTECHO")) != null) {}
>         //No environment variable either. Retrieve property value.
>         else {
>             notProperty = false;
>             //Set argString to null. If it's still null after we exit
>             //the try block, we've failed to retrieve the property
>             //value.
>             argString = null;
>             FileInputStream fileInputStream = null;
>             try {
>                 fileInputStream = new FileInputStream("PersistentEcho.txt");
>                 Properties inProperties = new Properties();
>                 inProperties.load(fileInputStream);
>                 argString = inProperties.getProperty("argString");
>             } catch (IOException e) {
>                 System.err.println("Can't read property file.");
>                 System.exit(1);
>             } finally {
>                 if (fileInputStream != null) {
>                     try {
>                         fileInputStream.close();
>                     } catch(IOException e) {};
>                 }
>             }
>         }
>         if (argString == null) {
>             System.err.println("Couldn't find argString property");
>             System.exit(1);
>         }
>
>         //Somehow, we got the value. Echo it already!
>         System.out.println(argString);
>
>         //If we didn't retrieve the value from the property, save it
>         //in the property.
>         if (notProperty) {
>             Properties outProperties = new Properties();
>             outProperties.setProperty("argString", argString);
>             FileOutputStream fileOutputStream = null;
>             try {
>                 fileOutputStream = new FileOutputStream("PersistentEcho.txt");
>                 outProperties.store(fileOutputStream,
>                         "PersistentEcho properties");
>             } catch (IOException e) {}
>             finally {
>                 if (fileOutputStream != null) {
>                     try {
>                         fileOutputStream.close();
>                     } catch(IOException e) {};
>                 }
>             }
>         }
>     }
> }
>
>
> ```

[« Previous](../QandE/questions.html)
•
[TOC](../../TOC.html)


---

Problems with the examples? Try [Compiling and Running
the Examples: FAQs](../../../information/run-examples.html).
  
Complaints? Compliments? Suggestions? [Give
us your feedback](http://download.oracle.com/javase/feedback.html).

Your use of this page and all the material on pages under "The Java Tutorials" banner,
and all the material on pages under "The Java Tutorials" banner is subject to the [Java SE Tutorial Copyright
and License](../../../information/license.html).
Additionally, any example code contained in any of these Java
Tutorials pages is licensed under the
[Code
Sample License](http://developers.sun.com/license/berkeley_license.html).

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| |  |  | | --- | --- | | duke image | Oracle logo | | [About Oracle](http://www.oracle.com/us/corporate/index.html) | [Oracle Technology Network](http://www.oracle.com/technology/index.html) | [Terms of Service](https://www.samplecode.oracle.com/servlets/CompulsoryClickThrough?type=TermsOfService) | Copyright © 1995, 2011 Oracle and/or its affiliates. All rights reserved. |

**Previous page:** Questions and Exercises: The Platform Environment




A browser with JavaScript enabled is required for this page to operate properly.