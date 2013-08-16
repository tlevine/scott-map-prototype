#!/bin/sh

# This skips parishes without impacts.
sqlite3 -header -csv applications.db << EOF
SELECT "parish", sum("acreage") AS 'acreage'
FROM application
WHERE "type" = 'impact'
GROUP BY "parish";
EOF
