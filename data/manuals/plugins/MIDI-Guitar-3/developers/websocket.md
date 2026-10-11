Source: https://jam.live/developers/websocket/

# JAM API, WebSocket

This API is not yet mature and is expected to change throughout the beta testing period.

---

Notes are sent from [MIDI Guitar](https://jam.live/products/MG3/)'s [Lua](https://jam.live/developers/lua/) and [Html](https://jam.live/developers/websocket/) modules on a WebSocket at localhost, port 8080.

---

## Note streaming format

```
time, beat, beat-fraction \n
```

```
number-of-played-notes \n
```

*for each played note:*

```
   note-id, age, string, pitch, bend, pressure, brightness \n
```

```
number-of-lua-processed-notes \n
```

*for each lua processed note:*

```
   note-id, age, string, pitch, bend, pressure, brightness \n
```
