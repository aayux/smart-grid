#!/bin/sh
# Change to local QGIS install
export QGISHOME=/usr
export PYTHONPATH=$QGISHOME/share/qgis/python
python smart_grid.py
