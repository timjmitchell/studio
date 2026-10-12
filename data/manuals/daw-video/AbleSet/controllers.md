Source: https://ableset.com/docs/controllers

# Third-Party Controllers

AbleSet offers support for third-party controllers like Elgato's Stream Deck and
Oaktone's Oakboard Floor Vista. Learn more about how to integrate them with
AbleSet.

## Stream Deck

AbleSet Standard and Pro offers support for Elgato's
[Stream Deck](https://www.elgato.com/eu/en/p/stream-deck-xl) using the free
[Companion](https://bitfocus.io/companion) app by BitFocus.

This allows you to create a control surface that's completely customized to your
needs. Buttons can display a variety of information about your set.

Here's a tutorial on how to set it up:

[Open YouTube Video](https://youtu.be/gi9Jq8VJ_hs?t=0)

## Oakboard Floor Vista

AbleSet officially supports Oaktone's Oakboard Floor Vista, a MIDI controller
with an integrated display that allows you to see and control your setlist on
stage.

[](/images/docs/21-controllers/oakboard-demo.webm)

By default, when you connect your Floor Vista to your computer via USB, AbleSet
will automatically detect it, set up default [MIDI mappings](https://ableset.com/docs/midi-mapping),
and show the current setlist on its display. You can change the MIDI mappings in
AbleSet's settings if you like.

### Oaktone and iConnectivity

You can also use the Floor Vista to control AbleSet in a redundant setup. For
AbleSet to recognize the controller, the names of its MIDI input and output
ports need to include "Oakboard". You can rename the MIDI ports of your
PlayAUDIO12, PlayAUDIO1U, mioXM, or mioXL by opening Auracle, clicking
"MIDI Mapping", and then clicking the pencil icon next to the MIDI port your
Floor Vista is connected to.

![MIDI Routing in Auracle](https://ableset.com/images/docs/21-controllers/auracle-midi-routing.png)

In some cases, macOS might not recognize the changed name right away. To fix
this, unplug your MIDI interface, remove it from Audio MIDI Setup, and then plug
it back in.
