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
# **Your Name:** Avra Saslow

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

# # Psuedocode for just HARV site
# 1. Go within 'ndvi-automation' folder four levels down to access tif files for HARV
# 2. Extract and sort bands 4-5 
# 3. Open up the bands with function open_clean_bands
#     - this will use rxr to open the raster, and crop_boundary as a crop extent
# 4. Calculate NDVI
# 5. Obtain QA data from landsat files for cloud mask
#     -extract all files from a tif folder that end in "pixel.tif"
#     -open up that qa data with rxr
# 6. Create cloud mask from ep cloud pixels
#     -refer to textbook for this 
# 7. Get the mean of the new masked xarray
# 8. Create df with 3 columns: mean, the site name, and the date in datetime
# 
# # Psuedocode for both sites
# Mostly the same as above, except we can't just name the tif file for a specific site. So...
# 1. One for loop for each site directory
# 2. A nested loop for each landsat file directory 
# 4. Extract just files for bands 4-5
# 3. Another nested for loop for each band in band folder
# 3. Open up the bands with function open_clean_bands
# 4. Calculate NDVI
# 5. Obtain QA data from landsat files for cloud mask 
#     - using cloud mask function
# 6. I'll have already created cloud mask from ep cloud pixels - don't need to repeat because it doesn't change
# 7. Get the mean of the new masked xarray
# 8. Create df with 3 columns: mean, the site name, and the date in datetime
#     - create list to do so 
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
import numpy as np
import pandas as pd
import geopandas as gpd
import rioxarray as rxr
import xarray as xr
from rasterio.plot import plotting_extent
import earthpy as et
import earthpy.mask as em
import earthpy.spatial as es
import earthpy.plot as ep

#set working directory

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


# _This first code block does quite a lot of the exploration of ndvi-automation folder structure. It sets path variables for the HARV site, creates the crop extent for that specific site, and opens the specific tif folder for LC080130302017031701T1-SC20181023151837. Finally, it extracts just the bands 4-5 to calculate the NDVI._
# 
# _Because this is just one site, there isn't really a better way to build a function or a for loop that will optimize this workflow._

# In[5]:


#----------------------------------------------
#exploration of folder structure
#----------------------------------------------

# list both site directories 
site_path = os.path.join("ndvi-automation", "sites")

# Get a list of both site directories 
sites = glob(site_path + "/*/")
#sites

#specifically create df for HARV site
site_name = 'HARV'

#----------------------------------------------
#open shp boundary file from vector directory
#----------------------------------------------

# go into vector directory to get shp file 
vector_dir = os.path.join(site_path, site_name,
                          "vector")

site_boundary_path = os.path.join(vector_dir,  site_name + "-crop.shp")
bound = gpd.read_file(site_boundary_path)

bound

#----------------------------------------------
#open tif files from landsat directory
#----------------------------------------------

# In the landsat directory, get files 
landsat_dir = os.path.join(site_path, site_name, "landsat-crop")
landsat_folder = os.path.join(landsat_dir, "LC080130302017031701T1-SC20181023151837")

# Open bands in a sorted format
band_files = sorted(glob(os.path.join(landsat_folder, "*band*[4-5].tif")))

band_files


# _The following code block is where my two functions reside - the code was first tested outside of the function and then added after it was confirmed it worked on one site._
# 
# _open_clean_bands takes one of the band files I just extracted above, opens it up, clips it to HARV's crop extent, cleans it up, and returns that same band for future use._
# 
# _cloud_mask takes the qa file from a tif folder, opens it up using rxr, clips it to HARV's crop extent as well, and then, using an input of mask values, crops whatever NDVI array is given to a specific cloud mask._
# 
# _It was important to me not to over complicate these functions. They should be useful and simple to help automate my workflow, and not try to do a billion things at once._

# In[6]:


# In this cell place all of the functions needed to run your notebook
# You will be graded here on function application, docstrings, efficiency so ensure
# All functions are placed here!

# YOUR CODE HERE

