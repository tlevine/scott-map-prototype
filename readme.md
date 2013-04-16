Map prototype for Scott
====
[Scott](http://scott.thomaslevine.com) is collecting data on applications to
dredge or fill Louisiana wetlands, and we want to display the overall data.

In particular, Scott thinks a choropleth map showing the impacts by watershed
would be informative. Here we prototype such a concept.


Transformed the shape files into GeoJSON using this command: ogr2ogr -f "GeoJSON" -t_srs "WGS84" parishes.json Parishes.shp
##
