from behave import *

from item import Item

use_step_matcher("re")


def get_sell_in_relative_day(relative_day):
    if relative_day == "yesterday":
        return -1
    if relative_day == "today":
        return 0
    if relative_day == "tomorrow":
        return 1


@given("an item with quality (?P<quality>.+) and sell by date (?P<relative_day>.+)")
def step_impl(context, quality, relative_day):
    """
    :type context: behave.runner.Context
    :type quality: str
    :type relative_day: str
    """
    sell_in = get_sell_in_relative_day(relative_day)
    context.item = Item("some name", sell_in, int(quality))
    context.gildedRose.inventory.items.append(context.item)
    pass


@given('an item of type "(?P<type_name>.+)" with quality (?P<quality>.+) and sell by date in the future')
def step_impl(context, type_name, quality):
    """
    :type context: behave.runner.Context
    :type type_name: str
    :type quality: str
    """
    context.item = Item(type_name, 15, int(quality))
    context.gildedRose.inventory.items.append(context.item)
    pass


@given("a backstage pass and quality (?P<quality>.+) and sell by date in (?P<days>.+) days")
def step_impl(context, quality, days):
    """
    :type context: behave.runner.Context
    :type quality: str
    :type days: str
    """
    context.item = Item("Backstage passes to a TAFKAL80ETC concert", int(days), int(quality))
    context.gildedRose.inventory.items.append(context.item)
    pass


@when("1 day passed")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.gildedRose.update_quality()
    pass


@then("the item has quality (?P<quality>\d*)")
def step_impl(context, quality):
    """
    :type context: behave.runner.Context
    :type quality: str
    """
    expected = int(quality)
    assert_equals(context.item.quality, expected)


@step("the item has sell by date today")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert_equals(context.item.sell_in, 0)


def assert_equals(actual, expected):
    assert actual == expected, "Expected {} {}, was: {} {}" \
        .format(expected, type(expected), actual, type(actual))
