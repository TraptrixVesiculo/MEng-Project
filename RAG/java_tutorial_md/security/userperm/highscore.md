[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** Security Features in Java SE
  
**Lesson:** Implementing Your Own Permission

[Implementing Your Own Permission](index.html)

[TerrysGame](game.html)

The HighScore Class

[The HighScorePermission Class](perm.html)

[A Sample Policy File](policy.html)

[Putting It All Together](together.html)

[Steps for the HighScore Developer (Chris)](chris.html)

[Steps for the TerrysGame Developer (Terry)](terry.html)

[Steps for a User Running TerrysGame (Kim)](kim.html)

[Home Page](../../index.html)
>
[Security Features in Java SE](../index.html)
>
[Implementing Your Own Permission](index.html)

[« Previous](game.html) • [Trail](../TOC.html) • [Next »](perm.html)

# The HighScore Class

The `HighScore` class stores and protects access to the user's
high score for `TerrysGame` (and any other games that call it).
For simplicity, this class saves
the high score value into a file, called `.highscore`, in the
user's home directory. However, before allowing `TerrysGame` to
retrieve or update the user's high score value, this class
checks to make sure that the user has granted `TerrysGame`
permission to access the high score in his/her security
policy file.

### Checking that `TerrysGame` has the HighScorePermission

> To check whether or not `TerrysGame` has permission to access
> the user's high score, the `HighScore` class must:
>
> 1. Call `System.getSecurityManager()` to get
>    the currently installed security manager.
>
>    - If the result is not null (i.e., there *is* a
>      security manager, as opposed to the caller being an
>      application that is unrestricted), then
>
>      1. Construct a `HighScorePermission` object, and
>
>         - Call the security manager's `checkPermission`
>           method, and pass it the newly constructed `HighScorePermission` object.
>
> Here is the code:
>
> ```
>
> SecurityManager sm = System.getSecurityManager();
> if (sm != null) {
>     sm.checkPermission(new HighScorePermission(gameName));
> }
>
> ```
>
> The `checkPermission` method essentially
> asks the security manager
> if `TerrysGame` has the specified `HighScorePermission`.
> In other words, it asks
> the security manager if `TerrysGame` has permission to update the user's
> high score value for the specified game (`TerrysGame`).
> The underlying security framework will consult
> the user's security policy to see if `TerrysGame` indeed has this
> permission.

### The HighScore Code

> [`Here`](examples/com/scoredev/scores/HighScore.java)
> is the complete source code for the `HighScore` class.
>
> Note: The `doPrivileged` method calls are used to enable
> `HighScore` to temporarily access resources that are
> available to it
> but that are not available to the code that calls it (`TerrysGame`).
> For example, it is expected that the policy file will
> grant `HighScore` permission to access the `.highscore`
> file in the user's home directory, but it will not grant this permission
> to games, such as `TerrysGame`.

[« Previous](game.html)
•
[Trail](../TOC.html)
•
[Next »](perm.html)

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

**Previous page:** TerrysGame
  
**Next page:** The HighScorePermission Class




A browser with JavaScript enabled is required for this page to operate properly.