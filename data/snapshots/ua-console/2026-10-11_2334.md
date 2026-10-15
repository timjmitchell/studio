# UAD Console snapshot: 2026-10-11T23:34:46

**Label:** Recall rerun C: after reopen without saving

Read-only from the UA Mixer Engine by `scripts/ua_snapshot.py`. Data: `data/snapshots/ua-console/2026-10-11_2334.toml`.
Terms: *main mix* = MONITOR; a *monitor mix* = a UA cue (see docs/studio/model.md §4.7).

**Channels:** 13 visible strips · driver (I/O Matrix) 44 in / 42 out · I/O preset: Default · Console session: ../../../Library/Preferences/Universal Audio/extAppSyncSession (see docs/studio/inventory-first-pass.md §3.1)

## Apollo x8

- speaker correction 'Mackie left mix - 2023-06-14' (off)
- headphone correction 'Sony MDR-7506 Wired Average' (off)

**Inputs**

| Input (Console label) | Port · DAW sees | Type | Fader | Preamp | Unison | Inserts | Sends |
|---|---|---|---|---|---|---|---|
| A1 Mic Dyn | `in-1` · A MIC/LINE/HIZ 1 | Mic | -0.74 dB | gain 39, low cut | Manley VOXBOX (on) | UA 1176 Rev A (off) | AUX 1 -23.7, CUE 2 -0.3, CUE 3 -18.2 |
| A2 Mic | `in-2` · A MIC/LINE/HIZ 2 | Mic | -1.19 dB (muted) | gain 17, low cut |  |  | CUE 2 -52.1 |
| A3 Mic Cond. | `in-3` · A MIC/LINE 3 | Mic | -0.09 dB | gain 12, low cut | Neve Preamp (on) | UA 1176 Rev A (off) | AUX 1 -24.1 |
| A4 Mic | `in-4` · A MIC/LINE 4 | Mic | -4.93 dB (muted) | gain 18 | API Vision Channel Strip (off) |  |  |
| A5 OX 1 | `in-5` · A LINE 5 | Line | -6 dB (muted) |  |  |  | CUE 2 0 |
| A6 OX2 | `in-6` · A LINE 6 | Line | -19.27 dB (muted) |  |  |  | CUE 2 -9.7 |
| A7 | `in-7` · A LINE 7 | Line | -13.43 dB |  |  |  |  |
| A8 | `in-8` · A LINE 8 | Line | -14.17 dB |  |  |  |  |
| VIRTUAL 1 | `virtual-1` · A VIRTUAL 1 | Virtual | -17.66 dB |  |  |  |  |
| VIRTUAL 3 | `virtual-3` · A VIRTUAL 3 | Virtual | -14.05 dB |  |  |  | CUE 2 0 |

Hidden in Console (active, not shown): ADAT 1, ADAT 2, ADAT 3, ADAT 4, ADAT 5, ADAT 6, ADAT 7, ADAT 8, S/PDIF L

**Outputs (main mix and monitor mixes)**

| Output | Type | Source | Mirror to | Mono | Level | State |
|---|---|---|---|---|---|---|
| CUE 1 | Cue | main mix |  |  |  | active |
| CUE 2 | Cue | own monitor mix | Line 7-8 |  |  | active |
| CUE 3 | Cue | own monitor mix |  |  |  | active |
| CUE 4 | Cue | main mix |  |  |  | inactive |
| MONITOR | Monitor | main mix |  |  | -43 dB | inactive |
| HP 1 | Headphone | cue1 |  |  |  | inactive |
| HP 2 | Headphone | cue2 |  |  |  | inactive |

**Plugin settings**

