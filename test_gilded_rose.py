# -*- coding: utf-8 -*-
import unittest

from gilded_rose import GildedRose
from item import Item

SOME_ITEM_NAME = "some-item-name"


class GildedRoseTest(unittest.TestCase):

    def test_example(self):
        items = [Item(SOME_ITEM_NAME, 0, 0)]
        gilded_rose = GildedRose()
        gilded_rose.update_quality()
        self.assertEqual(SOME_ITEM_NAME, items[0].name)

    def test_when_sell_by_date_has_passed_quality_degrades_twice_as_fast(self):
        self.assertEqual(True, False)

    def test_the_quality_is_never_negative(self):
        self.assertEqual(True, False)

    def test_aged_bries_increases_in_quality_as_it_gets_older(self):
        self.assertEqual(True, False)

    def test_quality_never_reaches_more_than_50(self):
        self.assertEqual(True, False)

    def test_sulfuras_legendary_item_never_has_to_be_sold(self):
        self.assertEqual(True, False)

    def test_backstage_passes_increases_in_quality(self):
        self.assertEqual(True, False)

    def test_backstage_passes_increases_by_2_in_quality_when_10_days_or_less(self):
        self.assertEqual(True, False)

    def test_backstage_passes_increases_by_3_in_quality_when_5_days_or_less(self):
        self.assertEqual(True, False)

    def test_backstage_passes_quality_drops_to_0_after_the_concert(self):
        self.assertEqual(True, False)

    # New requirement

    def test_conjured_degrades_twice_as_fast_as_normal_items(self):
        self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()
