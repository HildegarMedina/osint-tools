import re
import phonenumbers
from phonenumbers import geocoder, carrier, timezone

class PhoneGeolocation:

    def get_details(self, phone_number, lang='en'):
        """Get Phone geolocation."""
        number = phonenumbers.parse(phone_number)
        timezone_phone = timezone.time_zones_for_number(number)
        description = geocoder.description_for_number(number, lang)
        country = geocoder.country_name_for_number(number, lang)
        operator = carrier.name_for_number(number, lang)
        location_parts = description.split(", ")
        city = location_parts[0] if len(location_parts) > 0 else None
        state = location_parts[1] if len(location_parts) > 1 else None

        return {
            "number": phonenumbers.format_number(number, phonenumbers.PhoneNumberFormat.INTERNATIONAL),
            "data": {
                "Region": state or city,
                "Operator": operator,
                "Timezone": re.search(r"'(.*?)'", str(timezone_phone)).group(1),
                "Country": country,
                "City": city if state else None
            }
        }
