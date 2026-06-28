# Sparkle (macOS auto-update) — keys & signing

The Ve Browser has its **own** Sparkle EdDSA keypair, separate from the macOS menu-bar app.

## Public key (goes in the browser's Info.plist)
```
SUPublicEDKey = KXXaKE01leso861qSIPazlkAh4RdJNvbDBLoJuyCxRQ=
SUFeedURL     = https://veaiinc.github.io/vetheintentbrowserupdates/appcast.xml
```
(Public key is safe to ship — it only *verifies* signatures.)

## Private key (NEVER in git)
Lives only on the release machine at `~/Desktop/Vetheintentbrowser/.secrets/sparkle_ed_private.key`
(chmod 600, gitignored). It *signs* each DMG. If it leaks, anyone can push malicious updates.

## Signing a release (in scripts/publish-release.sh)
```
sign_update "Ve-<version>.dmg" --ed-key-file ~/Desktop/Vetheintentbrowser/.secrets/sparkle_ed_private.key
# → prints  sparkle:edSignature="…"  length="…"  → paste into the appcast <enclosure>
```
`sign_update` ships with Sparkle (e.g. the macOS app's
`Configuration/sparkle/` or Sparkle's SwiftPM checkout `bin/sign_update`).

## Windows (WinSparkle) uses its OWN keypair — generate separately when wiring task #19.
