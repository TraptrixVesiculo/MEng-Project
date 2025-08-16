[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** Security Features in Java SE
  
**Lesson:** Implementing Your Own Permission
  
**Section:** Putting It All Together

[Implementing Your Own Permission](index.html)

[TerrysGame](game.html)

[The HighScore Class](highscore.html)

[The HighScorePermission Class](perm.html)

[A Sample Policy File](policy.html)

[Putting It All Together](together.html)

[Steps for the HighScore Developer (Chris)](chris.html)

[Steps for the TerrysGame Developer (Terry)](terry.html)

Steps for a User Running TerrysGame (Kim)

[Home Page](../../index.html)
>
[Security Features in Java SE](../index.html)
>
[Implementing Your Own Permission](index.html)

[« Previous](terry.html) • [Trail](../TOC.html) • [Next »](../end.html)

# Steps for a User Running TerrysGame (Kim)

The steps a user, such as Kim, would take, are:

### Import the Certificates as Trusted Certificates

```

keytool -import -alias chris -file Chris.cer -keystore kim.keystore
keytool -import -alias terry -file Terry.cer -keystore kim.keystore

```

### Set Up a Policy File With the Required Permissions

> Here's the complete [kim.policy](examples/kim.policy) policy file,
> as described in [A Sample Policy File](policy.html).

### Run TerrysGame

> To set the high score:
>
> ```
>
> java -Djava.security.manager -Djava.security.policy=kim.policy
>  -classpath hs.jar;terry.jar com.gamedev.games.TerrysGame set 456
>
> ```
>
> To get the high score:
>
> ```
>
> java -Djava.security.manager -Djava.security.policy=kim.policy
>  -classpath hs.jar;terry.jar com.gamedev.games.TerrysGame get
>
> ```
>
> Notes:
>
> * If you don't specify `-Djava.security.manager`,
>   the application will run unrestricted (policy files and permissions
>   won't be checked).
>
>   * The `-Djava.security.policy=kim.policy`
>     tells where the policy file is.
>     Note: There are other ways of specifying the policy file.
>     For example, you can add an entry in the
>     security properties file that specifies the inclusion of `kim.policy`,
>     as discussed at the end of the
>     [See the Policy File Effects](../tour1/step3.html)
>     lesson.
>
>     * `-classpath hs.jar;terry.jar` specifies the JAR files
>       that contain the class files needed. For Windows, use a semicolon
>       (";") to separate JAR files; for Unix, use a colon (":").
>
>       * The policy file `kim.policy` specifies the keystore
>         `kim.keystore`. Since it does not provide an absolute
>         URL location for the keystore, the keystore is assumed to be in the
>         same directory as the policy file.

[« Previous](terry.html)
•
[Trail](../TOC.html)
•
[Next »](../end.html)

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

**Previous page:** Steps for the TerrysGame Developer (Terry)
  
**Next page:** End of Trail




A browser with JavaScript enabled is required for this page to operate properly.