def open_clean_bands(band_path,
                     crop_bound,
                     valid_range=None):
    """Open and mask a single landsat band using a pixel_qa layer.

    Parameters
    -----------
    band_path : string
        A path to the array to be opened
    crop_bound : GeoPandas DataFrame
        A data from that tells us the extent of the site of interest
    valid_range : tuple (optional)
        A tuple of min and max range of values for the data. Default = None


    Returns
    -----------
    arr : xarray DataArray
        An xarray DataArray with values that should be 
        masked set to 1 for True (Boolean)
    """
    
    band = (rxr.open_rasterio(band_path, masked=True)
        .rio.clip(crop_bound.geometry, from_disk=True)
        .squeeze())

    # Specify valid range of values
    if valid_range:
        mask = ((band <= 0) | (band > 10000))
        band = band.where(~mask, np.nan)

    return band


def cloud_mask(ndvi_array, site_folder, crop_bound, masked_values):
    """ This function masks clouds from a landsat band using a 
    pixel_qa layer.
    
     Parameters
    -----------
    ndvi_array: xarray DataArray
        An xarray DataArray with ndvi values
    site_folder : string
        A path to the site folder where QA array is
    crop_bound : GeoPandas DataFrame
        The crop extent of the area of interest
    masked_values : list
        A list of all values to be masked


    Returns
    -----------
    arr : xarray DataArray
        An xarray DataArray with ndvi values, masked to the specific values
    """
    
    #path to specific QA files - they end in pixel.tif
    qa_path = glob(os.path.normpath(os.path.join(site_folder, "*pixel*.tif")))
    
    #open path with rxr using crop extent of specific site
    qa_file = rxr.open_rasterio(
            qa_path[0], masked=True).rio.clip(crop_bound.geometry, 
                                              from_disk=True).squeeze()
    
    #crop the NDVI where NOT masked values are (i.e., where there isn't cloud cover) 
    ndvi_clean_crop = ndvi_array.where(~qa_file.isin(masked_values))
    
    return ndvi_clean_crop


# _This is the bulk of the processing for the HARV site. This code block loops through the bands, opens and cleans them, calculates the NDVI, and then finds the associative qa_path from the tif folder. It uses this to create a cloud mask, and then after the raster has been masked, it calculates the mean NDVI, and builds a dataframe from the site name, the date, and the mean NDVI. Because it doesn't have to do this with more than one site, it's pretty streamlined as is._

# In[7]:


# Create dataframe of mean NDVI in this cell using the functions created above
# Important: to use the ungraded tests below as a sanity check,
# name your columns: mean_ndvi and site
# Call the dataframe at the end of the cell so the tests run on it!
# Be sure that the date column is an index of type date
# HINT: the time series lessons may help you remember how to do this!

# YOUR CODE HERE

#----------------------------------------------------
#loop through each band file to open and clean bands
#----------------------------------------------------

bands = []
for aband in band_files:
    
    #run open_clean_bands function 
    cleaned_band = open_clean_bands(band_path=aband,
                                    crop_bound=bound,
                                    valid_range=(0, 10000))
    bands.append(cleaned_band)

#----------------------------------------------
#calculate NDVI
#----------------------------------------------

# NDVI = (NIR-RED)/(NIR+RED)
ndvi_xr = (bands[1] - bands[0]) / (bands[1] + bands[0])
#ndvi_xr.plot()

#------------------------------------------------
#obtain QA data from landsat files for cloud mask
#------------------------------------------------

qa_path = glob(os.path.normpath(os.path.join(landsat_folder, "*pixel*.tif")))

qa_file = rxr.open_rasterio(qa_path[0], masked=True).rio.clip(bound.geometry, 
                                                              from_disk=True).squeeze()

#------------------------------------------------
#create cloud mask from ep cloud pixels 
#------------------------------------------------
     
high_cloud_confidence = em.pixel_flags["pixel_qa"]["L8"]["High Cloud Confidence"]
cloud = em.pixel_flags["pixel_qa"]["L8"]["Cloud"]
cloud_shadow = em.pixel_flags["pixel_qa"]["L8"]["Cloud Shadow"]
    
all_masked_values = cloud_shadow + cloud + high_cloud_confidence


#mask ndvi with cloud mask 
ndvi_clean_crop = ndvi_xr.where(~qa_file.isin(all_masked_values))
#ndvi_clean_crop.plot()

#----------------------------------------------
#get mean of xarray
#----------------------------------------------

ndvi_mean = ndvi_clean_crop.mean()
#type(ndvi_mean)

#convert mean to a float instead of xarray
ndvi_mean_value = ndvi_mean.item()

#----------------------------------------------
#create df with site, date, and mean NDVI
#----------------------------------------------

#slice up the path into its components to utilize different names in the path
slice_path = landsat_folder.split(os.sep)

#site is the third slice
site = slice_path[2]

#the file name (with date) is the fifth slice
file_string = slice_path[4]

#the date is the the file name - before 01T1. Year, Month, Day
date = file_string[10:18]

#convert that date from string to datetime 
date_time = datetime.strptime(date, '%Y%m%d').strftime('%m/%d/%Y')

#create dataframe 
ndvi_df = pd.DataFrame([[site, date_time, ndvi_mean_value]], columns=['site', 'date', 'mean_ndvi'])

#make sure date is in datetime format
ndvi_df['date'] = pd.to_datetime(ndvi_df['date'])

#set date as index
ndvi_df.set_index("date", inplace = True)

ndvi_df


# In[8]:


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

# _This code snipped abstracts a lot of the work done above. It's the same concepts (open up site, open up landsat folder, open up band files, open and clean bands, mask for cloud cover, calculate NDVI, create df), but it does so with nested for loops so that it can be used with any site. While the code is concise, three for loops seems like not the most efficient way to do this, but I'm not sure what a more efficient method would be - perhaps another function for opening up each level of directories._

# In[9]:


# Create dataframe of NDVI including the cleaning data to deal with clouds

# Important: to use the ungraded tests below as a sanity check,
# name your columns: mean_ndvi and site
# Don't forget to set date as the index and make the values of type datetime

# YOUR CODE HERE

#I already have my sites variable from task 1, so no need to re-import

#both_sites_list is where all of the data will be stored and eventually put into a df
both_sites_list = []

#----------------------------------------------------
#for loop to go into each of the two site directories
#----------------------------------------------------
for site in sites:
    #path_parts gives me each independent string that makes up the path name
    path_parts = site.split(os.sep)
    site_name = path_parts[2]
    vector_dir = os.path.join(site_path, site_name,
                              "vector")
    
    #open crop boundary for each site
    site_boundary_path = os.path.join(vector_dir,  site_name + "-crop.shp")
    crop_bound = gpd.read_file(site_boundary_path)

    #open up the landsat directories for each site
    landsat_dir = os.path.join(site_path, site_name, "landsat-crop")
    landsat_folders = sorted(glob(os.path.join(landsat_dir, "*")))
    
    
    #---------------------------------------------------------------------
    #secondary for loop to go through each folder in the landsat directory
    #---------------------------------------------------------------------    
    
    for dirs in landsat_folders:
        print("Processing", dirs) #good way to check where I am in the for loop 
        
        #open bands required for NDVI calculation
        band_files = sorted(glob(os.path.join(dirs, "*band*[4-5].tif")))
        
        #---------------------------------------------------------------------
        #third for loop to go through each band in band files 
        #---------------------------------------------------------------------    
        
        #like in task 1, create empty list to save bands to 
        bands = []
        
        for aband in band_files:
            print("Opening", aband) #good way to check where I am in the for loop 
            
            #open and clean bands using function 
            cleaned_band = open_clean_bands(band_path=aband, 
                                            crop_bound=crop_bound,
                                            valid_range=(0, 10000))
            #add cleaned bands to bands list 
            bands.append(cleaned_band)
        
        #calculate NDVI 
        both_sites_ndvi_xr = (bands[1] - bands[0]) / (bands[1] + bands[0])
        
        #I've already created the cloud mask in task 1, so I can just run the function 
        both_sites_ndvi_clean_crop = cloud_mask(ndvi_array = both_sites_ndvi_xr, 
                                          site_folder = dirs,
                                          crop_bound = crop_bound, 
                                          masked_values = all_masked_values)
        
        #find ndvi mean, convert to a float
        both_sites_ndvi_mean = both_sites_ndvi_clean_crop.mean(skipna = True)
        both_sites_ndvi_mean_value = both_sites_ndvi_mean.item()
        
        #splice path_parts again now that we're in the directory and have each tif file name
        final_path_parts = dirs.split(os.sep)
        both_sites_site_name = final_path_parts[2]
        both_sites_file_string = final_path_parts[4]
        both_sites_date = both_sites_file_string[10:18]
        both_sites_date_time = datetime.strptime(both_sites_date, '%Y%m%d').strftime('%m/%d/%Y')
        
        both_sites_list.append([both_sites_site_name, both_sites_date_time, both_sites_ndvi_mean_value ])

