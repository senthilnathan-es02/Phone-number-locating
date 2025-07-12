import phonenumbers
from phonenumbers import geocoder, carrier, timezone
from datetime import datetime
import pytz

# ✅ Replace with any international phone number
number = phonenumbers.parse("+919025331238")

# ✅ Valid check
is_valid = phonenumbers.is_valid_number(number)git 

# ✅ Country Code
country_code = number.country_code

# ✅ National Number (without +country)
national_number = number.national_number

# ✅ Region / State
region = geocoder.description_for_number(number, "en")

# ✅ Timezone
time_zones = timezone.time_zones_for_number(number)

# ✅ Carrier / Network
network = carrier.name_for_number(number, "en")

# ✅ Output
print("Phone Number       :", number)
print("Is Valid Number?   :", is_valid)
print("Country Code       :", country_code)
print("National Number    :", national_number)
print("Region / State     :", region)
print("Carrier / Network  :", network)

# ✅ Timezone(s) and current local time(s)
for tz in time_zones:
    tz_obj = pytz.timezone(tz)
    local_time = datetime.now(tz_obj)
    print(f"Time Zone          : {tz}")
    print(f"Local Time         : {local_time.strftime('%Y-%m-%d %H:%M:%S')}")
