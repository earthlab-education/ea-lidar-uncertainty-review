#!/usr/bin/env python
# coding: utf-8

# # LiDAR Uncertainty: A Comparison of Two California Sites.

# ## The Soap Site
# ![image.png](attachment:image.png)
# image credit: National Ecological Observation Network

# In[13]:


## The SJER Site
get_ipython().system('[image.png](attachment:image.png)')
image credit: National Ecological Observation Network


# In[2]:


# Import necessary packages
import os
import pathlib

import earthpy as et
import geopandas as gpd
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import rasterstats as rs
import rioxarray as rxr
import seaborn as sns
import xarray as xr

# Download data from earth py
et.data.get_data('spatial-vector-lidar')

# General housekeeping
home_dir = os.path.join(pathlib.Path.home(), 'earth-analytics',
                        'data', 'spatial-vector-lidar')
os.chdir(home_dir)

# If the dir does not exist, create it
output_path = os.path.join(home_dir,
                           "outputs")


# In[3]:


class NEONDataLoader:

    '''This class creates all of our necessary paths for downloads

    parameters:
    ----------
    site_name = str
    id_col = str
    formatting_dict = key (?)

    returns:
    -------
    Data is opened and transferred to correct locations.
    '''

    # Create necessary variables for SOAP and SJER sites.
    base_dir_tmpl = os.path.join('california',
                                 'neon-{site_name_low}-site')

    insitu_path_tmpl = os.path.join('{base_dir}', '2013',
                                    'insitu', 'veg{separator}structure',
                                    'D17_2013_{site_name_up}_vegStr.csv')
    plots_path_tmpl = os.path.join(
        '{base_dir}', 'vector_data', '{site_name_up}{plot}_centroids.shp')
    chm_path_tmpl = os.path.join(
        '{base_dir}', '2013', 'lidar', '{site_name_up}_lidarCHM.tif')

    # Create init function download both sets of data.
    def __init__(self, site_name, id_col, formatting_dict={}):
        self.site_name = site_name
        self.id_col = id_col
        self.formatting_dict = formatting_dict
        self.formatting_dict['site_name_low'] = site_name.lower()
        self.formatting_dict['site_name_up'] = site_name.upper()
        self.formatting_dict['base_dir'] = self.base_dir_tmpl.format(
            **self.formatting_dict)

        self.insitu_path = self.insitu_path_tmpl.format(**self.formatting_dict)
        self.plots_path = self.plots_path_tmpl.format(**self.formatting_dict)
        self.chm_path = self.chm_path_tmpl.format(**self.formatting_dict)


# In[4]:


sjer_data_loader = NEONDataLoader('SJER', 'Plot_ID',
                                  {'separator': '_', 'plot': '_plot'})
sjer_data_loader


# In[5]:


soap_data_loader=NEONDataLoader('SOAP', 'ID', 
                                {'separator':'-', 'plot':''})

soap_data_loader.insitu_path


# In[91]:


class AnalyzeLidarUncertainty:

    '''This class calculates stats for lidar and insitu and merges the two data frames.

        parameters:
        ----------
        lidar_path: str (or path?) 
        insitu_path: str
        plots_path: str

        returns:
        -------
        Processed data frame.

        '''

    def __init__(self, lidar_path, insitu_path, plots_path, study_site):
        self.lidar_path = lidar_path
        self.insitu_path = insitu_path
        self.plots_path = plots_path
        self.study_site = study_site

    def calc_lidar_chm_stats(self):
        '''
        Calculates lidar mean and max tree heights.
        '''

        lidar_chm = rxr.open_rasterio(
            self.lidar_path, masked=True).squeeze()
        lidar_chm_clean = lidar_chm.where(lidar_chm > 0, np.nan)

        plots_gdf = gpd.read_file(self.plots_path)
        plots_gdf.geometry = plots_gdf.geometry.buffer(20)

        lidar_chm_stats = rs.zonal_stats(
            plots_gdf,
            lidar_chm_clean.values,
            affine=lidar_chm_clean.rio.transform(),
            nodata=-999,
            geojson_out=True,
            copy_properties=True,
            stats='count mean max')

        # Create a gdf based on the stats requested from zonal stats and rename columns.
        lidar_chm_gdf = gpd.GeoDataFrame.from_features(lidar_chm_stats)

        lidar_chm_gdf.rename(
            columns={'max': 'lidar_max',
                     'mean': 'lidar_mean',
                     'ID': 'plotid',
                     'Plot_ID': 'plotid'}, inplace=True)

        return lidar_chm_gdf

    def calc_insitu_dfs(self):
        '''
        Calculate insitu tree height mean and max.
        '''

        df = (pd.read_csv(self.insitu_path)
              .groupby('plotid')
              .stemheight
              .agg(['max', 'mean'])
              .rename(columns={'max': 'insitu_max',
                               'mean': 'insitu_mean',
                               'ID': 'plotid',
                               'Plot_ID': 'plotid'}))

        return df

    def merge_dfs(self):
        '''
        Merges insitu and lidar data frames together.

        '''

        chm_stats_gdf = self.calc_lidar_chm_stats()
        insitu_height_df = self.calc_insitu_dfs()

        if (self.study_site == 'soap'):
            ss = self.study_site.upper()
            chm_stats_gdf['plotid'] = ss + chm_stats_gdf['plotid']

        data_frame = chm_stats_gdf.merge(
            insitu_height_df, right_on='plotid', left_on='plotid')
        return data_frame


sjer_site = AnalyzeLidarUncertainty(
    sjer_data_loader.chm_path, sjer_data_loader.insitu_path,
    sjer_data_loader.plots_path, sjer_data_loader.formatting_dict['site_name_low'])

sjer_site.calc_lidar_chm_stats()


# In[84]:


soap_site = AnalyzeLidarUncertainty(soap_data_loader.chm_path, soap_data_loader.insitu_path,
                                    soap_data_loader.plots_path, soap_data_loader.formatting_dict['site_name_low'])
soap_site.calc_lidar_chm_stats()


# In[85]:


sjer_site.calc_insitu_dfs()


# In[86]:


soap_site.calc_insitu_dfs()


# In[87]:


soap_site.merge_dfs()


# In[88]:


sjer_site.merge_dfs()


# In[90]:


def plot_regression(lidar_mean, insitu_mean, lidar_max, insitu_max):

    # Plot SJER data with regression lines/scatterplot.
    Title= {'SJER', 'SOAP'}
    fig, (ax1, ax2)=plt.subplots(1,2, figsize=(12,12))
    fig.suptitle(
        '{} Insitu & Lidar Comparison', fontsize=14)
    ax1.scatter(df.lidar_mean, df.insitu_mean)
    ax1.set(xlim=(0,30), ylim=(0,30), aspect='equal', title='Mean Values')
    sns.regplot('lidar_mean', 'insitu_mean',
               data=df,
               color='purple',
               ax=ax1)
    ax1.plot((0,1),(0,1), transform=ax1.transAxes, ls='--', c='k')

    ax2.scatter(df.lidar_max, df.insitu_max)
    ax2.set(xlim=(0,30), ylim=(0,30), aspect='equal', title='Max Values')
    sns.regplot('lidar_max', 'insitu_max', 
                data=df, 
                color='purple', 
                ax=ax2)
    ax2.plot((0,1),(0,1), transform=ax2.transAxes, ls='--', c='k')
    return regression_plot

plot_regression(soap_site.merge_dfs(lidar_mean, insitu_mean, lidar_max, insitu_max))


# In[ ]:




