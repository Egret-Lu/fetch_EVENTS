# %% codecell 
from setup_parameters import *
import os
import sys
from os import listdir
f=open(search_dir+'evlist.txt','w')
# %% codecell
#get event list form file
for event in listdir(search_dir):
    if event[0:2] == '20':
        f.write(event+"\n")
f.close()
# %%
