#!/usr/bin/env python
# coding: utf-8

# <img style="float: left;" src="earth-lab-logo-rgb.png" width="150" height="150" />
# 
# # Earth Analytics Education - EA  Python Course Spring 2021

# ## Important  - Assignment Guidelines
# 
# 1. Before you submit your assignment to GitHub, make sure to run the entire notebook with a fresh kernel. To do this first, **restart the kernel** (in the menubar, select Kernel$\rightarrow$Restart & Run All)
# 2. Always replace the `raise NotImplementedError()` code with your code that addresses the activity challenge. If you don't replace that code, your notebook will not run.
# 
# ```
# # YOUR CODE HERE
# raise NotImplementedError()
# ```
# 
# 3. Any open ended questions will have a "YOUR ANSWER HERE" within a markdown cell. Replace that text with your answer also formatted using Markdown.
# 4. **DO NOT RENAME THIS NOTEBOOK File!** If the file name changes, the autograder will not grade your assignment properly.
# 6. When you create a figure, comment out `plt.show()` to ensure the autograder can grade your plots. For figure cells, DO NOT DELETE the code that says `DO NOT REMOVE LINE BELOW`.
# 
# ```
# ### DO NOT REMOVE LINE BELOW ###
# student_plot1_ax = nb.convert_axes(plt)
# ```
# 
# * Only include the package imports, code, and outputs that are required to run your homework assignment.
# * Be sure that your code can be run on any operating system. This means that:
#    1. the data should be downloaded in the notebook to ensure it's reproducible
#    2. all paths should be created dynamically using the `os.path.join`
# 
# ## Follow to PEP 8 Syntax Guidelines & Documentation
# 
# * Run the `autopep8` tool on all cells prior to submitting (HINT: hit shift + the tool to run it on all cells at once!
# * Use clear and expressive names for variables. 
# * Organize your code to support readability.
# * Check for code line length
# * Use comments and white space sparingly where it is needed
# * Make sure all python imports are at the top of your notebook and follow PEP 8 order conventions
# * Spell check your Notebook before submitting it.
# 
# For all of the plots below, be sure to do the following:
# 
# * Make sure each plot has a clear TITLE and, where appropriate, label the x and y axes. Be sure to include UNITS in your labels.
# 

# ### Add Your Name Below 
# **Your Name:** C. Emi Fergus

# <img style="float: left;" src="colored-bar.png"/>

# ---

# # Week 04 and 05 Homework - Automate NDVI Workflow
# 
# For this assignment, you will write code to generate a plot of the mean normalized difference vegetation index (NDVI) for two different sites in the United States across one year of data:
# 
# * San Joaquin Experimental Range (SJER) in Southern California, United States
# * Harvard Forest (HARV) in the Northeastern United States
# 
# The data that you will use for this week is available from **earthpy** using the following download: 
# 
# `et.data.get_data('ndvi-automation')`
# 
# ## Assignment Goals
# 
# Your goal in this assignment is to create the most efficient and concise workflow that you can that allows for:
# 
# 1. The code to scale if you added new sites or more time periods to the analysis.
# 2. Someone else to understand your workflow.
# 3. The LEAST and most efficient (i.e. runs fast, minimize repetition) amount of code that completes the task.
# 
# ### HINTS
# 
# * Remove values outside of the landsat valid range of values as specified in the metadata, as needed.
# * Keep any output files SEPARATE FROM input files. Outputs should be created in an outputs directory that is created in the code (if needed) and/or tested for.
# * Use the functions that we demonstrated during class to make your workflow more efficient.
# * BONUS - if you  chose - you can export your data as a csv file. You will get bonus points for doing this.
# 
# 
# ## Assignment Requirements
# 
# Your submission to the GitHub repository should include:
# * This Jupyter Notebook file (.ipynb) with:
#     * The code to create a plot of mean NDVI across a year for  2 NEON Field Sites:
#         * NDVI on the x axis and formatted dates on the y for both NEON sites on one figure/axis object
#     * The **data should be cleaned to remove the influence of clouds**. See the [earthdatascience website for an example of what your plot might look like with and without removal of clouds](https://www.earthdatascience.org/courses/earth-analytics-python/create-efficient-data-workflows/).
# * BONUS: Create one output `.csv` file that has 3 columns - NDVI, Date and Site Name - with values for SJER and HARV.
# 
# Your notebook should:
# * Have *at least* 2 well documented and well named functions with docstrings.
# * Include a Markdown cell at the top of the notebook that outlines the overall workflow using pseudocode (i.e. plain language, not code)
# * Include additional Markdown cells throughout the notebook to describe: 
#     * the data that you used - and where it is from
#     * how data are being processing
#     * how the code is optimized to run fast and be more concise

