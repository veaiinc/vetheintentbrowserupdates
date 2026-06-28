# Ve — The Intent Browser · Update Feed

Public release feed for **Ve - The Intent Browser** (macOS). Installed browsers poll the
Sparkle **appcast** here to auto-update.

> Brand-new, clean-room project built on pristine open-source **Chromium (BSD-3-Clause)** —
> no AGPL code. This repo hosts only our own signed release artifacts and the appcast.

## Download

Latest DMG:
```
https://github.com/veaiinc/vetheintentbrowserupdates/releases/latest
```

## Auto-update

The browser checks [`appcast.xml`](./appcast.xml) (Sparkle 2 EdDSA-signed). Each release:
1. Build → codesign (Developer ID) → notarize + staple → DMG
2. Sign the DMG with the Sparkle EdDSA key (release machine)
3. Upload DMG to a GitHub Release + append an `<item>` to `appcast.xml`

## Layout
```
appcast.xml      # Sparkle feed (one <item> per release)
releases/        # release notes (html/md) per version
scripts/         # clean-room publish pipeline (build→sign→notarize→publish)
```

© Ve. All rights reserved. Artifacts here are proprietary VE builds.
