#Log Duration (Time Zones) (екі уакыт арасындағы секундты есептейді)
import sys
from datetime import datetime, timedelta, timezone

def chtoto(n):
    time_part, tz_part, tz_offset = n.strip().split()
    y, m, d = map(int, time_part.split('-'))
    hh, mm, ss = map(int, tz_part.split(':'))
    sign = 1 if tz_offset[3] == '+' else -1
    tz_h, tz_m = int(tz_offset[4:6]), int(tz_offset[7:9])
    tz = timezone(sign * timedelta(hours=tz_h, minutes=tz_m))
    dt = datetime(y, m, d, hh, mm, ss, tzinfo=tz)
    return dt.astimezone(timezone.utc)

start_utc = chtoto(sys.stdin.readline())
end_utc = chtoto(sys.stdin.readline())

duration = int((end_utc - start_utc).total_seconds())
print(duration)