# # Workflow overview
# ## Assignment outputs
# 1. Mean NDVI over a year for two sites
# 2. A .csv file of dataframe used to create plots that includes site name, date, and mean NDVI values
# 
# ## Steps required to complete project
# 1. Get a list of all directories with Landsat data for two sites of interest
# 2. Open each site directory, get Landsat scenes, and calculate mean NDVI for each scene for that site.
# * Get a list of all GeoTIFF files
# * Subset the list of files to just what is needed to calculate NDVI (files with bands)
# * Sort the list to have the bands in the same order
# * Open and crop the bands needed to calculate NDVI
# ** Write a function to open files and combine into an xarray object
# ** Write function to calculate NDVI from Landsat bands NIR = band 5, Red = band 4
# * Mask cloud cover from the scenes
# * Calculate mean NDVI for a scene
# 3. Output variables (mean NDVI, date, and site name) into a dataframe indexed on date.
# 4. Export the dataframe to a .csv file

# # Replace this cell with your pseudocode  for this workflow
# 
# If you happen to be a diagram person a diagram is ok too
# 
# 

# In[1]:


# Autograding imports - do not modify this cell
import matplotcheck.autograde as ag
import matplotcheck.notebook as nb
import matplotcheck.timeseries as ts
from datetime import datetime


# In[2]:


# Import needed packages in PEP 8 order
# and no unused imports listed (10 points total)

# YOUR CODE HERE
import os
from glob import glob

import matplotlib.pyplot as plt
from matplotlib import patches as mpatches, colors
from matplotlib.dates import DateFormatter
import seaborn as sns
import numpy as np
from numpy import ma
import pandas as pd
import geopandas as gpd
import xarray as xr
import rioxarray as rxr
from rasterio.plot import plotting_extent
import earthpy as et
import earthpy.spatial as es
import earthpy.plot as ep
import earthpy.mask as em


# Prettier plotting with seaborn
sns.set_style('white')
sns.set(font_scale=1.5)

# Download data and set working directory
data = et.data.get_data('ndvi-automation')
os.chdir(os.path.join(et.io.HOME,
                      'earth-analytics',
                      'data'))


# In[3]:


# DO NOT MODIFY THIS CELL
# Tests that the working directory is set to earth-analytics/data

path = os.path.normpath(os.getcwd())
student_wd_parts = path.split(os.sep)

if student_wd_parts[-2:] == ['earth-analytics', 'data']:
    print("\u2705 Great - it looks like your working directory is set correctly to ~/earth-analytics/data")
else:
    print("\u274C Oops, the autograder will not run unless your working directory is set to earth-analytics/data")


# # Figure 1: Plot 1 - Mean NDVI For Each Site Across the Year (50 points)
# 
# Create a plot of the mean normalized difference vegetation index (NDVI) for the two different sites in the United States across the year: 
# 
# * NDVI on the x axis and formatted dates on the y for both NEON sites on one figure/axis object.
# * Each site should be identified with a different color in the plot and legend.
# * The final plot **data should be cleaned to remove the influence of clouds**.
# * Be sure to include appropriate title and axes labels.
# 
# Add additional cells as needed for processing data (e.g. defining functions, etc), but be sure to:
# * follow the instructions in the code cells that have been provided to ensure that you are able to use the sanity check tests that are provided. 
# * include only the plot code in the cell identified for the final plot code below

