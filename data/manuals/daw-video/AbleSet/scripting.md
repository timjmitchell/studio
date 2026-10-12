Source: https://ableset.com/docs/scripting

# Scripting in AbleSet

AbleSet offers scripting in [Canvases](https://ableset.com/docs/canvas), in
[MIDI Mapping](https://ableset.com/docs/midi-mapping), and in the
[Project Script](https://ableset.com/docs/scripting#the-project-script).

These scripts are written in JavaScript and support all features of ES2023. If
you're already familiar with writing JavaScript, you can skip the next section
and go straight to the list of [available functions](https://ableset.com/docs/scripting#available-functions).

The script editor provides autocompletion for available functions and variables
and automatically highlights incorrect code.

## JavaScript Basics

### Your First Script

The following script prints "Hello World!" to the console. The `log` function is
a handy tool to debug your scripts by showing values while your script runs.

```
log("Hello World!");
```

This is a function call. Each function call consists of the function name and
parentheses containing arguments. These arguments depend on which function you
call. In this case, we're passing the text "Hello World!" to the `log` function.

You can end each function call with a semicolon (recommended) or write one
function call per line without semicolons.

### Comments

If you'd like to add comments to your code, you can do so like this:

```
// This is a single-line comment

/*
  This is a multi-line comment
*/
```

### Variables

To store and reuse values in your scripts, you can define variables. There are two
variable declaration keywords: `const` and `let`. Use `const` when the value won't
change (recommended), and `let` when you need to modify it later:

```
// This variable can be re-assigned
let name = "Léo";
name = "The other Léo";

// This one can't be re-assigned - use this when possible
const answer = 42;
answer = 41; // <- this would result in an error

// Variables can't be defined twice
const app = "AbleSet 2";
const app = "AbleSet 3"; // <- this would fail
```

Variables only exist while your script runs and will be cleared afterwards.
If you need to store values between script runs, use the `setLocal` and `local`
functions described [here](https://ableset.com/docs/scripting#local-variables).

### Primitive Data Types

JavaScript supports a range of primitive data types: `number`, `string`,
`boolean`, `undefined`, and `null`:

```
// A number:
const num = 1234.56;

// Strings can use double or single quotes:
const hello = "Hello";
const world = "World";

// Booleans are either true or false:
const yes = true;
const no = false;
```

The values `undefined` and `null` are special values representing no data.

### Template Strings

Template strings are a special string type that use backticks (`` ` ``) as quotes
and allow you to include variables:

```
const name = "Léo";
const message = `Hello, ${name}!`;
```

### Operators

Operators allow you to manipulate and check data and variables:

```
// You can use +, -, *, /, and % (modulo) on numbers
const result = (3 + 5) / 2; // <- result will be 4

// To modify number variables, you can use ++, --, +=, -=, *=, and /=
let num = 3;
num++; // num is increased by 1
num--; // num is decreased by 1
num += 3; // 3 is added to num, same as num = num + 3
num -= 2; // 2 is subtracted from num, same as num = num - 2

// Use + to concatenate a string with other variables
const message = "The result is " + result;
```

To compare two or more values with each other, you can use these operators:

```
const name = "Léo";
const answer = 42;

// Use === (equal) and !== (not equal) to compare two values
const equal = answer === 42; // <- will be true
const unequal = name !== "Tom"; // <- will also be true

// Use && (AND), || (OR), and ! (NOT) to combine comparisons
const and = equal && name === "Léo"; // <- will be true
const or = equal || name === "Tom"; // <- will also be true
const not = !equal; // <- will be false
```

### Conditional Statements

Conditional (if) statements allow you to decide which code to run based on given
conditions:

```
const song = "Roads";
const artist = "Small Strides";

if (song === "Follow Night") {
  log("The song is Follow Night");
} else if (artist === "Small Strides") {
  // This code will run since the song condition wasn't satisfied,
  // but this one (artist) was
  log("The song is not Follow Night, but the artist is Small Strides");
} else {
  log("Neither song nor artist match");
}
```

### Ternary Operator

The ternary operator allows you to get a value based on a condition:

```
const number = 9001;

// This message variable will be "It's over 9000!".
const message = number > 9000 ? "It's over 9000!" : "Value is too small";

// Ternary operators can be used anywhere, e.g. in arguments:
const answer = 42;
log(answer === 42 ? "Correct" : "Wrong");
```

### Loops

To run a block of code multiple times, you can use loops:

```
// This runs the loop 10 times, starting with 1
// and increasing the variable i by 1 each time
for (let i = 1; i <= 10; i++) {
  log(`Hello, number ${i}`); // Logs "Hello, number 1", "Hello, number 2", etc.
}
```

Note that we have to use `let i = 1` instead of `const i = 1` here because the
variable needs to be modified on each run.

Alternatively, you can use `while` and `do...while` loops, but we'll skip them
here for brevity.

### Arrays

Arrays allow you to store a list of values in a variable. They can contain all
primitive data types and other arrays.

```
// This is how you define an array:
const songs = ["Roads", "Follow Night", "Why We Are"];

// Accessing array items can be done like this. Note that the index starts at 0:
const firstSong = songs[0]; // <- "Roads"
const lastSong = songs[2]; // <- "Why We Are"

// You can also access the length of the array:
const songCount = songs.length; // <- 3
```

### Further Information

To learn more about JavaScript, you might find the [Mozilla Docs](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Scripting) helpful.

## The Project Script

This script is run every time you open AbleSet or your Ableton Live project. It
allows you to react to changes in OSC values and send information to other
devices and applications via MIDI and OSC.

You can find this script by opening the settings page and clicking
"Project Script" in the "MIDI Mapping, OSC & Scripting" section.

## Available Functions

When writing scripts in AbleSet, you can access all objects and functions available in
JavaScript, including [Math](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math), [Date](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date), and
[JSON](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON). You can find an overview [here](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects#standard_objects_by_category).

Additionally, AbleSet offers a number of built-in functions to interact with the
app and other devices.

Here's a list of them. Arguments marked with a `?` are optional, a `...` before
arguments means you can add as many arguments of this type as you like.

### Basics

* `log(...values)` logs all values to the console
* `await sleep(time)` waits for the given number of milliseconds
* `now()` returns the current timestamp in milliseconds
  + This uses the time of the computer running AbleSet, and when used in a
    template, it updates every second

### Local Variables

To store values between script runs and access them from other scripts and
components, you can use these functions:

* `setLocal(key, value, persist?)` stores the given value under the given key
  + If `persist` is true, the value is stored in your browser's storage and
    persists between page refreshes
* `local(key, fallback?)` returns the value at the given key
  + If no value is stored at `key` yet, `fallback` is returned
* `resetLocal(key?)` deletes the variable stored at `key`
  + If no `key` is defined, all local variables are deleted

Example:

```
// Gets a counter and increases it by 1
const counter = local("counter", 0);
setLocal("counter", counter + 1);
```

### Shared Variables

Shared variables are available across all scripts on all devices and work
similarly to local variables:

* `setShared(key, value)` stores the given value under the given key
* `shared(key, fallback?)` returns the value at the given key
  + If no value is stored at `key` yet, `fallback` is returned
* `resetShared(key)` deletes the variable stored at `key`

Example:

```
// Gets a counter and increases it by 1
const counter = shared("counter", 0);
setShared("counter", counter + 1);
```

### OSC

* `osc(key, index?)` returns the OSC value for the given key
  + By default, it returns the first argument of the OSC value, but you can
    specify the index using the `index` argument
  + To get an array all arguments, set `index` to "all"
* `sendOsc(command, ...args)` sends an OSC command with the given arguments
  + This can either be an internal (e.g. "/global/play") or an external (e.g.
    "127.0.0.1:3000/test") command
* `int(number)` treats a given number as an integer instead of a float when
  sending it via OSC
* `await waitForOscChange(key)` waits until the value for the given key changes
* `await waitForOscValue(key, value)` waits for the given key to have the given value
* `onOscChange(key, callback, sendFirst)` calls the callback function every time
  the value for the given key changes

Example:

```
// Jumps to the next song if AbleSet isn't playing, waits
// for the name to change, and logs the value of the new song
if (!osc("/global/isPlaying")) {
  sendOsc("/setlist/jumpBySongs", 1);
  await waitForOscChange("/setlist/activeSongName");
  log("New song:", osc("/setlist/activeSongName"));
}
```

A list of all available OSC values and commands is available [here](https://ableset.com/docs/osc).

### MIDI

These functions are aliases for the `/midi/send` [OSC commands](https://ableset.com/docs/osc#sending-midi).
You can use these commands to send notes:

* `sendMidiNote(output, channel, note, velocity?, duration?)` sends a MIDI note on followed by a note off to the given output
  + Velocity is optional, the default value is 127
  + Duration is specified in milliseconds, the default value is 100
* `sendMidiNoteOn(output, channel, note, velocity?)` sends a note on with the given velocity to the specified output
  + Velocity is optional, the default value is 127
* `sendMidiNoteOff(output, channel, note, velocity?)` sends a note off with the given velocity to the specified output
  + Velocity is optional, the default value is 0

The note can either be a number between 0 and 127, or a string like `E#0` or `Cb-1`.

To send CC and PC, you can use these commands:

* `sendMidiCc(output, channel, controller, value)` sends a CC to the given output
  + Controller and value must both be numbers between 0 and 127
* `sendMidiPc(output, channel, program)` sends a PC to the given output
  + Program must be between 0 and 127

You can also send raw MIDI data to an output, for example for SysEx:

* `sendMidiRaw(output, ...data)`
  + Data can either be a list of numbers, or a string like "F0 03 A3 F7"

### Browser Control

These are only available in Canvas scripts.

* `navigate(path)` navigates the browser to the given path
  + The path can either be relative (e.g. "/lyrics") or absolute (e.g. "<https://ableset.app>")
* `pathname` contains the current pathname (e.g. "/canvas/main")

### Utility Functions

* `formatDuration(seconds)` formats a given number of seconds into a more readable string
  + For example, `formatDuration(135)` returns "02:15"
* `makeAscii(text)` converts a given string into an array of MIDI-friendly ASCII
  bytes, converting incompatible characters to compatible ones when possible
  + This is useful for sending text via SysEx

### Timing

These are only available in project scripts.

* `debounce(function, timeMs)` returns a debounced version of the given function
  that only runs it after the given timeout, with no further calls in between
  + Each call within that window resets the timer
* `setTimeout(function, timeMs)` runs the given function once after the given
  timeout. Returns an ID for `clearTimeout`
* `clearTimeout(id)` cancels the given timeout
* `setInterval(function, timeMs)` runs the given function repeatedly at the given
  interval until stopped. Returns an ID for `clearInterval`
* `clearInterval(id)` stops the given interval
