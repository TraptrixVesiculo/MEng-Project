[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** Sound

[Overview of the Sampled Package](sampled-overview.html)

[Accessing Audio System Resources](accessing.html)

[Playing Back Audio](playing.html)

Capturing Audio

[Processing Audio with Controls](controls.html)

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

[« Previous](playing.html) • [Trail](./TOC.html) • [Next »](controls.html)

# Capturing Audio

*Capturing* refers to the process of obtaining
a signal from outside the computer. A common application of audio capture is
recording, such as recording the microphone input to a sound file. However,
capturing isn't synonymous with recording, because recording implies that the
application always saves the sound data that's coming in. An application that
captures audio doesn't necessarily store the audio. Instead it might do something
with the data as it's coming in — such as transcribe speech into text — but
then discard each buffer of audio as soon as it's finished with that buffer.

As discussed in
[Overview of the Sampled Package](sampled-overview.html),
a typical audio-input
system in an implementation of the Java
Sound API consists of:

1. An input port, such as a microphone port or a line-in port, which feeds its incoming audio data into:
   - A mixer, which places the input data in:
     - One or more target data lines, from which an application can retrieve the data.

       Commonly, only one input port can be open at a time, but an audio-input mixer that mixes audio from multiple ports is also possible. Another scenario consists of a mixer that has no ports but instead gets its audio input over a network.

       The `TargetDataLine` interface was introduced
       briefly under
       [The Line Interface Hierarchy](sampled-overview.html#lineHierarchy).
       `TargetDataLine` is directly analogous to the `SourceDataLine`
       interface, which was discussed extensively in
       [Playing Back Audio](playing.html).
       Recall that the `SourceDataLine`
       interface consists of:

* A `write` method to send audio to the mixer
  * An `available` method to determine how much data can be written to the buffer without blocking

Similarly, `TargetDataLine` consists of:

* A `read` method to get audio from the mixer
  * An `available` method to determine how much data can be read from the buffer without blocking

### Setting Up a TargetDataLine

The process of obtaining a target data line was described
in
[Accessing Audio System Resources](accessing.html) but we repeat it here for convenience:

> ```
> TargetDataLine line;
> DataLine.Info info = new DataLine.Info(TargetDataLine.class,   
>
>     format); // format is an AudioFormat object
> if (!AudioSystem.isLineSupported(info)) {
>     // Handle the error ... 
>
> }
> // Obtain and open the line.
> try {  
>
>     line = (TargetDataLine) AudioSystem.getLine(info);
>     line.open(format);
> } catch (LineUnavailableException ex) {
>     // Handle the error ... 
> }
>
> ```

You could instead invoke `Mixer's` `getLine` method, rather than `AudioSystem's`.

As shown in this example, once you've obtained a target
data line, you reserve it for your application's use by invoking the `SourceDataLine`
method `open`, exactly as was described in the case of a source data
line in
[Playing Back Audio](playing.html).
The single-parameter version of the `open` method causes the line's
buffer to have the default size. You can instead set the buffer size according
to your application's needs by invoking the two-parameter version:

```

void open(AudioFormat format, int bufferSize)

```

### Reading the Data from the TargetDataLine

Once the line is open, it is ready to start capturing data, but it isn't active yet. To actually commence the audio capture, use the `DataLine` method `start`. This begins delivering input audio data to the line's buffer for your application to read. Your application should invoke start only when it's ready to begin reading from the line; otherwise a lot of processing is wasted on filling the capture buffer, only to have it overflow (that is, discard data).

To start retrieving data from the buffer, invoke `TargetDataLine's` read method:

```

int read(byte[] b, int offset, int length)

```

This method attempts to read `length` bytes of data into the array `b`, starting at the byte position `offset` in the array. The method returns the number of bytes actually read.

As with `SourceDataLine's write` method, you can request more data than actually fits in the buffer, because the method blocks until the requested amount of data has been delivered, even if you request many buffers' worth of data.

To avoid having your application hang during recording, you can invoke the read method within a loop, until you've retrieved all the audio input, as in this example:

> ```
>
> // Assume that the TargetDataLine, line, has already
> // been obtained and opened.
> ByteArrayOutputStream out  = new ByteArrayOutputStream();
> int numBytesRead;
> byte[] data = new byte[line.getBufferSize() / 5];
>
> // Begin audio capture.
> line.start();
>
> // Here, stopped is a global boolean set by another thread.
> while (!stopped) {
>    // Read the next chunk of data from the TargetDataLine.
>    numBytesRead =  line.read(data, 0, data.length);
>    // Save this chunk of data.
>    out.write(data, 0, numBytesRead);
> }     
>
> ```

Notice that in this example, the size of the byte array into which the data is read is set to be one-fifth the size of the line's buffer. If you instead make it as big as the line's buffer and try to read the entire buffer, you need to be very exact in your timing, because data will be dumped if the mixer needs to deliver data to the line while you are reading from it. By using some fraction of the line's buffer size, as shown here, your application will be more successful in sharing access to the line's buffer with the mixer.

The `read` method of `TargetDataLine` takes three arguments: a byte array, an offset into the array, and the number of bytes of input data that you would like to read. In this example, the third argument is simply the length of your byte array. The `read` method returns the number of bytes that were actually read into your array.

Typically, you read data from the line in a loop, as
in this example. Within the `while` loop, each chunk of retrieved
data is processed in whatever way is appropriate for the application—here,
it's written to a `ByteArrayOutputStream`. Not shown here is the
use of a separate thread to set the boolean `stopped`, which terminates
the loop. This boolean's value might be set to `true` when the user
clicks a Stop button, and also when a listener receives a `CLOSE`
or `STOP` event from the line. The listener is necessary for `CLOSE`
events and recommended for `STOP` events. Otherwise, if the line
gets stopped somehow without stopped being set to `true`, the `while`
loop will capture zero bytes on each iteration, running fast and wasting CPU
cycles. A more thorough code example would show the loop being re-entered if
capture becomes active again.

As with a source data line, it's possible to drain or flush a target data line. For example, if you're recording the input to a file, you'll probably want to invoke the `drain` method when the user clicks a Stop button. The `drain` method will cause the mixer's remaining data to get delivered to the target data line's buffer. If you don't drain the data, the captured sound might seem to be truncated prematurely at the end.

There might be some cases where you instead want to flush the data. In any case, if you neither flush nor drain the data, it will be left in the mixer. This means that when capture recommences, there will be some leftover sound at the beginning of the new recording, which might be undesirable. It can be useful, then, to flush the target data line before restarting the capture.

### Monitoring the Line's Status

Because the `TargetDataLine` interface extends
`DataLine`, target data lines generate events in the same way source
data lines do. You can register an object to receive events whenever the target
data line opens, closes, starts, or stops. For more information, see
the previous discussion of
[Monitoring a Line's Status](playing.html#113711).

### Processing the Incoming Audio

Like some source data lines, some mixers' target data
lines have signal-processing controls, such as gain, pan, reverb, or sample-rate
controls. The input ports might have similar controls, especially gain controls.
In the next section, you'll learn how to determine whether a line has such controls, and
how to use them if it does.

[« Previous](playing.html)
•
[Trail](./TOC.html)
•
[Next »](controls.html)

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

**Previous page:** Playing Back Audio
  
**Next page:** Processing Audio with Controls




A browser with JavaScript enabled is required for this page to operate properly.