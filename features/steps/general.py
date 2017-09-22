from behave import *

from gilded_rose import GildedRose
from item import Item

use_step_matcher("re")


def get_sell_in_relative_day(relativeDay):
    if relativeDay == "yesterday":
        return -1
    if relativeDay == "today":
        return 0
    if relativeDay == "tomorrow":
        return 1


@given("an item with quality (?P<quality>.+) and sell by date (?P<relativeDay>.+)")
def step_impl(context, quality, relativeDay):
    """
    :type context: behave.runner.Context
    """
    sell_in = get_sell_in_relative_day(relativeDay)
    context.item = Item("some name", sell_in, int(quality))
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
    :type quality: str
    """
    assert_equals(context.item.quality, int(quality))


@step("the item has sell by date today")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert_equals(context.item.sell_in, 0)


def assert_equals(actual, expected):
    assert actual == expected, "Expected {} {}, was: {} {}"\
        .format(expected, type(expected), actual, type(actual))
