# Errata for *The Java Tutorial, 4th Edition*

![](../images/shoeline2.GIF)
![](../images/shoeline2.GIF)

### First Printing

These errors are corrected in the 4th printing.

* CD problems on Linux:

  Some Linux systems automount the CD with a filesystem that forces all
  file names to lower case. This will break browser links to HTML files
  with mixed-case names, and also prevent the examples from compiling.

  If you have this problem, try manually mounting the CD with the UDF
  filesystem. To do this:
  + Become superuser.+ Unmount the cd:

      ```
      umount cd_device_path
      ```

      + Remount the the cd using the UDF filesystem:

        ```
        mount -t udf cd_device_path cd_mount_point
        ```

  ---

  * Chapter 1: Getting Started, page 3:

    The source code inside figure 1.2 is missing a closing bracket to
    end the class definition.

    The missing bracket appears in bold below:

    ```

    class HelloWorldApp {
        public static void main(String[] args) {
            System.out.println("Hello World!");
        }
    }

    ```

    Thanks to the anonymous reader who reported this!

    ---

    * Chapter 3: Language Basics, page 59:

      Typo fix: In the following sentence, the word "operand" (shown in bold) was mistakenly printed as "operator":

      "The equality and relational operators determine if one **operand** is greater than, less than, equal to, or not equal to another operand."

      Thanks to Dirk Henrici for reporting this!

      ---

      * Chapter 4: Classes and Objects, pages 89 and 116:

        In the `Bicycle` class, the `getspeed()` method should be called
        `getSpeed()`.

      ---

      * Chapter 4: Classes and Objects, page 97:

        In the example in the second paragraph, getX and getY should be changed to getX() and getY() so that the 3rdand 4th lines
        in the example read:

        ```

        circle.setX(circle.getX() + deltaX);
        circle.setY(circle.getY() + deltaY);

        ```

        Thanks to Laslo Vukovitch for reporting this.

      ---

      * Chapter 4: Classes and Objects, page 107:

        In the `SeeWhosFastest()` method, the method should be called
        `seeWhosFastest()`.

      ---

      * Chapter 4: Classes and Objects, page 114:

        The last word in the Note should be changed from "variables" to "methods" so that the sentence reads:
        "You can also refer to static methods with an object reference like instanceName.methodName(args) but
        this is discouraged because it does not make it clear that they are class methods."

      ---

      * Chapter 5: Interfaces and Inheritance, page 145:

        The code "if ( (obj1)isLargerThan(obj2)) ..." should be changed to "if ( (obj1)isLargerThan(obj2) ..."
        in three places by removing the extra parenthesis, ). The three lines should read:

        ```

        if ( (obj1)isLargerThan(obj2) > 0);
        if ( (obj1)isLargerThan(obj2) < 0);
        if ( (obj1)isLargerThan(obj2) == 0);

        ```

        Thanks to Clare Murnaghan for catching this.

      ---

      * Chapter 8: Numbers and Strings, page 200:

        In the title for Table 8.3, the file name should be `TestFormat.java`.

      ---

      * Chapter 8: Numbers and Strings, page 208:

        In the Random Numbers section:
        1. in the 4th line, change the sentence to read: "For example, to generate an integer
           between 0 and 9."
        2. change the code in line 6 to read `int number = (int)(Math.random() * 10);`
        3. in line 8, remove the entire sentence that begins "The compiler boxes...."

        Thanks to Serge Abrashevich for pointing this out.

      ---

      * Chapter 8: Numbers and Strings, page 223:

        In the picture, change substring(sep, dot) to substring(sep + 1, dot)

        Thanks to Tomec Czechowski for pointing this out.

      ---

      * Chapter 3: Language Basics, page 80:

        The second paragraph from the bottom reads:
        > To see this effect more clearly, try removing the `continue`
        > statement and recompiling. When you run the program again, the count
        > will be wrong, saying that it found **44** p's instead of 9.

        In fact, when you run the program again, the count is **35**.

        Thanks to Cesar Siqueira for being the first to report this error!

        ---

        * Chapter 17: Java Web Start, page 525:

          The footnote takes you to the wrong URL. The correct URL is:

          ```

          docs/books/tutorialJWS/deployment/webstart/examples/Notepad.jnlp

          ```

          ---

          * Chapter 17: Java Web Start, page 526:

            This is an older JNLP file and needs to be slightly modified to use release 6.

            The `codebase` line should read:

            ```

            codebase = "http://java.sun.com/docs/books/
                        tutorialJWS/deployment/webstart/examples/"
            href="Notepad.jnlp">

            ```

            and the `j2se` version should read:

            ```

            <j2se version="1.6+"
                  href="http://java.sun.com/products/autodl/j2se"/>

            ```

            Thanks to Ian Davis for catching this!

            ---

            * Appendix A

              There is a clarification to the descriptive text above the keyword list.

              Previous text:
              > "Here's a list of keywords in the Java language. These words are reserved — you cannot use any of these words as names in your programs. `true`, `false`, and `null` are not keywords but they are reserved words, so you cannot use them as names in your programs either."

              Clarified text:
              > "Here's a list of keywords in the Java programming language. You cannot use any of the following as identifiers in your programs. The keywords `const` and `goto` are reserved, even though they are not currently used. `true`, `false`, and `null` might seem like keywords, but they are actually literals; you cannot use them as identifiers in your programs."




A browser with JavaScript enabled is required for this page to operate properly.