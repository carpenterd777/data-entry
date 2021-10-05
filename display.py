"""
Functions just for displaying output
in a nice way.
"""

from typing import List
import json

import click
from rich import print_json, print

from input_function import wait_for_input
from commondata import CommonData


def page_through(data: List[dict]) -> None:
    """
    Print out each entry, one at a time, waiting for input before printing
    the next entry.
    """
    click.clear()
    for index in range(len(data)):
        _page_one(CommonData(data[index]), len(data) - index - 1)


def _page_one(data: CommonData, remaining: int) -> None:
    """
    Print out one entry.
    """

    # TODO: this should be a method of CommonData
    print("Current entry:\n")
    print(f"Remaining: [red]{remaining}[/red]")
    print_json(json.dumps(data.data))
    wait_for_input()
