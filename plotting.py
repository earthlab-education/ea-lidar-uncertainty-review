import numpy as np
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
import seaborn as sns

###################################


def quick_plot(lidar, points, study_site):
    """ 
    Creates a quick plot given a raster image and point file.

    Parameters:
    ----------
    lidar: datarray
        A datarray - Landsat in this case.
    points: geodataframe
        A geodatframe containing point locations

    Returns:
    -------
    A plot to screen.

    """

    fig, ax = plt.subplots(1, 1, figsize=(10, 6))

    lidar.plot(ax=ax)
    points.plot(ax=ax, marker='s', markersize=200, color='red')

    # Capitalize study_site for title.
    title = "{} Study Site:  LIDAR CHM and Study Sites".format(
        study_site.upper())
    ax.set_title(title)

    plt.show()

###################################


def create_comparison_plots(all_heights_gdf, study_site):
    """ 
    Create two plots of lidar vs insitu : MAx and Mean tree heights.
    Parameters:
    ----------
    all_heights_gdf: geodataframe
        Geodataframe holding merged lidar and insitu stats.
    study_site: str
        Name of study_site
    """

    # Why do I need to convert from a gdf to a df in order to plot?
    all_heights_gdf = pd.DataFrame(all_heights_gdf)

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8, 4), layout="constrained")

    all_heights_gdf.plot('lidar_max',
                         'insitu_max',
                         kind='scatter',
                         fontsize=14, s=20,
                         color="purple",
                         ax=ax1
                         )

    all_heights_gdf.plot('lidar_mean',
                         'insitu_mean',
                         kind='scatter',
                         fontsize=14, s=20,
                         color="purple",
                         ax=ax2
                         )

    # Auto-detect what value to use for the y & x axis max.
    # Get the max values for max and mean.
    lid_mx = all_heights_gdf['lidar_max'].max()
    lid_mn = all_heights_gdf['lidar_mean'].max()
    in_mx = all_heights_gdf['insitu_max'].max()
    in_mn = all_heights_gdf['insitu_mean'].max()

    # Figure out if lidar or insitu is larger.
    # Assign max value where true to y-axis max.
    if (lid_mx >= in_mx):
        y_mx = lid_mx
        y_mx = int(round(y_mx/10) * 10)
    else:
        y_mx = int(round(in_mx/10) * 10)

    # Figure out if lidar or insitu is larger.
    # Assign max value where true to y-axis mean.
    if (lid_mn >= in_mn):
        y_mn = lid_mn
        y_mn = int(round(y_mn/10) * 10 + 10)
    else:
        y_mn = int(round(in_mn/10) * 10 + 10)

    # Set up the x and y axes range.
    # Set tick intervals.
    ax1.set(xlim=[0, y_mx], ylim=[0, y_mx])
    ax1.set_aspect('equal')
    ax1.xaxis.set_major_locator(plt.MaxNLocator(5))
    ax1.yaxis.set_major_locator(plt.MaxNLocator(5))

    ax2.set(xlim=[0, y_mn], ylim=[0, y_mn])
    ax2.set_aspect('equal')
    ax2.xaxis.set_major_locator(plt.MaxNLocator(5))
    ax2.yaxis.set_major_locator(plt.MaxNLocator(5))

    # Add 1:1 lines ---------
    ax1.plot((0, 1), (0, 1), transform=ax1.transAxes, ls='--', c='k')
    ax2.plot((0, 1), (0, 1), transform=ax2.transAxes, ls='--', c='k')

    # Plot linear regression model fit.
    sns.regplot(x='lidar_max', y='insitu_max',
                data=all_heights_gdf, color="purple", ax=ax1)
    sns.regplot(x='lidar_mean', y='insitu_mean',
                data=all_heights_gdf, color="purple", ax=ax2)

    # Put a title together.
    title1 = "Tree Heights: Lidar Calculated vs. Manual Measurement\n"
    title2 = "{} Study Plot\n".format(study_site.upper())
    title3 = "Max Height, Mean Height"
    title = title1 + title2 + title3

    fig.suptitle(title, size='medium')

    plt.show()
###################################


def plot_maps(
        lidar, plots, study_site,
        cntry_path, states_path,
        roads_path, aoi_path):
    """ 
    Creates a quick plot given a raster image and point file.

    Parameters:
    ----------
    lidar: datarray
        A datarray - Landsat in this case.
    plots: geodataframe
        A geodatframe containing point locations
    study_site: str
        Name of study site.
    cntry_path: str
        Path to country boundary file.
    states_path: str
        Path to states boundary files.
    roads_path: str
        Path to road geometry file.
    aoi_path: str
        Path to study site boundary geometry.

    Returns:
    -------
    A plot to screen.

    """

    # Create map plots showing sjer location.
    usa_gdf = gpd.read_file(cntry_path)
    states_gdf = gpd.read_file(states_path)
    aoi_gdf = gpd.read_file(aoi_path)
    roads_gdf = gpd.read_file(roads_path)

    # Reproject to common crs.
    aoi_reproj_gdf = aoi_gdf.to_crs(usa_gdf.crs)
    roads_reproj_gdf = roads_gdf.to_crs(plots.crs)

    # Clip down roads to only lidar extent.
    roads_reproj_clip_gdf = gpd.clip(roads_reproj_gdf, lidar.rio.bounds())

    # Create a point representing the area of interest.
    # Easier for plotting.
    aoi_point = aoi_reproj_gdf["geometry"].centroid

    # Create larger scale map.
    fig1, (ax1) = plt.subplots(1, 1, figsize=(10, 6))

    # zoom in to map using.
    ax1.set(xlim=[-125, -110], ylim=[30, 45])
    ax1.yaxis.set_major_locator(plt.MaxNLocator(3))
    ax1.set_xlabel('')
    ax1.set_ylabel('')

    usa_gdf.plot(ax=ax1)
    states_gdf.plot(ax=ax1)
    aoi_point.plot(ax=ax1, color='r')

    ax1.set_title("Location of NEON {} Field Site".format(study_site.upper()))

    # Create Lidar map with roads.
    fig2, (ax2) = plt.subplots(1, 1, figsize=(10, 6))

    lidar.plot(ax=ax2, label="CHM (m)")
    plots.plot(ax=ax2, marker='s', markersize=50000, color='red')
    roads_reproj_clip_gdf.plot(
        ax=ax2, color='black', linewidth=2, label='Roads')
    # Addding a legend causes the cell execution to take a long time.
    # I dont know why this is happening.
    # ax2.legend()

    # Capitalize study_site for title.
    title = "LIDAR CHM and {} Study Sites".format(study_site.upper())
    ax2.set_title(title)
    ax2.set_xlabel('')
    ax2.set_ylabel('')

    plt.show()
######################################
