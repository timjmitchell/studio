Source: https://jam.live/developers/lua/

# JAM API, Lua

The JAM API will be available from MIDI Guitar 3.0.80 and on. This page is currently under construction!

[**MIDI Guitar 3**](https://jam.live/developers/products/mg3) has a powerful API, that offers direct access to **Jam Origin's** tracking and other technologies. The **MIDI Guitar 3** application itself, is made with (a superset and native version of) this API.

This [Lua API](https://jam.live/developers/lua/) aims to be low-level enough to enable developers to create a wide range of applications: live visuals for gigs, musical art installations, MIDI Machines, interactive guitar-learning apps and guitar-based games. Alternatively, there is a [WebSocket Hook](https://jam.live/developers/websocket/) for creating the visual side of apps in web browsers or external apps.

The API is in [Lua 5.1](https://lua.org/about.html) and the GLSL shading language, to keep it simple and fast.

The API is free to use for both personal and commercial projects.

---

## Example Apps

See the [tutorial](https://jam.live/developers/).

---

## App Structure

The app receives the tracked guitar notes as input, and will typically process/transform guitar notes and/or render out guitar notes graphically.

This is accomplished by two Lua functions: `Process` and `Render`:

```
function Initialize()
-- Starting up, so load and prepare things. Called only once at startup.
end

function Process(time, beat, notes)
-- Process guitar notes here. Called every ~3ms (~350fps)
end

function Render(time, beat, window, mouse, keys, notes)
-- Draw everything here. Called at every screen refresh (typically 60fps)
end
```

The app is thread safe, so don't worry about data race conditions. It is JIT compiled on systems that supports JIT compiling, reasonably efficient and supports hot-loading for quick development iterations.

---

## Graphics

The Graphics API wraps GPU hardware into just three functions:

```
  shader = Shader(glslCode) 
  texture = Texture(shader,  imageFile)
  Draw(texture, x, y, width, height)
```

1. Create a shader
2. Create textures with the shader and image files
3. Draw things with textures at a particular position, width and height

---

### Window

You are given a Window, which is a (x, y) coordinate system, where top left is (0, 0). For a square window the bottom right is (1,1).

---

### Shaders (basic)

In `Initialize`, create a basic shader from GLSL code:

```
  fireShader = Shader([[
```

```
                 vec4 pixel = texture(image, uv);
                 o = vec4(pixel.g, pixel.b, pixel.r, 1);
                 o *= pixel.a;
```

```
               ]]);
```

This is the default shader, which simply draws the pixels of a texture image.

---

### Textures

In `Initialize`, create a texture from a png image file and a shader:

```
  fireTexture = Texture(fireShader, "images/fire.png")
```

or load the texture directly from a png file on a server:

```
  fireTexture = Texture(fireShader, "https://myserver/images/fire.png")
```

This binds the image file `fire.png` to the `fireShader`.

---

### Sprites

In `Render`, draw some fire at coordinates x,y, with width and height both 0.1:

```
  Draw(fireTexture, x,y,0.1,0.1)
```

---

### Beams

There is a special `beamShader` built-in for drawing beams.

In `Initialize`, create a beam texture with beam thickness 0.01:

```
  beamTex = Texture(beamShader, 0.01)
```

In `Render`, draw a beam from (x,y) to (x+w, y+h):

```
  Draw(beamTex, x,y,w,h)
```

---

### Knobs

There is a special `knobShader` built-in for drawing knob parameters.

In `Initialize`, create a knob texture:

```
  param1Tex = Texture(knobShader, "FLAMES")
```

In `Render`, draw the knob at coordinates x,y, with width and height 0.1:

```
  Draw(param1Tex, x,y,0.1,0.1)
```

Grab the value of the knob position (in the range 0..1):

```
  local flames = Param(param1Tex)
```

Knobs can be cabled and modulated by MIDI Guitar's controllers or modulators.

Each knob must have its own texture.

---

### Switches

There is a special `switchShader` built-in for drawing switch parameters.

In `Initialize`, create a switch texture:

```
  param2Tex = Texture(switchShader, "")
```

In `Render`, draw the switch at coordinates x,y, with width and height 0.1:

```
  Draw(param2Tex, x,y,0.1,0.1)
```

Grab the value of the switch (0 or 1):

```
  local enabled = Param(param2Tex)
```

Switches can be cabled and modulated by MIDI Guitar's controllers or modulators.

Each switch must have its own texture.

---

### Selectors

There is a special `selectorShader` built-in for drawing selector parameters.

In `Initialize`, create a selector texture:

```
  param3Tex = Texture(selectorShader, "WATER, FIRE, AIR, EARTH")
```

In `Render`, draw the selector at coordinates x,y, with width and height 0.1:

```
  Draw(param3Tex, x,y,0.1,0.1)
```

Grab the value of the selector position (in the range 1..N):

```
  local element = Param(param3Tex)
```

Each selector must have its own texture.

---

### Painting Textures

The `Draw` function render textures to the screen at every frame, using GPUs and is very fast. But once in a while we want to draw, not on the screen, but on the textures. We call this *painting*. Unlike drawing, painting is CPU intensive and should only be once in a while to update mostly static textures, such as UI elements:

Paint a red rectangle on top of a fire texture:

```
  Color(1,0,0,1)
  Rect(fireTex, 0.1,0.1,0.8,0.8)
```

Paint a blue ellipse:

```
  Color(0,0,1,1)
  Ellipse(fireTex, 0.1,0.1,0.8,0.8)
```

Paint a green line with thickness 0.1:

```
  Color(0,1,0,1)
  Line(fireTex, 0.1,0.1,0.8,0.8, 0.1)
```

Paint a black text label:

```
  Color(0,0,0,1)
  Text(fireTex, 0.1,0.1,0.8,0.8, "Hello")
```

---

### Shaders (advanced)

For more advanced drawing, the GLSL shaders can operate directly on the texture data (images), guitar notes, mouse and UI parameters (knobs/switches/selectors).

Create an animating whirl:

```
  whirlShader = Shader([[
```

```
    // Cerulean Dreams, by Jaenam
    // License: Creative Commons (CC BY-NC-SA)

    #define N(p,t) sin(p*3.+sin(p*6.2)+t)*cos(p*1.2+cos(p*6.)+t)

    void main()
    {
        fc -= vec2(mouse.x-resolution.x/2,-mouse.y+resolution.y);
        float i=0, z=0, d=0;
        for (o*=i; ++i < 100;)
        {
            vec3 p = z * normalize(vec3(2.0*fc, 0) - resolution.xyy);
            float l = max(length(p.xy)-.15, .01);
            p.z -= beat;
            p.xy *= mat2(cos(p.z*1.1+vec4(0,11,33,0)));
            float r = max(length(sin(p.xz+.3*beat))-.2, .02);
            float d = 3;
            p += .8*N(p.yzx,.5*beat)/ d;
            z += d = .015 + max(d=length(p.xy) - 2.5, -d * .1)/3.;
            o += cos((.5-fract(length(p.xy))) + vec4(3,2,1,0) * .4)/d 
                 + vec4(3,2,1,0)*(.1/l +.4/r);
        }
        o = tanh(o * o /4e6);
    }
```

```
  ]]);

  whirlTexture = Texture(whirlShader, nil)
```

Behind the scenes, the full GLSL program looks like this:

```
#version 300 es // on iOS/iPadOS
#version 330    // on Mac/Windows

precision mediump float;
in vec2 uv;                // texture coordinates
uniform sampler2D image;   // the texture data
uniform vec2 resolution;   // window resolution in pixels
uniform vec2 mouse;        // mouse coordinates
uniform float beat;        // time in PPQ beat units
uniform vec4 param;        // parameters 1..4
vec2 fc = gl_FragCoord.xy; // input pixel coordinate
out vec4 o = vec4(0.f);    // output pixel (color of the pixel)

// your GLSL code is inserted here
```

---

## Controllers

The app gets inputs from the following devices:

### Guitar notes

The notes played on the guitar (processed by other modules).

### Parameters

When drawing Knobs, Switches and Selectors their values can be read by `Param(texture)`. Knobs and Switches can be wired and modulated from other modules or controllers in **MIDI Guitar 3**.

### Mouse/Touch

x,y and click

Check if the user clicked on the last drawn sprite:

```
if Clicked(mouse) then
  -- do something
end
```

### Keyboard

Typing...

### Play/Pause/Time

Time is in PPQ beat units.
When running in a plugin this stems from the DAW.

---

## Sound

The app can be a **MIDI Machine** or **Sampler** by implementing a `Process` function.

```
function Process(time, beat, notes)
-- Process notes/MIDI here. 
-- Called every ~3ms (~350fps) so not for intensive work!
end
```

---

### MIDI Machines

The `Process` function can process/transform the guitar notes. If you return those transformed notes, this becomes a **MIDI Machine**.

```
function Process(time, beat, notes)

   -- time is the time in number of frames
   -- beat is the time given in PPQ beat units.

   -- notes is an array of notes, where each note has six properties:
      note.id      -- a unique note ID to identify this note
      note.age     -- the current age/duration of the note
      note.string  -- the guitar string of this note [0..6] or -1 if no string
      note.pitch   -- the current MIDI pitch of the note
      note.strike  -- the strike and MIDI velocity of the note 
      note.pressure -- the current MIDI pressure or aftertouch of the note
      note.brightness -- the current MIDI brightness or CC74 of the note

   -- create an array of output notes
   transformedNotes = {}

   --- create output notes based on the input notes

   --- return output notes
   return transformedNotes

end
```

---

### Sampler

Not working yet.

The Sampler API consist of two functions:

```
sample = Sample(pathToAudioFile) 
Play(sample, age, pitch, amplitude)
```

Create a sample from a wav file

```
amenBreakSample = Sample("samples/amen-break.wav")
```

Play a sample

```
function Process(time, beat, notes)

   if something then
      Play(amenBreakSample, age, pitch, amplitude)
      -- age should be 1 at onset and increased by 1 for every frame, or can be scrambled for granular synthesis.
      -- pitch is the pitch/bend envelope, in MIDI pitch units
      -- amplitude is the amplitude envelope in the range [0...1]
   end

end
```

```

```

---

### Effects

```

```

To be continued...

---

## Safety

Apps are meant to be distributed and are (to the best of our knowledge) safe to run. They are sandboxed, cannot execute system calls or access any files outside of the installation folder.
