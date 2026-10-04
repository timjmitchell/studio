Source: https://jam.live/developers/

# JAM API

The JAM API will be available from MIDI Guitar 3.0.80 and on.

The [JAM API](https://jam.live/developers/) enable developers to create a wide range of applications and plugins: live visuals for gigs, musical art installations, MIDI machines, interactive guitar-learning apps and guitar-based games.

The APIs are free to use for both personal and commercial projects.

---

## External app or internal module?

There are two types of Apps/Plugins using the [JAM API](https://jam.live/developers/):

1. A [Lua module](https://jam.live/developers/lua/) plugin. This can be a sound module (synth or MIDI Machine) and lives inside [**MIDI Guitar 3**](https://jam.live/products/mg3) just like any other [module](https://jam.live/modules/modules/). The [Lua API](https://jam.live/developers/lua/) is suited for creating MIDI machines, such as sequencers, harmonizers and other audio/midi effects and can run full screen/window to "take over" the default **MIDI Guitar** user interface.
2. An external app, in any programming language. It communicates with **MIDI Guitar** over a standard web-socket. **MIDI Guitar** will send note data to your app which is suited to render musical scores or other kinds of guitar visualizations in the browser or native apps [in this format](https://jam.live/developers/websocket/).

It's possible to combine the two - for example a web-app with a Lua backend, which can render in the browser while also running as a sound module in **MIDI Guitar**.

---

## Showcase

[Jam Origin](https://jamorigin.com)'s **MIDI Guitar Mini**:
(not ready yet)

---

[LoFiLeif](https://www.youtube.com/@lofileif)'s **FretLab**:

---

[Vaultnaemsae](https://www.youtube.com/@Vaultnaemsae)'s **Scale Demon**:

---

## Tutorial

1. [Flappy Guitar](https://jam.live/developers/examples/flappyguitar/)

   Shows how to track a sequence of guitar notes, and simple animation of 2D sprites.
2. Tremolo picker MIDI Machine

   Shows how to transform each guitar note into serveral other ones.
3. MIDI Guitar UI and Modulations

   Shows how to draw a UI.
4. Guitar Shaders

   Shows how to create complex visuals animated by guitar notes.
5. [Whammy on the Web](https://jam.live/developers/examples/webwhammy/)

   Shows how to combine Lua, Html and Javascript to create an external web-app.
6. [MIDI Guitar Mini](https://jam.live/developers/examples/midiguitarmini/)

   Shows how to create a new skin for **MIDI Guitar**.

---
