# XDI.dll-for-1.11.240
Extended Dialogue Interface XDI.dll file for the updated Fallout 4 version 1.11.240

# Extended Dialogue Interface - Fallout 4 1.11.240 Compatibility Build

This project provides a compatibility build of **Extended Dialogue Interface (XDI)** for **Fallout 4 runtime 1.11.240**.

## Requirements

* Fallout 4 runtime **1.11.240**
* Fallout 4 Script Extender (F4SE) **0.7.9**
* The official **Extended Dialogue Interface (XDI)** mod installed

Official XDI:
https://www.nexusmods.com/fallout4/mods/27216

Official F4SE:
https://f4se.silverlock.org/

## Installation

1. Install Extended Dialogue Interface normally.
2. Install the appropriate F4SE version for Fallout 4 1.11.240.
3. Download the replacement `XDI.dll` from this repository's Releases page.
4. Replace:

   `Fallout 4\Data\F4SE\Plugins\XDI.dll`

   with the supplied version.

### Vortex

The DLL can also be installed as an override after the official XDI mod.

If Vortex reports a file conflict, configure this compatibility build to load **after XDI** so that its `XDI.dll` wins the conflict.

## Compatibility

Target game runtime:

`Fallout4.exe 1.11.240.0`

Target F4SE:

`F4SE 0.7.9`

The DLL was derived from the official XDI build for Fallout 4 1.11.221 and updated for the engine-address changes introduced with Fallout 4 1.11.240.

## Testing

The compatibility build has been tested with:

* normal dialogue
* dialogue with more than four response choices
* question and exit indicators
* unvoiced dialogue
* repeated conversations
* save/reload cycles
* interior and exterior cell transitions
* fast travel
* mod-added dialogue

No XDI-related errors or crashes were observed during initial testing.

## Important

This is an unofficial compatibility update.

Extended Dialogue Interface was created by **registrator2000 / reg2k**. This project is not affiliated with or endorsed by the original author or Bethesda Game Studios.

Please continue to endorse and support the original XDI project:

https://www.nexusmods.com/fallout4/mods/27216

## Credits

Extended Dialogue Interface:
registrator2000 / reg2k

F4SE:
ianpatt and the F4SE team

Fallout 4:
Bethesda Game Studios
