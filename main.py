# first install the dependencies needed:
# pip install phonenumbers

import phonenumbers as pn
from number import number_one, number_two, number_three
from phonenumbers import carrier

from phonenumbers import geocoder, timezone

number = number_one

# C for country and H for history
parsed_number = pn.parse(number, "CH")

# en for english
print(geocoder.description_for_number(parsed_number, "en"))

zone_number = pn.parse(number, "GB")
print(timezone.time_zones_for_number(zone_number))

# check to see if the number entered was even valid or not
# returns a bool
valid_check = pn.is_valid_number(parsed_number)
print(f"Number valid: {valid_check}")