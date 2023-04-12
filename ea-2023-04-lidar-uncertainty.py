#!/usr/bin/env python
# coding: utf-8

# <img style="float: left;" src="earth-lab-logo-rgb.png" width="150" height="150" />
# 
# # Earth Analytics Education

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
# 
# * Only include the package imports, code, and outputs that are required to run your homework assignment.
# * Be sure that your code can be run on any operating system. This means that:
#    1. the data should be downloaded in the notebook to ensure it's reproducible
#    2. all paths should be created dynamically using the `os.path.join`
#    3. sort lists of dated files even if they are sorted correctly by default on your machine
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
# **Your Name:**

# <img style="float: left;" src="colored-bar.png"/>

# ---

# # Week 03- Lidar Data Compared to Ground Measurements: Understanding Uncertainty
# 
# This week you will work with LiDAR data. You will explore the values in a LiDAR dataset - specifically tree height from a canopy height model. You will compare these measurements to the same types of measurements made by humans in the field.
# 
# You can download the data for this week from earthpy using: 
# 
# `et.data.get_data('spatial-vector-lidar')`
# 
# For both the SJER and SOAP field sites, create scatterplots (with regression and 1:1 lines) that compare:
# * **MAXIMUM** canopy height model height in meters, extracted within a 20 meter radius, compared to **MAXIMUM** tree
# height derived from the *insitu* field site data.
# * **MEAN** canopy height model height in meters, extracted within a 20 meter radius, compared to **MEAN** tree height derived from the *insitu* field site data.
# 
# Create one figure for each site with two subplots (ax1, ax2): one for the Max comparison and one for the Mean comparison.
# 
# 
# ## For All Plots
# 
# * Place lidar data values on the X axis and human measured tree height on the Y axis.
# * Include a calculated **regression line** (HINT: use `sns.regplot()` to achieve this line) that describes the relationship of lidar of the data.
# * Include a separate **1:1 line** that can be used to compare the regression fit to a perfect 1:1 fit. 
# * Set the x and y limits to be the SAME for each individual plot. (e.g. for plot 3, the x and y limits are set to the same range). 
# * Label x and y axes appropriately - include units.
# * Add a title to your plot that describes what the plot shows.
# * Ensure that your notebook is fully reproducible. This means you will:
#    * Create reproducible paths using the os module
#    * Download the data using code in the notebook
# 

# ![Colored Bar](colored-bar.png)

# ## Set up your analysis
# 
# In the following cell, import the libraries you use in this notebook, and change your working directory so that your paths are reproducible. Note that `earthpy` will download the data to `~` > `earth-analytics` > `data` >`spatial-vector-lidar`

# In[ ]:


# YOUR CODE HERE
raise NotImplementedError()


# ![Colored Bar](colored-bar.png)

# ## SJER Lidar vs Insitu Comparison Plots
# You will use the following SJER data for this figure:
# * `spatial-vector-lidar/california/neon-sjer-site/2013/insitu/veg_structure/D17_2013_SJER_vegStr.csv`
# * `spatial-vector-lidar/california/neon-sjer-site/vector_data/SJER_plot_centroids.shp`
# 
# Create a figure with 2 subplots for the NEON San Joaquin Experimental Range (SJER) field site.
# * Plot 1 should show **max** lidar vs insitu height with lidar on the x axis and insitu height on the y axis.
# * Plot 2 should show **mean** lidar vs insitu height with lidar on the x axis and insitu height on the y axis.
# 
# For each plot:
# 1. Set the x and y lims to be the same range: `(0, 30)` using `xlim=` and `ylim=`. This will make the plots more comparable.
# 2. Add a title that includes the field site name and the measurement being displayed (max or min height).
# 3. Add a 1:1 line to each plot.
# 4. Add a regression line using `sns.regplot()`. SNS is the alias for the seaborn plotting package (`import seaborn as sns`).
# 
# To create this plot, you will need to calculate a summary data frame for each site that contains both the lidar mean and max values and insitu (measured on the ground by humans) mean and max values. In the following cell, compute the summary values for the LiDAR data. **For the tests to work, rename your summary columns `lidar_max` and `lidar_mean`, and call your `GeoDataFrame`at the end of your answer cell.**
# 

# In[ ]:


# YOUR CODE HERE
raise NotImplementedError()


# In[ ]:


# Tests that the new columns exist and have the correct values
# IMPORTANT: Make sure you called the dataframe with the new columns at the end of the above cell.
# Do not modify this cell
student_sjer_lidar_sum = _
student_sjer_lidar_points = 0

if isinstance(student_sjer_lidar_sum, gpd.GeoDataFrame):
    print("\u2705 Great job! Your data are stored in a GeoDataFrame!")
    student_sjer_lidar_points += 1
else:
    print("\u274C Oops, the data are not stored in a GeoDataFrame.")

student_colunms = student_sjer_lidar_sum.columns

if 'lidar_max' in student_colunms:
    print("\u2705 Dataset has the correct column name for the maximum values!")
    student_sjer_lidar_points += 1
else:
    print("\u274C Oops, the dataset does not have the correct column name "
          "for the maximum values.")

if 'lidar_mean' in student_colunms:
    print("\u2705 Dataset has the correct column name for the mean values!")
    student_sjer_lidar_points += 1
else:
    print("\u274C Oops, the dataset does not have the correct column name "
          "for the mean values.")

if round(sjer_lidar_mean_max_answer.lidar_max.mean(), 2)==14.46:
    print("\u2705 Great - you correctly calculated the maximum values "
          "for each plot from lidar values!")
    student_sjer_lidar_points += 2
else:
    print("\u274C Oops - looks like your data frame values were not "
          "correct.")

if round(sjer_lidar_mean_max_answer.lidar_mean.mean(), 2)==7.56:
    print("\u2705 Great - you correctly calculated the mean values for each "
          "plot from lidar values!")
    student_sjer_lidar_points += 2
else:
    print("\u274C Oops - looks like your data frame values were not correct.")

print("\n \u27A1 You received {} out of 7 points for calculating "
      "lidar values.".format(student_sjer_lidar_points))

student_sjer_lidar_points


# In the following cell, compute the summary values for the insitu data, and merge the results with the LiDAR GeoDataFrame. **Name the new columns `insitu_max` and `insitu_mean` and call the completed `GeoDataFrame` at the end of you answer cell for the tests to work**

# In[ ]:


# YOUR CODE HERE
raise NotImplementedError()


# In[ ]:


# Tests that the new columns exist and have the correct values
# IMPORTANT: Make sure you called the dataframe with the new columns at the end of the above cell.
# Do not modify this cell

student_sjer_insitu_sum = _
student_sjer_insitu_points = 0

if isinstance(student_sjer_insitu_sum, gpd.GeoDataFrame):
    print("\u2705 Great job! Your data are stored in a GeoDataFrame!")
    student_sjer_insitu_points += 1
else:
    print("\u274C Oops, the data are not stored in a GeoDataFrame.")

student_columns = student_sjer_insitu_sum.columns

if 'insitu_max' in student_columns:
    print("\u2705 Dataset has the correct column name for the maximum values!")
    student_sjer_insitu_points += 1
else:
    print("\u274C Oops, the dataset does not have the correct column name "
          "for the maximum values.")

if 'insitu_mean' in student_columns:
    print("\u2705 Dataset has the correct column name for the mean values!")
    student_sjer_insitu_points += 1
else:
    print("\u274C Oops, the dataset does not have the correct column "
          "name for the mean values.")
    
if 'lidar_mean' in student_columns and 'lidar_max' in student_columns:
    print("\u2705 Dataset correctly merged!")
    student_sjer_insitu_points += 1
else:
    print("\u274C Oops, the insitu and lidar datasets were not merged.")


if round(student_sjer_insitu_sum.insitu_max.mean(), 2)==13.98:
    print("\u2705 Great - you correctly calculated the maximum values for "
          "each plot from insitu values!")
    student_sjer_insitu_points += 2
else:
    print("\u274C Oops - looks like your data frame values were not correct.")

if round(student_sjer_insitu_sum.insitu_mean.mean(), 2)==5.61:
    print("\u2705 Great - you correctly calculated the mean values for "
          "each plot from lidar values!")
    student_sjer_insitu_points += 2
else:
    print("\u274C Oops - looks like your data frame values were not correct.")

print("\n \u27A1 You received {} out of 8 points for calculating "
      "insitu values.".format(student_sjer_insitu_points))
student_sjer_insitu_points


# In[ ]:


In the cell below, plot the SJER data as specified above.


# In[ ]:


# YOUR CODE HERE
raise NotImplementedError()


# ## Figure 2: Plots 3 & 4 - SOAP Lidar vs Insitu Comparison Plots (15 points for each subplot)
# 
# You will use the following SOAP data for this figure:
# * `spatial-vector-lidar/california/neon-soap-site/2013/insitu/veg-structure/D17_2013_SOAP_vegStr.csv`
# * `spatial-vector-lidar/california/neon-soap-site/vector_data/SOAP_centroids.shp`
# 
# Create a figure with 2 subplots for the NEON Soaproot Saddle (SOAP) field site.
# * Plot 1 should show **max** lidar vs insitu height with lidar on the x axis and insitu height on the y axis.
# * Plot 2 should show **mean** lidar vs insitu height with lidar on the x axis and insitu height on the y axis.
# 
# For each plot:
# 
# 1. Set the x and y lims to be the same range using `xlim=` and `ylim=`: 
#     * `(0, 140)` for the SOAP Max height plot. 
#     * `(0, 40)` for the SOAP Mean height plot. 
# 2. Add a title that includes the field site name and the measurement being displayed (max or min height).
# 3. Add a 1:1 line to each plot.
# 4. Add a regression line using `sns.regplot()`
# 
# To create this plot, you will need to calculate a summary data frame for each site that contains lidar mean and max values and insitu (measured on the ground by humans) mean and max values.
# 
# **HINT**: the SOAP data have some inconsistencies in the column headings. One way to fix this is to use the syntax: 
# 
# `"text-to-append-to-column" + dataframe_name["column-name-here"]`
# 
# In the following cell, import and process the SOAP data like you did the SJER data. **Make sure to call your combined `GeoDataFrame` at the end of cell for the test cell to work.**

