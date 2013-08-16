#!/usr/bin/env python
import json
from dumptruck import DumpTruck
dt = DumpTruck(dbname = 'applications.db')

def scott_data():
    sql = '''
    SELECT "parish", sum("acreage") AS 'acreage'
    FROM application
    WHERE "type" = 'impact' AND "parish" != ''
    GROUP BY "parish";
    '''

    return {row['parish'].upper().replace('SAINT', 'ST'): row['acreage'] for row in dt.execute(sql)}

scott = scott_data()
parishes = json.load(open('parishes.json'))

max_impacted_acres = max(scott.values())
for feature in parishes['features']:
    feature['properties']['impacted_acres'] = scott.get(feature['properties']['COUNTY'], 0)
    feature['properties']['impacted_acres_prop_max'] = scott.get(feature['properties']['COUNTY'], 0) / max_impacted_acres

json.dump(parishes, open('impacts.json', 'w'))
