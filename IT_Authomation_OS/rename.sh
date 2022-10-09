#!/bin/bash
#moving files with .HTM extentinon to .html
# to test safely put echo before mv and see prints out of command
for file in *.HTM; do
    name=$(basname '$file' .HTM)
    mv "$file" "$name.html"
done