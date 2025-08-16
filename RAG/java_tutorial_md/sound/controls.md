[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** Sound

[Overview of the Sampled Package](sampled-overview.html)

[Accessing Audio System Resources](accessing.html)

[Playing Back Audio](playing.html)

[Capturing Audio](capturing.html)

Processing Audio with Controls

[Using Files and Format Converters](converters.html)

[Overview of the MIDI Package](overview-MIDI.html)

[Accessing MIDI System Resources](accessing-MIDI.html)

[Transmitting and Receiving MIDI Messages](MIDI-messages.html)

[Introduction to Sequencers](MIDI-seq-intro.html)

[Using Sequencer Methods](MIDI-seq-methods.html)

[Using Advanced Sequencer Features](MIDI-seq-adv.html)

[Synthesizing Sound](MIDI-synth.html)

[Introduction to the Service Provider Interfaces](SPI-intro.html)

[Providing Sampled-Audio Services](SPI-providing-sampled.html)

[Providing MIDI Services](SPI-providing-MIDI.html)

[Home Page](../index.html)
>
[Sound](./index.html)

[« Previous](capturing.html) • [Trail](./TOC.html) • [Next »](converters.html)

# Processing Audio with Controls

Previous sections have discussed how to play or capture audio samples. The implicit goal has been to deliver samples as faithfully as possible, without modification (other than possibly mixing the samples with those from other audio lines). Sometimes, however, you want to be able to modify the signal. The user might want it to sound louder, quieter, fuller, more reverberant, higher or lower in pitch, and so on. This page discusses the Java Sound API features that provide these kinds of signal processing.

There are two ways to apply signal processing:

* You can use any processing supported by the mixer or its component lines, by querying for
  [`Control`](http://download.oracle.com/javase/7/docs/api/javax/sound/sampled/Control.html)
  objects and then setting the controls as the user desires. Typical controls supported by mixers and lines include gain, pan, and reverberation controls.

  * If the kind of processing you need isn't provided by the mixer or its lines, your program can operate directly on the audio bytes, manipulating them as desired.

This page discusses the first technique in greater detail, because there is no special API for the second technique.

### Introduction to Controls

A mixer can have various sorts of signal-processing controls on some or all of its lines. For example, a mixer used for audio capture might have an input port with a gain control, and target data lines with gain and pan controls. A mixer used for audio playback might have sample-rate controls on its source data lines. In each case, the controls are all accessed through methods of the `Line` interface.

Because the `Mixer` interface extends `Line`, the mixer itself can have its own set of controls. These might serve as master controls affecting all the mixer's source or target lines. For example, the mixer might have a master gain control whose value in decibels is added to the values of individual gain controls on its target lines.

Others of the mixer's own controls might affect a special line, neither a source nor a target, that the mixer uses internally for its processing. For example, a global reverb control might choose the sort of reverberation to apply to a mixture of the input signals, and this "wet" (reverberated) signal would get mixed back into the "dry" signal before delivery to the mixer's target lines.

If the mixer or any of its lines have controls, you might wish to expose the controls via graphical objects in your program's user interface, so that the user can adjust the audio characteristics as desired. The controls are not themselves graphical; they just allow you to retrieve and change their settings. It's up to you to decide what sort of graphical representations (sliders, buttons, etc.), if any, to use in your program.

All controls are implemented as concrete subclasses of the abstract class `Control`. Many typical audio-processing controls can be described by abstract subclasses of `Control` based on a data type (such as boolean, enumerated, or float). Boolean controls, for example, represent binary-state controls, such as on/off controls for mute or reverb. Float controls, on the other hand, are well suited to represent continuously variable controls, such as pan, balance, or volume.

The Java Sound API specifies the following abstract subclasses of `Control`:

* [`BooleanControl`](http://download.oracle.com/javase/7/docs/api/javax/sound/sampled/BooleanControl.html)— represents a binary-state (true or false)
  control. For example, mute, solo, and on/off switches would be good candidates
  for `BooleanControls`. 

  * [`FloatControl`](http://download.oracle.com/javase/7/docs/api/javax/sound/sampled/FloatControl.html)
    — data model providing control over a range
    of floating-point values. For example, volume and pan are `FloatControls`
    that could be manipulated via a dial or slider. 

    * [`EnumControl`](http://download.oracle.com/javase/7/docs/api/javax/sound/sampled/EnumControl.html)— offers a choice from a set of objects. For
      example, you might associate a set of buttons in the user interface with an
      `EnumControl` to select one of several preset reverberation settings.

      * [`CompoundControl`](http://download.oracle.com/javase/7/docs/api/javax/sound/sampled/CompoundControl.html)—provides access to a collection of related
        items, each of which is itself an instance of a `Control` subclass.
        `CompoundControls` represent multi-control modules such as graphic
        equalizers. (A graphic equalizer would typically be depicted by a set of sliders,
        each affecting a `FloatControl`.)

Each subclass of `Control` above has methods appropriate for its underlying
data type. Most of the classes include methods that set and get the control's
current value(s), get the control's label(s), and so on.

Of course, each class has methods that are particular to it and the data model represented by the class. For example, `EnumControl` has a method that lets you get the set of its possible values, and `FloatControl` permits you to get its minimum and maximum values, as well as the precision (increment or step size) of the control.

Each subclass of `Control` has a corresponding `Control.Type` subclass, which includes static instances that identify specific controls.

The following table shows each `Control` subclass, its corresponding `Control.Type` subclass, and the static instances that indicate specific kinds of controls:

| `Control` | `Control.Type` | `Control.Type`**instances** |
| `BooleanControl` | `BooleanControl.Type` | `MUTE`  Mute status of line  `APPLY_REVERB`  Reverberation on/off |
| `CompoundControl` | `CompoundControl.Type` | (none) |
| `EnumControl` | `EnumControl.Type` | `REVERB` Access to reverb settings (each is an instance of ReverbType) |
| `FloatControl` | `FloatControl.Type` | `AUX_RETURN` Auxiliary return gain on a line  `AUX_SEND`  Auxiliary send gain on a line  `BALANCE`  Left-right volume balance  `MASTER_GAIN`  Overall gain on a line  `PAN`  Left-right position  `REVERB_RETURN`  Post-reverb gain on a line  `REVERB_SEND`  Pre-reverb gain on a line  `SAMPLE_RATE`  Playback sample rate  `VOLUME`  Volume on a line |

An implementation of the Java Sound API can provide any or all of these control types on its mixers and lines. It can also supply additional control types not defined in the Java Sound API. Such control types could be implemented via concrete subclasses of any of these four abstract subclasses, or via additional `Control` subclasses that don't inherit from any of these four abstract subclasses. An application program can query each line to find what controls it supports.

### Getting a Line that Has the Desired Controls

In many cases, an application program will simply display
whatever controls happen to be supported by the line in question. If the line
doesn't have any controls, so be it. But what if it's important to find a line
that has certain controls? In that case, you can use a `Line.Info` to
obtain a line that has the right characteristics, as previously described under
[Getting a Line of a Desired Type](accessing.html#113154).

For example, suppose you prefer an input port that lets the user set the volume of the sound input. The following code excerpt shows how one might query the default mixer to determine whether it has the desired port and control:

> ```
> Port lineIn;
> FloatControl volCtrl;
> try {
>   mixer = AudioSystem.getMixer(null);
>   lineIn = (Port)mixer.getLine(Port.Info.LINE_IN);
>   lineIn.open();
>   volCtrl = (FloatControl) lineIn.getControl(  
>
>       FloatControl.Type.VOLUME);
>
>   // Assuming getControl call succeeds, 
>   // we now have our LINE_IN VOLUME control.
> } catch (Exception e) {
>   System.out.println("Failed trying to find LINE_IN"
>     + " VOLUME control: exception = " + e);
> }
> if (volCtrl != null)
>   // ...
>
> ```

### Getting the Controls from the Line

An application program that needs to expose controls in its user interface might simply query the available lines and controls, and then display an appropriate user-interface element for every control on every line of interest. In such a case, the program's only mission is to provide the user with "handles" on the control; not to know what those controls do to the audio signal. As long as the program knows how to map a line's controls into user-interface elements, the Java Sound API architecture of `Mixer`, `Line`, and `Control` will generally take care of the rest.

For example, suppose your program plays back sound.
You're using a `SourceDataLine`, which you've obtained as previously described
under
[Getting a Line of a Desired Type](accessing.html#113154).
You can access the line's controls by invoking the following `Line` method:

```

Control[] getControls()

```

Then, for each of the controls in this returned array, you then use the following `Control` method to get the control's type:

```

Control.Type getType()

```

Knowing the specific `Control.Type` instance, your program can display a corresponding user-interface element. Of course, choosing "a corresponding user-interface element" for a specific `Control.Type` depends on the approach taken by your program. On the one hand, you might use the same kind of element to represent all `Control.Type` instances of the same class. This would require you to query the *class* of the `Control.Type` instance using, for example, the `Object.getClass` method. Let's say the result matched `BooleanControl.Type`. In this case, your program might display a generic checkbox or toggle button, but if its class matched `FloatControl.Type`, then you might display a graphic slider.

On the other hand, your program might distinguish between
different types of controls—even those of the same class—and use a
different user-interface element for each one. This would require you to test
the *instance* returned by `Control's getType` method. Then
if, for example, the type matched `BooleanControl.Type.APPLY_REVERB`,
your program might display a checkbox; while if the type matched `BooleanControl.Type.MUTE`,
you might instead display a toggle button.

### Using a Control to Change the Audio Signal

Now that you know how to access a control and determine its type, this section will describe how to use `Controls` to change aspects of the audio signal. This section doesn't cover every available control; rather, it provides a few examples in this area to show you how to get started. These example include:

* Controlling a line's mute state
  * Changing a line's volume
    * Selecting among various reverberation presets

Suppose that your program has accessed all of its mixers, their lines and the controls on those lines, and that it has a data structure to manage the logical associations between the controls and their corresponding user-interface elements. Then, translating the user's manipulations of those controls into the corresponding `Control` methods becomes a fairly straightforward matter.

The following subsections describe some of the methods that must be invoked to affect the changes to specific controls.

#### Controlling a Line's Mute State

Controlling the mute state of any line is simply a matter of calling the following `BooleanControl` method:

```

void setValue(boolean value)

```

(Presumably, the program knows, by referring to its control-management data structures, that the mute is an instance of a `BooleanControl`.) To mute the signal that's passing through the line, the program invokes the method above, specifying `true` as the value. To turn muting off, permitting the signal to flow through the line, the program invokes the method with the parameter set to `false`.

#### Changing a Line's Volume

Let's assume your program associates a particular graphic slider with a particular line's volume control. The value of a volume control (i.e., `FloatControl.Type.VOLUME`) is set using the following `FloatControl` method:

```

void setValue(float newValue)

```

Detecting that the user moved the slider, the program gets the slider's current value and passes it, as the parameter `newValue`, to the method above. This changes the volume of the signal flowing though the line that "owns" the control.

#### Selecting among Various Reverberation Presets

Let's suppose that our program has a mixer with a line that has a control of type `EnumControl.Type.REVERB`. Calling the `EnumControl` method:

```

java.lang.Objects[] getValues()

```

on that control produces an array of `ReverbType` objects. If desired, the particular parameter settings of each of these objects can be accessed using the following `ReverbType` methods:
> ```
>
> int getDecayTime() 
> int getEarlyReflectionDelay() 
> float getEarlyReflectionIntensity() 
> int getLateReflectionDelay() 
> float getLateReflectionIntensity() 
>
> ```

For example, if a program only wants a single reverb setting that sounds like a cavern, it can iterate over the `ReverbType` objects until it finds one for which `getDecayTime` returns a value greater than 2000. For a thorough explanation of these methods, including a table of representative return values, see the API reference documentation for `javax.sound.sampled.ReverbType`.

Typically, though, a program will create a user-interface element, for example, a radio button, for each of the `ReverbType` objects within the array returned by the `getValues` method. When the user clicks on one of these radio buttons, the program invokes the `EnumControl` method
> ```
> void setValue(java.lang.Object value) 
>
> ```

where `value` is set to the `ReverbType` that corresponds to the newly engaged button. The audio signal sent through the line that "owns" this `EnumControl` will then be reverberated according to the parameter settings that constitute the control's current `ReverbType` (i.e., the particular `ReverbType` specified in the `value` argument of the `setValue` method).

So, from our application program's perspective, enabling a user to move from one reverberation preset (i.e., ReverbType) to another is simply a matter of connecting each element of the array returned by `getValues` to a distinct radio button.

### Manipulating the Audio Data Directly

The `Control` API allows an implementation
of the Java Sound API, or a third-party provider of a mixer, to supply arbitrary
sorts of signal processing through controls. But what if no mixer offers the
kind of signal processing you need? It will take more work, but you might be
able to implement the signal processing in your program. Because the Java Sound
API gives you access to the audio data as an array of bytes, you can alter these
bytes in any way you choose.

If you're processing incoming sound, you can read the bytes from a `TargetDataLine` and then manipulate them. An algorithmically trivial example that can yield sonically intriguing results is to play a sound backwards by arranging its frames in reverse order. This trivial example may not be of much use for your program, but there are numerous sophisticated digital signal processing (DSP) techniques that might be more appropriate. Some examples are equalization, dynamic-range compression, peak limiting, and time stretching or compression, as well as special effects such as delay, chorus, flanging, distortion, and so on.

To play back processed sound, you can place your manipulated
array of bytes into a `SourceDataLine` or `Clip`. Of course,
the array of bytes need not be derived from an existing sound. You can synthesize
sounds from scratch, although this requires some knowledge of acoustics or else
access to sound-synthesis functions. For either processing or synthesis, you
may want to consult an audio DSP textbook for the algorithms in which you're
interested, or else import a third-party library of signal-processing functions
into your program. For playback of synthesized sound, consider whether the `Synthesizer`
API in the `javax.sound.midi` package meets your needs instead.
You'll learn about more about `javax.sound.midi` later
under
[Synthesizing Sound](MIDI-synth.html).

[« Previous](capturing.html)
•
[Trail](./TOC.html)
•
[Next »](converters.html)

---

Problems with the examples? Try [Compiling and Running
the Examples: FAQs](../information/run-examples.html).
  
Complaints? Compliments? Suggestions? [Give
us your feedback](http://download.oracle.com/javase/feedback.html).

Your use of this page and all the material on pages under "The Java Tutorials" banner,
and all the material on pages under "The Java Tutorials" banner is subject to the [Java SE Tutorial Copyright
and License](../information/license.html).
Additionally, any example code contained in any of these Java
Tutorials pages is licensed under the
[Code
Sample License](http://developers.sun.com/license/berkeley_license.html).

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| |  |  | | --- | --- | | duke image | Oracle logo | | [About Oracle](http://www.oracle.com/us/corporate/index.html) | [Oracle Technology Network](http://www.oracle.com/technology/index.html) | [Terms of Service](https://www.samplecode.oracle.com/servlets/CompulsoryClickThrough?type=TermsOfService) | Copyright © 1995, 2011 Oracle and/or its affiliates. All rights reserved. |

**Previous page:** Capturing Audio
  
**Next page:** Using Files and Format Converters




A browser with JavaScript enabled is required for this page to operate properly.