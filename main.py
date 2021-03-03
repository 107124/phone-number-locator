import phonenumbers as pn
from number import number
from phonenumbers import carrier

from phonenumbers import geocoder, timezone


# C for country and H for history
check_number = pn.parse(number, "CH")

# en for english
print(geocoder.description_for_number(check_number, "en"))

zone_number = pn.parse(number, "GB")
print(timezone.time_zones_for_number(zone_number))

valid_check = pn.is_valid_number(check_number)
print(valid_check)