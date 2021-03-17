{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<img style=\"float: left;\" src=\"earth-lab-logo-rgb.png\" width=\"150\" height=\"150\" />\n",
    "\n",
    "# Earth Analytics Education - EA  Python Course Spring 2021"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Important  - Assignment Guidelines\n",
    "\n",
    "1. Before you submit your assignment to GitHub, make sure to run the entire notebook with a fresh kernel. To do this first, **restart the kernel** (in the menubar, select Kernel$\\rightarrow$Restart & Run All)\n",
    "2. Always replace the `raise NotImplementedError()` code with your code that addresses the activity challenge. If you don't replace that code, your notebook will not run.\n",
    "\n",
    "```\n",
    "# YOUR CODE HERE\n",
    "raise NotImplementedError()\n",
    "```\n",
    "\n",
    "3. Any open ended questions will have a \"YOUR ANSWER HERE\" within a markdown cell. Replace that text with your answer also formatted using Markdown.\n",
    "4. **DO NOT RENAME THIS NOTEBOOK File!** If the file name changes, the autograder will not grade your assignment properly.\n",
    "6. When you create a figure, comment out `plt.show()` to ensure the autograder can grade your plots. For figure cells, DO NOT DELETE the code that says `DO NOT REMOVE LINE BELOW`.\n",
    "\n",
    "```\n",
    "### DO NOT REMOVE LINE BELOW ###\n",
    "student_plot1_ax = nb.convert_axes(plt)\n",
    "```\n",
    "\n",
    "* Only include the package imports, code, and outputs that are required to run your homework assignment.\n",
    "* Be sure that your code can be run on any operating system. This means that:\n",
    "   1. the data should be downloaded in the notebook to ensure it's reproducible\n",
    "   2. all paths should be created dynamically using the `os.path.join`\n",
    "\n",
    "## Follow to PEP 8 Syntax Guidelines & Documentation\n",
    "\n",
    "* Run the `autopep8` tool on all cells prior to submitting (HINT: hit shift + the tool to run it on all cells at once!\n",
    "* Use clear and expressive names for variables. \n",
    "* Organize your code to support readability.\n",
    "* Check for code line length\n",
    "* Use comments and white space sparingly where it is needed\n",
    "* Make sure all python imports are at the top of your notebook and follow PEP 8 order conventions\n",
    "* Spell check your Notebook before submitting it.\n",
    "\n",
    "For all of the plots below, be sure to do the following:\n",
    "\n",
    "* Make sure each plot has a clear TITLE and, where appropriate, label the x and y axes. Be sure to include UNITS in your labels.\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Add Your Name Below \n",
    "**Lauren Kremer**"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<img style=\"float: left;\" src=\"colored-bar.png\"/>"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "---"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "deletable": false,
    "editable": false,
    "nbgrader": {
     "cell_type": "markdown",
     "checksum": "482b6a6fad5a6b7297cd1f14b52b28e1",
     "grade": false,
     "grade_id": "hw-instructions",
     "locked": true,
     "schema_version": 3,
     "solution": false,
     "task": false
    }
   },
   "source": [
    "# Week 04 and 05 Homework - Automate NDVI Workflow\n",
    "\n",
    "For this assignment, you will write code to generate a plot of the mean normalized difference vegetation index (NDVI) for two different sites in the United States across one year of data:\n",
    "\n",
    "* San Joaquin Experimental Range (SJER) in Southern California, United States\n",
    "* Harvard Forest (HARV) in the Northeastern United States\n",
    "\n",
    "The data that you will use for this week is available from **earthpy** using the following download: \n",
    "\n",
    "`et.data.get_data('ndvi-automation')`\n",
    "\n",
    "## Assignment Goals\n",
    "\n",
    "Your goal in this assignment is to create the most efficient and concise workflow that you can that allows for:\n",
    "\n",
    "1. The code to scale if you added new sites or more time periods to the analysis.\n",
    "2. Someone else to understand your workflow.\n",
    "3. The LEAST and most efficient (i.e. runs fast, minimize repetition) amount of code that completes the task.\n",
    "\n",
    "### HINTS\n",
    "\n",
    "* Remove values outside of the landsat valid range of values as specified in the metadata, as needed.\n",
    "* Keep any output files SEPARATE FROM input files. Outputs should be created in an outputs directory that is created in the code (if needed) and/or tested for.\n",
    "* Use the functions that we demonstrated during class to make your workflow more efficient.\n",
    "* BONUS - if you  chose - you can export your data as a csv file. You will get bonus points for doing this.\n",
    "\n",
    "\n",
    "## Assignment Requirements\n",
    "\n",
    "Your submission to the GitHub repository should include:\n",
    "* This Jupyter Notebook file (.ipynb) with:\n",
    "    * The code to create a plot of mean NDVI across a year for  2 NEON Field Sites:\n",
    "        * NDVI on the x axis and formatted dates on the y for both NEON sites on one figure/axis object\n",
    "    * The **data should be cleaned to remove the influence of clouds**. See the [earthdatascience website for an example of what your plot might look like with and without removal of clouds](https://www.earthdatascience.org/courses/earth-analytics-python/create-efficient-data-workflows/).\n",
    "* BONUS: Create one output `.csv` file that has 3 columns - NDVI, Date and Site Name - with values for SJER and HARV.\n",
    "\n",
    "Your notebook should:\n",
    "* Have *at least* 2 well documented and well named functions with docstrings.\n",
    "* Include a Markdown cell at the top of the notebook that outlines the overall workflow using pseudocode (i.e. plain language, not code)\n",
    "* Include additional Markdown cells throughout the notebook to describe: \n",
    "    * the data that you used - and where it is from\n",
    "    * how data are being processing\n",
    "    * how the code is optimized to run fast and be more concise"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "deletable": false,
    "editable": false,
    "nbgrader": {
     "cell_type": "markdown",
     "checksum": "ca51bc48f62e7d3602d0567f742e1b15",
     "grade": false,
     "grade_id": "pseudo-code",
     "locked": true,
     "points": 15,
     "schema_version": 3,
     "solution": false,
     "task": true
    }
   },
   "source": [
    "# Replace this cell with your pseudocode  for this workflow\n",
    "\n",
    "If you happen to be a diagram person a diagram is ok too\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "1. Open each \"sites\" folder\n",
    "    a. open the landsat-crop folder\n",
    "        -generate a list of files for ndvi calcs (bands 4 and 5)\n",
    "        -access qa files from same folder for cloud mask\n",
    "    b. make a list of paths for crop .shp files \n",
    "\n",
    "2.  With bands 4 and 5 for each image, generate a function that:\n",
    "    a. mask invalid values (1-10000)\n",
    "    b. calculate NDVI\n",
    "    c. clip to boundary\n",
    "    d. mask clouds using qa layer\n",
    "    e. calculate mean NDVI for each image and generate a \n",
    "    dataframe with image date and site colums.\n",
    "    \n",
    "3. apply NDVI function \n",
    "    a. generate dateframes from band and crop shape lists in a loop \n",
    "    b. concatonate dataframe from each image into one plottable df\n",
    "     \n",
    "4. Plot ndvi values as a timeseries\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {
    "deletable": false,
    "editable": false,
    "nbgrader": {
     "cell_type": "code",
     "checksum": "9c7cd3e2e5089092e06ba301f2719a63",
     "grade": false,
     "grade_id": "core-imports",
     "locked": true,
     "schema_version": 3,
     "solution": false,
     "task": false
    }
   },
   "outputs": [],
   "source": [
    "# Autograding imports - do not modify this cell\n",
    "import matplotcheck.autograde as ag\n",
    "import matplotcheck.notebook as nb\n",
    "import matplotcheck.timeseries as ts\n",
    "from datetime import datetime"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {
    "deletable": false,
    "nbgrader": {
     "cell_type": "code",
     "checksum": "3c4d1141999885a9a9b09772962b180a",
     "grade": true,
     "grade_id": "student-imports-answer",
     "locked": false,
     "points": 10,
     "schema_version": 3,
     "solution": true,
     "task": false
    },
    "tags": [
     "hide",
     "hide_output"
    ]
   },
   "outputs": [],
   "source": [
    "# Import needed packages in PEP 8 order\n",
    "# and no unused imports listed (10 points total)\n",
    "\n",
    "import os\n",
    "from glob import glob\n",
    "\n",
    "import matplotlib.pyplot as plt\n",
    "import numpy as np\n",
    "import geopandas as gpd\n",
    "import rioxarray as rxr\n",
    "import xarray as xr\n",
    "import earthpy as et\n",
    "import pandas as pd\n",
    "\n",
    "# Download data \n",
    "et.data.get_data('ndvi-automation')\n",
    "\n",
    "# Set working directory\n",
    "os.chdir(os.path.join(et.io.HOME,\n",
    "                      \"earth-analytics\",\n",
    "                      \"data\"))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {
    "deletable": false,
    "editable": false,
    "hideCode": false,
    "hidePrompt": false,
    "nbgrader": {
     "cell_type": "code",
     "checksum": "dcf5b59326bf066172ff61520b658a3d",
     "grade": true,
     "grade_id": "student-download-tests",
     "locked": true,
     "points": 0,
     "schema_version": 3,
     "solution": false,
     "task": false
    }
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "✅ Great - it looks like your working directory is set correctly to ~/earth-analytics/data\n"
     ]
    }
   ],
   "source": [
    "# DO NOT MODIFY THIS CELL\n",
    "# Tests that the working directory is set to earth-analytics/data\n",
    "\n",
    "path = os.path.normpath(os.getcwd())\n",
    "student_wd_parts = path.split(os.sep)\n",
    "\n",
    "if student_wd_parts[-2:] == ['earth-analytics', 'data']:\n",
    "    print(\"\\u2705 Great - it looks like your working directory is set correctly to ~/earth-analytics/data\")\n",
    "else:\n",
    "    print(\"\\u274C Oops, the autograder will not run unless your working directory is set to earth-analytics/data\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [],
   "source": [
    "# The NDVI automation download provides 30m resolution Landsat data and shapefiles for\n",
    "# two study sites, one in San Joaquin, CA and the other in Harvard Forest, MA. The two sites\n",
    "# differ in vegetation coverage density and type, making them ideal for reviewing potential \n",
    "# differences in NDVvi time series analysis. Landsat data provided includes images for \n",
    "# approximately 23 days between Jan 12, 2017 to December 30, 2017 and for each image, \n",
    "# bands 1-5 and a quality assessment band are included in the download."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "deletable": false,
    "editable": false,
    "nbgrader": {
     "cell_type": "markdown",
     "checksum": "35205d12dc9e8fa05a26fb927c0a2307",
     "grade": false,
     "grade_id": "ndvi-mean-site-instructions",
     "locked": true,
     "schema_version": 3,
     "solution": false,
     "task": false
    }
   },
   "source": [
    "# Figure 1: Plot 1 - Mean NDVI For Each Site Across the Year (50 points)\n",
    "\n",
    "Create a plot of the mean normalized difference vegetation index (NDVI) for the two different sites in the United States across the year: \n",
    "\n",
    "* NDVI on the x axis and formatted dates on the y for both NEON sites on one figure/axis object.\n",
    "* Each site should be identified with a different color in the plot and legend.\n",
    "* The final plot **data should be cleaned to remove the influence of clouds**.\n",
    "* Be sure to include appropriate title and axes labels.\n",
    "\n",
    "Add additional cells as needed for processing data (e.g. defining functions, etc), but be sure to:\n",
    "* follow the instructions in the code cells that have been provided to ensure that you are able to use the sanity check tests that are provided. \n",
    "* include only the plot code in the cell identified for the final plot code below"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "deletable": false,
    "editable": false,
    "nbgrader": {
     "cell_type": "markdown",
     "checksum": "ce17d4d685cd4c7034bd7b0bb389342a",
     "grade": false,
     "grade_id": "single-scene-instructions",
     "locked": true,
     "schema_version": 3,
     "solution": false,
     "task": false
    }
   },
   "source": [
    "## Task 1: \n",
    "\n",
    "In the cell below, create a single dataframe containing MEAN NDVI, the site name, \n",
    "and the date of the data for the HARV site \n",
    "scene `HARV/landsat-crop/LC080130302017031701T1-SC20181023151837`.  The column names for the  final\n",
    "DataFrame should be`mean_ndvi`, and `site`, and the data should be **indexed on the date**. \n",
    "\n",
    "Use the functions that we reviewed in class (or create your own versions of them) to implement your code\n",
    "\n",
    "### In the Cell below Place  All Functions Needed to Run this Notebook (20 points)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {
    "deletable": false,
    "editable": false,
    "nbgrader": {
     "cell_type": "code",
     "checksum": "0ee340cd9af6c949a08eb4b325716ae0",
     "grade": false,
     "grade_id": "cell-618e3588853f3ed8",
     "locked": true,
     "schema_version": 3,
     "solution": false,
     "task": false
    }
   },
   "outputs": [],
   "source": [
    "### DO NOT REMOVE THIS LINE OR EDIT / MOVE THIS CELL ###\n",
    "start_time = datetime.now()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {
    "deletable": false,
    "nbgrader": {
     "cell_type": "code",
     "checksum": "653ebd5db668245408615979f6c20944",
     "grade": true,
     "grade_id": "function-definitions-check",
     "locked": false,
     "points": 40,
     "schema_version": 3,
     "solution": true,
     "task": false
    }
   },
   "outputs": [],
   "source": [
    "# In this cell place all of the functions needed to run your notebook\n",
    "# You will be graded here on function application, docstrings, efficiency so ensure\n",
    "# All functions are placed here!\n",
    "\n",
    "# Function 1. Generate a crop_boundary for each site \n",
    "\n",
    "def open_boundary(site_path):\n",
    "    \"\"\"generate a list of boundary shapefiles for clipping landsat data to study area\n",
    "    Parameters\n",
    "    -----------\n",
    "    vector_path : a path to the directory containing desire shapefile\n",
    "        \n",
    "    Returns\n",
    "    -----------\n",
    "    gpd : a geopandas geodataframe \n",
    "    \"\"\"\n",
    "    # Open crop boundary\n",
    "    vector_dir = os.path.join(site_path, \"vector\")\n",
    "    site_name = os.path.basename(os.path.normpath(site_path))\n",
    "    site_boundary_path = os.path.join(vector_dir,  site_name + \"-crop.shp\")\n",
    "    crop_bound = gpd.read_file(site_boundary_path)\n",
    "    crop_bound['Site'] = site_name \n",
    "    return crop_bound\n",
    "\n",
    "# Function 2. Generate a list of landsat 8 image folders for each site\n",
    "  \n",
    "def build_image_list(landsat_dir):\n",
    "    \"\"\"generates a list of landsat bands 4 and 5 from folder of images\n",
    "    Parameters\n",
    "    -----------\n",
    "    landsat_dir : a path to the folder/directory of image subfolders which\n",
    "    contain landsat bands\n",
    "        \n",
    "    Returns\n",
    "    -----------\n",
    "    list : a list of .tif filepaths that can be used to calculate NDVI\n",
    "    \"\"\"\n",
    "    \n",
    "    image_list = []\n",
    "\n",
    "    image_paths = sorted(glob(os.path.join(landsat_dir, \"LC08*\")))\n",
    "    image_list.append(image_paths)\n",
    "    image_list = [i for b in map(lambda x:[x] if not isinstance(x, list) \n",
    "                                 else x, image_list) for i in b] # unlists nested lists\n",
    "    return image_list\n",
    "\n",
    "# Function 3. \n",
    "def mask_crop_ndvi(image_folder, vals, crop_extent, valid_range = None):\n",
    "    \n",
    "    \"\"\"Open bands 4 and 5 in each image folder, mask according to valid_range of pixel\n",
    "    values, then stores them in a two band list used to calculate NDVI at each pixel.  \n",
    "    Then masks clouds using the qa file in the image folder and clips them from a\n",
    "    .shp file indicated by the function parameter (crop_extent). Then\n",
    "    generates dataframe from image mean NDVI with date and site name. \n",
    "\n",
    "    Parameters\n",
    "    -----------\n",
    "    image_folder : list of Landsat 8 folders containing image bands\n",
    "    vals: A list of values needed to create the cloud mask\n",
    "    crop_extent: geopandas GeoDataFrame\n",
    "        A geopandas dataframe to be used to crop the raster data\n",
    "    valid_range : tuple (optional)\n",
    "        A tuple of min and max range of values for the data. Default = None \n",
    "\n",
    "    Returns\n",
    "    -----------\n",
    "    ndvi_df : Pandas dataframe\n",
    "        a dataframe containing cropped image mean NDVI values indexed by date\n",
    "    \"\"\"\n",
    "    \n",
    "    band_path = sorted(glob(os.path.join(image_folder, \"*band*[4-5].tif\")))\n",
    "    opened_bands = []\n",
    "    \n",
    "    for i in band_path:\n",
    "        landsat_45 = rxr.open_rasterio(i, masked=True).rio.clip(crop_extent.geometry,\n",
    "                                                            from_disk=True).squeeze()\n",
    "        if valid_range:\n",
    "            mask = ((landsat_45 < valid_range[0]) | (landsat_45 > valid_range[1]))\n",
    "            band = landsat_45.where(~xr.where(mask, True, False))\n",
    "            opened_bands.append(band)\n",
    "          \n",
    "    img_ndvi = (opened_bands[1] - opened_bands[0]) / (opened_bands[1] + opened_bands[0])\n",
    "\n",
    "    # # then open pixel_qa \n",
    "    qa_paths = glob(os.path.join(image_folder, \"*qa*\"))\n",
    "    path_str = ' '.join([str(elem) for elem in qa_paths]) \n",
    "    qa_open = rxr.open_rasterio(path_str).rio.clip(crop_extent.geometry,\n",
    "                                                              from_disk=True).squeeze()\n",
    "    ndvi_mask = img_ndvi.where(~qa_open.isin(vals))\n",
    "    \n",
    "    # create the dataframe\n",
    "    ndvi_df = pd.DataFrame()\n",
    "    ndvi_df['mean_ndvi'] = pd.Series({\"mean\": ndvi_mask.mean()}, dtype=float)\n",
    "    ndvi_df['site'] = image_folder[22:26]\n",
    "    ndvi_df['date'] = pd.to_datetime(image_folder[50:58], format = '%Y%m%d')\n",
    "    ndvi_df.set_index('date', inplace=True)\n",
    "    return ndvi_df\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [],
   "source": [
    "# For optimal processing, only bands needed for NDVI calculations and cloud masking (qa)\n",
    "# were opened. Bands were clipped upon opening to decrease file size to only geographic\n",
    "# area of interest, and the cloudmask was applied only to the the NDVI array to reduce \n",
    "# processing time over applying a mask to each band used for the calculation. The output \n",
    "# of the above function only returns a dataframe of required data, rather than any arrays \n",
    "# used for calculations within the dataframe. "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {
    "deletable": false,
    "nbgrader": {
     "cell_type": "code",
     "checksum": "d124eef1d9cf2d0063ab450c9a20dc8e",
     "grade": false,
     "grade_id": "single-scene-answer",
     "locked": false,
     "schema_version": 3,
     "solution": true,
     "task": false
    },
    "tags": [
     "hide"
    ]
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>mean_ndvi</th>\n",
       "      <th>site</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>date</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>2017-03-17</th>\n",
       "      <td>0.281132</td>\n",
       "      <td>HARV</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "            mean_ndvi  site\n",
       "date                       \n",
       "2017-03-17   0.281132  HARV"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Create dataframe of mean NDVI in this cell using the functions created above\n",
    "# Important: to use the ungraded tests below as a sanity check,\n",
    "# name your columns: mean_ndvi and site\n",
    "# Call the dataframe at the end of the cell so the tests run on it!\n",
    "# Be sure that the date column is an index of type date\n",
    "# HINT: the time series lessons may help you remember how to do this!\n",
    "\n",
    "# Indicate path to site directories\n",
    "path = os.path.join(\"ndvi-automation\", \"sites\")\n",
    "\n",
    "# Get a list of both site directories \n",
    "sites = sorted(glob(path + \"/*/\"))\n",
    "\n",
    "# build list (build_image_list)of landsat image folders containing bands:\n",
    "sitelists = []\n",
    "for i in sites:\n",
    "    site_list = build_image_list(landsat_dir = os.path.join(i, \"landsat-crop\"))\n",
    "    sitelists.append(site_list)\n",
    "    #sitelists = [i for b in map(lambda x:[x] if not isinstance(x, list) else x, sitelists) for i in b]\n",
    "sitelists[0][4] #identify one image folder specific to Task 1.\n",
    "\n",
    "# Open shapefiles using open_boundary function\n",
    "bounds = []\n",
    "for i in sites:\n",
    "    boundy = open_boundary(i)\n",
    "    bounds.append(boundy)\n",
    "\n",
    "bounds[0] # identify harv geodf for Task 1.\n",
    "\n",
    "# Identify variables for mask_cloud function:\n",
    "\n",
    "# Cloud no data vals for Landsat 8 -\n",
    "vals = [328, 392, 840, 904, 1350, 352, 368, 416,\n",
    "        432, 480, 864, 880, 928, 944, 992, 480, 992]\n",
    "               \n",
    "# apply ndvi calculation and masking function for specific image\n",
    "mask_crop_ndvi(image_folder = sitelists[0][4], vals = vals, crop_extent = bounds[0], \n",
    "               valid_range = (0, 10000))\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {
    "deletable": false,
    "editable": false,
    "nbgrader": {
     "cell_type": "code",
     "checksum": "6121e3a0293ed64f09521b5d248496c3",
     "grade": true,
     "grade_id": "single-scene-tests",
     "locked": true,
     "points": 15,
     "schema_version": 3,
     "solution": false,
     "task": false
    }
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "✅ Your data is stored in a DataFrame!\n",
      "✅ You have the index set to the date column!\n",
      "✅ The data in your date column is datetime!\n",
      "✅ You have the correct site name!\n",
      "✅ You have the correct mean NDVI value!\n",
      "\n",
      " ➡ You received 15 out of 15 points for creating a dataframe.\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "15"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# This cell  is testing your data output above\n",
    "\n",
    "student_ndvi_ts_single_site = _\n",
    "\n",
    "single_scene_points = 0\n",
    "\n",
    "# Ensure the data is stored in a dataframe.\n",
    "if isinstance(student_ndvi_ts_single_site, pd.DataFrame):\n",
    "    print('\\u2705 Your data is stored in a DataFrame!')\n",
    "    single_scene_points += 1\n",
    "else:\n",
    "    print('\\u274C It appears your data is not stored in a DataFrame. ',\n",
    "          'To see what type of object your data is stored in, check its type with type(object)')\n",
    "\n",
    "# Ensure that the date column is the index\n",
    "if isinstance(student_ndvi_ts_single_site.index, pd.core.indexes.datetimes.DatetimeIndex):\n",
    "    print('\\u2705 You have the index set to the date column!')\n",
    "    single_scene_points += 2\n",
    "else:\n",
    "    print('\\u274C You do not have the index set to the date column.')\n",
    "\n",
    "# Ensure that the date column is datetime\n",
    "if isinstance(student_ndvi_ts_single_site.index[0], pd._libs.tslibs.timestamps.Timestamp):\n",
    "    print('\\u2705 The data in your date column is datetime!')\n",
    "    single_scene_points += 2\n",
    "else:\n",
    "    print('\\u274C The data in your date column is not datetime.')\n",
    "\n",
    "# Ensure the site name is correct\n",
    "if student_ndvi_ts_single_site.site.values[0] == 'HARV':\n",
    "    print('\\u2705 You have the correct site name!')\n",
    "    single_scene_points += 5\n",
    "else:\n",
    "    print('\\u274C You do not have the correct site name.')\n",
    "\n",
    "if np.allclose(0.281131628228094, student_ndvi_ts_single_site.mean_ndvi.values[0]):\n",
    "    print('\\u2705 You have the correct mean NDVI value!')\n",
    "    single_scene_points += 5\n",
    "else:\n",
    "    print('\\u274C You do not have the correct mean ndvi value.')\n",
    "\n",
    "print(\"\\n \\u27A1 You received {} out of 15 points for creating a dataframe.\".format(\n",
    "    single_scene_points))\n",
    "single_scene_points"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Task 2:\n",
    "\n",
    "In the cell below, process all of the landsat scenes. Create a DataFrame that contains the following \n",
    "information for each scene\n",
    "\n",
    "\n",
    "|   | index  | site  | mean_ndvi  | \n",
    "|---|---|---|---|\n",
    "| Date  |   |   |   |\n",
    "|  2017-01-07  | 0  | SJER  | .4  |  \n",
    "\n",
    "Be sure to call your dataframe at the end of the cell to ensure autograding works.\n",
    "HINT: FOR THIS STEP, leave any rows containing missing values (`NAN`)."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {
    "deletable": false,
    "nbgrader": {
     "cell_type": "code",
     "checksum": "848dd486333246e15b6b8f0dff745a4b",
     "grade": false,
     "grade_id": "cleaned_dataframes_answer",
     "locked": false,
     "schema_version": 3,
     "solution": true,
     "task": false
    },
    "tags": [
     "hide"
    ]
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>mean_ndvi</th>\n",
       "      <th>site</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>date</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>2017-01-12</th>\n",
       "      <td>NaN</td>\n",
       "      <td>HARV</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2017-01-28</th>\n",
       "      <td>NaN</td>\n",
       "      <td>HARV</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2017-02-13</th>\n",
       "      <td>NaN</td>\n",
       "      <td>HARV</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2017-03-01</th>\n",
       "      <td>NaN</td>\n",
       "      <td>HARV</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2017-03-17</th>\n",
       "      <td>0.281132</td>\n",
       "      <td>HARV</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2017-04-02</th>\n",
       "      <td>0.251133</td>\n",
       "      <td>HARV</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2017-04-18</th>\n",
       "      <td>0.541080</td>\n",
       "      <td>HARV</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2017-05-04</th>\n",
       "      <td>0.568924</td>\n",
       "      <td>HARV</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2017-05-20</th>\n",
       "      <td>0.811310</td>\n",
       "      <td>HARV</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2017-06-05</th>\n",
       "      <td>NaN</td>\n",
       "      <td>HARV</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2017-06-21</th>\n",
       "      <td>0.881739</td>\n",
       "      <td>HARV</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2017-07-07</th>\n",
       "      <td>NaN</td>\n",
       "      <td>HARV</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2017-07-23</th>\n",
       "      <td>0.819768</td>\n",
       "      <td>HARV</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2017-08-08</th>\n",
       "      <td>NaN</td>\n",
       "      <td>HARV</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2017-08-24</th>\n",
       "      <td>0.864464</td>\n",
       "      <td>HARV</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2017-09-09</th>\n",
       "      <td>0.857701</td>\n",
       "      <td>HARV</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2017-09-25</th>\n",
       "      <td>0.840639</td>\n",
       "      <td>HARV</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2017-10-11</th>\n",
       "      <td>0.652435</td>\n",
       "      <td>HARV</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2017-10-27</th>\n",
       "      <td>0.688382</td>\n",
       "      <td>HARV</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2017-11-12</th>\n",
       "      <td>0.613321</td>\n",
       "      <td>HARV</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2017-11-28</th>\n",
       "      <td>0.617948</td>\n",
       "      <td>HARV</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2017-12-14</th>\n",
       "      <td>0.498205</td>\n",
       "      <td>HARV</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2017-12-30</th>\n",
       "      <td>NaN</td>\n",
       "      <td>HARV</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2017-01-07</th>\n",
       "      <td>NaN</td>\n",
       "      <td>SJER</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2017-01-23</th>\n",
       "      <td>NaN</td>\n",
       "      <td>SJER</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2017-02-08</th>\n",
       "      <td>NaN</td>\n",
       "      <td>SJER</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2017-02-24</th>\n",
       "      <td>0.665524</td>\n",
       "      <td>SJER</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2017-03-12</th>\n",
       "      <td>0.664109</td>\n",
       "      <td>SJER</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2017-03-28</th>\n",
       "      <td>0.702343</td>\n",
       "      <td>SJER</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2017-04-13</th>\n",
       "      <td>NaN</td>\n",
       "      <td>SJER</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2017-04-29</th>\n",
       "      <td>0.610209</td>\n",
       "      <td>SJER</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2017-05-15</th>\n",
       "      <td>0.444847</td>\n",
       "      <td>SJER</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2017-05-31</th>\n",
       "      <td>NaN</td>\n",
       "      <td>SJER</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2017-06-16</th>\n",
       "      <td>0.358551</td>\n",
       "      <td>SJER</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2017-07-02</th>\n",
       "      <td>0.334559</td>\n",
       "      <td>SJER</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2017-07-18</th>\n",
       "      <td>0.319796</td>\n",
       "      <td>SJER</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2017-08-03</th>\n",
       "      <td>NaN</td>\n",
       "      <td>SJER</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2017-08-19</th>\n",
       "      <td>0.327455</td>\n",
       "      <td>SJER</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2017-09-04</th>\n",
       "      <td>NaN</td>\n",
       "      <td>SJER</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2017-09-20</th>\n",
       "      <td>0.330920</td>\n",
       "      <td>SJER</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2017-10-06</th>\n",
       "      <td>0.305331</td>\n",
       "      <td>SJER</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2017-10-22</th>\n",
       "      <td>0.317006</td>\n",
       "      <td>SJER</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2017-11-07</th>\n",
       "      <td>0.313494</td>\n",
       "      <td>SJER</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2017-11-23</th>\n",
       "      <td>0.324650</td>\n",
       "      <td>SJER</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2017-12-09</th>\n",
       "      <td>0.352040</td>\n",
       "      <td>SJER</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2017-12-25</th>\n",
       "      <td>0.271738</td>\n",
       "      <td>SJER</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "            mean_ndvi  site\n",
       "date                       \n",
       "2017-01-12        NaN  HARV\n",
       "2017-01-28        NaN  HARV\n",
       "2017-02-13        NaN  HARV\n",
       "2017-03-01        NaN  HARV\n",
       "2017-03-17   0.281132  HARV\n",
       "2017-04-02   0.251133  HARV\n",
       "2017-04-18   0.541080  HARV\n",
       "2017-05-04   0.568924  HARV\n",
       "2017-05-20   0.811310  HARV\n",
       "2017-06-05        NaN  HARV\n",
       "2017-06-21   0.881739  HARV\n",
       "2017-07-07        NaN  HARV\n",
       "2017-07-23   0.819768  HARV\n",
       "2017-08-08        NaN  HARV\n",
       "2017-08-24   0.864464  HARV\n",
       "2017-09-09   0.857701  HARV\n",
       "2017-09-25   0.840639  HARV\n",
       "2017-10-11   0.652435  HARV\n",
       "2017-10-27   0.688382  HARV\n",
       "2017-11-12   0.613321  HARV\n",
       "2017-11-28   0.617948  HARV\n",
       "2017-12-14   0.498205  HARV\n",
       "2017-12-30        NaN  HARV\n",
       "2017-01-07        NaN  SJER\n",
       "2017-01-23        NaN  SJER\n",
       "2017-02-08        NaN  SJER\n",
       "2017-02-24   0.665524  SJER\n",
       "2017-03-12   0.664109  SJER\n",
       "2017-03-28   0.702343  SJER\n",
       "2017-04-13        NaN  SJER\n",
       "2017-04-29   0.610209  SJER\n",
       "2017-05-15   0.444847  SJER\n",
       "2017-05-31        NaN  SJER\n",
       "2017-06-16   0.358551  SJER\n",
       "2017-07-02   0.334559  SJER\n",
       "2017-07-18   0.319796  SJER\n",
       "2017-08-03        NaN  SJER\n",
       "2017-08-19   0.327455  SJER\n",
       "2017-09-04        NaN  SJER\n",
       "2017-09-20   0.330920  SJER\n",
       "2017-10-06   0.305331  SJER\n",
       "2017-10-22   0.317006  SJER\n",
       "2017-11-07   0.313494  SJER\n",
       "2017-11-23   0.324650  SJER\n",
       "2017-12-09   0.352040  SJER\n",
       "2017-12-25   0.271738  SJER"
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Create dataframe of NDVI including the cleaning data to deal with clouds\n",
    "\n",
    "# Important: to use the ungraded tests below as a sanity check,\n",
    "# name your columns: mean_ndvi and site\n",
    "# Don't forget to set date as the index and make the values of type datetime\n",
    "\n",
    "# apply ndvi calc and masking function using bounds list as the crop-extent parameter\n",
    "#in mask_crop_ndvi\n",
    "indexed_dfs = []\n",
    "\n",
    "for i, j  in zip(sitelists, bounds):\n",
    "    for k in i:\n",
    "        output_df = mask_crop_ndvi(image_folder = k, vals = vals, crop_extent = j, \n",
    "                   valid_range = (0, 10000))\n",
    "        indexed_dfs.append(output_df) #add it to a new list sorted in order\n",
    "\n",
    "mean_masked_ndvi = pd.concat(indexed_dfs) #combine dfs in list to new dataframe\n",
    "mean_masked_ndvi # call final object \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Using a parallel loop to call the appropriate boundary shapefile in each iteration \n",
    "# cloud_mask function may not be ideal for processing time (loops costly in terms \n",
    "# of processing time?), but the script is efficiently short, easy to follow and produces \n",
    "# the entire dataframe with one command (at least before concatonation of the dataframe), \n",
    "# rather than having to run the mask function separately for each site/shapefile. "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {
    "deletable": false,
    "editable": false,
    "nbgrader": {
     "cell_type": "code",
     "checksum": "1ce5d7d7519d5e569e6cf7c5927c6ffb",
     "grade": true,
     "grade_id": "cleaned_dataframes_test",
     "locked": true,
     "points": 10,
     "schema_version": 3,
     "solution": false,
     "task": false
    }
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "✅ Your data is stored in a DataFrame!\n",
      "✅ Correct number of masked data values!\n",
      "✅ You have the index set to the date column!\n",
      "✅ The data in your date column is datetime!\n",
      "Your total run time for processing the data was 0:00:12.571908.\n",
      "\n",
      " ➡ You received 10 out of 10 points for creating a dataframe.\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "10"
      ]
     },
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Last sanity check before creating your plot (10 points)\n",
    "\n",
    "# Ensure that you call your dataframe at the bottom of the cell above\n",
    "# and that it has columns called: mean_ndvi and site\n",
    "\n",
    "# Ensure the data is stored in a dataframe.\n",
    "student_ndvi_df = _\n",
    "\n",
    "df_points = 0\n",
    "\n",
    "if isinstance(student_ndvi_df, pd.DataFrame):\n",
    "    print('\\u2705 Your data is stored in a DataFrame!')\n",
    "    df_points +=2\n",
    "else:\n",
    "    print('\\u274C It appears your data is not stored in a DataFrame. ',\n",
    "          'To see what type of object your data is stored in, check its type with type(object)')\n",
    "\n",
    "# Check that dataframe contains the appropriate number of NAN values\n",
    "if student_ndvi_df.mean_ndvi.isna().sum() == 15:\n",
    "    print('\\u2705 Correct number of masked data values!')\n",
    "    df_points +=2\n",
    "else:\n",
    "    print('\\u274C The amount of null data in your dataframe is incorrect.')\n",
    "\n",
    "\n",
    "# Ensure that the date column is the index\n",
    "if isinstance(student_ndvi_df.index, pd.core.indexes.datetimes.DatetimeIndex):\n",
    "    print('\\u2705 You have the index set to the date column!')\n",
    "    df_points +=3\n",
    "else:\n",
    "    print('\\u274C You do not have the index set to the date column.')\n",
    "\n",
    "# Ensure that the date column is datetime\n",
    "if isinstance(student_ndvi_df.index[0], pd._libs.tslibs.timestamps.Timestamp):\n",
    "    print('\\u2705 The data in your date column is datetime!')\n",
    "    df_points +=3\n",
    "else:\n",
    "    print('\\u274C The data in your date column is not datetime.')\n",
    "\n",
    "# Output for timer, # DO NOT MODIFY\n",
    "end_time = datetime.now()\n",
    "total_time = end_time - start_time\n",
    "print(\n",
    "    \"Your total run time for processing the data was {0}.\".format(total_time))\n",
    "\n",
    "print(\"\\n \\u27A1 You received {} out of 10 points for creating a dataframe.\".format(\n",
    "    df_points))\n",
    "\n",
    "df_points"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {
    "caption": "Plot showing NDVI for each time period at both NEON Sites. In this example the cloudy pixels were removed using the pixel_qa cloud mask. Notice that this makes a significant different in the output values. Why do you think this difference is so significant?",
    "deletable": false,
    "nbgrader": {
     "cell_type": "code",
     "checksum": "f9d5ebf0557e366fa6f1727fd85a7e45",
     "grade": false,
     "grade_id": "plot_cleaned_dataframes_answer",
     "locked": false,
     "schema_version": 3,
     "solution": true,
     "task": false
    },
    "tags": [
     "hide"
    ]
   },
   "outputs": [
    {
     "data": {
      "image/png": "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ia4A2Itm8nngvPOOZfnynzN0aFduuSVPmyaLiMQpFVOJLrhYpwafe6Jt21RmzbqQ3NwRrFy5haysR3n44YXajkZEJI6omEp083HzM9vXdKI0FGMMl13Wg+XLr+G00zL4xS/e4JxznmLDhm1ehyYiImFQMZXotFhnzGjfvhVvvHEZU6b8lA8/XE/37g/z739r02QRkVinYiqRbQK+QF18McQYw89+ls2SJRPo0aMdV175MhdcMIvNm7VpsohIrFIxlcg0XipmHXXUobz7rts0+fXX13D88Q/z8survA5LRERCUDGVyOYDycAJXgcioQQ3TV60KIcOHVoxfPizjBnzMsXF2jRZRCSWqJhKZAuAXkCq14FIdbp3P4z588fz+9+fxlNPuU2T8/K0abKISKxQMZWoSoGPURdfnGjcOJk77zydDz+8itTUFM46y22aPH36J2RmTiYp6Q4yMyeTm7vM61BFRBKONhBJVKuA7WgmX5zp06c9n3zyM265JY/771+AMRCc7FdYWExOzmwARo3SRosiItGilqlENT9wqZapuNOsWQqTJw/msMOaU3nVhF279jFxYp43gYmIJCgVU4lqPnAI0MXrQKSuqlouoaiomNLSsihHIyLi5OYuS7jhByqmEtUCXKuU8ToQqatOndJCHrcWOnWazK235vG//2mvPxGJntzcZeTkzKawsBhrDww/8HtBpWIqEW0HlqPxUnFu0qQzSU1NqXAsNTWF66/vywknHME99/yXY499kP79pzNt2ids377Ho0hFJFFMnJjHrl37KhxLhOEHKqYS0ULAovFScW7UqB5MnXoeGRlpGAMZGWlMnXoekycPZvbskaxf/yvuvvsstmzZxVVXvcoRR/yNsWNfYd68Qm1RIyIRt3btdxQWFoe8rago9HG/MF69qWZnZ9v8/HxPnjvh/QW4FfgWN25KfM1ay/z5G5g+vYCZM5ezfftejj76UMaM6cXo0Vl06NDK6xBFJE5Za3n33XXcf/8CXn119UGTYoIyMtJYt+6GqMYWacaYRdba7JC3qZhKQEOB1bjlESSh7Ny5lxdfXMn06QXMnbsOY2DQoKMYOzaLoUO70rSpVksRkZr98MM+nn56GQ888DFLl35D27ap/OxnJ3L44S24+eZ3KnT1GQMPP/wTJkw4ycOI60/FlBxggcOBc4EZ3oYi3lq79jueeKKA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\n",
      "text/plain": [
       "<Figure size 720x432 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "# Add only the plot code to this cell\n",
    "\n",
    "# This is the final figure of mean NDVI\n",
    "# for both sites across the year\n",
    "# with data cleaned to deal with clouds\n",
    "\n",
    "# subset dataframe to exclude \"NA\" values\n",
    "plot_data = mean_masked_ndvi[mean_masked_ndvi['mean_ndvi'].notna()]\n",
    "\n",
    "\n",
    "colorPalette = {'HARV': 'magenta',\n",
    "                'SJER': 'navy'}\n",
    "\n",
    "# # Create figure and plot space\n",
    "fig, ax = plt.subplots(figsize=(10, 6))\n",
    "\n",
    "for key, data in plot_data.groupby('site'):\n",
    "    data.plot(use_index=True, \n",
    "              y='mean_ndvi', \n",
    "              ax=ax, \n",
    "              marker='o', \n",
    "              label=key,\n",
    "              color = colorPalette)\n",
    " \n",
    "\n",
    "### DO NOT REMOVE LINES BELOW ###\n",
    "final_masked_solution = nb.convert_axes(plt, which_axes=\"current\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {
    "deletable": false,
    "editable": false,
    "nbgrader": {
     "cell_type": "code",
     "checksum": "d2bc7d91b553a74e6382776fface9c70",
     "grade": true,
     "grade_id": "plot_cleaned_dataframes_test_answers",
     "locked": true,
     "points": 0,
     "schema_version": 3,
     "solution": false,
     "task": false
    }
   },
   "outputs": [],
   "source": [
    "# Ignore this cell for the autograding tests\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {
    "deletable": false,
    "editable": false,
    "nbgrader": {
     "cell_type": "code",
     "checksum": "23a1c68916e304be754ea15d9495e781",
     "grade": true,
     "grade_id": "plot_cleaned_dataframes_tests",
     "locked": true,
     "points": 50,
     "schema_version": 3,
     "solution": false,
     "task": false
    }
   },
   "outputs": [],
   "source": [
    "# Ignore this cell for the autograding tests\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "deletable": false,
    "editable": false,
    "nbgrader": {
     "cell_type": "markdown",
     "checksum": "c660ce8da16752276c4b16e35c7d2726",
     "grade": false,
     "grade_id": "question-1",
     "locked": true,
     "schema_version": 3,
     "solution": false,
     "task": false
    }
   },
   "source": [
    "# Question 1 (10 points)\n",
    "\n",
    "Imagine that you are planning NEON’s upcoming flight season to capture remote sensing data in these locations and want to ensure that you fly the area when the vegetation is the most green.\n",
    "\n",
    "When would you recommend the flights take place for each site? \n",
    "\n",
    "Answer the question in 2-3 sentences in the Markdown cell below."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "deletable": false,
    "nbgrader": {
     "cell_type": "markdown",
     "checksum": "26a85257b913135d401b6dc4fd2a4fc3",
     "grade": true,
     "grade_id": "question-1-answer",
     "locked": false,
     "points": 10,
     "schema_version": 3,
     "solution": true,
     "task": false
    }
   },
   "source": [
    "1. I would opt to fly at a time near the peak mean NDVI, likely early April for San Joaquin and near the end of June for Harvard Forest.  However, I would likely pick a period from several years worth of data.  Using Landsat 8, we may be able to determine an ideal period from up to eight years of data. "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "deletable": false,
    "editable": false,
    "nbgrader": {
     "cell_type": "markdown",
     "checksum": "603922a2076d0940962432ebc5069ef9",
     "grade": false,
     "grade_id": "question-2",
     "locked": true,
     "schema_version": 3,
     "solution": false,
     "task": false
    }
   },
   "source": [
    "# Question 2 (10 points)\n",
    "\n",
    "How could you modify your workflow to look at vegetation changes over time in each site? \n",
    "\n",
    "Answer the question in 2-3 sentences in the Markdown cell below."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "deletable": false,
    "nbgrader": {
     "cell_type": "markdown",
     "checksum": "f4ae5b1f3a47c9bf44714a2de486da54",
     "grade": true,
     "grade_id": "question-2-answer",
     "locked": false,
     "points": 10,
     "schema_version": 3,
     "solution": true,
     "task": false
    }
   },
   "source": [
    "2. My current workflow would support that pretty easily. To look at an individual site, I could skip the part of the loops that incorporated 'sites' which was a means to access multiple sites. The current functions review all image folders in the supplied path, so we could extend the time period reviewed simply by adding more image folders. If I wanted to review NDVI images rather than compare changes in a dataframe, I could remove the dataframe building chunk from my mask_cloud function and the function would instead return a list of arrays that I could plot from. "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "deletable": false,
    "editable": false,
    "nbgrader": {
     "cell_type": "markdown",
     "checksum": "df53001e9821bf3baef478a3b29bde33",
     "grade": false,
     "grade_id": "additional-markdown-cell-check",
     "locked": true,
     "points": 10,
     "schema_version": 3,
     "solution": false,
     "task": true
    }
   },
   "source": [
    "# Do not edit this cell! (10 points)\n",
    "\n",
    "The notebook includes:\n",
    "* additional Markdown cells throughout the notebook to describe: \n",
    "    * the data that you used - and where it is from\n",
    "    * how data are being processing\n",
    "    * how the code is optimized to run fast and be more concise"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "deletable": false,
    "editable": false,
    "nbgrader": {
     "cell_type": "markdown",
     "checksum": "bcc0e446306a9db445d1ab243227c563",
     "grade": false,
     "grade_id": "pep8-formatting-check",
     "locked": true,
     "points": 30,
     "schema_version": 3,
     "solution": false,
     "task": true
    }
   },
   "source": [
    "# Do not edit this cell! (20 points)\n",
    "\n",
    "The notebook will also be checked for overall clean code requirements as specified at the **top** of this notebook. Some of these requirements include (review the top cells for more specifics): \n",
    "\n",
    "* Notebook begins at cell [1] and runs on any machine in its entirety.\n",
    "* PEP 8 format is applied throughout (including lengths of comment and code lines).\n",
    "* No additional code or imports in the notebook that is not needed for the workflow.\n",
    "* Notebook is fully reproducible. This means:\n",
    "   * reproducible paths using the os module.\n",
    "   * data downloaded using code in the notebook.\n",
    "   * all imports at top of notebook."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "deletable": false,
    "editable": false,
    "nbgrader": {
     "cell_type": "markdown",
     "checksum": "67969627ed2d8a81a168d0ed1831224d",
     "grade": false,
     "grade_id": "cell-bf1766fe2443b94a",
     "locked": true,
     "points": 0,
     "schema_version": 3,
     "solution": false,
     "task": true
    }
   },
   "source": [
    "## BONUS - Export a  .CSV File to Share (10 points possible)\n",
    "\n",
    "This is optional - if you export a **.csv** file with the columns specified above: Site, Date and NDVI Value you can get an additional 10 points.\n",
    "\n",
    "* FULL CREDIT: File exists in csv format and contains the columns specified.\n",
    "We will check your github repo for this file!\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [],
   "source": [
    "#csvfile= os.path.join(et.io.HOME,\n",
    "#                      \"earth-analytics\", \n",
    "#                      \"ea-2021-04-ndvi-automation-streamfireflies\",\n",
    "#                      \"mean_masked_ndvi.csv\")\n",
    "#mean_masked_ndvi.to_csv(csvfile)\n",
    "\n",
    "# Was able to generate a .csv to be pushed to my repo, but the CI didn't like this. \n",
    "# Is it because the file isn't in the main (earthlab) repo?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.8"
  },
  "toc": {
   "base_numbering": 1,
   "nav_menu": {},
   "number_sections": true,
   "sideBar": true,
   "skip_h1_title": false,
   "title_cell": "Table of Contents",
   "title_sidebar": "Contents",
   "toc_cell": false,
   "toc_position": {
    "height": "calc(100% - 180px)",
    "left": "10px",
    "top": "150px",
    "width": "244.59375px"
   },
   "toc_section_display": true,
   "toc_window_display": true
  },
  "varInspector": {
   "cols": {
    "lenName": 16,
    "lenType": 16,
    "lenVar": 40
   },
   "kernels_config": {
    "python": {
     "delete_cmd_postfix": "",
     "delete_cmd_prefix": "del ",
     "library": "var_list.py",
     "varRefreshCmd": "print(var_dic_list())"
    },
    "r": {
     "delete_cmd_postfix": ") ",
     "delete_cmd_prefix": "rm(",
     "library": "var_list.r",
     "varRefreshCmd": "cat(var_dic_list()) "
    }
   },
   "types_to_exclude": [
    "module",
    "function",
    "builtin_function_or_method",
    "instance",
    "_Feature"
   ],
   "window_display": false
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
