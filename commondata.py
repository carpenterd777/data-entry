"""
Class that makes a dict of
people data more accessible to generic field
names.
"""

import json
from typing import List

import rich

class CommonFieldNames:
    """
    A collection of field names that are
    common and generalized for multiple documents
    in the data entry that I plan to do.
    """

    LAST_NAME = "last name"
    FIRST_NAME = "first name"
    EMAIL_ADDRESS = "email address"
    MAIN_NUMBER = "main number"
    CELL_NUMBER = "cell number"
    ADDRESS = "address"
    CITY = "city"
    STATE = "state"
    ZIP = "zip"


class CommonData:
    """
    Class that makes a dict of
    people data more accessible to generic field
    names.
    """

    _last_name_field_names = [CommonFieldNames.LAST_NAME, "Last Name :: General"]
    _first_name_field_names = [
        CommonFieldNames.FIRST_NAME,
        "First Name :: General",
        "\ufeffFirst Name :: General",
    ]
    _email_address_field_names = [
        CommonFieldNames.EMAIL_ADDRESS,
        "Email Address :: General",
    ]
    _main_number_field_names = [
        CommonFieldNames.MAIN_NUMBER,
        "Main Contact Number :: General",
    ]
    _cell_number_field_names = [
        CommonFieldNames.CELL_NUMBER,
        "Cell Phone Number :: General",
    ]

    _address_field_names = [CommonFieldNames.ADDRESS, "Address1 :: General"]

    _city_field_names = [CommonFieldNames.CITY, "City :: General"]

    _state_field_names = [CommonFieldNames.STATE, "State :: General"]

    _zip_field_names = [CommonFieldNames.ZIP, "Zip :: General"]

    def __init__(self, data: dict) -> None:
        self.data = data

    def __repr__(self) -> str:
        return json.dumps(self.data)

    def __str__(self) -> str:
        return self.__repr__()

    def has_field_like(self, field: str) -> bool:
        """
        Returns True if data has a field
        that is close to the passed argument
        *field* for the purposes of data entry.
        """

        for field_name in self._get_field_name_list(field):
            if field_name in self.data:
                return True

        return False

    def get_field_like(self, field: str) -> str:
        """
        Returns the field that the data has
        that is close the passed argument
        *field* for the purposes of data entry.
        """
        for field_name in self._get_field_name_list(field):
            if field_name in self.data:
                return self.data[field_name]

        raise Exception("got field name that is not yet handled by CommonData")

    def _get_field_name_list(self, field: str) -> List[str]:
        # find the array where the given field is entry 0
        all_predicted_fields = [
            self._last_name_field_names,
            self._first_name_field_names,
            self._email_address_field_names,
            self._main_number_field_names,
            self._cell_number_field_names,
            self._address_field_names,
            self._city_field_names,
            self._zip_field_names,
            self._state_field_names,
        ]

        predicted_fields = None
        for fields in all_predicted_fields:
            if fields[0] == field:
                predicted_fields = fields

        if predicted_fields is None:
            raise Exception("got field name that is not yet handled by CommonData")

        return predicted_fields

    def print(self) -> None:
        """
        Nicely prints this data.
        """
        rich.print_json(str(self))
