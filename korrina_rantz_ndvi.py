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
# **Your Name: Korrina Rantz**

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

# # Replace this cell with your pseudocode  for this workflow
# 
# If you happen to be a diagram person a diagram is ok too
# 
# 

# Goal: Calculate and plot the mean normalized difference vegetation index (NDVI) for two Landsat scenes. Include functions so more scenes or time could be easily added. To accomplish this use the following steps:
# 1. Create functions to automate workflow
# 2. Open the data, use glob to access necessary files
# 3. Get study area crop file and open with .gpd to create boundary
# 4. Get .tif files for bands 4 and 5, open and clip using function created above
# 5. Get values to create cloud mask
# 6. Open and clip cloud mask layer
# 7. Use function created above to open and mask landsat band using a pixel_qa layer, calculate NDVI
# 8. Use numpy function np.nanmean(xarray_name) to calculate the mean
# 9. Create pandas dataframe date with NDVI mean values, site name and indexed date
# 10. Plot the data

# In[1]:


# Autograding imports - do not modify this cell
import matplotcheck.autograde as ag
import matplotcheck.notebook as nb
import matplotcheck.timeseries as ts
from datetime import datetime


# In[2]:


# Import packages
import os
from glob import glob

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import geopandas as gpd
import rioxarray as rxr
import xarray as xr
import earthpy as et

# Get data and set working directory
data = et.data.get_data('ndvi-automation')
os.chdir(os.path.join(et.io.HOME,
                      "earth-analytics",
                      "data"))


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


# In[5]:


# Functions needed to run notebook

def open_clean_bands(band_path,
                     crop_extent,
                     valid_range=None,):
    """Opens and crops a single landsat band using a vector file.

    Parameters
    -----------
    band_path : string
        A path to the array to be opened
    crop_extent : geopandas GeoDataFrame
        A geopandas dataframe to be used to crop the raster data using rasterio mask().
    valid_range : tuple (optional)
        A tuple of min and max range of values for the data. Default = None


    Returns
    -----------
    arr : xarray DataArray
        An xarray DataArray with values that should be masked set to 1 for True (Boolean)
    """
    band = rxr.open_rasterio(band_path, masked=True).rio.clip(crop_extent.geometry,
                                                              from_disk=True).squeeze()

    if valid_range:
        mask = ((band < valid_range[0]) | (band > valid_range[1]))
        band = band.where(~xr.where(mask, True, False))

    return band

# This function opens the cloud mask, calculates NDVI & masks the data


def mask_crop_ndvi(all_bands,
                   crop_bound,
                   pixel_qa_path,
                   vals):
    """Open and mask landsat band/s using a pixel_qa layer. Create a cloud mask.
    Calculate NDVI with applied cloud mask. 

    Parameters
    -----------
    all_bands : list
        A list containing two xarray objects for landsat bands 4 and  5
    crop_bound: geopandas GeoDataFrame
        A geopandas dataframe to be used to crop the raster data using rasterio mask().
    pixel_qa_path: string
        A path to a pixel qa tif file.
    vals: list
        A list of values needed to create the cloud mask


    Returns
    -----------
    ndvi_crop : Xarray Dataset
        a cropped and masked xarray object containing NDVI values
    """

    crop_json = crop_bound.geometry

    # Open and clip qa layer
    pixel_qa = rxr.open_rasterio(pixel_qa_path[0], masked=True).rio.clip(crop_json,
                                                                         from_disk=True).squeeze()

    # Calculate NDVI
    ndvi_xr = (all_bands[1]-all_bands[0]) / (all_bands[1]+all_bands[0])
    # Apply cloud mask to NDVI
    ndvi_mask = ndvi_xr.where(~pixel_qa.isin(vals))

    return ndvi_mask


# Created two functions for repetitive tasks in the notebook. These functions will be reusable, create fewer variables and make updates and additions to the code easier.  

# In[6]:


