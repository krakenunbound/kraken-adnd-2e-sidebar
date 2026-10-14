#!/usr/bin/env python3
"""Build KrakenADD2ESidebar.ext and publish it as a GitHub Release.

Usage:
    python release.py               # tag = "v" + version from extension.xml
    python release.py v1.1          # explicit tag
    python release.py --build-only  # build the .ext, no release

Requires: Python 3 and, to publish, the GitHub CLI (`gh`) authenticated.
"""
import os, sys, subprocess, zipfile
import xml.etree.ElementTree as ET

REPO = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(REPO, "build", "KrakenADD2ESidebar.ext")
FILES = ["extension.xml", "scripts/sidebar_default.lua"]


def version():
    r = ET.parse(os.path.join(REPO, "extension.xml")).getroot()
    return r.findtext("properties/version") or "0.0"


def main():
    args = list(sys.argv[1:])
    build_only = "--build-only" in args
    if build_only:
        args.remove("--build-only")
    tag = args[0] if args else "v" + version()
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with zipfile.ZipFile(OUT, "w", zipfile.ZIP_DEFLATED) as z:
        for f in FILES:
            z.write(os.path.join(REPO, f), f)
    print(f"[build] {os.path.basename(OUT)}")
    if build_only:
        return
    title = f"Kraken AD&D 2E Sidebar by Default {tag}"
    notes = ("Install: KrakenADD2ESidebar.ext -> Fantasy Grounds \\extensions\\, then enable it in your "
             "AD&D 2E campaign. New players start with the sidebar instead of the top Menus bar.")
    exists = subprocess.run(["gh", "release", "view", tag], cwd=REPO,
                            stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL).returncode == 0
    if exists:
        subprocess.run(["gh", "release", "upload", tag, OUT, "--clobber"], cwd=REPO, check=True)
    else:
        subprocess.run(["gh", "release", "create", tag, OUT, "--title", title, "--notes", notes],
                       cwd=REPO, check=True)
    print("[done]", tag)


if __name__ == "__main__":
    main()
