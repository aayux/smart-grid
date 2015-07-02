# Smart-Grid
### A GIS application for raster and vector maps

Current developments -

- Login screen
- Tool-bar with functionalities to import .tif, .dgn and .shp types of data and display on 'canvas', zoom and pan
- Widget to show a Layer Tree of currently active layers
- Display coordinates on mouse hover
- Connection to PostGIS database

Now working on -

- Tool to import maps directly from Google or Bing
- Plotting points onto map, based on user entry and drawing range around point using *st_buffer*

Known issues -

- Dataset size too large, slows down application – possible solution using *raster2psql* directly import through database entry

---------------------------------

Code contributors -
- [Aayush](https://github.com/ThePentium)
- [Pranay](https://github.com/pranay360)
- [Aman](https://github.com/metalaman)
- [Rishabh](https://github.com/rishirock)
