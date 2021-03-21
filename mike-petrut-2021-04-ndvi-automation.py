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
# **Mike Petrut**

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
***Workflow for Mean NDVI Modelling***

1. Get list of all directories and associated site names.

2. Open each site directory, get Landsat scenes, and calculate mean NDVI for each scene for that site.
   # Steps for calculating the mean NDVI for each Landsat Scene
   1. Create a loop that reads the site and date from each directory
   2. Sort the bands by number 
   3. Crop to the extent of the focus shapefile
   4. Mask to the range of Landsat Values 
   5. Optionally clean the image using the pixel cloud cover image 
   
3. Capture results (including mean NDVI, date, and site name) to a list or dataframe.
   # Steps for sorting the table
   1. append all values from the looped tasks in Step 2
   2. Create pandas data frame, setting date as index 
   
4. Export dataframe with mean NDVI values to csv.
# In[1]:


# Autograding imports - do not modify this cell
import matplotcheck.autograde as ag
import matplotcheck.notebook as nb
import matplotcheck.timeseries as ts
from datetime import datetime


# In[2]:


# Import necessary packages
import os
from glob import glob
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from shapely.geometry import box
import geopandas as gpd
import xarray as xr
import rasterio as rio
import rioxarray as rxr
from rasterio.plot import plotting_extent
from rasterio.mask import mask
import earthpy as et
import earthpy.spatial as es
import earthpy.plot as ep
from datetime import datetime
import matplotlib.dates as mdates


# Get the data
data = et.data.get_data('ndvi-automation')

# Set working directory
os.chdir(os.path.join(et.io.HOME, 'earth-analytics', 'data'))


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


# In this cell place all of the functions needed to run your notebook
# You will be graded here on function application, docstrings, efficiency so ensure
# All functions are placed here!

def combine_tifs(tif_list):
    
    """A function that combines a list of tifs in the same CRS
    and of the same extent into an xarray object

    Parameters
    ----------
    tif_list : list
        A list of paths to the tif files that you wish to combine.

    Returns
    -------
    An xarray object with all of the tif files in the listmerged into 
    a single object.

    """
    out_xr = []
    for i, tif_path in enumerate(tif_list):
        out_xr.append(rxr.open_rasterio(tif_path, masked = True).squeeze())
        out_xr[i]["band"] = i + 1

    return xr.concat(out_xr, dim = "band")

