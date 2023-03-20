#!/usr/bin/env python
# coding: utf-8

# <img style="float: left;" src="earth-lab-logo-rgb.png" width="150" height="150" />
# 
# # Earth Analytics Education

# # LiDAR Uncertainty at SOAP and SJER NEON sites

# ## The Soap Site
# ![Soaproot panorama](img/Soaproot_pano.jpeg)
# Image Credit: National Ecological Observation Network, available at https://www.neonscience.org/field-sites/soap

# ## The SJER Site
# ![SJER panorama](img/sjer_site.jpeg)
# Image Credit: National Ecological Observation Network, available at https://www.neonscience.org/field-sites/sjer

# In[3]:


import os
import pathlib

import earthpy as et 
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
import rasterstats as rs
import xarray as xr
import rioxarray as rxr
import seaborn as sns

import clean

# download the data from EarthPy
et.data.get_data('spatial-vector-lidar')

# set home directory
home_dir = os.path.join(
    pathlib.Path.home(),
    'earth-analytics',
    'data',
    'spatial-vector-lidar'
)
os.chdir(home_dir)   


# In[7]:


class SOAPDataLoader(clean.NEONDataLoader):
    site_name = 'SOAP'
    id_col_name = 'ID'
    formatting_dict = {'seperator':'-', 'plot': ''}
    
    def id_modifier(self, id):
        return 'SOAP' + str(id)


soap_data_loader = SOAPDataLoader()


# In[8]:


class SJERDataLoader(clean.NEONDataLoader):
    site_name = 'SJER'
    id_col_name = 'Plot_ID'
    formatting_dict = {'seperator':'_', 'plot': '_plot'}
    
sjer_data_loader = SJERDataLoader()


# In[9]:


sjer_data_loader.plots()


# In[10]:


soap_data_loader.plots()


# In[ ]:




