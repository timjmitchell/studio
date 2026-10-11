## ES-8 Version 2 Su lementar Manual pp y 

This manual explains the functions that have been added or improved in ES-8 Version 2. Read it in conjunction with the owner’s manual. 

## ~~“Separate” Added as an Efect Loop Connection Type~~ 

Now you can assign separate effect loops to the two inputs of OUT (L, R) or effect loop 8. This is called “separate” (SEPARATE). 

- In Version 2, the OUT indication has changed from “ O” to “ L” “ R.” 

L   _R 7-6-5-4-3-8-2- 

## ~~Loop On/Of Screen (Play Screen) Indications Changed~~ 

In the play screen, the Loop On/Off screen indication has been changed as follows, making it easier to check the on/off status of the effect loops. The on/off status of all effect loops is shown in a single screen. 

Patch Name 8765*321 V 

**1. Use the [** K **] [** J **] buttons to move the cursor to the branch point, and then press the [+] button.** 

The path between the branch point to OUT (L, R) or effect loop 8 is connected in parallel. 

L        _R 7-6-5-4-3-8-2- 

L-7-6-5-4 3-8-2-R--------_ 

- If an effect loop is off, the screen indicates “ *.” 

## ~~“Patch MIDI” Added as an Assign Target~~ 

As a Target for Assign, we have added Cate: Pat.M and Target: PMIDI1–8. By using the Assign settings to control the above target, you can not only switch patches but also transmit Patch MIDI settings at the desired timing. 

   - If you press the [ENTER] button while the Patch MIDI screen is displayed, the MIDI messages specified for Patch MIDI 1–8 are transmitted together. 

   - If you don’t want these messages to be transmitted when you switch patches, set Patch MIDI 1–8: Transmit to “MANUAL.” 

**2. To cancel the separate connection, press the [–] button at the branch point.** 

L-7-6-5-4 3-8-2-R--------_ L 7-6-5-4-3-8-2-        _R 

## ~~Link Function Added~~ 

Now you can use two ES-8 units in synchronization. 

Operations on one ES-8 unit (such as switching the play screen, switching patches, manual mode operations, Patch MIDI output, or CTL/EXP output) have the same result on the second ES-8 unit. 

- Do not edit the parameters while units are linked. The Link function is disabled if the parameter edit screen is shown. 

- If you use the Link function, the MIDI Setting (system setting) “MIDI Out Mode” and “Sync” settings are disabled. 

**1. Before you continue, set all parameters of the two ES-8 units to the same settings.** It is convenient to use bulk dump or ES-8 Editor to do this. 

**2. Use MIDI cables to connect the first unit’s MIDI IN connector to the second unit’s MIDI OUT connector, and the first unit’s MIDI OUT connector to the second unit’s MIDI IN connector.** 

## Example setting 

**In Assign1, use a footswitch connected to CTL1 IN to transmit the MIDI PC messages that are specified by Patch MIDI1** 

**==> picture [98 x 243] intentionally omitted <==**

**----- Start of picture text -----**<br>
Parameter Value<br>Patch MIDI 1 settings<br>Ch 1<br>LSB OFF<br>MSB OFF<br>PC 5 (as desired)<br>Ctl1 CC# OFF<br>Val 0<br>Ctl2 CC# OFF<br>Val 0<br>Transmit MANUAL<br>Assign1 settings<br>Sw ON<br>Src CTL1<br>Mod MOM<br>Cate Pat.M<br>Num PMIDI1<br>Min OFF<br>Max ON<br>Act L 0<br>Act H 127<br>**----- End of picture text -----**<br>


**3. On the first ES-8 unit, set Play Option: Link to “MASTER.”** 

**4. On the second ES-8 unit, set Play Option: Link to “SLAVE.”** 

**1** 

Copyright © 2017 ROLAND CORPORATION 

01 

- ES 8 Version 2 Supplementary Manual 

## ~~Added Patch/System Parameters~~ 

In conjunction with the functions added in Version 2, we added the following patch parameters that can be specified for each patch, and additional system setting parameters. 

## ~~Patch Parameters~~ 

## Patch 