def ndvi_mean(main_path, cloud_mask):
    
    """A function that takes a file path of Landsat imagery (which includes 
    separate .tif files for different bands), and combines the files as an
    xarray, then calculates the NDVI.
    
    The function includes the following tasks:
    
    1) Read in the path, sort the files in each imagery file by band number 
    2) Find the cropping extent file for each site 
       (assuming this is a shapefile)
    3) Combine imagery as a xarray and apply the pixel mask 
       if cloud mask is entered as True
    4) Mask the file to the Landsat range 0:10000
    5) Calculate the NDVI and Mean NDVI values 
    6) Append the loop results to the list
    7) Summarise the appended lists ass a pandas data frame, 
       convert the string extracted date as
       date-time and assign to the index
    8) Return panel data frame of mean NDVI values, 
       with key = site and index = date 
    
    The function finally calculates the mean for all file paths and combines them as a pandas
    data frame.
    
    The function extracts the site and date from the Landsat path file and adds 
    them as columns to the table, the 
    
    Parameters
    ----------
    
    Path_list : list
        A list of paths to the paths of tif files that you wish to combine.
        
    cloud_mask : logical
        True or False based on whether you want the function 
        to apply the cloud cover layer to clean the data

    Returns
    -------
    A pandas dataframe of mean NDVI values from the main path provided
    
    """
    
    #Create ists to append looped values to 
    all_mean = []
    dates = []
    sites = []

    # Specify the valid range of values for landsat
    valid_range = (0, 10000)
    
    # Cloud no data vals for Landsat 8 -
    vals = [328, 392, 840, 904, 1350, 352, 368, 416,
            432, 480, 864, 880, 928, 944, 992, 480, 992]
    
    paths = glob(os.path.join(main_path, "*/"))

    for path in paths:
        
        # Extract site from path
        site = os.path.basename(os.path.normpath(path))  
        
        # Extract list of imigery file paths
        band_files = glob(os.path.join(path, 'landsat-crop', "*/"))
        
        # Isolate path to shapefile needed for cropping 
        crop_path = glob(os.path.join(path, 'vector', "*.shp"))[0]
        
        # Import the cropping shapefile
        crop_shape = gpd.read_file(crop_path)
        
        # Create loop to calculate for all imigery files in the site folders
        for files in band_files:
            
            # Sort files by band
            sorted_files = sorted(glob(os.path.join(files, '*band*')))
            
            # Use combined_tif fuction to crease an xarray from the sorted tif files 
            combined_tif = combine_tifs(sorted_files)
            
            # Crop the newly combined imagery file to the cropped shape
            ## Each site has one cropping shape file, hence why it is defined in the path loop not the file loop
            combined_crop = combined_tif.rio.clip(crop_shape.geometry, from_disk = True).squeeze()             
            
            # Define cropped xarray as either filtered to the pixel could cover imagery or not 
            
            if(cloud_mask == True):
                
                pixel_qa_path = glob(os.path.join(files, "*qa*"))
                pixel_qa = rxr.open_rasterio(pixel_qa_path[0], 
                                             masked = True).rio.clip(crop_shape.geometry,
                                                                     from_disk = True).squeeze()
                combined_crop = combined_crop.where(~pixel_qa.isin(vals))
                
            else: combined_crop
            
            # Mask the cropped range to the Landsat 8 values range
            if valid_range:
                mask = ((combined_crop < valid_range[0]) | (combined_crop > valid_range[1]))
                combined_crop = combined_crop.where(~xr.where(mask, True, False))
            
            # Calculate the NDVI - 
            ## Function will not run properly if this is changed the the earthpy normalized_diff fuction - Do not change
            ndvi = (combined_crop[4] - combined_crop[3]) / (combined_crop[4] + combined_crop[3]) 
            
            # Calc the mean NDVI
            ndvi_mean = np.nanmean(ndvi)
            
            # Isolate filename from the path 
            file_name = os.path.basename(os.path.normpath(files))
            
            # Extract date values from the file name string
            date = file_name[10:18]
            
            #image - file_name[1:18]
            
            # Append looped values to the predefined lists 
            dates.append(date)
            sites.append(site)
            all_mean.append(ndvi_mean)     
            
            # Generate pandas dataframe from the three lists 
            ndvi_mean_df = pd.DataFrame({'date': dates,
                                         'site': sites,
                                         'mean_ndvi': all_mean})
    
    # Coerce date string to date-time values 
    ndvi_mean_df['date'] = pd.to_datetime(ndvi_mean_df['date'], format = '%Y%m%d')
    
    # Set index as the date values 
    ndvi_mean_df.set_index('date', inplace = True)
    
    return ndvi_mean_df


def ndvi_filter_date(image_directory):
    
    """A function that extracts the date of image collection from the imagery path name

    Parameters
    ----------
    directory: directory to file including study 
    site e.g: "'HARV/landsat-crop/LC080130302017031701T1-SC20181023151837'"
    
    Returns
    -------
    Date string of the image directory

    """
    filter_path = image_directory
    filter_year = filter_path[28:32]
    filter_month = filter_path[32:34]
    filter_day = filter_path[34:36]

    filter_date = filter_year + "-" + filter_month + "-" + filter_day

    return filter_date


def ndvi_filter_site(image_directory):
    
    """A function that extracts the site name from the imagery path name

    Parameters
    ----------
    directory: directory to file including study 
    site e.g: "'HARV/landsat-crop/LC080130302017031701T1-SC20181023151837'"
    
    Returns
    -------
    Date string of the image site

    """
    filter_path = image_directory
    filter_site = filter_path[0:4]

    return filter_site


# In[6]:


# Create dataframe of mean NDVI in this cell using the functions created above
# Important: to use the ungraded tests below as a sanity check,
# name your columns: mean_ndvi and site
# Call the dataframe at the end of the cell so the tests run on it!
# Be sure that the date column is an index of type date
# HINT: the time series lessons may help you remember how to do this!


sanity_date = ndvi_filter_date('HARV/landsat-crop/LC080130302017031701T1-SC20181023151837')

sanity_site = ndvi_filter_site('HARV/landsat-crop/LC080130302017031701T1-SC20181023151837')

main_path = os.path.join('ndvi-automation', 'sites')

ndvi_mean_results = ndvi_mean(main_path, cloud_mask = False)

