# OsmTileMerger

A simple tool to merge multiple Openstreetmap tiles into a single PNG image.

Requirements:
Python 3 + requests + matplotlib + numpy

## How to use
1. Determine the required zoom level (for example, if URL is https://www.openstreetmap.org/#map=13/55.7217/37.5140 then zoom level is 13)
2. Determine the top-left and bottom-right tile numbers for you area (e.g. open Network tab in the browser console, refresh the Openstreetmap page and see which tiles are loading)
3. Launch the script.   
It will download the tiles (saving them as temporary file), then merge them into a single result and save as PNG.
