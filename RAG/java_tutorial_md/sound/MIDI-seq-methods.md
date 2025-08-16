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

[Processing Audio with Controls](controls.html)

[Using Files and Format Converters](converters.html)

[Overview of the MIDI Package](overview-MIDI.html)

[Accessing MIDI System Resources](accessing-MIDI.html)

[Transmitting and Receiving MIDI Messages](MIDI-messages.html)

[Introduction to Sequencers](MIDI-seq-intro.html)

Using Sequencer Methods

[Using Advanced Sequencer Features](MIDI-seq-adv.html)

[Synthesizing Sound](MIDI-synth.html)

[Introduction to the Service Provider Interfaces](SPI-intro.html)

[Providing Sampled-Audio Services](SPI-providing-sampled.html)

[Providing MIDI Services](SPI-providing-MIDI.html)

[Home Page](../index.html)
>
[Sound](./index.html)

[« Previous](MIDI-seq-intro.html) • [Trail](./TOC.html) • [Next »](MIDI-seq-adv.html)

# Using Sequencer Methods

The
[`Sequencer`](http://download.oracle.com/javase/7/docs/api/javax/sound/midi/Sequencer.html)
interface provides methods in several categories:

* Methods to load sequence data from a MIDI file or a `Sequence` object, and to save the currently loaded sequence data to a MIDI file.
  * Methods analogous to the transport functions of a tape recorder, for stopping and starting playback and recording, enabling and disabling recording on specific tracks, and shuttling the current playback or recording position in a `Sequence`.
    * Advanced methods for querying and setting the synchronization and timing parameters of the object. A `Sequencer` may play at different tempos, with some `Tracks` muted, and in various synchronization states with other objects.
      * Advanced methods for registering "listener" objects that are notified when the `Sequencer` processes certain kinds of MIDI events.

Regardless of which `Sequencer` methods you'll invoke, the first step is to obtain a `Sequencer` device from the system and reserve it for your program's use.

### Obtaining a Sequencer

An application program doesn't instantiate a `Sequencer`;
after all, `Sequencer` is just an interface. Instead, like all devices
in the Java Sound API's MIDI package, a `Sequencer` is accessed through
the static `MidiSystem` object. As previously mentioned in
[Accessing MIDI System Resources](accessing-MIDI.html),
the following `MidiSystem` method can
be used to obtain the default `Sequencer`:

```

static Sequencer getSequencer()

```

The following code fragment obtains the default `Sequencer`, acquires any system resources it needs, and makes it operational:

```

Sequencer sequencer;
// Get default sequencer.
sequencer = MidiSystem.getSequencer(); 
if (sequencer == null) {
    // Error -- sequencer device is not supported.
    // Inform user and return...
} else {
    // Acquire resources and make operational.
    sequencer.open();
}

```

The invocation of `open` reserves the sequencer device for your program's use. It doesn't make much sense to imagine sharing a sequencer, because it can play only one sequence at a time. When you're done using the sequencer, you can make it available to other programs by invoking `close`.

Non-default sequencers can be obtained as described
in
[Accessing MIDI System Resources](accessing-MIDI.html).

### Loading a Sequence

Having obtained a sequencer from the system and reserved it, you then need load the data that the sequencer should play. There are three typical ways of accomplishing this:

* Reading the sequence data from a MIDI file
  * Recording it in real time by receiving MIDI messages from another device, such as a MIDI input port
    * Building it programmatically "from scratch" by adding tracks to an empty sequence and adding `MidiEvent` objects to those tracks

We'll now look at the first of these ways of getting sequence data. (The other
two ways are described below under [Recording
and Saving Sequences](#124654) and [Editing a Sequence](#124674),
respectively.) This first way actually encompasses two slightly different approaches.
One approach is to feed MIDI file data to an `InputStream` that you
then read directly to the sequencer by means of `Sequencer.setSequence(InputStream)`.
With this approach, you don't explicitly create a `Sequence` object.
In fact, the `Sequencer` implementation might not even create a `Sequence`
behind the scenes, because some sequencers have a built-in mechanism for handling
data directly from a file.

The other approach is to create a `Sequence`
explicitly. You'll need to use this approach if you're going to edit the sequence
data before playing it. With this approach, you invoke `MidiSystem's`
overloaded method `getSequence`. The method is able to get the sequence
from an `InputStream`, a `File`, or a `URL`.
The method returns a `Sequence` object that can then be loaded into
a `Sequencer` for playback. Expanding on the previous code excerpt,
here's an example of obtaining a `Sequence` object from a `File`
and loading it into our `sequencer`:

```

try {
    File myMidiFile = new File("seq1.mid");
    // Construct a Sequence object, and
    // load it into my sequencer.
    Sequence mySeq = MidiSystem.getSequence(myMidiFile);
    sequencer.setSequence(mySeq);
} catch (Exception e) {
   // Handle error and/or return
}

```

Like `MidiSystem's` `getSequence`
method, `setSequence` may throw an `InvalidMidiDataException`—and,
in the case of the `InputStream` variant, an `IOException`—if
it runs into any trouble.

### Playing a Sequence

Starting and stopping a `Sequencer` is accomplished using the following methods:

> ```
>     void start()
>
> ```

and
> ```
>     void stop()
>
> ```

The `Sequencer.start` method begins playback of the sequence. Note that playback starts at the current position in a sequence. Loading an existing sequence using the `setSequence` method, described above, initializes the sequencer's current position to the very beginning of the sequence. The `stop` method stops the sequencer, but it does not automatically rewind the current `Sequence`. Starting a stopped `Sequence` without resetting the position simply resumes playback of the sequence from the current position. In this case, the `stop` method has served as a pause operation. However, there are various `Sequencer` methods for setting the current sequence position to an arbitrary value before playback is started. (We'll discuss these methods below.)

