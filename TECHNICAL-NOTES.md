# Technical Notes

## Purpose

This repository contains an unofficial compatibility update for Extended Dialogue Interface (XDI) for Fallout 4 runtime 1.11.240 and F4SE 0.7.9.

The working compatibility DLL was produced from the official XDI 1.11.221 DLL by updating runtime-specific Fallout 4 / F4SE address constants and XDI's runtime compatibility metadata.

## Method

The compatibility work used:

- Static analysis of the official XDI 1.11.221 DLL.
- Comparison against Fallout4.exe 1.11.240.
- F4SE 0.7.9 / Fallout 4 1.11.240 runtime information.
- The F4SE 0.7.8 -> 0.7.9 address changes as the authoritative source for moved engine/F4SE addresses.
- Verification of XDI's signature-based lookups against Fallout4.exe 1.11.240.

This is not an Address Library/CommonLib-style relocation conversion. It is a runtime-specific compatibility patch for Fallout 4 1.11.240.

## Changes

- 77 distinct Fallout/F4SE RVA mappings updated.
- 250 compiled RVA occurrences updated in the XDI 1.11.221 DLL.
- 7 runtime metadata entries changed from Fallout 4 1.11.221 to Fallout 4 1.11.240.

## Tested Output

Target:

- Fallout4.exe: 1.11.240.0
- F4SE: 0.7.9

Tested DLL SHA-256:

`bc513de06bfe9390872e5af250716a8e92f3523df6c4828043d795f102036d77`

## Functional Testing

The compatibility build was tested with:

- normal dialogue
- more than four dialogue choices
- question and exit indicators
- unvoiced dialogue
- companion dialogue
- repeated conversations
- save/reload cycles
- interior/exterior transitions
- fast travel
- mod-added dialogue
- extended gameplay sessions

No XDI-related failures were observed during the reported testing.

## Source Folder

`source/patch_xdi_1_11_240.py`

This reproduces the binary transformation but does not contain or distribute XDI itself. Users must provide their own official XDI 1.11.221 DLL.

`source/address-map.csv`

This documents the 77 old-to-new RVA mappings used by the compatibility patch.

## Attribution

Extended Dialogue Interface (XDI):
- registrator2000 / reg2k - original developer
- Neanka - current maintainer/developer

Fallout 4 Script Extender (F4SE):
- ianpatt and the F4SE team

Fallout 4:
- Bethesda Game Studios
