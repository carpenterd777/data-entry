"""
Module containing all of the functions relating to instruction
of the user on entering a data entry.
"""

import json
from typing import List

import click
from rich import print_json
from rich.console import Console

from commondata import CommonData, CommonFieldNames
from input_function import wait_for_input, wait_for_confirmation


def printt(*values, style=None, end="\n") -> None:
    """
    Shortcut to use styled rich print.
    """
    console = Console()
    console.print(*values, style=style, end=end)


def instruct(data: List[dict]) -> None:
    """
    Print out step-by-step instructions on
    how to enter every entry into the
    database program. Displays one entry
    at a time, pausing and allowing the user to continue when ready.

    Begins by clearing the terminal.
    """
    click.clear()
    printt("Get ready by going to Records > New Individual\n")
    for entry in data:
        _instruct_one(CommonData(entry))


def _instruct_one(data: CommonData) -> None:
    """
    Print out step-by-step instructions on
    how to enter this entry into the database
    program.

    Displays one step at a time, pausing and allowing
    the user to continue when ready.
    """

    printt("Current entry:\n")
    print_json(json.dumps(data.data))
    wait_for_input()
    _last_name_instruct(data)
    _first_name_instruct(data)
    _email_address_instruct(data)
    _phone_number_instruct(data)
    _address_instruct(data)
    _bio2_instruct()
    _addressee_and_salutation_instruct()
    _relationships_instruct(data)


def _last_name_instruct(data: CommonData) -> None:
    if data.has_field_like(CommonFieldNames.LAST_NAME):
        printt("Put ", end="")
        printt(
            data.get_field_like(CommonFieldNames.LAST_NAME), style="bold blue", end=""
        )
        printt(' in the blue "Last name" box under Biographical')
        wait_for_input()


def _first_name_instruct(data: CommonData) -> None:
    if data.has_field_like(CommonFieldNames.FIRST_NAME):
        printt("Put ", end="")
        printt(
            data.get_field_like(CommonFieldNames.FIRST_NAME), style="bold blue", end=""
        )
        printt(' in the blue "First name" box under Biographical')
        wait_for_input()

        printt('Add a title in the "Titles" box\n')
        printt("First name was: ", end="")
        printt(
            data.get_field_like(CommonFieldNames.FIRST_NAME), style="bold blue", end=""
        )
        wait_for_input()

        printt(
            'Add a nickname in the "Nickname" box that is the same as their first name\n'
        )
        printt("First name was: ", end="")
        printt(
            data.get_field_like(CommonFieldNames.FIRST_NAME), style="bold blue", end=""
        )
        wait_for_input()

        printt("Add their gender\n")
        printt("First name was: ", end="")
        printt(
            data.get_field_like(CommonFieldNames.FIRST_NAME), style="bold blue", end=""
        )
        wait_for_input()


def _email_address_instruct(data: CommonData) -> None:
    if data.has_field_like(CommonFieldNames.EMAIL_ADDRESS):
        directions = """
        Switch to the tab on the right called email addresses.
        Add a new type called "Email" and in the address field put the address.
        Mark this email as Primary.
        """
        printt(fix_multiline(directions) + "\n")
        printt("Email address: ", end="")
        printt(
            data.get_field_like(CommonFieldNames.EMAIL_ADDRESS),
            style="bold blue",
            end="",
        )
        wait_for_input()


def _phone_number_instruct(data: CommonData) -> None:
    if data.has_field_like(CommonFieldNames.MAIN_NUMBER) or data.has_field_like(
        CommonFieldNames.CELL_NUMBER
    ):
        main_number = data.get_field_like(CommonFieldNames.MAIN_NUMBER)
        cell_number = data.get_field_like(CommonFieldNames.CELL_NUMBER)

        directions = """
        Switch to the tab "Telephone number".
        Add a new type called "Mobile" and in the "Number" field put the mobile number below.
        Mark the number as primary.
        """

        if main_number == cell_number:
            printt(fix_multiline(directions) + "\n")
            printt("Phone number: ", end="")
            printt(main_number, style="bold blue")
        elif cell_number == "":
            directions = """
            Switch to the tab "Telephone number".Add a new type called "Phone" and in the "Number" field put the main number below.
            Add a new type called "Phone" and in the "Number" field put the mobile number below.
            Mark the number as primary.
            """
            printt(fix_multiline(directions) + "\n")
            printt("Phone number: ", end="")
            printt(main_number, style="bold blue")
        elif main_number == "":
            printt(fix_multiline(directions) + "\n")
            printt("Phone number: ", end="")
            printt(cell_number, style="bold blue")
        else:
            directions = """
            Switch to the tab "Telephone number".
            Add a new type called "Phone" and in the "Number" field put the main number below.
            Add a new type called "Mobile" and in the "Number" field put the cell number below.
            Mark the mobile number as primary.
            """
            printt(fix_multiline(directions) + "\n")
            printt("Main number: ", end="")
            printt(main_number + "\n", style="bold blue")
            printt("Cell number: ", end="")
            printt(cell_number + "\n", style="bold blue")

        wait_for_input()


