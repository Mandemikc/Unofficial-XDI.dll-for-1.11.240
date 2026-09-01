#!/usr/bin/env python3
"""
XDI 1.11.221 -> Fallout 4 1.11.240 compatibility patcher.

This script DOES NOT contain or distribute XDI itself.
The user must supply their own official XDI.dll from the XDI 1.11.221 build.

It updates known Fallout 4/F4SE RVA constants and the runtime compatibility
metadata required for Fallout 4 1.11.240 / F4SE 0.7.9.

The resulting DLL should have SHA-256:
bc513de06bfe9390872e5af250716a8e92f3523df6c4828043d795f102036d77
"""

from pathlib import Path
import argparse
import hashlib
import struct
import sys

PATCHES = {
    0x0021E3F0: 0x0021E710,
    0x002A0540: 0x002A0860,
    0x00311860: 0x00311B80,
    0x00513310: 0x00513630,
    0x00564590: 0x005648B0,
    0x005645B0: 0x005648D0,
    0x00768B10: 0x00768E20,
    0x009DCC10: 0x009DCF20,
    0x00A37980: 0x00A37C90,
    0x01044170: 0x01044500,
    0x01086220: 0x01086570,
    0x01089E50: 0x0108A1A0,
    0x010E02C0: 0x010E0610,
    0x01180CD0: 0x01181020,
    0x01657AC0: 0x01657DE0,
    0x01657F20: 0x01658240,
    0x01658F10: 0x01659230,
    0x01658F70: 0x01659290,
    0x01658FE0: 0x01659300,
    0x016590E0: 0x01659400,
    0x016593B0: 0x016596D0,
    0x0167BEC0: 0x0167C1E0,
    0x0167D180: 0x0167D4A0,
    0x01A7FE60: 0x01A80320,
    0x01AD66F0: 0x01AD6BB0,
    0x01ADD3A0: 0x01ADD860,
    0x01AE6A40: 0x01AE6F00,
    0x01B03280: 0x01B03740,
    0x01B17FB0: 0x01B18470,
    0x01B18000: 0x01B184C0,
    0x01B18180: 0x01B18640,
    0x020DC030: 0x020E3A60,
    0x020E10A0: 0x020E8AD0,
    0x020E5130: 0x020ECB60,
    0x020E55F0: 0x020ED020,
    0x020E6CE0: 0x020EE710,
    0x020F32F0: 0x020FAD20,
    0x020F3360: 0x020FAD90,
    0x020F97D0: 0x02101200,
    0x020F97F0: 0x02101220,
    0x020F9870: 0x021012A0,
    0x020F9DE0: 0x02101810,
    0x020F9FD0: 0x02101A00,
    0x021607B0: 0x021681E0,
    0x022BCC7E: 0x022C46AE,
    0x02468160: 0x024701C0,
    0x02468300: 0x02470360,
    0x02468860: 0x024708C0,
    0x0246A070: 0x024720D0,
    0x02F94108: 0x02F9F158,
    0x02F95430: 0x02FA0480,
    0x02F9D3B8: 0x02FA8408,
    0x02F9D418: 0x02FA8468,
    0x02FA8090: 0x02FB30E0,
    0x030DA200: 0x030E5280,
    0x030DBE40: 0x030E6EC0,
    0x030DC080: 0x030E7100,
    0x030DD8B0: 0x030E8930,
    0x030DDAA0: 0x030E8B20,
    0x030E0288: 0x030EB308,
    0x030E0950: 0x030EB9D0,
    0x030E0E50: 0x030EBED0,
    0x030E0EA0: 0x030EBF20,
    0x030ED338: 0x030F83B8,
    0x030ED8A0: 0x030F8920,
    0x03262324: 0x0326D3A4,
    0x03268AB8: 0x03273B48,
    0x032D22E0: 0x032DD370,
    0x033077A0: 0x03312820,
    0x03394A60: 0x0339FAE0,
    0x0343B038: 0x0344B4B8,
    0x038CA960: 0x038E11E0,
    0x03DA6AF0: 0x03DBD370,
    0x03DA7440: 0x03DBDCC0,
    0x03DA7500: 0x03DBDD80,
    0x03E46CF0: 0x03E5D630,
    0x03E5E170: 0x03E74AB0,
}