**Parameter Value/Explanation Output** The gain settings for mixers 1 and 2 settings are automatically set to -6 dB for “parallel connection,” and to 0 dB for “Carry Over.” By using this parameter and Mixer Gain1 and 2, you can specify the gain manually. Mixers 1 and 2 are used in that order starting from the effect loop at the right of the Loop Structure screen. AUTO The gain of mixers 1 and 2 is set automatically by the system. **Mixer Mode** MANUAL The gain of mixers 1 and 2 is set manually. Mixers 1 and 2 are shown as follows in the Loop Structure screen. Mixer 2 Mixer 1 8-7-6        _5 4 3 2-1 - ~~-~~ **Mixer Gain1** Specifies the gain when Mixer Mode is set to “MANUAL.” **Mixer Gain2** -6 dB, 0 dB **Patch MIDI 1–8** In Version 2, the contents specified in Patch MIDI can be transmitted using Assign; however, you can specify that the Patch MIDI settings are not automatically transmitted when you switch patches. **Transmit** For details, refer to “ ’Patch MIDI’ Added as an Assign Target” (p. 1). AUTO Patch MIDI settings are transmitted when you switch patches. MANUAL Patch MIDI settings are not transmitted when you switch patches. For each patch, specifies whether MIDI Clock messages are transmitted. This is convenient if you don’t want to use MIDI synchronization for certain patches. **MIDI Clock Out** SYSTEM The settings in MIDI Setting determine whether MIDI Clock messages are transmitted. OFF MIDI Clock messages are not transmitted regardless of the settings in MIDI Setting. 

## ~~System Parameters~~ 

**==> picture [251 x 436] intentionally omitted <==**

**----- Start of picture text -----**<br>
Parameter Value/Explanation<br>Category: Play Option<br>This lets you change the correspondence between the<br>number switches and the effect loops in manual mode.<br>Number 1–8 (MAN) AUTO Pressing a number switch [1]–[8] turns on/off the<br>effect loop of the same number.<br>Pressing a number switch turns on/off the effect<br>1–8, V<br>loop of the specified number or a volume loop.<br>Specifies how Master BPM is switched when you switch<br>patches.<br>Tempo Hold OFF When you switch patches, the Master BPM becomes the value specified by each patch.<br>ON When you switch patches, the Master BPM maintains<br>the value of the patch prior to switching patches.<br>This setting specifies how the Link function operates.<br>For details, refer to “Link Function Added” (p. 1)<br>OFF The Link function is not used.<br>MASTER The Link function operates as the master unit. The<br>Master BPM is also used by the master unit.<br>Link SLAVE The Link function operates as the slave unit. The Master BPM reflects the setting of the master unit.<br>If this is set to SLAVE, the patch name screen of play mode<br>shows a display like the following.<br>Patch Name<br>         [Ì=120]     _<br>Category: Preference<br>These specify the settings that determine the operations of<br>the [MEMORY/MANUAL] switch, [MUTE] switch, [BANK I]<br>[BANK H] switches, number switches [1]–[8], and a footswitch<br>connected to the CTL IN jack.<br>MEMORY MANUAL PAT Each switch operates according to the settings of<br>each patch.<br>MUTE<br>BANK DOWN SYS Each switch operates according to the system<br>BANK UP settings.<br>NUMBER 1–8 If this is set to SYS, the settings for each switch that you make<br>in the CTL/EXP screen are common to the entire unit. In this<br>CTL IN 1–4<br>case, the indication (SYS) is shown below the name of the<br>EXP IN 1–2 switch.<br> MEMORY MANUAL<br> (SYS)   [ENTER]<br>**----- End of picture text -----**<br>


## ~~Other Added Functions~~ 

- 5 ES-8 Editor is now supported. 

- 5 Bypass/mute are no longer cleared when you re-select the currently selected patch. 

- 5 When bypassed, the display now indicates “ byP.” 

- 5 Even when the lock function is on, you can now use the [K] [J] buttons to scroll the screen. 

- 5 The value that is first transmitted when the Assign setting Mode = TGL is now the value that is specified as MAX. 

**2** 