# # Data description and processing
# I compared normalized difference vegetation index (NDVI) values from two NEON research sites with different regional characteristics. The San Joaquin Experimental Range (SJER) site is 18.2 km2 and located north of Fresno, CA at the foothills of the Sierra Nevada Mountains. The SJER climate is characterized as a Mediterranean climate with cool, wet winters (October-April) and hot, dry summers. SJER vegetation is characterized as grassy open oak woodland.
# The Harvard Forest (HARV) site is 48.1 km2 and located west of Boston, MA that spans a urban-rural gradient from the suburbs of Boston to northeast wildland. The HARV climate is temperate with stable annual precipitation. HARV vegetation is dominated by northern hardwood and coniferous forest and some agriculture. 
# Information on the sites: <a href="https://www.neonscience.org/field-sites/sjer" target="_blank">SJER</a> and <a href="https://www.neonscience.org/field-sites/harv" target="_blank">HARV</a>
# 
# I calculated NDVI from Landsat 8 multispectral data collected at the SJER site from 1/7/2017 to 12/25/2017 and HARV site from 1/12/2017 to 12/30/2017. I collected the near infrared (NIR) and red bands from each date that were available. Bands were processed for each site and date by setting the valid pixel range and masking out pixels that were classified as cloud cover. NDVI was calculated by taking the difference between NIR and red spectral values and dividing by the sum NIR and red bands. Mean NDVI was calculated for each scene by date. 
# 
# # Code optimization
# To accomplish the tasks, I developed code that could gather NIR and red bands for each of the dates and for each of the sites of interest to plot mean NDVI over the year. I created functions to open and clean bands and looped through scenes for each of the sites grabing the date from the file name. I was not able to get a nested loop to work to loop through each site but rather processed each site separately. This is an area that can be improved to reduce redundancy and simplify the code. To optimize the time it takes to run the code, I first calculated NDVI and then applied the cloud mask to that single layer - as opposed to applying the mask to each band layer separately. I also specified "from_disk = True" from rio.xarray to only open and load the specified crop layer. These steps helped to improve the speed and performance of the code. 

# ## Task 1: 
# 
# In the cell below, create a single dataframe containing MEAN NDVI, the site name, 
# and the date of the data for the HARV site 
# scene `HARV/landsat-crop/LC080130302017031701T1-SC20181023151837`.  The column names for the  final
# DataFrame should be`mean_ndvi`, and `site`, and the data should be **indexed on the date**. 
# 
# Use the functions that we reviewed in class (or create your own versions of them) to implement your code
# 
# ### In the Cell below Place  All Functions Needed to Run this Notebook (20 points)

# In[4]:


### DO NOT REMOVE THIS LINE OR EDIT / MOVE THIS CELL ###
start_time = datetime.now()


# In[3]:


# In this cell place all of the functions needed to run your notebook
# You will be graded here on function application, docstrings, efficiency so ensure
# All functions are placed here!

# YOUR CODE HERE

# FUNCTION TO OPEN A SINGLE LANDSAT BAND AND SPECIFY VALID PIXEL ATTRIBUTE RANGE
def open_clean_bands(band_path,
                     crop_extent,
                     valid_range=None,):
    """Open and mask a single landsat band using a pixel_qa layer.

    Parameters
    -----------
    band_path : string
        A path to the array to be opened
    valid_range : tuple (optional)
        A tuple of min and max range of values for the data. Default = None


    Returns
    -----------
    arr : xarray DataArray
        An xarray DataArray with values that should be masked 
        set to 1 for True (Boolean)
    """
    # TODO add tests to ensure the arrays are the same .shape
    band = rxr.open_rasterio(band_path, masked=True).rio.clip(crop_extent.geometry,
                                                              from_disk=True).squeeze()

    # Only run this step if a valid range tuple is provided
    if valid_range:
        mask = ((band < valid_range[0]) | (band > valid_range[1]))
        band = band.where(~xr.where(mask, True, False))

    return band


