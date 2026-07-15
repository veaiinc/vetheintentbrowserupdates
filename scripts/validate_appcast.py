#!/usr/bin/env python3
"""Validate mac/appcast.xml: well-formed, every enclosure signed + reachable,
newest version first. No third-party deps (stdlib only). Exit 1 on any problem."""
import sys, urllib.request, xml.etree.ElementTree as ET

PATH = "mac/appcast.xml"
SPARKLE = "http://www.andymatuschak.org/xml-namespaces/sparkle"


def vtuple(v):
    out = []
    for part in v.split("."):
        try:
            out.append(int(part))
        except ValueError:
            out.append(0)
    return tuple(out)


def main():
    errors, warnings = [], []
    try:
        tree = ET.parse(PATH)
    except Exception as e:
        print(f"::error::appcast is not well-formed XML: {e}")
        return 1

    items = tree.getroot().findall(".//item")
    if not items:
        print("::error::appcast has no <item> entries")
        return 1

    versions = []
    for it in items:
        ver_el = it.find(f"{{{SPARKLE}}}version")
        title = (it.findtext("title") or "?").strip()
        ver = (ver_el.text or "").strip() if ver_el is not None else ""
        if not ver:
            errors.append(f"[{title}] missing <sparkle:version>")
        else:
            versions.append(vtuple(ver))

        enc = it.find("enclosure")
        if enc is None:
            errors.append(f"[{title}] missing <enclosure>")
            continue
        url = enc.get("url", "")
        sig = enc.get(f"{{{SPARKLE}}}edSignature", "")
        length = enc.get("length", "")
        if not sig:
            errors.append(f"[{title}] enclosure has NO sparkle:edSignature — Sparkle would REJECT this update")
        if not length or not length.isdigit() or int(length) <= 0:
            errors.append(f"[{title}] enclosure length missing/invalid ('{length}')")
        if not url.startswith("https://"):
            errors.append(f"[{title}] enclosure url is not https ('{url}')")
        else:
            try:
                req = urllib.request.Request(url, method="HEAD")
                with urllib.request.urlopen(req, timeout=30) as r:
                    if r.status not in (200, 302):
                        errors.append(f"[{title}] enclosure URL returned HTTP {r.status}: {url}")
            except Exception as e:
                errors.append(f"[{title}] enclosure URL not reachable ({e}): {url}")

    if versions and versions[0] != max(versions):
        warnings.append(f"newest version is not the FIRST item — check publish order")

    for w in warnings:
        print(f"::warning::{w}")
    for e in errors:
        print(f"::error::{e}")
    if errors:
        print(f"\nFAILED: {len(errors)} problem(s) in {PATH}")
        return 1
    print(f"OK: {len(items)} item(s) validated; all enclosures signed + reachable.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
