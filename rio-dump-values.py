#! /usr/bin/env python3

# install with sudo cp rio-dump-values.py /usr/bin/.

from collections import Counter
import numpy as np
import rasterio as rio
from sys import argv

_, filepath = argv

def pad(inpt, maxlen=5):
  string = str(inpt)
  length = len(string)
  padding = maxlen - length
  return string + " " * padding

with rio.open(filepath) as src:
    firstband = src.read().tolist()
    for bandid, band in enumerate(src.read()):
      print("\nband:", bandid)
      for rowid, row in enumerate(band):
        print("\n" + pad(rowid, 3) + ":", end=" ")
        rowtext = []
        for colid, cell in enumerate(row.tolist()):
          #print(str(bandid) + ":" + str(rowid) + ":" + str(colid) + " >> " + str(cell) + "\n")
          print(pad(cell, 10), end="")