###############
#  FUNCTION TO OPEN and CLEAN UP SPECIFIC LANDSAT BANDS 
#  AND MASK USING PIXEL QA LAYER (CLOUD COVER) AND CALCULATE NDVI
def mask_crop_ndvi(band_paths,
                   crop_bound,
                   pixel_qa_path,
                   vals):
    """Open and mask a single landsat band using the open_clean_bands function, 
    calculate NDVI and mask using a pixel_qa layer.

    Parameters
    -----------
    band_paths : string
        A path to the landsat scene of interest
    all_bands : list
        A list containing two xarray objects for landsat bands 4 and  5
    crop_bound: geopandas GeoDataFrame
        A geopandas dataframe to crop the raster data using rasterio mask().
    pixel_qa_path: string
        A path to a pixel qa tif file.
    vals: list
        A list of values needed to create the cloud mask


    Returns
    -----------
    ndvi_crop : Xarray Dataset
        a cropped and masked xarray object containing NDVI values
    """
    # For loop using open_clean_bands function
    all_bands = []
    for aband in band_paths:
        cleaned_band = open_clean_bands(band_path=aband,
                                        crop_extent=crop_bound,
                                        valid_range=(0, 10000))
        all_bands.append(cleaned_band)

    crop_json = crop_bound.geometry

    # Open and clip qa layer
    pixel_qa = rxr.open_rasterio(pixel_qa_path[0], masked=True).rio.clip(crop_json,
                                                                         from_disk=True).squeeze()

    # Calculate NDVI
    ndvi_xr = (all_bands[1]-all_bands[0]) / (all_bands[1]+all_bands[0])

    # Apply cloud mask to NDVI
    ndvi_mask = ndvi_xr.where(~pixel_qa.isin(vals))

    return ndvi_mask


###############
#  FUNCTION to create a pandas dataframe from NDVI and grab site and date from file path


def mean_ndvi_df(ndvi_mask,
                 dir_path,
                 file_path):
    """Calculate the mean NDVI for a single site and scene with 
    NDVI calculated and clouds masked out

    Parameters
    -----------
    ndvi_mask : Xarray Dataset
        A cropped and masked xarray object containing NDVI values.
    dir_path: string 
        Path to the landsat site folders to grab the site name.
    file_path: string
        The name of a individual landsat scene file to grab the date.


    Returns
    -----------
    mean_ndvi_df : Pandas dataframe
        a dataframe of mean NDVI by site name and indexed on the date
    """

    # Calculate mean NDVI for the scene
    mean_ndvi = np.nanmean(ndvi_mask)

    # Grab site name from file path
    site = os.path.basename(os.path.normpath(dir_path))

    # Grab date from file name
    file_name = os.path.basename(file_path)
    date = file_name[10:18]

    # Create pandas dataframe
    data = {'date': [date],
            'site': [site],
            'mean_ndvi': [mean_ndvi]}
    mean_ndvi_df = pd.DataFrame(data, columns=['date', 'site', 'mean_ndvi'])
    mean_ndvi_df['date'] = pd.to_datetime(mean_ndvi_df['date'])  # date format
    mean_ndvi_df = mean_ndvi_df.set_index('date')  # index dataframe on date

    return mean_ndvi_df


# Note: "from_disk" needs updated rioxarray package


# In[4]:


# Create dataframe of mean NDVI in this cell using the functions created above
# Important: to use the ungraded tests below as a sanity check,
# name your columns: mean_ndvi and site
# Call the dataframe at the end of the cell so the tests run on it!
# Be sure that the date column is an index of type date
# HINT: the time series lessons may help you remember how to do this!

# Get a list of each directory
path = os.path.join("ndvi-automation", "sites")

# Get a list of both site directories
sites = glob(path + "/*/")

# Get the site name
site_name = os.path.basename(os.path.normpath(sites[0]))

# Open up the shapefile for clipping your landsat data to the study area for just HARV=sites[0]
vector_dir = os.path.join(sites[0],
                          "vector")

# Open crop boundary shapefile
site_boundary_path = os.path.join(vector_dir,  site_name + "-crop.shp")
crop_bound = gpd.read_file(site_boundary_path)

# Landsat cropped files for HARV site
landsat_dir = os.path.join(sites[0],
                           "landsat-crop")

# Open bands for specific Harvard site of interest
band_paths = sorted(glob(os.path.join(
    landsat_dir, "LC080130302017031701T1-SC20181023151837", "*band*[4-5].tif")))

# Cloud no data vals for Landsat 8 -
vals = [328, 392, 840, 904, 1350, 352, 368, 416,
        432, 480, 864, 880, 928, 944, 992, 480, 992]