ndvi_mean_results[(ndvi_mean_results.index == sanity_date) & (ndvi_mean_results['site'] == sanity_site)]


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
# Important: to use the ungraded tests below as a sanity check,
# name your columns: mean_ndvi and site
# Don't forget to set date as the index and make the values of type datetime

###__________________________________________________________

# Call 
ndvi_mean_cloud_cover = ndvi_mean(main_path, cloud_mask = True)
ndvi_mean_cloud_cover 


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

###___________________________AX1______________________________

# Remove NaNs from cleaned dataset 
ndvi_mean_cloud_cover_exnan = ndvi_mean_cloud_cover.dropna()

# Set Colors
color_map = {'HARV' : '#7BBDD6',
             'SJER' : '#140034'}

months = mdates.MonthLocator()  # every month

fig, (ax1,ax2) = plt.subplots(2, 1, 
                              figsize = (12,15),  
                              constrained_layout = False)

for label, grp in ndvi_mean_results.groupby("site"):
    grp.plot(use_index = True,
             y = 'mean_ndvi',
             ax = ax1,
             color = color_map[label],
             label = label,
             style = '.-',
             markersize = 12)

    
# Set up formatting for graph 

ax1.set_xlabel('Date', fontsize=16)
ax1.set_ylabel('Mean NDVI', fontsize=16)
ax1.set_title('Mean Normalized Difference Vegetation Index (NDVI) \n Jan 2017- Dec-2017 \n Landsat 8 Not Cleaned', 
              fontsize = 18)

ax1.legend(fontsize = 12)

ax1.xaxis.set_major_formatter(mdates.DateFormatter('%b'))

ax1.tick_params(axis = 'both',
               which = 'major', 
               labelsize = 12)

ax1.set_ylim([0, 1])

ax1.grid(True)

###____________________________AX2______________________________

for label, grp in ndvi_mean_cloud_cover_exnan.groupby("site"):
    grp.plot(use_index = True,
             y = 'mean_ndvi',
             ax = ax2,
             color = color_map[label],
             label = label,
             style = '.-',
             markersize = 12)
    
# Set title and label axes
ax2.set(xlabel = "Date",
        ylabel = "Mean NDVI",
        title = "NDVI")

# Set up formatting for graph 

ax2.set_xlabel('Date', fontsize = 16)
ax2.set_ylabel('Mean NDVI', fontsize = 16)
ax2.set_title('Mean Normalized Difference Vegetation Index (NDVI) \n Jan 2017- Dec-2017 \n Landsat With Clouds Removed', 
              fontsize = 18)

ax2.legend(fontsize = 12)

ax2.xaxis.set_major_formatter(mdates.DateFormatter('%b %y'))

ax2.tick_params(axis = 'both',
               which = 'major', 
               labelsize = 12)

ax2.set_ylim([0, 1]) 

ax2.grid(True)

fig.tight_layout(pad = 2.5) 

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

# For the HARV study area it would be recommended that to avoid cloud cover and gather high vegetation imagery that the flight taken place late-August to September.
# 
# For the SJER study area it would be recommended that to avoid cloud cover and gather high vegetation imagery that the flight taken place late-Feb to March.

# # Question 2 (10 points)
# 
# How could you modify your workflow to look at vegetation changes over time in each site? 
# 
# Answer the question in 2-3 sentences in the Markdown cell below.

# To better understand the vegetation changes over time we could modify the workflow to classify each NDVI model to categorise the xarray into bins for not-vegetation (-1 to 0.19), low vegetation (0. 2 to 0.5) and high vegetation (0.501 to 1.0) and calculate both the mean and total observations of he three bins to see where areas of land have maintained lose or gained vegetation across the categorisations. This would be useful to understand the impact of seasonal variables such as weather and rainfall on the vegetation index over time.  

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


### CSV EXPORT ###

# Set working directory
os.chdir(os.path.join(et.io.HOME, 
                      'earth-analytics', 
                      'ea-2021-04-ndvi-automation-mike-petrut',
                      'csv_output'))


ndvi_mean_results.to_csv('ndvi_mean_no_clean.csv', index = True)

ndvi_mean_cloud_cover_exnan.to_csv('ndvi_mean_clean.csv', index = True)

# Revert working directory
os.chdir(os.path.join(et.io.HOME, 'earth-analytics', 'data'))

