from gilded_rose import GildedRose


def before_scenario(context, scenario):
    context.gildedRose = GildedRose()
    context.gildedRose.inventory.items = []
