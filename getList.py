# get station and event list
# generate a station document
from setup_parameters import *
import matplotlib.pyplot as plt
import obspy
from obspy.clients.fdsn import Client
from obspy import UTCDateTime
from obspy.core import AttribDict
from obspy.io.sac import SACTrace
from obspy.geodetics import gps2dist_azimuth, locations2degrees
import numpy as np
import os
from datetime import datetime
import calendar
import urllib
import json

# %% codecell
if not os.path.exists(search_dir):
    os.makedirs(search_dir)
    
# LOAD CLIENT
client = Client(webservice)
print(client)
# %% codecell
# LOAD EVENT CATALOGUE
t1 = UTCDateTime(tstart)
t2 = UTCDateTime(tend)
if isCMT_params==1 :
    # Load events from GCMT catalogue using IRIS SPUD
    url_query = 'http://ds.iris.edu/spudservice/momenttensor/ids?' \
               +'evtstartdate='+t1.strftime('%Y-%m-%dT%H:%M:%S') \
               +'&evtenddate='+t2.strftime('%Y-%m-%dT%H:%M:%S') \
               +'&evtminmag='+str(minmagnitude)
    evids = urllib.request.urlopen(url_query)
    events_str = '&'.join([line.decode("utf-8").replace("\n", "") for line in evids])+'&'
    url_ndk = 'http://ds.iris.edu/spudservice/momenttensor/bundleids/ndk?'+events_str
    cat_evts = obspy.read_events(url_ndk)
    if iscentroid: # Use centroid parameters
        ortype = 'centroid'
    else: # Use hypocenter parameters
        ortype = 'hypocenter'
else: # Read events from IRIS catalogue
    cat_evts = client.get_events(starttime=t1, endtime=t2, minmagnitude=minmagnitude)

# %% codecell
# LOAD STATIONS
inventory = client.get_stations(network=network, station=stations, channel=comps[0], starttime=t1, endtime=t2)
##plot all stations
# inventory.plot(projection="local",label=False)
fig = inventory.plot(show=False) 
##plot all events and stations
# cat_evts.plot(fig=fig)  
# fig.savefig(search_dir+"events.jpg", bbox_inches="tight")

file = open('stations.txt', 'w')
for i in range(len(inventory)):
    for ista in range(0,len(inventory[i])) :
        file.write("%5s %12f %12f %12f\n" % (inventory[i].stations[ista]._code, 
                                            inventory[i].stations[ista]._latitude, 
                                            inventory[i].stations[ista]._longitude, 
                                            inventory[i].stations[ista]._elevation))
file.close()
inventory.write("stations.xml",format="STATIONXML",level='station')  
cat_evts.write(search_dir+"events.json", format="JSON") 

