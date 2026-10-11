Source: https://jam.live/developers/examples/webwhammy/

# Web Whammy

This example shows:

* How to whammy/pitch shift the guitar notes.
* How to pass messages among [**MIDI Guitar 3**](https://jam.live/developers/examples/products/MG3.md) and the web browser. This allows you to code apps using any web framework and display/record notes in the browser.

---

### Run this example

1. Copy the Lua code below to a file named `MyWhammy.lua`.
2. Copy the Html code below to a file named `MyWhammy.html`.
3. Drag the Lua file into a chain in **MIDI Guitar 3**.

### Lua audio/MIDI

```
local mute = false
local whammy = 0
local outputNotes = {}

function Initialize()
end  

function Message(key, value)
    if key == "param1" then
        mute = value < 50
    elseif key == "param2" then
        whammy = 24 * value/100 - 12
    end
end

function Process(time, beat, inputNotes)
    if mute then
        return nil
    end

    outputNotes = inputNotes
    for k, v in pairs(outputNotes) do
        outputNotes[k].pitch = outputNotes[k].pitch + whammy
    end

    return outputNotes
end
```

### HTML/JavaScript visuals

```
<!doctype html>
<html>
    <head>
        <title>JAM API, JavaScript example app</title>
        <script>
            let client;
            append = function (text) {
                let html = text.replace(/\n/g, "<br />");
                document.getElementById("midi_guitar_events").innerHTML = html;
            };
            window.onload = function () {
                client = new WebSocket("ws://127.0.0.1:8080");
                client.onmessage = function (event) {
                    append(event.data);
                };
                client.onopen = function () {
                    append("Connected to WebSocket.");
                };
                client.onclose = function () {
                    append("Connection closed. Refresh to reload.");
                };
                client.onerror = function () {
                    append("WebSocket error.");
                };
            };

            function sendMessage(event) {
                console.log(event);
                client.send(document.getElementById("message").value);
            }
            function changeParameter(parameter, value) {
                client.send("param"+parameter+"="+value);
            }
        </script>
        <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@picocss/pico@2/css/pico.min.css" />
    </head>

    <body>
        <main class="container">
            <h1>MIDI Guitar 3 Web App Example</h1>
            <h3>Say something to MIDI Guitar 3</h3>
            <div class="grid">
              <input value="Hello from the web!" type="text" id="message" />
              <input type="button" value="Say something to MIDI Guitar" onclick="sendMessage(event)"/>
            </div>

            <h3>Control MIDI Guitar 3</h3>
            <div class="grid">
              <div><p>Your App can control <b>MIDI Guitar 3</b>'s sound processing.</p></div>
              <div>
              <div>
              <label>Mute</label>
              <input id="param1" type="range" oninput="changeParameter(1, this.value)"/>
              </div>
              <div>
              <label>Whammy</label>
              <input id="param2" type="range" oninput="changeParameter(2, this.value)"/>
              </div>
              <div>
              <label>CC3</label>
              <input id="param3" type="range" oninput="changeParameter(3, this.value)"/>
              </div>
              <div>
              <label>CC4</label>
              <input id="param4" type="range" oninput="changeParameter(4, this.value)"/>
              </div>
              </div>
            </div>

            <h3>Notes streaming from MIDI Guitar 3</h3>
            <div class="grid">
            <div>

            <p>Your App recieves the note data in the format:
            <code>time, beat, beat-fraction \n</code>
            <code>number-of-input-notes \n</code> and for every input note:
            <code>note-id, age, string, pitch, bend, pressure, brightness \n</code>
            <code>number-of-output-notes \n</code> and for every output note:
            <code>note-id, age, string, pitch, bend, pressure, brightness \n</code>
            </p>

            <p><small>where <code>time</code> and <code>age</code> are in units of frames: 128/44100*1000 or 128/48000*1000 milliseconds each. <code>beat</code> is the PPQ (pulse pr quater) value, used in DAWs, depending on the BPM-tempo. Notes are streamed at >30fps (every tenth frame).</small></p>
            </div>
            <div><code><ul id="midi_guitar_events"></ul></code></div>
            </div>
        </main>
    </body>
</html>
```
