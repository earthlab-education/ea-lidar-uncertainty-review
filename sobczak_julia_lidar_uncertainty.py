#!/usr/bin/env python
# coding: utf-8

# # Comparison of Tree Height Measurements(LiDAR vs insitu)
# 
# This notebook analyzes canopy height data collected with two different methods: in-person onsite (insitu) and aerial LiDAR. The data are merged by site name, and then compared using a regression plot.
# 
# Data from two National Ecological Observation (NEON) sites are used for comparison between the methods.
# 1. [Soaproot Saddle](https://www.neonscience.org/field-sites/soap)
# <img src="img\Soaproot_pano.jpg" />
# 
# 
# 2. [San Joaquin Experimental Range](https://www.neonscience.org/field-sites/sjer)
# <img src="img\SJER_pano.jpg" />
# 
# 
# ### Step 1: Import libraries and set plotting parameters

# In[1]:


# import libraries
import os
import pathlib

# import local function directory
import clean

import earthpy as et
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
import rasterstats as rs
import xarray as xr
import rioxarray as rxr
import seaborn as sns


# Set consistent plotting style
sns.set_style("white")
sns.set(font_scale=1.5)


# ### Step 2: Set data paths
# 
# Four paths are needed per site:
# * base directory
# * insitu csv
# * plot location shapefile
# * LiDAR Canopy Height Model GeoTIFF
# 
# Checks have been added to path_check_1 and path_check_2 ensure all of these paths exist.

# In[2]:


# Set home dir
home_dir = os.path.join(
    pathlib.Path.home(),
    'earth-analytics',
    'data',
    'spatial-vector-lidar')
# Update directory to home dir
os.chdir(home_dir)


# Set base SJER path
sjer_base_dir = os.path.join(
    home_dir,
    'california',
    'neon-sjer-site')
# Set SJER insitu path
sjer_insitu_path = os.path.join(
    sjer_base_dir,
    '2013',
    'insitu',
    'veg_structure',
    'D17_2013_SJER_vegStr.csv')
# Set SJER plot locations path
sjer_plots_path = os.path.join(
    sjer_base_dir,
    'vector_data',
    'SJER_plot_centroids.shp')
# Set SJER LiDAR Canopy Height Model path
sjer_chm_path = os.path.join(
    sjer_base_dir,
    '2013',
    'lidar',
    'SJER_lidarCHM.tif')
# Check if SJER paths exist
path_check_1 = [sjer_base_dir, sjer_insitu_path, sjer_plots_path, sjer_chm_path]
for path in path_check_1:
    print(os.path.exists(path))
    

# Set SOAP home directory
soap_dir = os.path.join(home_dir,
                       'california',
                       'neon-soap-site')
# Set SOAP insitu path
soap_insitu_path = os.path.join(soap_dir,
                          '2013',
                           'insitu',
                           'veg-structure',
                           'D17_2013_SOAP_vegStr.csv')
# Set SOAP plot locations path
soap_plots_path = os.path.join(soap_dir,
                        'vector_data',
                         'SOAP_centroids.shp')
# Set SOAP LiDAR Canopy Height Model path
soap_chm_path = os.path.join(soap_dir,
                         '2013',
                          'lidar',
                         'SOAP_lidarCHM.tif')
# Check if SOAP paths exist
path_check_2 = [soap_dir, soap_insitu_path, soap_plots_path, soap_chm_path]
for path in path_check_2:
    print(os.path.exists(path))


# ### Step 3: Start downloading data from earthpy 
# 
# Find original data and activity in the [Earth Data Analytics textbook](https://www.earthdatascience.org/courses/use-data-open-source-python/spatial-data-applications/lidar-remote-sensing-uncertainty/summarize-and-compare-lidar-insitu-tree-height/).
# 

# In[3]:


# Use earthpy to import data
et.data.get_data('spatial-vector-lidar')


# ### Step 4: Calculate zonal stats
# Use the zstats_meanmax() function and calculate for both NEON sites. View the function in clean.py directory.

# In[4]:


# SJER zstats
sjer_zstats = clean.zstats_meanmax(sjer_plots_path, sjer_chm_path)
# SOAP zstats
soap_zstats = clean.zstats_meanmax(soap_plots_path, soap_chm_path)

# Check datasets
soap_zstats.head()


# ### Step 5:  Get stats for insitu data
# Use the insitu_meanmax() function and calculate for both NEON sites. View the function in clean.py directory.

# In[5]:


# SJER site insitu data
sjer_insitu = clean.insitu_meanmax(sjer_insitu_path, 'plotid')
# SOAP site insitu data
soap_insitu = clean.insitu_meanmax(soap_insitu_path, 'plotid')

# Check datasets
sjer_insitu.head(), soap_insitu.head()


# ### Step 6: Merge datasets
# Use the merge_df() function and calculate for both NEON sites. View the function in clean.py directory.

# In[6]:


# Adjust SOAP site ID's before merging
if not soap_zstats['ID'].str.contains('SOAP').any():
    soap_zstats['ID'] = ('SOAP' + soap_zstats['ID'])
    
# Merge data for SOAP site
soap_merge_df = clean.merge_df(soap_zstats, soap_insitu, id_col='ID')

# Merge data for SJER site
sjer_merge_df = clean.merge_df(sjer_zstats, sjer_insitu, id_col='Plot_ID')

sjer_merge_df.head(), soap_merge_df.head()


# ### Step 7: Plot the data
# 
# The regression plots in seaborn are primarily intended to add a visual guide that helps to emphasize patterns in a dataset during exploratory data analyses. Regression plots as the name suggests creates a regression line between 2 parameters and helps to visualize their linear relationships ([source: geeksforgeeks.org](https://www.geeksforgeeks.org/seaborn-regression-plots/)).

# In[7]:


# Run plotting function over NEON sites
sjer_plot = clean.plot_mergedf('San Joaquin Experimental Range', sjer_merge_df)
soap_plot = clean.plot_mergedf('Soaproot Saddle', soap_merge_df)

sjer_plot, soap_plot


# ### Alternate option: use the class saved in clean.py
# Use this class to obtain the zonal stats, insitu aggregation, and merged dataframes found in the steps above.

# In[8]:


# Use data loader class on SJER site
neon_dl = clean.NEONDataLoader('SJER', 'Plot_ID', {'separator':'_', 'plot':'_plot'})

sjer_merge_class = neon_dl.merge_df()