OLD_RUNTIME = 0x010B0DD0  # Fallout 4 1.11.221
NEW_RUNTIME = 0x010B0F00  # Fallout 4 1.11.240

EXPECTED_DISTINCT_RVAS = 77
EXPECTED_RVA_OCCURRENCES = 250
EXPECTED_RUNTIME_OCCURRENCES = 7
EXPECTED_OUTPUT_SHA256 = "bc513de06bfe9390872e5af250716a8e92f3523df6c4828043d795f102036d77"


def all_hits(data: bytearray, needle: bytes):
    hits = []
    start = 0
    while True:
        pos = data.find(needle, start)
        if pos < 0:
            return hits
        hits.append(pos)
        start = pos + 1


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def patch_xdi(input_path: Path, output_path: Path):
    data = bytearray(input_path.read_bytes())

    if len(PATCHES) != EXPECTED_DISTINCT_RVAS:
        raise RuntimeError(
            f"Internal patch table error: expected {EXPECTED_DISTINCT_RVAS} RVAs, "
            f"found {len(PATCHES)}."
        )

    patched_occurrences = 0
    missing = []

    for old_rva, new_rva in PATCHES.items():
        old_bytes = struct.pack("<I", old_rva)
        new_bytes = struct.pack("<I", new_rva)

        hits = all_hits(data, old_bytes)
        if not hits:
            missing.append(old_rva)
            continue

        for pos in hits:
            data[pos:pos + 4] = new_bytes

        patched_occurrences += len(hits)

    if missing:
        formatted = ", ".join(f"0x{x:08X}" for x in missing)
        raise RuntimeError(
            "Input DLL does not match the expected XDI 1.11.221 build. "
            f"Missing expected RVA constants: {formatted}"
        )

    if patched_occurrences != EXPECTED_RVA_OCCURRENCES:
        raise RuntimeError(
            "Input DLL does not match the tested XDI 1.11.221 binary. "
            f"Expected {EXPECTED_RVA_OCCURRENCES} RVA occurrences, "
            f"found {patched_occurrences}. No output was written."
        )

    old_runtime_bytes = struct.pack("<I", OLD_RUNTIME)
    new_runtime_bytes = struct.pack("<I", NEW_RUNTIME)

    runtime_hits = all_hits(data, old_runtime_bytes)
    if len(runtime_hits) != EXPECTED_RUNTIME_OCCURRENCES:
        raise RuntimeError(
            "Unexpected XDI runtime metadata layout. "
            f"Expected {EXPECTED_RUNTIME_OCCURRENCES} instances of "
            f"0x{OLD_RUNTIME:08X}, found {len(runtime_hits)}. No output was written."
        )

    for pos in runtime_hits:
        data[pos:pos + 4] = new_runtime_bytes

    output_hash = sha256_bytes(data)

    if output_hash.lower() != EXPECTED_OUTPUT_SHA256.lower():
        raise RuntimeError(
            "Patch completed but output hash does not match the tested build.\n"
            f"Expected: {EXPECTED_OUTPUT_SHA256}\n"
            f"Actual:   {output_hash}\n"
            "No output was written."
        )

    output_path.write_bytes(data)

    print("Patch successful.")
    print(f"Input:  {input_path}")
    print(f"Output: {output_path}")
    print(f"Distinct RVA mappings: {len(PATCHES)}")
    print(f"RVA occurrences patched: {patched_occurrences}")
    print(f"Runtime entries patched: {len(runtime_hits)}")
    print(f"SHA-256: {output_hash}")


def main():
    parser = argparse.ArgumentParser(
        description="Patch the official XDI 1.11.221 DLL for Fallout 4 1.11.240."
    )
    parser.add_argument(
        "input",
        type=Path,
        help="Path to the official XDI 1.11.221 XDI.dll",
    )
    parser.add_argument(
        "-o",
        "--output",
        type=Path,
        default=Path("XDI_1.11.240.dll"),
        help="Output DLL path (default: XDI_1.11.240.dll)",
    )

    args = parser.parse_args()

    if not args.input.is_file():
        print(f"ERROR: Input file not found: {args.input}", file=sys.stderr)
        return 1

    if args.output.resolve() == args.input.resolve():
        print(
            "ERROR: Refusing to overwrite the source XDI.dll. "
            "Choose a different output filename.",
            file=sys.stderr,
        )
        return 1

    try:
        patch_xdi(args.input, args.output)
    except Exception as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
