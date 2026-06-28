#!/usr/bin/env bash
# Ve — The Intent Browser · clean-room release publisher  (SCAFFOLD — WIP)
#
# Pipeline (filled in once the Chromium build + DMG packaging land, tasks #16/#18):
#   1. build      : autoninja -C out/Release chrome   (from the Chromium source tree)
#   2. assemble   : produce "Ve - The Intent Browser.app" with VE branding + app.icns
#   3. codesign   : Developer ID Application (release machine identity)
#   4. notarize   : xcrun notarytool submit --wait  +  xcrun stapler staple
#   5. dmg        : build Ve-<version>.dmg
#   6. sparkle    : sign_update Ve-<version>.dmg  ->  EdDSA signature + length
#   7. publish    : gh release create v<version> Ve-<version>.dmg  (this repo)
#   8. appcast    : append <item> to appcast.xml, commit + push
#
# Usage (planned):  ./scripts/publish-release.sh <version> <build-number>
set -euo pipefail
echo "publish-release.sh is a scaffold — pipeline implemented in tasks #16/#18 after the build exists."
exit 0
