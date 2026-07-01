# /// script
# requires-python = ">=3.10"
# ///
"""One-time import: copy studio manuals from ~/Desktop and iCloud Drive into
docs/manuals/<category>/ with clean, vendor-prefixed filenames.

Idempotent: skips a destination that already exists. Reports any missing
sources instead of failing. Re-runnable as gear is added.
"""
from __future__ import annotations

import shutil
from pathlib import Path

HOME = Path.home()
DESK = HOME / "Desktop"
ICLOUD = HOME / "Library/Mobile Documents/com~apple~CloudDocs/Documents/Manuals"
DEST = Path(__file__).resolve().parent.parent / "docs" / "manuals"

# (category, dest_filename, source_path)
MANIFEST: list[tuple[str, str, Path]] = [
    # --- daw-video ---
    ("daw-video", "Ableton-Live-12-Manual.pdf", DESK / "live12-manual-en.pdf"),
    ("daw-video", "DaVinci-Resolve.pdf", ICLOUD / "DaVinci Resolve.pdf"),
    ("daw-video", "Guitar-Pro-8-user-guide.pdf", ICLOUD / "Guitar-Pro-8-user-guide.pdf"),
    # --- plugins ---
    ("plugins", "UAD-Plug-Ins-Manual.pdf", ICLOUD / "UAD+Plug-Ins+Manual.pdf"),
    ("plugins", "Soundtoys-Users-Guide.pdf", ICLOUD / "Soundtoys-Users-Guide.pdf"),
    ("plugins", "Sonnox-Limiter-Manual.pdf", ICLOUD / "SonnoxLimMan.pdf"),
    ("plugins", "oeksound-soothe2-User-Manual.pdf", DESK / "oeksound soothe2 user manual.pdf"),
    ("plugins", "Klanghelm-VUMT-deluxe-Manual.pdf", DESK / "VUMTdeluxe-manual.pdf"),
    ("plugins", "Youlean-Loudness-Meter-2-Manual.pdf", DESK / "Youlean Loudness Meter 2 - MANUAL.pdf"),
    ("plugins", "Melodyne-5-studio-Standalone.pdf", ICLOUD / "Melodyne 5 studio Reference Manual, Stand-alone, English.pdf"),
    ("plugins", "Melodyne-5-studio-Other-DAW-no-ARA.pdf", ICLOUD / "Melodyne 5 studio Reference Manual, Other DAW without ARA, English.pdf"),
    ("plugins", "Scaler-2-Manual.pdf", ICLOUD / "PLUGINBOUTIQUE_Scaler2_Manual.pdf"),
    ("plugins", "Scaler-3-User-Guide.pdf", ICLOUD / "Scaler-3-User-Guide.pdf"),
    ("plugins", "Scaler-1-Manual.pdf", ICLOUD / "PLUGINBOUTIQUE_Scaler_Manual.pdf"),
    ("plugins", "Superior-Drummer-3-Manual.pdf", ICLOUD / "Superior Drummer 3 _ Manual _ Toontrack.pdf"),
    ("plugins", "Akai-VIP-3.0-User-Guide.pdf", ICLOUD / "VIP 3.0 - User Guide.pdf"),
    # --- controllers-interfaces ---
    ("controllers-interfaces", "Akai-MPK249-User-Guide.pdf", ICLOUD / "MPK249 - User Guide - v1.0.pdf"),
    ("controllers-interfaces", "Novation-Launchkey-Mk4-Mini-25-User-Guide.pdf", ICLOUD / "launchkey_mk4_mini_25_user_guide_v1.1_pdf-en.pdf"),
    ("controllers-interfaces", "IK-iRig-HD-X-User-Manual.pdf", ICLOUD / "iRig_HD_X_User_Manual.pdf"),
    # --- boss-roland ---
    ("boss-roland", "Boss-CE-2W-Chorus.pdf", DESK / "CE-2W_eng02_W.pdf"),
    ("boss-roland", "Boss-DD-200-Delay.pdf", ICLOUD / "DD-200_eng03_W.pdf"),
    ("boss-roland", "Boss-ES-8-Switcher.pdf", ICLOUD / "ES-8_e02_W.pdf"),
    ("boss-roland", "Boss-ES-8-Editor.pdf", ICLOUD / "ES-8_Editor_manual.pdf"),
    ("boss-roland", "Boss-ES-8-Supplement.pdf", ICLOUD / "ES-8_v2_eng01_W.pdf"),
    ("boss-roland", "Boss-RC-1-Loop-Station.pdf", DESK / "RC-1_M_eng02_W.pdf"),
    ("boss-roland", "Boss-SY-1-Synth.pdf", DESK / "SY-1_eng03_W.pdf"),
    ("boss-roland", "Roland-TD-17.pdf", ICLOUD / "TD-17_eng01_W.pdf"),
    ("boss-roland", "Roland-TD-17-DataList.pdf", ICLOUD / "TD-17_DataList_eng03_W.pdf"),
    ("boss-roland", "Roland-TD-17-Addendum.pdf", DESK / "TD-17_add_eng01_W.pdf"),
    ("boss-roland", "Boss-GM-800-Reference.pdf", ICLOUD / "GM-800_ReferenceManual_eng02_W.pdf"),
    ("boss-roland", "Boss-GM-800-Parameter-Guide.pdf", ICLOUD / "GM-800_ParameterGuide_eng02_W.pdf"),
    ("boss-roland", "Boss-GM-800-Sound-List.pdf", ICLOUD / "GM-800_soundlist_multi01_W.pdf"),
    ("boss-roland", "Roland-FP-30X-Piano.pdf", ICLOUD / "FP-30X_eng04_W.pdf"),
    # --- pedals ---
    ("pedals", "Dunlop-CryBaby-535Q.pdf", ICLOUD / "535Q.pdf"),
    ("pedals", "Strymon-Flint-v2.pdf", ICLOUD / "Flint_v2_UserManual_RevB.pdf"),
    ("pedals", "Radial-EXTC-Stereo.pdf", DESK / "EXTC-Stereo-manual-web.pdf"),
    ("pedals", "KHE-ACS-Series.pdf", DESK / "KHE-ACS-Series-User-Manual-V1.3+2021-07-06.pdf"),
    ("pedals", "Pinwheel-Expression-Pedal-Guide.pdf", DESK / "Pinwheel_Experssion_Pedal_Guide.pdf"),
    ("pedals", "Pinwheel-Rev-B.pdf", DESK / "The_Pinwheel_REV_B.pdf"),
    ("pedals", "Meteore-Reverb.pdf", DESK / "Meteore-Manual-original.pdf"),
    ("pedals", "Catalinbread-Naga-Viper.pdf", DESK / "NAGAmanual.pdf"),
    ("pedals", "SourceAudio-Vertigo-Tremolo.pdf", ICLOUD / "vertigo_user_manual.pdf"),
    ("pedals", "IK-TONEX-Pedal-User-Manual.pdf", ICLOUD / "TONEX_Pedal_User_Manual.pdf"),
    ("pedals", "IK-TONEX-Pedal-Quick-Start.pdf", DESK / "TONEX_Pedal_Quick_Start_Guide.pdf"),
    ("pedals", "Vertex-Boost-MKII.pdf", ICLOUD / "BOOST-MKII-Manual.pdf"),
    ("pedals", "ChaseBliss-MOOD.pdf", ICLOUD / "MOOD_Manual_Pedal_Chase+Bliss.pdf"),
    # --- guitar-gear ---
    ("guitar-gear", "EMG-JMaster-Set.pdf", ICLOUD / "jmaster_set_0230-0378ra.pdf"),
    ("guitar-gear", "EMG-JMaster-System.pdf", ICLOUD / "jmaster_system_0230-0377rb.pdf"),
    ("guitar-gear", "Certano-T-Bender.pdf", ICLOUD / "Certano T-Bender Installation Guide.pdf"),
    # --- monitors ---
    ("monitors", "Turbosound-TFM-AN-Monitors.pdf", ICLOUD / "Turbosound_TFM-AN_Monitors.pdf"),
    ("monitors", "Turbosound-TFM-AN-Quick-Start.pdf", ICLOUD / "TFM-AN_TFX-AN-Series_QSG_WW.pdf"),
    # --- loopers ---
    ("loopers", "HeadRush-Looperboard-User-Guide.pdf", ICLOUD / "Looperboard-User-Guide-v2_0_0[0805].pdf"),
]


def main() -> None:
    copied = skipped = 0
    missing: list[str] = []
    for category, dest_name, src in MANIFEST:
        dst_dir = DEST / category
        dst_dir.mkdir(parents=True, exist_ok=True)
        dst = dst_dir / dest_name
        if dst.exists():
            skipped += 1
            continue
        if not src.exists():
            missing.append(f"{category}/{dest_name}  <-  {src}")
            continue
        shutil.copy2(src, dst)
        print(f"  + {category}/{dest_name}  ({dst.stat().st_size // 1024} KB)")
        copied += 1

    print(f"\nCopied {copied}, skipped {skipped} (already present).")
    if missing:
        print(f"\nMISSING SOURCES ({len(missing)}):")
        for m in missing:
            print(f"  ! {m}")


if __name__ == "__main__":
    main()