- **A1 Mic Dyn** · Manley VOXBOX (on): Source Select Mic, Low Cut 80 Hz, Phase 0, Input 6.4, Gain 50 dB, SC Link Link, Comp Byp In, Comp Thresh 6.2, Comp Attack Fast, Comp Rel Medium, EQ Byp Byp, Lo Peak 0.0 dB, Lo Peak Freq 70 Hz, Mid Dip -7.4 dB, Mid Dip Freq 500 Hz, Hi Peak 1.5 dB, Hi Peak Freq 12 kHz, De Ess Byp Byp, De Ess Sel 6K, De Ess Thr 6.5, Meter GR, Transformer Byp Byp, Output -0.3 dB, Power On
- **A1 Mic Dyn** · UA 1176 Rev A (off): Input -32.68 dB, Output -20.08 dB, Attack 7.00, Release 4.01, Ratio 4:1, Meter GR, SC Filter Off, Mix 100 %, Headroom 16 dB, Power On
- **A3 Mic Cond.** · Neve Preamp (on): Input Select Mic, Gain -50 dB, HP Filt 80 Hz, Phase Normal, Output -0.5 dB, Power On
- **A3 Mic Cond.** · UA 1176 Rev A (off): Input -35.04 dB, Output -14.80 dB, Attack 4.36, Release 4.22, Ratio 4:1, Meter GR, SC Filter Off, Mix 100 %, Headroom 16 dB, Power On
- **A4 Mic** · API Vision Channel Strip (off): Input Select Mic, Mic Gain 40.5 dB, Line Gain 0.0 dB, Pad Off, Phase Normal, Cut Filter Off, 215 LP Filter 40.8 k, 215 HP Filter 21.3 Hz, 215 Dyn SC Off, 215 On 50 Hz, 235 Thresh -12.7 dB, 235 Depth 46.7 dB, 235 Attack Normal, 235 Release 0.72 s, 235 R/H Release, 235 G/E Gate, 235 On Off, 225 Thresh -4.5 dB, 225 Ratio 3.1, 225 Attack Medium, 225 Release 0.35 s, 225 Knee Soft, 225 Type New (FF), 225 On On, 550 HF Freq 15 kHz, 550 HF Gain 4 dB, 550 HF Filter Shelf, 550 HMF Freq 5 kHz, 550 HMF Gain 2 dB, 550 LMF Freq 700 Hz, 550 LMF Gain 0 dB, 550 LF Freq 100 Hz, 550 LF Gain 0 dB, 550 LF Filter Shelf, 560 16kHz 0.3 dB, 560 8kHz -0.9 dB, 560 4kHz 1.8 dB, 560 2kHz 0.0 dB, 560 1kHz 1.8 dB, 560 500Hz -6.8 dB, 560 250Hz 0.0 dB, 560 125Hz 0.0 dB, 560 63Hz 4.6 dB, 560 31Hz 4.9 dB, EQ Predyn Off, EQ Dyn SC Off, EQ Type 550L, EQ On On, Level -0.0 dB, SC Link On, Power Off

## Apollo Twin X

- remote monitor controller

**Inputs**

| Input (Console label) | Port · DAW sees | Type | Fader | Preamp | Unison | Inserts | Sends |
|---|---|---|---|---|---|---|---|
| B1 PdlBrd | `in-1` · B MIC/LINE/HIZ 1 | Line | -6.58 dB | gain 25, Hi-Z |  |  | AUX 1 -19.6, CUE 3 -41.6 |
| B2 Guit Dir | `in-2` · B MIC/LINE 2 | Mic | -0.49 dB (muted) | gain 13 | Manley VOXBOX (off) |  | AUX 1 -32.4, LINE 3-4 -4.4 |
| VIRTUAL 1 | `virtual-1` · B VIRTUAL 1 | Virtual | -16.87 dB |  |  |  | LINE 3-4 -23 |

Hidden in Console (active, not shown): S/PDIF L

**Outputs (main mix and monitor mixes)**

| Output | Type | Source | Mirror to | Mono | Level | State |
|---|---|---|---|---|---|---|
| HP | Cue | main mix |  |  |  | active |
| LINE 3/4 | Cue | own monitor mix |  |  |  | active |
| CUE 3 | Cue | own monitor mix |  |  |  | active |
| CUE 4 | Cue | main mix |  |  |  | inactive |
| MONITOR | Monitor | main mix |  |  | -43 dB | inactive |
| HP | Headphone | cue1 |  |  |  | active |
| LINE 3/4 | Headphone | cue2 |  |  |  | active |

**Plugin settings**

- **B2 Guit Dir** · Manley VOXBOX (off): Source Select Mic, Low Cut Off, Phase 0, Input 7.5, Gain 50 dB, SC Link Link, Comp Byp In, Comp Thresh 5.9, Comp Attack Med Fast, Comp Rel Med Slow, EQ Byp Byp, Lo Peak 0.0 dB, Lo Peak Freq 70 Hz, Mid Dip -7.3 dB, Mid Dip Freq 500 Hz, Hi Peak 1.0 dB, Hi Peak Freq 10 kHz, De Ess Byp Byp, De Ess Sel 6K, De Ess Thr 3.3, Meter GR, Transformer Byp Byp, Output 7.1 dB, Power Off
