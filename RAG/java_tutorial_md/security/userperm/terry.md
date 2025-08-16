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

Steps for the TerrysGame Developer (Terry)

[Steps for a User Running TerrysGame (Kim)](kim.html)

[Home Page](../../index.html)
>
[Security Features in Java SE](../index.html)
>
[Implementing Your Own Permission](index.html)

[« Previous](chris.html) • [Trail](../TOC.html) • [Next »](kim.html)

# Steps for the TerrysGame Developer (Terry)

The steps Terry would take, after creating a game (`TerrysGame` )
that calls the `HighScore` `getHighScore` and
`setHighScore`
methods to get and set, respectively, the user's high scores, are:

### Compile the Game Class

```

javac TerrysGame.java -classpath hs.jar -d .

```

### Place its class file in a JAR File

```

jar cvf terry.jar com/gamedev/games/TerrysGame.class

```

### Create a Keystore and Keys for Signing

```

keytool -genkey -keystore terry.keystore -alias signTJars

```

> Specify whatever you want for the passwords and distinguished
> name information.

### Sign the JAR File

```

jarsigner -keystore terry.keystore terry.jar signTJars

```

### Export the Public Key Certificate

```

keytool -export -keystore terry.keystore
    -alias signTJars -file Terry.cer

```

### Supply Files and Information Needed by Users

> That is, supply them
>
> * the signed JAR File `terry.jar,`
>
>   * the public key certificate file `Terry.cer`, and
>
>     * information as to the permissions the `TerrysGame` class needs.
>       For this, Terry could supply the exact grant entry needed.
>
> Game users also need files and information from Chris.
> For their convenience, Terry may forward this information to them:
>
> * the signed JAR File `hs.jar`,
>
>   * the public key certificate file `Chris.cer`, and
>
>     * information as to the permissions the `HighScore`
>       and `HighScorePermission`
>       classes must be granted in a policy file
>       in order to work. This could be the exact grant entry needed.

[« Previous](chris.html)
•
[Trail](../TOC.html)
•
[Next »](kim.html)

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

**Previous page:** Steps for the HighScore Developer (Chris)
  
**Next page:** Steps for a User Running TerrysGame (Kim)




A browser with JavaScript enabled is required for this page to operate properly.