#create dataframe from both_sites_list 
both_sites_ndvi_df = pd.DataFrame(both_sites_list, columns=['site', 'date', 'mean_ndvi'])
both_sites_ndvi_df['date'] = pd.to_datetime(both_sites_ndvi_df['date'])
both_sites_ndvi_df.set_index("date", inplace = True)
both_sites_ndvi_df


# In[10]:


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


# _Finally, this code block plots the data, grouped by site, and plots the mean NDVI by the date. It also drops all NaNs in the process. I think it's a fairly efficient way to plot._

# In[11]:


# Add only the plot code to this cell

# This is the final figure of mean NDVI
# for both sites across the year
# with data cleaned to deal with clouds

# YOUR CODE HERE
f, ax = plt.subplots(figsize=(15, 6))

for site, df in both_sites_ndvi_df.dropna().groupby('site'):
    ax.plot(df['mean_ndvi'], 'd-',  label = site)
    
ax.set(title = "Mean NDVI for HARV and SJER Sites (2017-2018)",
       xlabel = 'Date',
       ylabel = 'Mean NDVI')

plt.legend(bbox_to_anchor=(0.99,0.99))

### DO NOT REMOVE LINES BELOW ###
final_masked_solution = nb.convert_axes(plt, which_axes="current")


# In[12]:


# Ignore this cell for the autograding tests


# In[13]:


# Ignore this cell for the autograding tests


# # Question 1 (10 points)
# 
# Imagine that you are planning NEON’s upcoming flight season to capture remote sensing data in these locations and want to ensure that you fly the area when the vegetation is the most green.
# 
# When would you recommend the flights take place for each site? 
# 
# Answer the question in 2-3 sentences in the Markdown cell below.

# Well, the higher the NDVI, the more green the vegetation at each site is. So the highest NDVI for SJER takes place in April, and the highest NDVI for HARV takes places around early July. It's also important to note that these data points aren't regular in their timing. Perhaps there's even a better time for both of these sites in the longer gaps between the diamonds on the plot. 
# 
# 

# # Question 2 (10 points)
# 
# How could you modify your workflow to look at vegetation changes over time in each site? 
# 
# Answer the question in 2-3 sentences in the Markdown cell below.

# I might try other types of statistics to see if that changes the way the NDVI looks over the year...I might create 
# two graphs for each site, with the mean, mode and max NDVI calculated. That way I could tell if maybe the mean is creating some error in the way I interpret the data.
# 
# 
# 
# 

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

# In[14]:


both_sites_ndvi_df.to_csv("/Users/avrasaslow/Documents/Earth_Lab/"
                          "Semester2/ea-2022-04-ndvi-automation-AvraSaslow/HARV_SJER_NDVI.csv")


# In[15]:


HARV_SJER_NDVI = pd.read_csv("HARV_SJER_NDVI.csv")
HARV_SJER_NDVI


# In[ ]:




