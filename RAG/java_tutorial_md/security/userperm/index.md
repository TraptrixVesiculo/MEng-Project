[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

Implementing Your Own Permission

[TerrysGame](game.html)

[The HighScore Class](highscore.html)

[The HighScorePermission Class](perm.html)

[A Sample Policy File](policy.html)

[Putting It All Together](together.html)

[Steps for the HighScore Developer (Chris)](chris.html)

[Steps for the TerrysGame Developer (Terry)](terry.html)

[Steps for a User Running TerrysGame (Kim)](kim.html)

**Trail:** Security Features in Java SE

[Home Page](../../index.html)
>
[Security Features in Java SE](../index.html)

[« Previous](../apisign/index.html) • [Trail](../TOC.html) • [Next »](game.html)

# Lesson: Implementing Your Own Permission

This lesson demonstrates how to write a class that
defines its own special permission. The basic components
in this lesson include:

1. A sample game called **TerrysGame**.

   - A class called **HighScore**, which is used by `TerrysGame`
     to store a user's latest high score.

     - A class called **HighScorePermission**, which is used to
       protect access to the user's stored high score value.

       - A user's security **policy file**, which grants permission
         to `TerrysGame` to update his/her high score.

The basic scenario is as follows:

1. A user plays `TerrysGame`.

   - If the user reaches a new high score, `TerrysGame`
     uses the `HighScore` class to save this new value.

     - The `HighScore` class looks into the user's security policy to
       check if `TerrysGame` has permission to update the user's
       high score value.

       - If `TerrysGame` has permission to update the high score,
         then the HighScore class updates that value.

We describe the key points of each of the basic components
and then show a sample run:

* [TerrysGame](game.html)

  * [The HighScore Class](highscore.html)

    * [The HighScorePermission Class](perm.html)

      * [A Sample Policy File](policy.html)

        * [Putting It All Together](together.html)

[« Previous](../apisign/index.html)
•
[Trail](../TOC.html)
•
[Next »](game.html)

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
  
**Next page:** TerrysGame




A browser with JavaScript enabled is required for this page to operate properly.