# Open cloud mask layer
pixel_qa_path = glob(os.path.join(
    landsat_dir, "LC080130302017031701T1-SC20181023151837", "*qa*"))

# Run function to open, clean, and calculate NDVI and mask cloud pixels
ndvi_clean = mask_crop_ndvi(band_paths=band_paths,
                            crop_bound=crop_bound,
                            pixel_qa_path=pixel_qa_path,
                            vals=vals)

# Run function to create a dataframe of mean NDVI values by site and date
mean_ndvi = mean_ndvi_df(ndvi_mask=ndvi_clean,
                         dir_path=site_name,
                         file_path=os.path.join(landsat_dir, "LC080130302017031701T1-SC20181023151837"))
mean_ndvi


# In[7]:


# This cell  is testing your data output above

student_ndvi_ts_single_site = _

single_scene_points = 0

# Ensure the data is stored in a dataframe.
if isinstance(student_ndvi_ts_single_site, pd.DataFrame):
    print('\u2705 Your data is stored in a DataFrame!')
    single_scene_points += 1
else:
    print('\u274C It appears your data is not stored in a DataFrame. ',
          'To see what type of object your data is stored in, check its type with type(object)')

# Ensure that the date column is the index
if isinstance(student_ndvi_ts_single_site.index, pd.core.indexes.datetimes.DatetimeIndex):
    print('\u2705 You have the index set to the date column!')
    single_scene_points += 2
else:
    print('\u274C You do not have the index set to the date column.')

# Ensure that the date column is datetime
if isinstance(student_ndvi_ts_single_site.index[0], pd._libs.tslibs.timestamps.Timestamp):
    print('\u2705 The data in your date column is datetime!')
    single_scene_points += 2
else:
    print('\u274C The data in your date column is not datetime.')

# Ensure the site name is correct
if student_ndvi_ts_single_site.site.values[0] == 'HARV':
    print('\u2705 You have the correct site name!')
    single_scene_points += 5
else:
    print('\u274C You do not have the correct site name.')

if np.allclose(0.281131628228094, student_ndvi_ts_single_site.mean_ndvi.values[0]):
    print('\u2705 You have the correct mean NDVI value!')
    single_scene_points += 5
else:
    print('\u274C You do not have the correct mean ndvi value.')

print("\n \u27A1 You received {} out of 15 points for creating a dataframe.".format(
    single_scene_points))
single_scene_points


# ## Task 2:
# 
# In the cell below, process all of the landsat scenes. Create a DataFrame that contains the following 
# information for each scene
# 
# 
# |   | index  | site  | mean_ndvi  | 
# |---|---|---|---|
# | Date  |   |   |   |
# |  2017-01-07  | 0  | SJER  | .4  |  
# 
# Be sure to call your dataframe at the end of the cell to ensure autograding works.
# HINT: FOR THIS STEP, leave any rows containing missing values (`NAN`).

# In[5]:


# Create dataframe of NDVI including the cleaning data to deal with clouds

# Important: to use the ungraded tests below as a sanity check,
# name your columns: mean_ndvi and site
# Don't forget to set date as the index and make the values of type datetime

# YOUR CODE HERE
# RUN FOR EACH SITE SEPARATELY BC HAVING TROUBLE WITH NESTED FOR LOOP
# Get a list of each directory
#path = os.path.join("ndvi-automation", "sites")

# Get a list of both site directories
#sites = glob(path + "/*/")


# Cloud no data vals for Landsat 8 -
# vals = [328, 392, 840, 904, 1350, 352, 368, 416,
#        432, 480, 864, 880, 928, 944, 992, 480, 992]

# HARVARD
# Get the site name
site_name = os.path.basename(os.path.normpath(sites[0]))

# Open up the shapefile for clipping your landsat data to the study area for just HARV=sites[0]
vector_dir = os.path.join(sites[0],
                          "vector")

# Open crop boundary shapefile
site_boundary_path = os.path.join(vector_dir,  site_name + "-crop.shp")
crop_bound = gpd.read_file(site_boundary_path)

# Landsat cropped files for HARV site
landsat_dir = os.path.join(sites[0], "landsat-crop")