# In[ ]:


# YOUR CODE HERE
raise NotImplementedError()


# In[ ]:


student_soap_gdf = _
student_soap_points = 0

if isinstance(student_soap_gdf, gpd.GeoDataFrame):
    print("\u2705 Great job! Your data are stored in a GeoDataFrame!")
    student_soap_points += 1
else:
    print("\u274C Oops, the data are not stored in a GeoDataFrame.")

student_columns = student_soap_gdf.columns

if 'lidar_max' in student_columns:
    print("\u2705 Dataset has the correct column name for the maximum "
          "values!")
    student_soap_points += 1
else:
    print("\u274C Oops, the dataset does not have the correct column "
          "name for the maximum values.")

if 'lidar_mean' in student_columns:
    print("\u2705 Dataset has the correct column name for the mean values!")
    student_soap_points += 1
else:
    print("\u274C Oops, the dataset does not have the correct column name "
          "for the mean values.")

if 'insitu_max' in student_colunms:
    print("\u2705 Dataset has the correct column name for the maximum values!")
    student_soap_points += 1
else:
    print("\u274C Oops, the dataset does not have the correct column name "
          "for the maximum values.")

if 'insitu_mean' in student_colunms:
    print("\u2705 Dataset has the correct column name for the mean values!")
    student_soap_points += 1
else:
    print("\u274C Oops, the dataset does not have the correct column name "
          "for the mean values.")

student_summary = (
    student_soap_gdf
   [['lidar_max', 'lidar_mean', 'insitu_max', 'insitu_mean']]
   .mean()
   .apply(lambda x: round(x, 2))
   .values)

if all(student_summary==[33.54, 13.87, 40.68,  5.06]):
    print("\u2705 Great - you correctly calculated summary values!")
    student_soap_points += 8
else:
    print("\u274C Oops - looks like your data frame values were not correct.")

print("\n \u27A1 You received {} out of 13 points for calculating lidar "
      "values.".format(student_soap_points))
student_soap_points


# ### In the cell below plot the SOAP site values the same way your plotted the SJER site values

# In[ ]:


# YOUR CODE HERE
raise NotImplementedError()


# ![Colored Bar](colored-bar.png)

# ## Question 1 Figure One: SJER mean vs max height -- Plots 1 and 2 Interpretation
# In the markdown cell below, answer the following questions:
# 
# 1. Looking at the plots above, which metric: mean or max height, has a stronger relationship or is closer to a one:one relationship?
# 2. List one reason why mean or max (whatever you answered for question 1 above) has a stronger relationship.
# 
# You answers can be brief -- a single word or sentence or two is fine. 

# YOUR ANSWER HERE

# ![Colored Bar](colored-bar.png)

# 
# ## Question 2. Of all four relationships that you plotted above, which site (SOAP or SJER) and metric (mean or max height) showed the strongest relationship? 
# 
# **A strong relationship is one that is closer to 1:1 in this case.**
# 
# Add your answer in the markdown cell below. It can be short - 2-5 sentences. You do not need to perform any additional calculations. Consider the readings and the data and suggest why a particular metric might have a strong relationship.

# YOUR ANSWER HERE

# ![Colored Bar](colored-bar.png)

# ## Question 3. List 2 reasons why lidar max height values may be larger than human measurements.
# 
# Add your answer to the markdown cell below.

# YOUR ANSWER HERE

# ![Colored Bar](colored-bar.png)

# ## Question 4. List 2 systematic sources of error could impact differences between lidar and measured tree height values ( 5 points)
# 
# Add your answer in the markdown cell below.

# YOUR ANSWER HERE

# ![Colored Bar](colored-bar.png)

# ## Question 5. List 2 random sources of error that could impact differences between lidar and measured tree height values.  (5 points)
# 
# Add your answer to the markdown cell below. Note that you can provide sources of random error for lidar OR insitu measurements. You only need two total examples. 

# YOUR ANSWER HERE

# ![Colored Bar](colored-bar.png)

# 
# # Do not edit this cell!
# * Notebook begins at cell [1] and runs on any machine in its entirety.
# * Pep8 format is applied throughout.
# * Notebook is fully reproducible. This means:
#    * reproducible paths using the os module
#    * data downloaded using code in the notebook.
