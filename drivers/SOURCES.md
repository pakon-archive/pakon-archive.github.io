# Driver sources

The Windows USB driver folders as installed by the F-X35 software under
`C:\Program Files\Pakon\`. Folder names and layout are kept as installed:
`F-135/F135Driver`, `F-335/F335Driver`, `F235Driver` and `FX35Driver`.
Every file is a byte-for-byte copy. Nothing was renamed, re-encoded or
unpacked.

Each file was taken from three separate copies and compared:

- **A**: archive.org/details/pakonf-135, `PAKONF135.iso`
  (MD5 `395b5be041eca1ccc7c0d4e24065beac`, SHA-1
  `8c1e1b130e008f3238ae5fcd39d5e7b0c3431691`, matching archive.org's
  published hashes), path `fx35install/program files/Pakon/` inside the ISO.
  Extracted with bsdtar; the ISO was not mounted.
- **B**: github.com/plonsker/pakon-scanning-software, commit
  `1260d00a5fb4389525d8458d4fcbcd6c7fe40da3`, folder
  `Pakon Update/fx35install/program files/Pakon/`
  (https://github.com/plonsker/pakon-scanning-software/tree/1260d00a5fb4389525d8458d4fcbcd6c7fe40da3/Pakon%20Update/fx35install/program%20files/Pakon)
- **C**: github.com/nunocruz/pakon_135plus, commit
  `fb519e147152796d5b2b45801315dcef8c00ade0`, folder
  `Software/Pakon Update/fx35install/program files/Pakon/`
  (https://github.com/nunocruz/pakon_135plus/tree/fb519e147152796d5b2b45801315dcef8c00ade0/Software/Pakon%20Update/fx35install/program%20files/Pakon)

All 44 files were identical in A, B and C.

These are three separately uploaded copies, but probably not three separate
releases. B and C both name their top folder `Pakon Update` and have the same
`fx35install` layout as the ISO, although their trees differ slightly (756
and 754 files). The comparison shows that no copy was corrupted or altered
along the way. It doesn't show that Kodak shipped these exact files in more
than one release.

`F235Ldr.sys` (MD5 `6be781bad6fb9cf7ade4095baed336e0`) and the F-135
`Pakon7.hex` (MD5 `07f5001a951c4be179008d948be82b69`) also match the
checksums an existing open-source client uses.

`FX35Driver/Pakon7.hex` is a different file from the `Pakon7.hex` in
`F135Driver` and `F335Driver` (30213 vs 30129 bytes). Both sources agree on
each version, so this is how Kodak shipped it, not a copying error.

| File | Bytes | SHA-256 | Path under `program files/Pakon/` in A, B and C | A = B = C |
|---|---|---|---|---|
| `F-135/F135Driver/F135usb2.sys` | 12928 | `03f3b5a1b0ceb13ba2d74154db893ac2de6f3e9a3620d0c9470fce823128a95e` | `F-135/F135Driver/F135usb2.sys` | yes |
| `F-135/F135Driver/F235Disk.tag` | 175 | `312f06b717a2764d19aba0e3ed9b0ba2557fe53d2b57b90ecb34dfc738b49245` | `F-135/F135Driver/F235Disk.tag` | yes |
| `F-135/F135Driver/F235Ldr.sys` | 16000 | `785bd29f37f8e49286be7a9b033e3741825952f5c293e2e143906504838ed2f1` | `F-135/F135Driver/F235Ldr.sys` | yes |
| `F-135/F135Driver/F235Lib.sys` | 16000 | `6cfba708fd8fd982331cf0f93ffb238a2b964c8aa6b020cb0a2f96cd42995059` | `F-135/F135Driver/F235Lib.sys` | yes |
| `F-135/F135Driver/F235usb2.inf` | 7559 | `da50b0469cfc5b79171d87f0b217f0572368b0b46d64c885c45e8082c727dbf6` | `F-135/F135Driver/F235usb2.inf` | yes |
| `F-135/F135Driver/F235usb2.sys` | 12928 | `8bc878aa0108206f72cd2ca987245e5a06eef82a675eed4f66cf252c7d2cd093` | `F-135/F135Driver/F235usb2.sys` | yes |
| `F-135/F135Driver/FX35usb2.sys` | 12928 | `5b49d574cc5375161725d39bf05f3ef1586a16a58953ff59abbabd9c2f3e5b3c` | `F-135/F135Driver/FX35usb2.sys` | yes |
| `F-135/F135Driver/Pakon5.hex` | 30180 | `6ea86ecf77e281cf0fbea0a94eea16ec9661bcc6ca265e69660e74a2b569f2da` | `F-135/F135Driver/Pakon5.hex` | yes |
| `F-135/F135Driver/Pakon7.hex` | 30129 | `f0074bb306780b628b4087e0f5f9c9dda3c15d31102b1ce3fa5abce94bdff414` | `F-135/F135Driver/Pakon7.hex` | yes |
| `F-135/F135Driver/Pakon8.hex` | 29914 | `1f21fb0809a432ab1b4c4cf566be609a2eee9c156017018e645a8088aab70a67` | `F-135/F135Driver/Pakon8.hex` | yes |
| `F-135/F135Driver/PknInit.hex` | 31323 | `e116ca855ccf45c608e892b25b9c9b5eb7ecf96640313082d082403b84edb8f3` | `F-135/F135Driver/PknInit.hex` | yes |
| `F-335/F335Driver/F135usb2.sys` | 12928 | `03f3b5a1b0ceb13ba2d74154db893ac2de6f3e9a3620d0c9470fce823128a95e` | `F-335/F335Driver/F135usb2.sys` | yes |
| `F-335/F335Driver/F235Disk.tag` | 175 | `312f06b717a2764d19aba0e3ed9b0ba2557fe53d2b57b90ecb34dfc738b49245` | `F-335/F335Driver/F235Disk.tag` | yes |
| `F-335/F335Driver/F235Ldr.sys` | 16000 | `785bd29f37f8e49286be7a9b033e3741825952f5c293e2e143906504838ed2f1` | `F-335/F335Driver/F235Ldr.sys` | yes |
| `F-335/F335Driver/F235Lib.sys` | 16000 | `6cfba708fd8fd982331cf0f93ffb238a2b964c8aa6b020cb0a2f96cd42995059` | `F-335/F335Driver/F235Lib.sys` | yes |
| `F-335/F335Driver/F235usb2.inf` | 7559 | `da50b0469cfc5b79171d87f0b217f0572368b0b46d64c885c45e8082c727dbf6` | `F-335/F335Driver/F235usb2.inf` | yes |
| `F-335/F335Driver/F235usb2.sys` | 12928 | `8bc878aa0108206f72cd2ca987245e5a06eef82a675eed4f66cf252c7d2cd093` | `F-335/F335Driver/F235usb2.sys` | yes |
| `F-335/F335Driver/FX35usb2.sys` | 12928 | `5b49d574cc5375161725d39bf05f3ef1586a16a58953ff59abbabd9c2f3e5b3c` | `F-335/F335Driver/FX35usb2.sys` | yes |
| `F-335/F335Driver/Pakon5.hex` | 30180 | `6ea86ecf77e281cf0fbea0a94eea16ec9661bcc6ca265e69660e74a2b569f2da` | `F-335/F335Driver/Pakon5.hex` | yes |
| `F-335/F335Driver/Pakon7.hex` | 30129 | `f0074bb306780b628b4087e0f5f9c9dda3c15d31102b1ce3fa5abce94bdff414` | `F-335/F335Driver/Pakon7.hex` | yes |
| `F-335/F335Driver/Pakon8.hex` | 29914 | `1f21fb0809a432ab1b4c4cf566be609a2eee9c156017018e645a8088aab70a67` | `F-335/F335Driver/Pakon8.hex` | yes |
| `F-335/F335Driver/PknInit.hex` | 31323 | `e116ca855ccf45c608e892b25b9c9b5eb7ecf96640313082d082403b84edb8f3` | `F-335/F335Driver/PknInit.hex` | yes |
| `F235Driver/F235Disk.tag` | 175 | `312f06b717a2764d19aba0e3ed9b0ba2557fe53d2b57b90ecb34dfc738b49245` | `F235Driver/F235Disk.tag` | yes |
| `F235Driver/F235Ldr.sys` | 16000 | `785bd29f37f8e49286be7a9b033e3741825952f5c293e2e143906504838ed2f1` | `F235Driver/F235Ldr.sys` | yes |
| `F235Driver/F235Lib.sys` | 16000 | `6cfba708fd8fd982331cf0f93ffb238a2b964c8aa6b020cb0a2f96cd42995059` | `F235Driver/F235Lib.sys` | yes |
| `F235Driver/F235usb2.inf` | 6925 | `66c057d6157cf2651421e8e20d97cb4a5d2578bf8d3d639a7a0d413fe9cb6018` | `F235Driver/F235usb2.inf` | yes |
| `F235Driver/F235usb2.sys` | 12928 | `8bc878aa0108206f72cd2ca987245e5a06eef82a675eed4f66cf252c7d2cd093` | `F235Driver/F235usb2.sys` | yes |
| `F235Driver/LDRCFG.txt` | 864 | `7ea30040cac810c02245256ad92cb33fb230b2aa63b78080c089a9f61ed7ae99` | `F235Driver/LDRCFG.txt` | yes |
| `F235Driver/Pakon.hex` | 37770 | `06dc3674f72cad2dfaa7a56279b6088958a3e0b0f2f07df9ca19209a65632100` | `F235Driver/Pakon.hex` | yes |
| `F235Driver/Pakon1.hex` | 35574 | `383393e8db7624fd1bdc0deb4665f5d0ee4a6030f47aa227ca0bed10f86872ce` | `F235Driver/Pakon1.hex` | yes |
| `F235Driver/pakon2.hex` | 37163 | `e815ff8d9063d5daa9fac80a13d37f344036abcaca08a220284c43f3eae6bf07` | `F235Driver/pakon2.hex` | yes |
| `F235Driver/Pakon5.hex` | 30180 | `6ea86ecf77e281cf0fbea0a94eea16ec9661bcc6ca265e69660e74a2b569f2da` | `F235Driver/Pakon5.hex` | yes |
| `F235Driver/PknInit.hex` | 16344 | `490f7356751ad4dc0c2a4c8fb7a4781a2c23d3afff9f06b04422f5a6e615a432` | `F235Driver/PknInit.hex` | yes |
| `FX35Driver/F135usb2.sys` | 12928 | `03f3b5a1b0ceb13ba2d74154db893ac2de6f3e9a3620d0c9470fce823128a95e` | `FX35Driver/F135usb2.sys` | yes |
| `FX35Driver/F235Disk.tag` | 175 | `312f06b717a2764d19aba0e3ed9b0ba2557fe53d2b57b90ecb34dfc738b49245` | `FX35Driver/F235Disk.tag` | yes |
| `FX35Driver/F235Ldr.sys` | 16000 | `785bd29f37f8e49286be7a9b033e3741825952f5c293e2e143906504838ed2f1` | `FX35Driver/F235Ldr.sys` | yes |
| `FX35Driver/F235Lib.sys` | 16000 | `6cfba708fd8fd982331cf0f93ffb238a2b964c8aa6b020cb0a2f96cd42995059` | `FX35Driver/F235Lib.sys` | yes |
| `FX35Driver/F235usb2.inf` | 7559 | `da50b0469cfc5b79171d87f0b217f0572368b0b46d64c885c45e8082c727dbf6` | `FX35Driver/F235usb2.inf` | yes |
| `FX35Driver/F235usb2.sys` | 12928 | `8bc878aa0108206f72cd2ca987245e5a06eef82a675eed4f66cf252c7d2cd093` | `FX35Driver/F235usb2.sys` | yes |
| `FX35Driver/FX35usb2.sys` | 12928 | `5b49d574cc5375161725d39bf05f3ef1586a16a58953ff59abbabd9c2f3e5b3c` | `FX35Driver/FX35usb2.sys` | yes |
| `FX35Driver/Pakon5.hex` | 30180 | `6ea86ecf77e281cf0fbea0a94eea16ec9661bcc6ca265e69660e74a2b569f2da` | `FX35Driver/Pakon5.hex` | yes |
| `FX35Driver/Pakon7.hex` | 30213 | `edd840680ef7714c5d93b89c3def5ed6ba3085166bc8e0a6a15a0390bef3f2b4` | `FX35Driver/Pakon7.hex` | yes |
| `FX35Driver/Pakon8.hex` | 29914 | `1f21fb0809a432ab1b4c4cf566be609a2eee9c156017018e645a8088aab70a67` | `FX35Driver/Pakon8.hex` | yes |
| `FX35Driver/PknInit.hex` | 31323 | `e116ca855ccf45c608e892b25b9c9b5eb7ecf96640313082d082403b84edb8f3` | `FX35Driver/PknInit.hex` | yes |