# FOR LOOP THROUGH SCENES IN HARVARD SITE
scene_paths = sorted(glob(os.path.join(landsat_dir, "LC08*")))

mean_ndvi_all_harv = []
for ascene in scene_paths:
    ndvi_clean = mask_crop_ndvi(band_paths=sorted(glob(os.path.join(ascene, "*band*[4-5].tif"))),
                                crop_bound=crop_bound,
                                pixel_qa_path=glob(
                                    os.path.join(ascene, "*qa*")),
                                vals=vals)
    # Create dataframe of mean ndvi values from the cleaned up ndvi scene
    site_mean_ndvi = mean_ndvi_df(ndvi_clean,
                                  dir_path=site_name,
                                  file_path=ascene)
    mean_ndvi_all_harv.append(site_mean_ndvi)
    mean_ndvi_all_harv_df = pd.concat(mean_ndvi_all_harv)

# mean_ndvi_all_harv_df

# SAN JOAQUIN EXPERIMENTAL STATION
site_name_sjer = os.path.basename(os.path.normpath(sites[1]))

# Directory to shapefile
vector_dir_sjer = os.path.join(sites[1],
                               "vector")

# Open crop boundary shapefile
site_boundary_path_sjer = os.path.join(
    vector_dir_sjer,  site_name_sjer + "-crop.shp")
crop_bound_sjer = gpd.read_file(site_boundary_path_sjer)

# Landsat cropped files for HARV site
landsat_dir_sjer = os.path.join(sites[1],
                                "landsat-crop")

# Path to site scenes
scene_paths_sjer = sorted(glob(os.path.join(landsat_dir_sjer, "LC08*")))

# FOR LOOP THROUGH SCENES IN SJER SITE
scene_paths = sorted(glob(os.path.join(landsat_dir, "LC08*")))

mean_ndvi_all_sjer = []
for ascene in scene_paths_sjer:
    ndvi_clean_sjer = mask_crop_ndvi(band_paths=sorted(glob(os.path.join(ascene, "*band*[4-5].tif"))),
                                     crop_bound=crop_bound_sjer,
                                     pixel_qa_path=glob(
                                         os.path.join(ascene, "*qa*")),
                                     vals=vals)

    # Create dataframe of mean ndvi values from the cleaned up ndvi scene
    site_mean_ndvi_sjer = mean_ndvi_df(ndvi_clean_sjer,
                                       dir_path=site_name_sjer,
                                       file_path=ascene)
    mean_ndvi_all_sjer.append(site_mean_ndvi_sjer)
    mean_ndvi_all_sjer_df = pd.concat(mean_ndvi_all_sjer)

# Concatenate two dataframes from each site into a single dataframe
mean_ndvi_all_sites = pd.concat(
    [mean_ndvi_all_harv_df, mean_ndvi_all_sjer_df], axis=0)
mean_ndvi_all_sites


# In[9]:


# Last sanity check before creating your plot (10 points)

# Ensure that you call your dataframe at the bottom of the cell above
# and that it has columns called: mean_ndvi and site

# Ensure the data is stored in a dataframe.
student_ndvi_df = _

df_points = 0

if isinstance(student_ndvi_df, pd.DataFrame):
    print('\u2705 Your data is stored in a DataFrame!')
    df_points +=2
else:
    print('\u274C It appears your data is not stored in a DataFrame. ',
          'To see what type of object your data is stored in, check its type with type(object)')

# Check that dataframe contains the appropriate number of NAN values
if student_ndvi_df.mean_ndvi.isna().sum() == 15:
    print('\u2705 Correct number of masked data values!')
    df_points +=2
else:
    print('\u274C The amount of null data in your dataframe is incorrect.')


# Ensure that the date column is the index
if isinstance(student_ndvi_df.index, pd.core.indexes.datetimes.DatetimeIndex):
    print('\u2705 You have the index set to the date column!')
    df_points +=3
else:
    print('\u274C You do not have the index set to the date column.')

# Ensure that the date column is datetime
if isinstance(student_ndvi_df.index[0], pd._libs.tslibs.timestamps.Timestamp):
    print('\u2705 The data in your date column is datetime!')
    df_points +=3
