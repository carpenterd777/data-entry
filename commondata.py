"""
Class that makes a dict of
people data more accessible to generic field
names.
"""

from typing import List

class CommonFieldNames:
    LAST_NAME = "last name"
    FIRST_NAME = "first name"

class CommonData:
    """
    Class that makes a dict of
    people data more accessible to generic field
    names.
    """

    _last_name_field_names = [CommonFieldNames.LAST_NAME, "Last Name :: General"]
    _first_name_field_names = [CommonFieldNames.FIRST_NAME, "First Name :: General"]

    def __init__(self, data : dict) -> None:
        self.data = data

    def has_field_like(self, field: str) -> bool:
        """
        Returns True if data has a field
        that is close to the passed argument
        *field* for the purposes of data entry.
        """

        for field_name in self._get_field_name_list(field):
            if field_name in self.data:
                return True

    def get_field_like(self, field: str) -> str:
        """
        Returns the field that the data has
        that is close the passed argument
        *field* for the purposes of data entry.
        """
        for field_name in self._get_field_name_list(field):
            if field_name in self.data:
                return self.data[field_name]

    def _get_field_name_list(self, field: str) -> List[str]:
        # find the array where the given field is entry 0
        all_predicted_fields = [self._last_name_field_names, self._first_name_field_names]

        predicted_fields = None
        for fields in all_predicted_fields:
            if fields[0] == field:
                predicted_fields = fields

        if predicted_fields == None:
            raise Exception("got field name that is not yet handled by CommonData")

        return predicted_fields

