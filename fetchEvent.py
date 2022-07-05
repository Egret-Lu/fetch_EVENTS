from setup_parameters import *
import matplotlib.pyplot as plt
import obspy
from obspy.clients.fdsn import Client
from obspy import UTCDateTime
from obspy.core import AttribDict
from obspy.io.sac import SACTrace
from obspy.geodetics import gps2dist_azimuth, locations2degrees
from obspy.core.inventory.inventory import read_inventory
from obspy.core.event.catalog import read_events
import numpy as np
import os
from datetime import datetime
import calendar
import urllib
import json

inventory= read_inventory("stations.xml")
print(inventory[0].stations[0].elevation)

with open(search_dir+"events.json", 'r') as f:
     cat_evts = json.loads(f.read())

print(cat_evts["events"][0].keys())