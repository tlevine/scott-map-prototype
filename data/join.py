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

    return {row['parish'].upper().replace('SAINT', 'ST'): (row['parish'], row['acreage']) for row in dt.execute(sql)}

scott = scott_data()
parishes = json.load(open('parishes.json'))

max_impacted_acres = max([v[1] for v in scott.values()])
for feature in parishes['features']:
    feature['properties']['impacted_acres'] = scott.get(feature['properties']['COUNTY'], (None, 0))[1]
    feature['properties']['impacted_acres_prop_max'] = scott.get(feature['properties']['COUNTY'], (None, 0))[1] / max_impacted_acres

    sql = '''
SELECT "permitApplicationNumber", "projectDescription", "acreage", "parish"
FROM application
WHERE "parish" = ? AND "type" = 'impact'
'''
    if feature['properties']['COUNTY'] in scott:
        applications = dt.execute(sql, [scott[feature['properties']['COUNTY']][0]])
        for a in applications:
            a['parish'] = a['parish'].upper().replace('SAINT', 'ST')
        feature['properties']['applications'] = applications
    else:
        feature['properties']['applications'] = []

json.dump(parishes, open('impacts.json', 'w'))
