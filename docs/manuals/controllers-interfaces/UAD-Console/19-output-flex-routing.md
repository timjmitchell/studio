Source: https://help.uaudio.com/hc/en-us/articles/25351234458260-Output-Flex-Routing
Updated: 2025-03-31T22:23:52Z

# Output Flex Routing

By default, Apollo’s input channels are routed to the monitor outputs only. Optionally, Apollo’s inputs can be routed to any available Apollo rack mount hardware output. A maximum of 16 channel output route assignments are available for each connected Apollo rack model.

**Important:** If an output is in use by Flex Routing, it is no longer available to be assigned as an output within the DAW. The Flex channel output(s) route overrides the DAW output channels assigned to the same hardware output(s).

Multiple input signals cannot be merged to the same output(s) with Flex Routing because this feature is not a mix bus. However, the cue mix buses can be used for this purpose.

**Notes**

* This feature is available with Apollo rack models only (Flex Routing is unavailable with Apollo desktop models).
* Flex Routing is unavailable at sample rates of 176.4 kHz and 192 kHz.

# Output Route Display

![](https://help.uaudio.com/hc/article_attachments/25351227596820)

*Output route display*

The Output Route display is located above each channel’s main input mix controls. The active output assignment is displayed here. Clicking the display opens the Flex Route browser.

# Flex Route Browser

The Flex Route Browser is where the hardware output assignment for the input channel can be changed.

![](https://help.uaudio.com/hc/article_attachments/25351227597204)

*The Flex Route Browser*

## To change the output route:

1. Click anywhere in the Output display to reveal the Flex Route browser.
2. Select an output (or output pair, for stereo linked channels) in the browser.
3. Click the X at the top of the browser to close.

**Tip:** If an output does not appear in the window, the output is already in use by another input channel, cue output, or ALT output.

![](https://help.uaudio.com/hc/article_attachments/25351227599380)

*Channel is routed to line output 7*

## Routes Available Count

The number of currently available mono and stereo channel output routes is displayed in yellow text at the bottom of the browser, and depends on the connected Apollo model. The number is decremented with each assignment.

**Apollo X rack models –** Up to 16 outputs can be assigned with Flex Routing for each connected Apollo X rack model.

**Other rack models –** Up to eight outputs can be assigned with Flex Routing for each connected Apollo rack model.

## Mirror to Monitor

When a channel is routed to an output other than the monitor outputs, the channel is simultaneously routed to the monitor outputs (mirrored) by default. Mirroring to the monitor outputs can be disabled so the channel is routed only to the output selected in the Output Route menu.

To toggle monitor mirroring, click the “Mirror to Monitor” button in the Flex Route browser. Monitor mirroring is active when the text is orange colored. Mirroring is off when the text is white.

## Multi-Unit Routing

When two or more Apollo rack models are connected in an Apollo Expanded multi-unit configuration, Flex Routing can be used within each unit. Up to eight output routes can be assigned for each connected Apollo rack model.

**Note:** Inputs can only be routed to outputs of the same unit.
