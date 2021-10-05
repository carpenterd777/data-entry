"""
Functions just for displaying output
in a nice way.
"""

from typing import List
import json

import click
import rich

from user_input import wait_for_input
from commondata import CommonData


def page_through(data: List[dict]) -> None:
    """
    Print out each entry, one at a time, waiting for input before printing
    the next entry.
    """
    click.clear()
    for index, _ in enumerate(data):
        _page_one(CommonData(data[index]), len(data) - index - 1)


def _page_one(data: CommonData, remaining: int) -> None:
    """
    Print out one entry.
    """

    rich.print("Current entry:\n")
    rich.print(f"Remaining: [red]{remaining}[/red]")
    rich.print_json(json.dumps(data.data))
    wait_for_input()