As mentioned earlier, a `Sequencer` typically
has one or more `Transmitter` objects, through which it sends `MidiMessages`
to a `Receiver`. It is through these `Transmitters` that
a `Sequencer` plays the `Sequence`, by emitting appropriately
timed `MidiMessages` that correspond to the `MidiEvents`
contained in the current `Sequence`. Therefore, part of the setup
procedure for playing back a `Sequence` is to invoke the `setReceiver`
method on the `Sequencer's` `Transmitter` object, in effect
wiring its output to the device that will make use of the played-back data.
For more details on `Transmitters` and `Receivers`,
refer back to
[Transmitting and Receiving MIDI Messages](MIDI-messages.html).

### Recording and Saving Sequences

To capture MIDI data to a `Sequence`, and subsequently to a file, you need to perform some additional steps beyond those described above. The following outline shows the steps necessary to set up for recording to a `Track` in a `Sequence`:

1. Use `MidiSystem.getSequencer` to get a new sequencer to use for recording, as above.

   - Set up the "wiring" of the MIDI connections. The object that is transmitting the MIDI data to be recorded should be configured, through its `setReceiver` method, to send data to a `Receiver` associated with the recording `Sequencer`.

     - Create a new `Sequence` object, which will store the recorded data. When you create the `Sequence` object, you must specify the global timing information for the sequence. For example:
       > ```
       >       Sequence mySeq;
       >       try{
       >           mySeq = new Sequence(Sequence.PPQ, 10);
       >       } catch (Exception ex) { 
       >           ex.printStackTrace(); 
       >       }
       >
       > ```

       The constructor for `Sequence` takes as arguments a `divisionType` and a timing resolution. The `divisionType` argument specifies the units of the resolution argument. In this case, we've specified that the timing resolution of the `Sequence` we're creating will be 10 pulses per quarter note. An additional optional argument to the `Sequence` constructor is a number of tracks argument, which would cause the initial sequence to begin with the specified number of (initially empty) `Tracks`. Otherwise the `Sequence` will be created with no initial `Tracks`; they can be added later as needed.

       - Create an empty `Track` in the `Sequence`, with `Sequence.createTrack`. This step is unnecessary if the `Sequence` was created with initial `Tracks`.

         - Using `Sequencer.setSequence`, select our new `Sequence` to receive the recording. The `setSequence` method ties together an existing `Sequence` with the `Sequencer`, which is somewhat analogous to loading a tape onto a tape recorder.

           - Invoke `Sequencer.recordEnable` for each `Track` to be recorded. If necessary, get a reference to the available `Tracks` in the `Sequence` by invoking `Sequence.getTracks`.

             - Invoke `startRecording` on the `Sequencer`.

               - When done recording, invoke `Sequencer.stop` or `Sequencer.stopRecording`.

                 - Save the recorded `Sequence` to a MIDI file with `MidiSystem.write`. The `write` method of `MidiSystem` takes a `Sequence` as one of its arguments, and will write that `Sequence` to a stream or file.

### Editing a Sequence

Many application programs allow a sequence to be created by loading it from a file, and quite a few also allow a sequence to be created by capturing it from live MIDI input (that is, recording). Some programs, however, will need to create MIDI sequences from scratch, whether programmatically or in response to user input. Full-featured sequencer programs permit the user to manually construct new sequences, as well as to edit existing ones.

These data-editing operations are achieved in the Java Sound API not by `Sequencer` methods, but by methods of the data objects themselves: `Sequence`, `Track`, and `MidiEvent`. You can create an empty sequence using one of the `Sequence` constructors, and then add tracks to it by invoking the following `Sequence` method:

> ```
>     Track createTrack()
> ```

If your program allows the user to edit sequences, you'll need this `Sequence` method to remove tracks:
> ```
>     boolean deleteTrack(Track track) 
>
> ```

Once the sequence contains tracks, you can modify the contents of the tracks by invoking methods of the `Track` class. The `MidiEvents` contained in the `Track` are stored as a `java.util.Vector` in the `Track` object, and `Track` provides a set of methods for accessing, adding, and removing the events in the list. The methods `add` and `remove` are fairly self-explanatory, adding or removing a specified `MidiEvent` from a `Track`. A `get` method is provided, which takes an index into the `Track's` event list and returns the `MidiEvent` stored there. In addition, there are `size` and `tick` methods, which respectively return the number of `MidiEvents` in the track, and the track's duration, expressed as a total number of `Ticks`.

To create a new event before adding it to the track, you'll of course use the `MidiEvent` constructor. To specify or modify the MIDI message embedded in the event, you can invoke the `setMessage` method of the appropriate `MidiMessage` subclass (`ShortMessage`, `SysexMessage`, or `MetaMessage`). To modify the time that the event should occur, invoke `MidiEvent.setTick`.

In combination, these low-level methods provide the basis for the editing functionality needed by a full-featured sequencer program.

[« Previous](MIDI-seq-intro.html)
•
[Trail](./TOC.html)
•
[Next »](MIDI-seq-adv.html)

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

**Previous page:** Introduction to Sequencers
  
**Next page:** Using Advanced Sequencer Features




A browser with JavaScript enabled is required for this page to operate properly.