# Create dataframe of mean NDVI in this cell using the functions created above
# Create path for single directory
harv_dir = os.path.join("ndvi-automation", "sites", "HARV", "landsat-crop",
                        "LC080130302017031701T1-SC20181023151837")

# Parse out date and site_name to add into dataframe
date = harv_dir[-29:-21]
site = harv_dir[22:26]

# Open crop
harv_crop_path = os.path.join("ndvi-automation", "sites", "HARV",
                              "vector", "HARV-crop.shp")
harv_crop_bound = gpd.read_file(harv_crop_path)

# Open and sort bands needed to calculate NDVI, use function to combine bands
harv_dir = os.path.join("ndvi-automation", "sites", "HARV", "landsat-crop",
                        "LC080130302017031701T1-SC20181023151837")
harv_bands_path = sorted(glob(os.path.join(harv_dir, "*band[4-5]*.tif")))

# Apply function that opens & clips the data using loop for both bands
all_bands = []
for aband in harv_bands_path:
    cleaned_band = open_clean_bands(band_path=aband,
                                    crop_extent=harv_crop_bound,
                                    valid_range=(0, 10000))
    all_bands.append(cleaned_band)

# Cloud no data vals
vals = [328, 392, 840, 904, 1350, 352, 368, 416,
        432, 480, 864, 880, 928, 944, 992, 480, 992]
# Open cloud mask layer
pixel_qa_path = glob(os.path.join(harv_dir, "*qa*"))
# Open and mask landsat band using a pixel_qa layer, calculate NDVI
harv_ndvi_clean = mask_crop_ndvi(all_bands=all_bands,
                                 crop_bound=harv_crop_bound,
                                 pixel_qa_path=pixel_qa_path,
                                 vals=vals)
# Get mean from ndvi_clean
harv_ndvi_mean = np.nanmean(harv_ndvi_clean)

# Create dataframe, append and name columns
data = {"date": [date], "site": [site], "mean_ndvi": [harv_ndvi_mean]}
harv_df = pd.DataFrame(data=data)
harv_df['date'] = pd.to_datetime(harv_df['date'])
harv_df = harv_df.set_index('date')
harv_df


# Able to use the open_clean_bands function to open multiple bands, crop to the needed extent and within the valid range.  The steps within this code help save time with processing because only the data needed in the crop extent is processed rather than the full dataset.  Putting this function into a loop allows you to iterate through all of the bands that need to be opened and cropped.  The second function is also used to calculate the NDVI with the cloud mask.  Putting the mask in the functions saves steps so you do not have to repeatedly mask data.  Again a crop is used so processing time is saved by just processing a slice.  

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

# In[8]:


# Create dataframe of NDVI including the cleaning data to deal with clouds
# Unable to complete can not figure out how/why/where code breaks

# Capture  the site name, and  date in  a list
# Important: to use the ungraded tests below as a sanity check,
# name your columns: mean_ndvi and site
# Don't forget to set date as the index and make the values of type datetime

# Create paths
path = os.path.join("ndvi-automation", "sites")
sites = glob(path + "/*/")
all_dirs = glob(os.path.join(path, "*/"))
crop_sites = glob(os.path.join(path, "*", "vector", "*.shp"))
landsat_dirs = glob(os.path.join(path, "*", "landsat-crop", "LC08*"))

all_sites = []
for a_dir in all_dirs:
    print(a_dir)
    crop_bound = gpd.read_file(crop_path)
    crop_site.append(crop_bound)

# Loop through and sort all 4-5 band .tif files
for a_dir in landsat_dirs:
    bands_path = sorted(glob(os.path.join(a_dir, "*band[4-5]*.tif")))

    # Apply function that opens & clips the data using loop for both bands
    all_bands_2 = []
    for a_band in bands_path:
        clean_band = open_clean_bands(band_path=bands_path,
                                      crop_extent=crop_bound,
                                      valid_range=(0, 10000))
        all_bands_2.append(clean_band)
