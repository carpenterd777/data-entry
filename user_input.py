"""
Functions that handle user input.
"""
import click


def wait_for_input() -> None:
    """
    Prints a prompt stating that the program
    is waiting for Enter to be pressed
    and halts the program. Clears the screen after
    it is pressed.
    """

    input("\nPress Enter to continue")
    click.clear()


def wait_for_confirmation() -> bool:
    """
    Returns True if the user entered Y. If the
    user entered anything else, returns False.
    """

    response = input()
    click.clear()
    return response in ["Y", "y", "yes"]
