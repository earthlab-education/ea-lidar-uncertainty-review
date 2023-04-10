## Import libraries for functions
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



fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 10))

## Function definitions ##
def zstats_meanmax(plots_path, lidar_path):
    '''
    Extracts zonal stats based on buffered sampled site locations.
    
    Parameters
    ----------
    plots_path: str
        Local path to the shapefile containing sample plot locations.
        
    lidar_path: str
        Local path to the GeoTIFF containing LiDAR canopy height model values.
        
    Returns
    ---------
    Geodataframe containing mean and max values of LidAR points within buffered plot locations .
    '''
    # Read in plots shapefile with geopandas
    plots_gdf = gpd.read_file(plots_path)
    # Buffer shapefile by 20
    plots_gdf.geometry = plots_gdf.geometry.buffer(20)
    # Run zonal stats tool to extract mean and max from lidar dataset
    # Select by buffered plot locations
    lidar_stats = rs.zonal_stats(plots_gdf,
                                 lidar_path,
                                 stats = ['mean', 'max'],
                                 geojson_out = True,
                                 nodata=0,
                                 copy_properties=True)
    # Put zonal stats output into geodataframe
    plots_stats_gdf = gpd.GeoDataFrame.from_features(lidar_stats)
    # Rename stat columns
    plots_stats_gdf.rename(columns = {'max': 'lidar_max', 'mean': 'lidar_mean'}, inplace=True)
    
    return plots_stats_gdf
 

def insitu_meanmax(insitu_path, groupby):
    '''
    Extracts tree height (stemheight) data from a csv, user can choose which column to group the data by. 
    Max and mean values are aggregated and the columns renamed.
    
    Parameters
    ----------
    insitu_path: str
        Local path to a csv containing insitu observations on tree height.
        
    groupby: str
        Column on which the data should be grouped by.
        
    Returns
    ---------
    Dataset of max and mean stemheight values based on groupby parameter.
    '''
    
    # Read in csv using pandas, select max and mean of 'stemheight' column
    insitu_df = (pd.read_csv(insitu_path)
                      .groupby(groupby)
                      .stemheight
                      .agg(['max', 'mean'])
                      .rename(columns={'max': 'insitu_max', 'mean': 'insitu_mean'}))
    
    return insitu_df


def merge_df(site_zstats, site_insitu, id_col):
    '''
    Merge two datasets based on a user-selected column.
    
    Parameters
    ----------
    site_zstats: gdf
        Geodatframe containing canopy height model zonal stats of the AOI (area of interest).
        
    site_insitu: df
        Dataframe containing insitu measurements of tree height.
    
    id_col: str
        The key column on which to merge the datasets.
        
    Returns
    --------
    Merged dataframe based on the id_col parameter.
    '''
    
    # Use zstats_meanmax function....
    merge_df = site_zstats.merge(site_insitu,
                                right_index=True,
                                left_on=id_col)
    return merge_df

def plot_mergedf(site_name, site_merge_df):
    '''
    Plot merged dataframe
    '''
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 10))
    
    # Plot mean comparison on ax1
    ax1.scatter(site_merge_df.lidar_mean, site_merge_df.insitu_mean)

    # Plot max comparison on ax2
    ax2.scatter(site_merge_df.lidar_max, site_merge_df.insitu_max)

    # Equalize plot areas for best comparison
    ax1.set(xlim=(0, 30),
            ylim=(0, 30),
            aspect='equal')

    ax2.set(xlim=(0, 30),
            ylim=(0, 30),
            aspect='equal')

    # Plot 1:1 comparison line on each plot
    ax1.plot((0, 1), (0, 1),
             transform=ax1.transAxes,
             ls='--',
             c='k')

    ax2.plot((0, 1), (0, 1),
             transform=ax2.transAxes,
             ls='--',
             c='k')

    # create regression area on plots
    sns.regplot(x='lidar_mean',
                y='insitu_mean',
                data=site_merge_df,
                color='purple',
                ax=ax1)

    sns.regplot(x='lidar_max',
                y='insitu_max',
                data=site_merge_df,
                color='purple',
                ax=ax2)

    # Set labels and fontsizes
    for ax in [ax1, ax2]:
        ax.tick_params(axis='both', which='major', labelsize=10)
        if ax==ax1:
            ax.set_xlabel('LiDAR-derived Mean Tree Height (m)', fontsize=14)
            ax.set_ylabel('Mean Measured Tree Height (m)', fontsize=14)
        if ax==ax2:
            ax.set_xlabel('LiDAR-derived Max Tree Height (m)', fontsize=14)
            ax.set_ylabel('Max Measured Tree Height (m)', fontsize=14)


    # Set descriptive suptitle
    fig.suptitle('Comparison of Tree Height Measurement Methods'
                 '\nSite: NEON {}'.format(site_name), y=0.75)

    # Set better spacing between plots
    fig.tight_layout(rect=[0, 0.03, 1, 0.95])

    plt.show()

## Class definition ##
class NEONDataLoader:
    """Parent class to load NEON height data"""

    # Set home directory to start the process
    home_dir = os.path.join(pathlib.Path.home(),'earth-analytics','data','spatial-vector-lidar')
    os.chdir(home_dir)
    def __init__(self, site_name, id_col, f_dict):
        # Set attributes
        self.site_name = site_name
        self.id_col = id_col
        self.f_dict = f_dict
        # Set formatting dictionary names, lower for paths, and upper for data
        self.f_dict['site_name_low'] = site_name.lower()
        self.f_dict['site_name_up'] = site_name.upper()
        
        # Set base dir
        self.base_dir = os.path.join(
            'california',
            'neon-{site_name_low}-site').format(**self.f_dict)
        # Set insitu dir
        self.insitu_path = os.path.join(
            self.base_dir,
            '2013',
            'insitu',
            'veg{separator}structure',
            'D17_2013_{site_name_up}_vegStr.csv').format(**self.f_dict)
        # Set plot dir
        self.plots_path = os.path.join(
            self.base_dir,
            'vector_data',
            '{site_name_up}{plot}_centroids.shp').format(**self.f_dict)
        # Set lidar dir - canopy height model is chm
        self.chm_path = os.path.join(
            self.base_dir,
            '2013',
            'lidar',
            '{site_name_up}_lidarCHM.tif').format(**self.f_dict)
        
        # Run zonal stats
    def calc_chm_stats(self):
        plots_gdf = gpd.read_file(self.plots_path)
        plots_gdf.geometry = plots_gdf.geometry.buffer(20)
        chm_stats = rs.zonal_stats(plots_gdf, self.chm_path, stats = ['mean', 'max'], nodata=0, geojson_out=True, copy_properties=True)
        chm_stats_gdf = gpd.GeoDataFrame.from_features(chm_stats)
        chm_stats_gdf.rename(columns = {'max':'lidar_max', 'mean':'lidar_mean'}, inplace=True)
            
        return chm_stats_gdf
    
    def insitu_meanmax(self):
        insitu_df = (pd.read_csv(self.insitu_path)
                      .groupby('plotid')
                      .stemheight
                      .agg(['max', 'mean'])
                      .rename(columns={'max': 'insitu_max', 'mean': 'insitu_mean'}))
        return insitu_df
    
    # Merge datasets
    def merge_df(self):
        chm_stats_gdf = self.calc_chm_stats()
        calc_insitu = self.insitu_meanmax()

        merge_df = chm_stats_gdf.merge(calc_insitu,
                                    right_index=True,
                                    left_on=self.id_col)
        return merge_df

    
    
    
    