def _address_instruct(data: CommonData) -> None:
    if data.has_field_like(CommonFieldNames.ADDRESS):
        directions = """
        Go to the top right section labeled "Preferred Address : Home.
        Add the following to the box labeled "Address lines":\n
        """
        printt(fix_multiline(directions))
        printt(
            "Address: " + data.get_field_like(CommonFieldNames.ADDRESS) + "\n",
            style="bold blue",
        )
        wait_for_input()
    else:
        directions = """
        Click "no valid address" in the bottom right corner.
        """
        printt(fix_multiline(directions))
        wait_for_input()

    address_accelerated = False
    if data.has_field_like(CommonFieldNames.CITY):
        directions = """
        Go to the top right section labeled "Preferred Address : Home.
        Add the following to the box labeled "City":\n
        """
        printt(fix_multiline(directions))
        printt("City: " + data.get_field_like(CommonFieldNames.CITY), style="bold blue")
        directions = """
        After this, go to the bar at the top and click the mail icon.
        This is the address accelerator - if this works the other address fields will not
        need to be filled out.

        Enter Y if the address was accelerated, otherwise enter any other key.
        """
        printt(fix_multiline(directions))
        address_accelerated = wait_for_confirmation()

    if not address_accelerated:
        if data.has_field_like(CommonFieldNames.STATE):
            directions = """
            Go to the top right section labeled "Preferred Address : Home.
            Add the following to the box labeled "State":\n
            """
            printt(fix_multiline(directions))
            printt(
                "State: " + data.get_field_like(CommonFieldNames.CITY),
                style="bold blue",
            )
            wait_for_input()

        if data.has_field_like(CommonFieldNames.ZIP):
            directions = """
            Go to the top right section labeled "Preferred Address : Home.
            Add the following to the box labeled "Zip Code":\n
            """
            printt(fix_multiline(directions))
            printt(
                "State: " + data.get_field_like(CommonFieldNames.ZIP), style="bold blue"
            )
            wait_for_input()


def _bio2_instruct() -> None:
    directions = """
    Move to the tab "Bio2". At the "Constituent Codes" table at the
    bottom, under the column "Description", enter "Parent" in a new row.
    """
    printt(fix_multiline(directions))
    wait_for_input()


def _addressee_and_salutation_instruct() -> None:
    directions = """
    Move to the tab "Addressee and Salutations". At the "Primary Addressee" box
    pick the first option provided from the drop-down. At the "Primary Salutation" box
    pick the fifth option provided from the drop-down.
    """
    printt(fix_multiline(directions))
    wait_for_input()


def _relationships_instruct(data: CommonData) -> None:
    directions = """
    Move to the tab "Relationships". Click the "Individuals" button in the column on 
    the left. Above that, click "New Individual Relationship". In the dialog box that
    appears, find the field labeled "Last Name". Next to this field is button with a binoculars
    icon, click this. This will open a dialog box to match students to their parents. Enter the last
    name of the parent.
    
    Students will only be matches as a child of a parent if both their last name and address
    match the parent.
    
    Only double click on a match to link the student if the above criteria are met.\n
    """
    printt(fix_multiline(directions))
    printt("Last Name: ", end="")
    printt(data.get_field_like(CommonFieldNames.LAST_NAME), style="bold blue")
    printt("Address: ", end="")
    printt(data.get_field_like(CommonFieldNames.ADDRESS), style="bold blue", end=", ")
    printt(data.get_field_like(CommonFieldNames.CITY), style="bold blue", end=", ")
    printt(data.get_field_like(CommonFieldNames.STATE), style="bold blue", end=", ")
    printt(data.get_field_like(CommonFieldNames.ZIP), style="bold blue")

    wait_for_input()


def fix_multiline(old: str) -> str:
    """
    Get rid of excess tabs (4 spaces) in
    multiline strings.
    """
    new = old.split(" ")
    new = " ".join(filter(lambda x: x != "", new))
    return new
