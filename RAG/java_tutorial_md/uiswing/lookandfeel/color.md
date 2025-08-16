[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** Creating a GUI With JFC/Swing
  
**Lesson:** Modifying the Look and Feel
  
**Section:** Nimbus Look and Feel

[Modifying the Look and Feel](index.html)

[How to Set the Look and Feel](plaf.html)

[The Synth Look and Feel](synth.html)

[A Synth Example](synthExample.html)

[Nimbus Look and Feel](nimbus.html)

[Changing the Look of Nimbus](custom.html)

[Resizing a Component](size.html)

Changing the Color Theme

[For More Information](info.html)

[Home Page](../../index.html)
>
[Creating a GUI With JFC/Swing](../index.html)
>
[Modifying the Look and Feel](index.html)

[« Previous](size.html) • [Trail](../TOC.html) • [Next »](info.html)

# Changing the Color Theme

The Nimbus look and feel has a set of default
colors, but you are not required to use them.
You can change the colors to match your corporate brand
or other color scheme.

All of the colors used by Nimbus are stored as a set of
`UIManager` properties. You can change any or all
of these properties before you set the look and feel. For example:

```

UIManager.put("nimbusBase", new Color(...));
UIManager.put("nimbusBlueGrey", new Color(...));
UIManager.put("control", new Color(...));

for (LookAndFeelInfo info : UIManager.getInstalledLookAndFeels() {
    if ("Nimbus".equals(info.getName())) {
        UIManager.setLookAndFeel(info.getClassName());
        break;
    }
}

```

These three base colors, `nimbusBase`, `nimbusBlueGrey`,
and `control`, will address most of your needs.
See a full list of color keys and their default values on the
[Nimbus Defaults](_nimbusDefaults.html#primary) page.

[« Previous](size.html)
•
[Trail](../TOC.html)
•
[Next »](info.html)

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

**Previous page:** Resizing a Component
  
**Next page:** For More Information




A browser with JavaScript enabled is required for this page to operate properly.