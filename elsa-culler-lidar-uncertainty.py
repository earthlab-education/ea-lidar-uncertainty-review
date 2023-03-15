#!/usr/bin/env python
# coding: utf-8

# # LiDAR Uncertainty at SOAP and SJER NEON sites

# ## The SOAP site
# ![Soaproot panorama](https://www.neonscience.org/sites/default/files/styles/he/public/image-content-images/Soaproot_pano.jpg?h=38da9059&itok=XfdBWdLh)
# Image credit: National Ecological Observation Network, available at https://www.neonscience.org/field-sites/soap

# In[1]:


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

et.data.get_data('spatial-vector-lidar')

home_dir = os.path.join(
    pathlib.Path.home(),
    'earth-analytics',
    'data',
    'spatial-vector-lidar')
os.chdir(home_dir)


# NEONDataLoader object:
#   - takes:
#     - name of the dataset
#     - id column name
#     - dictionary of formatting to apply to file paths
#     - id modifier
#   - has:
#     - name of the dataset
#     - id column name
#     - paths
#     - LiDAR GeoDataFrame
#     - insitu DataFrame
#     - merged GeoDataFrame
#   - does:
#     - plot the data
#     - (caching)
#     - (save the plot to a file)

# In[2]:


class NEONDataLoader:
    """Parent class to load NEON height data"""

    base_dir_tmpl = os.path.join(
        'california',
        'neon-{site_name_low}-site')
    insitu_path_tmpl = os.path.join(
        '{base_dir}',
        '2013',
        'insitu',
        'veg{separator}structure',
        'D17_2013_{site_name_up}_vegStr.csv')
    chm_path_tmpl = os.path.join(
        '{base_dir}',
        '2013',
        'lidar',
        '{site_name_up}_lidarCHM.tif')
    plots_path_tmpl = os.path.join(
        '{base_dir}',
        'vector_data',
        '{site_name_up}{plot}_centroids.shp')
    
    site_name = NotImplemented
    id_col_name = NotImplemented
    formatting_dict = NotImplemented
    id_modifier = None

    def __init__(self):
        self.formatting_dict['site_name_low'] = self.site_name.lower()
        self.formatting_dict['site_name_up'] = self.site_name.upper()
        self.formatting_dict['base_dir'] = (
            self.base_dir_tmpl.format(**self.formatting_dict))

        self.insitu_path = self.insitu_path_tmpl.format(**self.formatting_dict)
        self.chm_path = self.chm_path_tmpl.format(**self.formatting_dict)
        self.plots_path = self.plots_path_tmpl.format(**self.formatting_dict)

        self._insitu_height_stats = None
        self._lidar_chm_stats = None
        self._height_stats = None

    @property
    def lidar_chm_stats(self):
        """
        Calculate max and mean tree height from LiDAR
        """
        if self._lidar_chm_stats is None:
            plots_gdf = gpd.read_file(self.plots_path)
            plots_gdf.geometry = plots_gdf.geometry.buffer(20)

            # Calculate the zonal stats
            chm_stats = rs.zonal_stats(
                plots_gdf, self.chm_path,
                stats=['mean', 'max'], nodata=0,
                geojson_out=True, copy_properties=True)
            self._lidar_chm_stats = gpd.GeoDataFrame.from_features(chm_stats)
            self._lidar_chm_stats.rename(
                columns={'max': 'lidar_max', 'mean': 'lidar_mean'},
                inplace=True)
            if not self.id_modifier is None:
                self._lidar_chm_stats[self.id_col_name] = (
                    self._lidar_chm_stats[self.id_col_name]
                    .apply(self.id_modifier))
        return self._lidar_chm_stats
    
    @property
    def insitu_height_stats(self):
        """
        Calculate insitu tree height data max and mean.
        """
        if self._insitu_height_stats is None:
            self._insitu_height_stats = (
                pd.read_csv(self.insitu_path)
                .groupby('plotid')
                .stemheight
                .agg(['max', 'mean'])
                .rename(columns={'max': 'insitu_max', 
                                 'mean': 'insitu_mean'}))
        return self._insitu_height_stats
    
    @property
    def height_stats(self):
        """
        Calculate LiDAR and insitu height stats.
        """
        if self._height_stats is None:
            self._height_stats = (
                self.lidar_chm_stats
                .merge(self.insitu_height_stats, 
                    right_index=True, 
                    left_on=self.id_col_name))
        return self._height_stats


# In[3]:


class SJERDataLoader(NEONDataLoader):

    site_name = 'SJER'
    id_col_name = 'Plot_ID'
    formatting_dict = {
        'separator': '_', 
        'plot': '_plot'}

sjer_data_loader = SJERDataLoader()
sjer_data_loader.height_stats.head()


# In[4]:


class SOAPDataLoader(NEONDataLoader):

    site_name = 'SOAP'
    id_col_name = 'ID'
    formatting_dict = {
        'separator': '-', 
        'plot': ''}
    
    def id_modifier(self, id):
        return 'SOAP' + str(id)

soap_data_loader = SOAPDataLoader()
soap_data_loader.height_stats.head()

