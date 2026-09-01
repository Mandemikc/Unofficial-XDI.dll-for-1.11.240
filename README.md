# XDI.dll for Fallout 4 1.11.240

Unofficial compatibility DLL for **Extended Dialogue Interface (XDI)** on **Fallout 4 runtime 1.11.240**.

This project updates the official XDI 1.11.221 DLL for compatibility with Fallout 4 1.11.240 and F4SE 0.7.9.

## Requirements

- Fallout 4 runtime **1.11.240**
- Fallout 4 Script Extender (F4SE) **0.7.9**
- The official **Extended Dialogue Interface (XDI)** mod installed

Official XDI:

https://www.nexusmods.com/fallout4/mods/27216

Official F4SE:

https://f4se.silverlock.org/

## Download

The replacement `XDI.dll` is available from the **Releases** section on the right-hand side of this GitHub repository.

1. Click **Releases** on the right side of the repository page.
2. Open the latest release.
3. Download the attached `XDI.dll`.
4. Follow the installation instructions below.

Direct link to the latest release:

https://github.com/Mandemikc/Unofficial-XDI.dll-for-1.11.240/releases/latest

## Installation

### Vortex

1. Install the official Extended Dialogue Interface normally through Vortex.
2. Open the installed XDI mod folder.
3. Navigate to:

   `F4SE\Plugins\`

4. Back up the existing:

   `XDI.dll`

5. Replace it with the `XDI.dll` supplied here.
6. In Vortex, **Purge Mods**, then **Deploy Mods**.
7. If Vortex detects two versions of `XDI.dll`, select the **newer replacement file** so that it wins the conflict.
8. Launch Fallout 4 through F4SE.

Depending on your Vortex staging configuration, the original DLL may be located somewhere similar to:

`...\Extended Dialogue Interface...\F4SE\Plugins\XDI.dll`

The exact staging-folder name will vary between installations.

### Alternative: Vortex Override Mod

The replacement DLL can also be installed as a separate Vortex mod using this folder structure:

`F4SE\Plugins\XDI.dll`

Configure the compatibility mod to load **after the official XDI mod**, allowing this version of `XDI.dll` to win the conflict.

This method leaves the original XDI installation untouched and is easier to reverse.

## Compatibility

**Target Fallout 4 runtime:**

`Fallout4.exe 1.11.240.0`

**Target F4SE:**

`F4SE 0.7.9`

**Source XDI build:**

`Fallout 4 1.11.221`

This DLL was derived from the official XDI build for Fallout 4 1.11.221 and updated for the engine-address changes introduced with Fallout 4 1.11.240.

### Verified DLL

SHA-256:

`bc513de06bfe9390872e5af250716a8e92f3523df6c4828043d795f102036d77`

This hash identifies the exact DLL that was tested.

## Testing

The compatibility build has been tested successfully with:

- normal dialogue
- dialogue containing more than four response choices
- question and exit indicators
- unvoiced dialogue
- repeated conversations
- companion dialogue
- save and reload cycles
- interior and exterior cell transitions
- fast travel
- mod-added dialogue
- extended gameplay sessions

No XDI-related crashes or dialogue failures were observed during testing.

## Important

This is an **unofficial compatibility update**.

It is intended specifically for:

- Fallout 4 **1.11.240**
- F4SE **0.7.9**

Do not use this DLL with another Fallout 4 runtime unless compatibility has been confirmed.

The official Extended Dialogue Interface mod is still required. This project does not replace the rest of the XDI installation.

This project is not affiliated with or endorsed by Bethesda Game Studios or the official XDI development team.

If a current XDI rights-holder or maintainer requests removal of the redistributed DLL, the binary will be removed.

Please continue to download, endorse and support the official XDI project:

https://www.nexusmods.com/fallout4/mods/27216

## Credits

### Extended Dialogue Interface

**registrator2000 / reg2k**  
Original XDI developer

**Neanka**  
Current XDI maintainer/developer

### Fallout 4 Script Extender

**ianpatt and the F4SE team**

https://f4se.silverlock.org/

### Fallout 4

**Bethesda Game Studios**

## Disclaimer

Use at your own risk.

Although this build has undergone functional testing, Fallout 4 installations vary considerably because of differences in mod lists, load orders, F4SE plugins and game configuration.

Back up your existing `XDI.dll` and important save files before installing.
