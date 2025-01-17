########## 1-get_event_waveforms ##########
minmagnitude = 6.5 #6.5; 7.0; # Lower magnitude cutoff for event search
webservice = "IRIS"
network = "_HAWAII" # YO ENAM

input_stalist = False# 0 if use all stations
if input_stalist: # List of stations
    stalist = '/Users/russell/Lamont/ENAM/DATA/stalist_good.txt'
    text_file = open(stalist, "r")
    stations = text_file.read().split('\n')
    text_file.close()
    stations = ','.join(stations).replace(" ", "")
else: # Use all available stations
    stations = "*"
    
tstart = "2005-01-01T00:00:00"
tend = "2008-01-01T00:00:00"
is_downsamp = 1 # Downsample?
sr_new = 1 # Downsample Hz (samples/sec)
trlen = 6000 # Length of traces (sec)
# WARNING! List the full channel names. Do not use wildcards. Bad things will happen...
#comps = ["BHZ", "BH1", "BH2", "BDH"] # Components to download
comps = ["BHZ"]
is_removeresp = 1 # Remove response?
outunits = 'DISP' # DISP, VEL, ACC [For pressure channels, should use "VEL"]
isCMT_params = 1 # Use GCMT parameters for SAC header or default IRIS? (time, lat, lon, depth)
iscentroid = 1 # if isCMT_params=1, use centroid instead of epicentral?
search_dir = './' + webservice + '_' + network + '_' + str(minmagnitude) + '/' # OUTPUT PATH

########## 2-rotate_H1H2_NE_RT ##########
# Read orientations
ori_path = '/Users/russell/Lamont/ENAM/DATA/orientations/YO_orientations.txt'
iscleandir = 0 # Clean directories by removing all BHT, BHR, BHE, and BHN before calculating.
# Define Naming Conventions
Zcomp = "BHZ" # input (same as above)
H1comp = "BH1" # input (same as above)
H2comp = "BH2" # input (same as above)
Ncomp = "BHN" # output
Ecomp = "BHE" # output
Tcomp = "BHT" # output
Rcomp = "BHR" # output


########## 3-CMT2idagrn ##########
CMT2idagrn_path = search_dir+'CMT2idagrn/' # OUTPUT PATH

########## 4-writeCMTSOLUTION ##########
CMTSOLUTION_path = search_dir+'CMTSOLUTIONS/' # OUTPUT PATH
