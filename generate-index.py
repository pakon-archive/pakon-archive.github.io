#!/usr/bin/env python3
"""Regenerate index.html and SHA256SUMS from the files in this directory.

Run after adding or removing files, then commit the results along with the
files themselves. Sections below control the order and description of each
folder on the index page; a new folder must be added there to appear.
"""
import hashlib
import os
import re
import urllib.parse

ROOT = os.path.dirname(os.path.abspath(__file__))

# (folder, section title, description)
SECTIONS = [
    ("docs/Service Manuals", "Service manuals",
     "Service and disassembly manuals for the F-135, F-235 and F-335."),
    ("docs/User Manuals", "User manuals",
     "Operator manuals, quick start and setup guides."),
    ("docs/Calibration", "Calibration",
     "Calibration Wizard guides (Word originals, as distributed)."),
    ("docs/Troubleshooting", "Troubleshooting",
     "The FX35 troubleshooting guide."),
    ("docs/COM API", "COM API / SDK",
     "The F235 COM Server API reference and guide, and the FX35 SDK release"
     " notes, for software that drives the scanner programmatically."),
    ("docs/PSI", "PSI software documentation",
     "Help manual, release notes and download instructions for the PSI"
     " scanning software."),
    ("docs/Marketing", "Marketing",
     "Salesheets, datasheets and the model comparison brochure — useful for"
     " identifying models and original specifications."),
    ("firmware", "Firmware",
     "Scanner application firmware (HEX files) as shipped with the F-X35 COM"
     " Server. The scanner loads firmware into RAM over USB at every"
     " power-on; nothing here flashes the hardware. Kodak's own readme files"
     " describe the naming and which files each model uses."),
]

# Not part of the archived payload: never checksummed, never listed.
PAPERWORK = {"SHA256SUMS", "README.md", "index.html", ".nojekyll",
             "generate-index.py", ".DS_Store"}

HEAD = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Pakon Scanner Archive — manuals, firmware and documentation for Kodak Pakon F-135, F-235, F-335 film scanners</title>
<meta name="description" content="Preservation archive for Kodak Pakon film scanners: F-135, F-135 Plus, F-235, F-335 service manuals, user manuals, disassembly manuals, firmware, calibration guides, PSI documentation and error code references.">
<style>
body { font-family: Georgia, serif; max-width: 46rem; margin: 2rem auto; padding: 0 1rem; line-height: 1.5; color: #222; background: #fff; }
h1 { font-size: 1.6rem; } h2 { font-size: 1.15rem; margin-top: 2rem; border-bottom: 1px solid #ccc; padding-bottom: .2rem; }
ul { list-style: none; padding-left: 0; } li { padding: .15rem 0; }
li span { color: #888; font-size: .85em; margin-left: .5em; }
footer { margin-top: 3rem; font-size: .85em; color: #666; border-top: 1px solid #ccc; padding-top: 1rem; }
</style>
</head>
<body>
<h1>Pakon Scanner Archive</h1>
<p>Preservation copies of the vendor files needed to keep Kodak / Pakon film
scanners (F-135, F-135&nbsp;Plus, F-235, F-235&nbsp;Plus, F-335) running. The
product line is long discontinued and the original distribution channels are
gone; without these files, working hardware becomes unusable.</p>
<p>All files are unmodified originals. Checksums: <a href="SHA256SUMS">SHA256SUMS</a>.
Wanted items and more detail: see the <a href="README.md">README</a>.</p>
"""

FOOT = """
<footer>
These materials are © Kodak / Pakon. They are preserved solely to keep
discontinued hardware in service; no ownership is claimed. Rights holders
with concerns can open an issue on the repository.
</footer>
</body>
</html>
"""


def payload_files():
    for dirpath, dirnames, filenames in os.walk(ROOT):
        dirnames[:] = sorted(d for d in dirnames if d != ".git")
        for name in sorted(filenames):
            if name in PAPERWORK:
                continue
            yield os.path.relpath(os.path.join(dirpath, name), ROOT)


def size_label(nbytes):
    if nbytes > 1048576:
        return f"{nbytes / 1048576:.1f} MB"
    return f"{nbytes // 1024} KB"


def sort_key(relpath):
    """Readmes and the loader lead their folder; then alphabetical."""
    name = os.path.basename(relpath)
    if name.startswith("Readme"):
        return (0, name)
    if name == "FirmwareLoader.exe":
        return (1, name)
    if os.sep + "older" + os.sep in relpath:
        return (3, name.lower())
    return (2, name.lower())


def section(folder, title, blurb):
    rows = []
    files = [f for f in payload_files()
             if f.startswith(folder + os.sep)]
    for rel in sorted(files, key=sort_key):
        href = urllib.parse.quote(rel.replace(os.sep, "/"))
        label = os.path.basename(rel)
        if os.sep + "older" + os.sep in rel:
            label += " (older edition)"
        nbytes = os.path.getsize(os.path.join(ROOT, rel))
        rows.append(f'      <li><a href="{href}">{label}</a>'
                    f' <span>{size_label(nbytes)}</span></li>')
    return (f"  <section>\n    <h2>{title}</h2>\n    <p>{blurb}</p>\n"
            "    <ul>\n" + "\n".join(rows) + "\n    </ul>\n  </section>")


def main():
    listed = set()
    parts = []
    for folder, title, blurb in SECTIONS:
        parts.append(section(folder, title, blurb))
        listed.update(f for f in payload_files()
                      if f.startswith(folder + os.sep))
    unlisted = sorted(set(payload_files()) - listed)
    if unlisted:
        raise SystemExit("not covered by any section (add one): "
                         + ", ".join(unlisted))
    with open(os.path.join(ROOT, "index.html"), "w") as fh:
        fh.write(HEAD + "\n".join(parts) + FOOT)
    with open(os.path.join(ROOT, "SHA256SUMS"), "w") as fh:
        for rel in sorted(payload_files()):
            digest = hashlib.sha256(
                open(os.path.join(ROOT, rel), "rb").read()).hexdigest()
            fh.write(f"{digest}  {rel}\n")
    count = len(list(payload_files()))
    print(f"index.html and SHA256SUMS regenerated: {count} files")


if __name__ == "__main__":
    main()
