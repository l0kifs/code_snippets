# Convert local datetime date to the ISO8601+TimeZone date string
import datetime
import time

date = datetime.datetime.now()
utc_offset_sec = time.altzone if time.localtime().tm_isdst else time.timezone
utc_offset = datetime.timedelta(seconds=-utc_offset_sec)
iso_date_str = date.replace(tzinfo=datetime.timezone(offset=utc_offset)).isoformat()


# Revers conversion
import dateutil.parser

datetime_date = dateutil.parser.parse(iso_date_str)