##########################
#Classes to load NEON data
##########################

import os
import pathlib

import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
import rasterstats as rs
import xarray as xr
import rioxarray as rxr
import seaborn as sns

class NEONDataLoader:
    """
    Parent class to load NEON height data and calculate mean and max
            
        Attributes
        ----------
        base_dir_tmpl: str
            template for path to base directory
        
        insitu_path_tmpl:
            template for path to insitu directory
        
        chm_path_tmpl: str
            template for path to lidar directory
        
        plots_path_tmpl:
            template for path to plots directory
        
        site_name: str
            name of the site
    
        id_col_name: str
            name of the ID column header
    
        formatting_dict: str
            specific formatting for the site paths
    
        id_modifier: function
            function to modify the values in the id column
            
    """
    # Set as attributes
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
        # set arguments as attributes
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
        
    # dont need () with property
    @property    
    def lidar_chm_stats(self):
        """
        Calculates max and mean tree height from LiDAR

        Attributes
        ----------
        plots_path: path
            path to the plot shapefile

        chm_paths: path
            path to the lidar CHM data (tif file)

        Returns
        ---------
        self._lidar_chm_stats: gdf
            geodataframe containing max and mean lidar canopy height
        """
        if self._lidar_chm_stats is None:
            # Calculate the plot perimeters
            plots_gdf = gpd.read_file(self.plots_path)
            plots_gdf.geometry = plots_gdf.geometry.buffer(20)

            # Calculate zonal statistics - creates Dictionary
            chm_stats = rs.zonal_stats(
                    plots_gdf, self.chm_path,
                    stats =['mean', 'max'], nodata=0, 
                    geojson_out=True, copy_properties=True)
            # Create GDF with max and mean
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
        Calculate max and mean tree height from insitu data
        
        Attributes
        ----------
        insitu_path: path
            path to the insitu data (csv)

        Returns
        ---------
        self._insitu_height_stats: gdf
            dataframe containing max and mean insitu tree height
        """
        if self._insitu_height_stats is None:
            self._insitu_height_stats =(
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
        Calculate max and mean tree height from lidar and insitu data
    
        Parameters
        ----------
        lidar_chm_stats: property
            Property that creates gdf of LiDAR max and mean tree height

        insitu_height_stats: property
            Property that creates df of insitu max and mean tree height

        Returns
        ---------
        self._height_stats: gdf
            geodataframe containing plot IDs and lidar and insitu
            max and mean canopy height
        """
        if self._height_stats is None:
            self._height_stats = (
                self.lidar_chm_stats
                .merge(self.insitu_height_stats,
                       right_index=True,
                       left_on=self.id_col_name))
        return self._height_stats
    
    def plot_height(self, site_name, ax1max, ax2max):
        """Plots the insitu vs lidar max and mean canopy height

        Parameters
        ----------
        site_name: str
            name of the site

        ax1max: int 
            maximum lim for max height data 

        ax2max: int
            maximum lim for mean height data 

        """

        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12,4))

        ax1.scatter(self.height_stats.lidar_max, self.height_stats.insitu_max)
        ax1.plot((0,1), (0,1), transform=ax1.transAxes, ls='--', c='k')
        sns.regplot(x='lidar_max', y='insitu_max',
                    data=self.height_stats,
                    color='blue',
                    ax=ax1)
        ax1.set(xlim=(0,ax1max), ylim=(0,ax1max), aspect='equal',
               title=('Max canopy height: lidar vs insitu at {}'
                      .format(site_name)),
               xlabel='Lidar max height (m)',
               ylabel='In-situ max height (m)')
        ax1.xaxis.label.set_fontsize(14)
        ax1.yaxis.label.set_fontsize(14)
        ax1.title.set_fontsize(14)
        
        ax2.scatter(self.height_stats.lidar_mean, self.height_stats.insitu_mean)
        ax2.plot((0,1), (0,1), transform=ax2.transAxes, ls='--', c='k')
        sns.regplot(x='lidar_mean', y='insitu_mean',
                    data=self.height_stats,
                    color='blue',
                    ax=ax2)
        ax2.set(xlim=(0,ax2max), ylim=(0,ax2max), aspect='equal',
               title=('Mean canopy height: lidar vs insitu at {}'
                      .format(site_name)),
               xlabel='Lidar mean height (m)',
               ylabel='In-situ mean height (m)')
        ax2.xaxis.label.set_fontsize(14)
        ax2.yaxis.label.set_fontsize(14)
        ax2.title.set_fontsize(14)

        plt.show()

class SJERDataLoader(NEONDataLoader):
    site_name = 'SJER'
    id_col_name = 'Plot_ID'
    formatting_dict = {
        'separator': '_', 
        'plot': '_plot'}
    
class SOAPDataLoader(NEONDataLoader):
    
    site_name = 'SOAP'
    id_col_name = 'ID'
    formatting_dict = {
        'separator': '-', 
        'plot': ''}
    
    def id_modifier(self, id):
        return 'SOAP' + str(id)
