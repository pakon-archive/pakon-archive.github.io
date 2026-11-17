# Pakon scanner archive

Preservation copies of the vendor files needed to keep Kodak / Pakon film
scanners (F-135, F-135 Plus, F-235, F-235 Plus, F-335) running. The product
line is long discontinued and the original distribution channels are gone;
without these files, working hardware becomes unusable.

All files are unmodified originals. Checksums are in `SHA256SUMS`; verify
with `shasum -a 256 -c SHA256SUMS` (macOS/Linux) or
`sha256sum -c SHA256SUMS` (Linux). Firmware especially is worth verifying
after copying it anywhere -- a truncated HEX file just fails silently.

After adding or removing files, run `python3 generate-index.py` to
regenerate `index.html` and `SHA256SUMS`, and commit those along with the
files.

## Contents

- `firmware/` — scanner application firmware (`*.HEX`), as shipped in the
  F-X35 COM Server's `Config/Firmware` directory. The scanner loads firmware
  into RAM over USB at every power-on; nothing here flashes or modifies the
  hardware. Kodak's own `ReadmeF135.txt` / `ReadmeF235.txt` / `ReadmeF335.txt`
  describe the file naming and which files each model uses.
  `FirmwareLoader.exe` is Kodak's loader utility.
- `drivers/` — the Windows USB driver folders, kept as the F-X35 installer
  laid them out under `Program Files\Pakon\`: `F-135/F135Driver`,
  `F-335/F335Driver`, `F235Driver` and `FX35Driver`. Besides the `.sys` and
  `.inf` driver files these hold the stage-1 loader `F235Ldr.sys` and the
  USB bridge firmware (`Pakon*.hex`), which open-source clients need to
  boot the scanner. `drivers/SOURCES.md` records where each file came from;
  every file was checked against two other copies.
- `docs/Service Manuals/` — F-135, F-235, F-335 service manuals and the
  F-235 / F-335 disassembly manuals. Where several editions of a manual
  circulate, the best available copy is at the top level and earlier
  editions are kept in `older/`.
- `docs/User Manuals/` — F-135 (English and Spanish), F-235, F-335 user
  manuals and the F-335 setup guide. Earlier editions in `older/`.
- `docs/COM API/` — the F235 COM Server API reference and user guide, and
  the FX35 SDK release notes, for software that drives the scanner
  programmatically.
- `docs/PSI/` — the PSI scanning software's help manual (PDF and CHM),
  release notes, and download instructions.
- `docs/Troubleshooting/` — the FX35 troubleshooting guide.
- `docs/Calibration/` — the F-135 / F-235 / F-335 Calibration Wizard
  guides (Word `.doc` originals, as distributed).
- `docs/Marketing/` — salesheets, datasheets, and the model comparison
  brochure. Useful for identifying models and original specifications.

## Wanted

Copies of the following are sought. Open an issue if you can provide one.

- Original installers: TLX Client Demo, PSI, TLX, F-X35 COM Server
- Service and calibration tools (DxPots, film track utilities)
- Pakon software for the F-K35 or other models not listed here

These materials are © Kodak / Pakon. They are preserved here solely to keep
discontinued hardware in service; no ownership is claimed. Rights holders
with concerns can open an issue.
