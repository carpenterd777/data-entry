"""
Functions just for displaying output
in a nice way.
"""

from typing import List

import click
import rich

from user_input import wait_for_input
from commondata import CommonData
from exceptions import DataEntryHelperException


def page_through(data: List[dict], start: int = 0) -> None:
    """
    Print out each entry, one at a time, waiting for input before printing
    the next entry.
    """
    if start > len(data):
        raise DataEntryHelperException(
            f"cannot start at index {start} for list size {len(data)}"
        )
    if start < 0:
        raise DataEntryHelperException(
            f"cannot start at negative index {start}"
        )
    click.clear()
    for i in range(start, len(data)):
        _page_one(CommonData(data[i]), len(data) - i)


def _page_one(data: CommonData, remaining: int) -> None:
    """
    Print out one entry.
    """

    rich.print(f"Remaining: [red]{remaining}[/red]")
    data.print()
    wait_for_input()
