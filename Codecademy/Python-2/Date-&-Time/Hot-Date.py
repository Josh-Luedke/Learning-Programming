# You can use the standalone % operator for a stand in for variables.

from datetime import datetime
now = datetime.now()

print '%02d/%02d/%04d' % (now.month, now.day, now.year)