# Cloud no data vals
        vals = [328, 392, 840, 904, 1350, 352, 368, 416,
                432, 480, 864, 880, 928, 944, 992, 480, 992]
# Loop through all cloud mask layer
        for qa_file in landsat_dirs:
            pixels_qa_path = glob(os.path.join(qa_file, "*qa*"))
# Open and mask landsat band using a pixel_qa layer

            ndvi_clean = mask_crop_ndvi(all_bands=all_bands_2,
                                        crop_bound=crop_bound,
                                        pixel_qa_path=pixels_qa_path,
                                        vals=vals)
        # Get mean from ndvi_clean
            ndvi_mean = np.nanmean(ndvi_clean)
            all_sites.append(ndvi_mean)


# Side note: I think this code is more broken than the original I turned in.
# Ideally the loops and functions would have saved steps and processing time on a larger scale than just the single site.  Adding the nested loop would allow you to loop through multiple sites and bands. It is important to have a list [] or dictionary {} to store data in so that it is not just over written. 

# In[ ]:


# Create dataframe
sitename = os.path.basename(os.path.normpath(a_crop[-13:-9]))
date = os.path.basename(os.path.normpath(a_band))
date = date[26:34]
data_2 = {"date": [date], "site": [sitename], "mean_ndvi": [ndvi_mean]}
ndvi_df = pd.DataFrame(data=data_2)
ndvi_df['date'] = pd.to_datetime(ndvi_df['date'])
ndvi_df = ndvi_df.set_index('date')
ndvi_df


# In[ ]:


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


# In[ ]:


# Add only the plot code to this cell
# Unable to complete/ figure out without dataframe

# This is the final figure of mean NDVI
# for both sites across the year
# with data cleaned to deal with clouds
# Define plot space
fig, ax = plt.subplots(figsize=(10, 10))
fig.suptitle(
    "Landsat 8 - Clouds Removed \n Mean Normalized Difference Vegetetation Index (NDVI)",
    fontsize=20)

# Create a dictionary with site atrributes
label_dict = {'SJER': 'SJER', 'HARV': 'HARV'}
color_map = {'SJER': 'green', 'HARV': 'magenta'}

# Create a for loop to plot data
for label, grp in all_sites.groupby(['site']):
    grp.plot(date.index,
             y='mean_ndvi',
             ax=ax,
             label=label_dict[label],
             color=color_map[label],
             marker="o")
# Set plot labels
ax.set(xlabel="Date",
       ylabel="Mean NDVI")

plt.tight_layout()
plt.show()


### DO NOT REMOVE LINES BELOW ###
final_masked_solution = nb.convert_axes(plt, which_axes="current")


# In[ ]:


# Ignore this cell for the autograding tests


# In[ ]:


# Ignore this cell for the autograding tests


# # Question 1 (10 points)
# 
# Imagine that you are planning NEON’s upcoming flight season to capture remote sensing data in these locations and want to ensure that you fly the area when the vegetation is the most green.
# 
# When would you recommend the flights take place for each site? 
# 
# Answer the question in 2-3 sentences in the Markdown cell below.

# If I were planning NEON's upcoming flight season and wanted to capture when the vegetation is the most green I would plan flights throughout the summer for the Harvard site. NDVI values are consistently high from mid-May until mid-September.  The SJER sight would have a different flight plan and the most green would be seen in the Spring, mid-March through April.

# # Question 2 (10 points)
# 
# How could you modify your workflow to look at vegetation changes over time in each site? 
# 
# Answer the question in 2-3 sentences in the Markdown cell below.

# To look at vegetation changes over time we would need more data.  The data files could be combined with the current ones adding more years.  If the data collected was the same Landsat data these files could be combined with the current files and you would just have to update the data and make sure the file paths remained the same. You could use the existing functions and loops to look at data over a longer period of time.

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
