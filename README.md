# Kraken AD&D 2E Sidebar by Default

A tiny Fantasy Grounds Unity extension for the **AD&D 2E** ruleset: new players start with the standard **sidebar** like every other ruleset, instead of the old-school **Menus / Records / Books** bar across the top.

## What it does

The 2E ruleset ships with **Options → Menu Style** set to **Menus** by default, so everyone who hasn't changed it gets the top bar. This extension changes only the **default** of that option to **Sidebar**:

- Players who never touched the option get the sidebar automatically.
- Anyone who picks **Menus** in Options keeps it. The choice is per user and is never overwritten.
- Nothing else changes, and no campaign data is touched.

## Install

1. Download `KrakenADD2ESidebar.ext` from the latest [**Release**](../../releases/latest).
2. Put it in your Fantasy Grounds data folder under `extensions\` (usually `%appdata%\SmiteWorks\Fantasy Grounds\extensions`).
3. On the FGU load screen, select your AD&D 2E campaign, click **Extensions**, and enable **Kraken AD&D 2E Sidebar by Default**.

Players don't need to install anything. They get the extension from the host when they connect.

### Requirements
- Fantasy Grounds Unity
- The AD&D 2E ruleset

## Release

`python release.py` builds `KrakenADD2ESidebar.ext` and publishes a GitHub Release with it attached (the tag is `v` plus the version in `extension.xml`). It needs Python 3 and an authenticated GitHub CLI (`gh`).

## See also

[Kraken AD&D 2E Character Wizard](https://github.com/krakenunbound/kraken-adnd-2e-charwizard), a guided 2E character-creation wizard for FGU.
