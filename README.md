# Overview

A tool to help with running Pathfinder 2e Society Games, including Bounties, Quests, and Season scenarios. Multi-Import available to import multiple PDFs at a time, but requires signed PDFs with Paizo's header information intact to function.

If no PDFs have been extracted there will be no other buttons available. Seasons with no module implemented yet will be grayed out, as will any imported scenarios that have yet to be implemented.


The importer will pull the images and text from the PDF and store them in a bin folder that is generated with its own file structure.

# Development

## Pre-requisite

* python 3.13 built with Tkinter enabled

## Setup

1. [Install](https://docs.astral.sh/uv/getting-started/installation/) uv
2. Create a [fork of this repository](https://github.com/Wolfie192/DMs-Halfling/fork)
3. Clone your fork locally where you plan to develop
4. `cd DMs-Halfling`
5. `uv run main.py` to validate the app is in working order
