"""
Name        : __main__.py
Author      : David Carpenter
Date        : 2021-10-01
Description : A program to assist me in entering data into a database.
"""

import argparse
import csv
import pathlib
from typing import List

from exceptions import DataEntryHelperException
from instruct_module import instruct


def validate_path(path_as_string: str) -> pathlib.Path:
    """
    Ensures that the passed file name exists
    and is of the appropriate file type.
    """
    path = pathlib.Path(path_as_string)

    if not path.exists():
        raise DataEntryHelperException(f"the path {path_as_string} does not exist")

    if path.suffix != ".csv":
        raise DataEntryHelperException(f"the extension {path.suffix} is not supported")

    return path


def get_data(path: pathlib.Path) -> List[dict]:
    """
    Gets all data from the passed csv file
    and returns a list of all of the entries.
    """
    data = []
    with path.open() as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data.append(row)
    return data


def main() -> None:
    """
    Main method of the program.
    """
    parser = argparse.ArgumentParser(
        description="Step-by-step instructions on what data to enter into the database."
    )
    parser.add_argument("path", type=str, help="path to the csv file containing info")
    args = parser.parse_args()
    path_as_string: str = args.path

    try:
        path = validate_path(path_as_string)
        data = get_data(path)
        instruct(data)
    except DataEntryHelperException as ex:
        parser.error(ex)


if __name__ == "__main__":
    main()