else:
    print('\u274C The data in your date column is not datetime.')

# Output for timer, # DO NOT MODIFY
end_time = datetime.now()
total_time = end_time - start_time
print(
    "Your total run time for processing the data was {0}.".format(total_time))

print("\n \u27A1 You received {} out of 10 points for creating a dataframe.".format(
    df_points))

df_points


# In[10]:


# Add only the plot code to this cell

# This is the final figure of mean NDVI
# for both sites across the year
# with data cleaned to deal with clouds

# YOUR CODE HERE
# Resample by month
test = mean_ndvi_all_sites.groupby(
    ['site'])[['mean_ndvi']].resample('M').mean()
# Reset so only index on date
test.reset_index(inplace=True)
mean_ndvi_for_plot = test.set_index('date')

fig, ax = plt.subplots(figsize=(10, 10))

fig.suptitle(
    "Mean Normalized Difference Vegetation Index (NDVI)\n Jan 2017 - Dec 2017", fontsize=16)

mean_ndvi_for_plot.groupby('site')['mean_ndvi'].plot(legend=True,
                                                     ax=ax,
                                                     marker='o')

ax.set(xlabel="Month",
       ylabel="Mean NDVI",
       title="Mean NDVI 2017")

# Define the date format
date_form = DateFormatter("%b")  # %m-%d
ax.xaxis.set_major_formatter(date_form)

### DO NOT REMOVE LINES BELOW ###
final_masked_solution = nb.convert_axes(plt, which_axes="current")


# In[11]:


# Ignore this cell for the autograding tests


# In[12]:


# Ignore this cell for the autograding tests


# # Question 1 (10 points)
# 
# Imagine that you are planning NEON’s upcoming flight season to capture remote sensing data in these locations and want to ensure that you fly the area when the vegetation is the most green.
# 
# When would you recommend the flights take place for each site? 
# 
# Answer the question in 2-3 sentences in the Markdown cell below.

# Mean NDVI values are the greatest from June to end of September at the Harvard site and from Februar to April at the San Joaquin Experimental Range. These time periods are when the vegetation at each respective site is most green. 

# # Question 2 (10 points)
# 
# How could you modify your workflow to look at vegetation changes over time in each site? 
# 
# Answer the question in 2-3 sentences in the Markdown cell below.

# Adding Landsat scenes for other years would allow one to look at vegetation changes over time at each site. The workflow can be modified by adding another layer to loop through each year of data that is available. 

# # Do not edit this cell! (10 points)
# 
# The notebook includes:
# * additional Markdown cells throughout the notebook to describe: 
#     * the data that you used - and where it is from
#     * how data are being processing
#     * how the code is optimized to run fast and be more concise

# # Do not edit this cell! (20 points)
# 
# The notebook will also be checked for overall clean code requirements as specified at the **top** of this notebook. Some of these requirements include (review the top cells for more specifics): 
# 
# * Notebook begins at cell [1] and runs on any machine in its entirety.
# * PEP 8 format is applied throughout (including lengths of comment and code lines).
# * No additional code or imports in the notebook that is not needed for the workflow.
# * Notebook is fully reproducible. This means:
#    * reproducible paths using the os module.
#    * data downloaded using code in the notebook.
#    * all imports at top of notebook.

# ## BONUS - Export a  .CSV File to Share (10 points possible)
# 
# This is optional - if you export a **.csv** file with the columns specified above: Site, Date and NDVI Value you can get an additional 10 points.
# 
# * FULL CREDIT: File exists in csv format and contains the columns specified.
# We will check your github repo for this file!
# 

# In[13]:


# Export mean NDVI dataframe as .csv file in "outputs" folder
# If the dir does not exist, create it
output_path = os.path.join("ndvi-automation",
                           "outputs")

if not os.path.isdir(output_path):
    os.mkdir(output_path)

# Export the buffered point layer as a shapefile to use in zonal stats
mean_ndvi_path = os.path.join(output_path,
                                "mean_ndvi_all_sites.csv")

mean_ndvi_all_sites.to_csv(mean_ndvi_path)


#mean_ndvi_all_sites
#df.to_csv('hrdata_modified.csv')

