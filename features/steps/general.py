from behave import *

from gilded_rose import GildedRose
from item import Item

use_step_matcher("re")


@given("an item with quality (?P<quality>.+) and sell by date tomorrow")
def step_impl(context, quality):
    """
    :type context: behave.runner.Context
    """
    context.item = Item("some name", 1, int(quality))
    context.gildedRose = GildedRose()
    context.gildedRose.inventory.items.append(context.item)
    pass


@when("1 day passed")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.gildedRose.update_quality()
    pass


@then("the item has quality (?P<quality>.+)")
def step_impl(context, quality):
    """
    :type context: behave.runner.Context
    """
    assert context.item.quality == int(quality)


@step("the item has sell by date today")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert context.item.sell_in == 0, "Sell in days expected 0, was: %r" % context.item.sell_in
