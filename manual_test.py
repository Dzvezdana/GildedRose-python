# -*- coding: utf-8 -*-
from __future__ import print_function

from gilded_rose import *

if __name__ == "__main__":
    print("OMGHAI!")
    inventory = Inventory()

    days = 2
    import sys

    if len(sys.argv) > 1:
        days = int(sys.argv[1]) + 1
    for day in range(days):
        print("-------- day %s --------" % day)
        print("name, sellIn, quality")
        for item in inventory.items:
            print(item)
        print("")
        GildedRose().update_quality()
