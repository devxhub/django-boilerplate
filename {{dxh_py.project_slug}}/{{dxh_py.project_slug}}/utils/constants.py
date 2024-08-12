from django.utils.translation import gettext_lazy as _
from django.conf import settings
import json
import os

TIME_FORMAT_CHOICES = [
    ('HH:MM AM/PM', 'HH:MM AM/PM (e.g., 08:15 PM)'),
    ('HH:MM', 'HH:MM (24-hour format, e.g., 20:15)'),
]

DATE_FORMAT_CHOICES = [
    ('MM/DD/YYYY', 'MM/DD/YYYY (e.g., 04/03/2024)'),
    ('DD.MM.YYYY', 'DD.MM.YYYY (e.g., 03.04.2024)'),
    ('DD/MM/YYYY', 'DD/MM/YYYY (e.g., 03/04/2024)'),
    ('MMM/DD/YYYY', 'MMM/DD/YYYY (e.g., Apr/03/2024)'),
    ('DD.MMM.YYYY', 'DD.MMM.YYYY (e.g., 03.Apr.2024)'),
    ('DD/MMM/YYYY', 'DD/MMM/YYYY (e.g., 03/Apr/2024)')
]

timezones_file_path = os.path.join(settings.BASE_DIR, '{{ dxh_py.project_slug }}', 'assets', 'timezones.json')
with open(timezones_file_path, 'r') as file:
    timezones_data = json.load(file)

TIMEZONES = [(tz["utc"][0], tz["text"])
             for tz in timezones_data if tz.get("utc")]

currencies_file_path = os.path.join(settings.BASE_DIR, '{{ dxh_py.project_slug }}', 'assets', 'countries.json')
with open(currencies_file_path, 'r') as file:
    currencies_data = json.load(file)

CURRENCY_CHOICES = []
for country_code, country_info in currencies_data.items():
    currencies = country_info.get("currency", [])
    country_name = country_info.get("name", "")
    for currency_code in currencies:
        CURRENCY_CHOICES.append((currency_code, f"{currency_code} - {country_name}"))
