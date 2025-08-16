[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** Internationalization
  
**Lesson:** Working with Text
  
**Section:** Comparing Strings

[Working with Text](index.html)

[Checking Character Properties](charintro.html)

[Comparing Strings](collationintro.html)

[Performing Locale-Independent Comparisons](locale.html)

Customizing Collation Rules

[Improving Collation Performance](perform.html)

[Unicode](unicode.html)

[Terminology](terminology.html)

[Supplementary Characters as Surrogates](supplementaryChars.html)

[Character and String APIs](characterClass.html)

[Sample Usage](usage.html)

[Design Considerations](design.html)

[More Information](info.html)

[Detecting Text Boundaries](boundaryintro.html)

[About the BreakIterator Class](about.html)

[Character Boundaries](char.html)

[Word Boundaries](word.html)

[Sentence Boundaries](sentence.html)

[Line Boundaries](line.html)

[Converting Latin Digits to Other Unicode Digits](shapedDigits.html)

[Converting Non-Unicode Text](convertintro.html)

[Byte Encodings and Strings](string.html)

[Character and Byte Streams](stream.html)

[Normalizing Text](normalizerapi.html)

[Home Page](../../index.html)
>
[Internationalization](../index.html)
>
[Working with Text](index.html)

[« Previous](locale.html) • [Trail](../TOC.html) • [Next »](perform.html)

# Customizing Collation Rules

The previous section discussed how to use the predefined rules for a
locale to compare strings. These collation rules determine the sort
order of strings. If the predefined collation rules do not meet your
needs, you can design your own rules and assign them to a
`RuleBasedCollator`  object.

Customized collation rules are contained in a `String`
object that is passed to the `RuleBasedCollator`
constructor. Here's a simple example:

```

String simpleRule = "< a < b < c < d";
RuleBasedCollator simpleCollator =  new RuleBasedCollator(simpleRule);

```

For the `simpleCollator` object in the previous example,
`a` is less than `b`, which is less that
`c`, and so forth. The `simpleCollator.compare` 
method references these rules when comparing strings. The full syntax
used to construct a collation rule is more flexible and complex than
this simple example. For a full description of the syntax, refer to the
API documentation for the
[`RuleBasedCollator`](http://download.oracle.com/javase/7/docs/api/java/text/RuleBasedCollator.html) class.

The example that follows sorts a list of Spanish words with two
collators. Full source code for this example is in
[`RulesDemo.java`](examples/RulesDemo.java).

The `RulesDemo` program starts by defining collation rules
for English and Spanish. The program will sort the Spanish words in the
traditional manner. When sorting by the traditional rules, the letters
ch and ll and their uppercase equivalents each have their own positions
in the sort order. These character pairs compare as if they were one
character. For example, ch sorts as a single letter, following cz in
the sort order. Note how the rules for the two collators differ:

```

String englishRules =
    ("< a,A < b,B < c,C < d,D < e,E < f,F " +
     "< g,G < h,H < i,I < j,J < k,K < l,L " +
     "< m,M < n,N < o,O < p,P < q,Q < r,R " +
     "< s,S < t,T < u,U < v,V < w,W < x,X " +
     "< y,Y < z,Z");

String smallnTilde = new String("\u00F1"); // ñ
String capitalNTilde = new String("\u00D1"); // Ñ

String traditionalSpanishRules =
    ("< a,A < b,B < c,C " +
     "< ch, cH, Ch, CH " +
     "< d,D < e,E < f,F " +
     "< g,G < h,H < i,I < j,J < k,K < l,L " +
     "< ll, lL, Ll, LL " +
     "< m,M < n,N " +
     "< " + smallnTilde + "," + capitalNTilde + " " +
     "< o,O < p,P < q,Q < r,R " +
     "< s,S < t,T < u,U < v,V < w,W < x,X " +
     "< y,Y < z,Z");

```

The following lines of code create the collators and invoke the sort routine:

```

try {
    RuleBasedCollator enCollator =
        new RuleBasedCollator(englishRules);
    RuleBasedCollator spCollator =
        new RuleBasedCollator(traditionalSpanishRules);

    sortStrings(enCollator, words);
    printStrings(words);

    System.out.println();

    sortStrings(spCollator, words);
    printStrings(words);
} catch (ParseException pe) {
    System.out.println("Parse exception for rules");
}

```

The sort routine, called `sortStrings`, is generic. It will
sort any array of words according to the rules of any
`Collator` object:

```

public static void sortStrings(Collator collator, String[] words) {
    String tmp;
    for (int i = 0; i < words.length; i++) {
	for (int j = i + 1; j < words.length; j++) {
	    if (collator.compare(words[i], words[j]) > 0) {
		tmp = words[i];
		words[i] = words[j];
		words[j] = tmp;
	    }
	}
    }
}

```

When sorted with the English collation rules, the array of words is as follows:

```

chalina
curioso
llama
luz

```

Compare the preceding list with the following, which is sorted
according to the traditional Spanish rules of collation:

```

curioso
chalina
luz
llama

```

[« Previous](locale.html)
•
[Trail](../TOC.html)
•
[Next »](perform.html)

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

**Previous page:** Performing Locale-Independent Comparisons
  
**Next page:** Improving Collation Performance




A browser with JavaScript enabled is required for this page to operate properly.