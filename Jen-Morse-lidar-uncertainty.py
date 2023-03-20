#!/usr/bin/env python
# coding: utf-8

# # LiDAR Uncertainty at two NEON Field Sites
# ## Soaproot Saddle (SOAP) Field Site
# ![Soaproot Saddle Field Site](img/Soaproot_pano.jpeg)
# Image Credit: National Ecological Oberservatory Network, https://www.neonscience.org/field-sites/soap
# 
# ## San Joaquin Experimental Range (SJER) Field Site 
# ![SJER Field Site](img/SJER_pano.jpeg)
# Image Credit: National Ecological Observatory Network, https://www.neonscience.org/field-sites/sjer

# In[1]:


# Import packages
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

# Get lidar data
et.data.get_data('spatial-vector-lidar')

# Set working directory
working_dir = os.path.join(
    pathlib.Path.home(),
    'earth-analytics',
    'data',
    'spatial-vector-lidar')

# Check working directory exists, create directory if does not exist
if not os.path.exists(working_dir):
    print('Path does not exist. Creating...')
    os.makedirs(working_dir)
os.chdir(working_dir)

# Check working directory path is correct
print(working_dir)


# In[2]:


class NEONDataLoader:
    """
    Parent class to load NEON tree height data.
    """

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
    id_mod = None
    
    def __init__(self):
        self.formatting_dict = self.formatting_dict
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
        Calculate max, mean tree height from LiDAR data.
        """
        if self._lidar_chm_stats is None:
            plots_gdf = gpd.read_file(self.plots_path)
            plots_gdf.geometry = plots_gdf.geometry.buffer(20)

            # Calculate Zonal statistics
            chm_stats = rs.zonal_stats(
                plots_gdf,
                self.chm_path,
                stats=['mean', 'max'],
                geojson_out=True,
                nodata=0,
                copy_properties=True)

            # Create GeoDataFrame
            self._lidar_chm_stats = gpd.GeoDataFrame.from_features(chm_stats)

            # Rename GeoDataFram columns
            self._lidar_chm_stats.rename(
                columns={'max':'lidar_max', 'mean':'lidar_mean'},
                inplace=True)
            if not self.id_mod is None:
                self._lidar_chm_stats[self.id_col_name] = (
                    self._lidar_chm_stats[self.id_col_name]
                    .apply(self.id_mod))
        return self._lidar_chm_stats
    
    @property
    def insitu_height_stats(self):
        """ 
        Load and calculate insitu max and mean tree height data.
        """
        if self._insitu_height_stats is None:
            self._insitu_height_stats = (
                pd.read_csv(self.insitu_path)
                .groupby('plotid')
                .stemheight
                .agg(['max', 'mean'])
                .rename(columns={'max': 'insitu_max', 'mean': 'insitu_mean'}))
        return self._insitu_height_stats
    
    @property
    def height_stats(self):
        """
        Merge insitu data with LiDar data.
        """
        if self._height_stats is None:
            self._height_stats = (
                self.lidar_chm_stats
                .merge(
                    self.insitu_height_stats, 
                    right_index=True, 
                    left_on=self.id_col_name))
        return self._height_stats


# In[3]:


class SJERDataLoader(NEONDataLoader):

    site_name = 'SJER'
    id_col_name = 'Plot_ID'
    formatting_dict = {'separator': '_', 'plot': '_plot'}

sjer_data_loader = SJERDataLoader()
sjer_gdf = sjer_data_loader.height_stats
sjer_gdf


# In[4]:


class SOAPDataLoader(NEONDataLoader):

    site_name = 'SOAP'
    id_col_name = 'ID'
    formatting_dict = {'separator': '-', 'plot': ''}

    def id_mod(self, id):
        """ Adds site name to plot number in ID column."""
    
        return 'SOAP' + str(id)

soap_data_loader = SOAPDataLoader()
soap_gdf = soap_data_loader.height_stats
soap_gdf


# In[5]:


def plot_height_stats(height_stats_gdf, axs, site, aggr):
    """
    Plot of Insitu and LiDAR tree height max and means.
    ----------
    Parameters:
    height_stats_gdf: GeoPandasDataFrame 
        GeoPandasDataFrame with LiDAR and insitu tree height statistics.
    
    axs: figure ax
        Ax figure to add to plot.
    
    site: str
        Site Name.
    
    aggr: str
        Aggregation statistic to plot (mean or max)
    -------
    Returns: 
    plot_height_stats: Plot of tree height statistics.
    """
    # Set limits and aspect of plot
    axs.set(xlim=(0, 30), ylim=(0, 30), aspect='equal')
    
    # Define plot type and columns to plot
    sns.scatterplot(
        x='lidar_{aggr}'.format(aggr=aggr),
        y='insitu_{aggr}'.format(aggr=aggr),
        data=height_stats_gdf, color='black',ax=axs)

    # Plot regression
    sns.regplot(
        x='lidar_{aggr}'.format(aggr=aggr),
        y='insitu_{aggr}'.format(aggr=aggr),
        data=height_stats_gdf, color='purple', ax=axs)

    # Set plot title labels
    axs.set_title(site)

    # Plot 1:1 line
    axs.plot(
        (0, 1), (0, 1), 
        transform=axs.transAxes, 
        ls='--', c='k')
    return plot_height_stats

# Plot Insitu vs LiDAR Tree Height Data
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(10, 10))
plt.suptitle(
    'Comparison of Insitu and LiDAR Tree Height Data\n'
    'From Two California Field Sites (meters)',
    fontweight='bold',
    fontsize=16)
plt.tight_layout(pad=2, h_pad=4, w_pad=0.5)

plot_height_stats(sjer_gdf, ax1, 'San Joaquin Experimental Range', 'mean')
plot_height_stats(sjer_gdf, ax2, 'San Joaquin Experimental Range', 'max')
plot_height_stats(soap_gdf, ax3, 'Soaproot Saddle', 'mean')
plot_height_stats(soap_gdf, ax4, 'Soaproot Saddle', 'max')

plt.show()



# In[ ]:




