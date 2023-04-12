{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<img style=\"float: left;\" src=\"earth-lab-logo-rgb.png\" width=\"150\" height=\"150\" />\n",
    "\n",
    "# Earth Analytics Education"
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
    "\n",
    "* Only include the package imports, code, and outputs that are required to run your homework assignment.\n",
    "* Be sure that your code can be run on any operating system. This means that:\n",
    "   1. the data should be downloaded in the notebook to ensure it's reproducible\n",
    "   2. all paths should be created dynamically using the `os.path.join`\n",
    "   3. sort lists of dated files even if they are sorted correctly by default on your machine\n",
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
    "**Your Name:**\n"
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
    "Matison Lakstigala"
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
     "checksum": "48a86f37895d93d54dde5dcb921d939f",
     "grade": false,
     "grade_id": "hw-instructions",
     "locked": true,
     "schema_version": 3,
     "solution": false,
     "task": false
    }
   },
   "source": [
    "# Fire Management Regimes - Yosemite National Park\n",
    "\n",
    "For this assignment, you will write code to generate a plot of the mean normalized difference vegetation index (NDVI) over time for the Illilouette watershed near Yosemite National Park, USA.\n",
    "\n",
    "The eventual goal is to characterize different fire regimes by comparing Illilouette watershed over time with control watersheds using the Normalized Burn Ratio index. This assignment will get you started on that larger goal.\n",
    "\n",
    "## Assignment Goals:\n",
    "  1. Download the Illilouette watershed boundary\n",
    "  2. Use a pre-written `EarthExplorerDownloader` *class* to automatically download and decompress one year of Landsat Analysis Ready Multispectral data\n",
    "  3. Load the downloaded data into a single xarray DataArray, performing necessary pre-processing tasks\n",
    "  4. Compute and plot the mean NDVI in the watershed over time\n",
    "\n",
    "## About the Earth Explorer M2M Interface\n",
    "The data that you will use for this week is available Earth Explorer. However, you will need more data that you can reasonably download using the web interface for Earth Explorer. Instead, you will need to write some code to download data using the Earth Explorer [Machine to Machine (M2M) interface](https://m2m.cr.usgs.gov/).\n",
    "\n",
    "**You will need to [sign up for access the the M2M interface](https://ers.cr.usgs.gov/profile/access) to complete this assignment -- please note that it can take a day or two to get access**"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Requirement already satisfied: ipykernel in /opt/conda/lib/python3.8/site-packages (5.4.2)\n",
      "Requirement already satisfied: tornado>=4.2 in /opt/conda/lib/python3.8/site-packages (from ipykernel) (6.1)\n",
      "Requirement already satisfied: ipython>=5.0.0 in /opt/conda/lib/python3.8/site-packages (from ipykernel) (7.20.0)\n",
      "Requirement already satisfied: traitlets>=4.1.0 in /opt/conda/lib/python3.8/site-packages (from ipykernel) (5.0.5)\n",
      "Requirement already satisfied: jupyter-client in /opt/conda/lib/python3.8/site-packages (from ipykernel) (6.1.11)\n",
      "Requirement already satisfied: pygments in /opt/conda/lib/python3.8/site-packages (from ipython>=5.0.0->ipykernel) (2.7.4)\n",
      "Requirement already satisfied: jedi>=0.16 in /opt/conda/lib/python3.8/site-packages (from ipython>=5.0.0->ipykernel) (0.18.0)\n",
      "Requirement already satisfied: setuptools>=18.5 in /opt/conda/lib/python3.8/site-packages (from ipython>=5.0.0->ipykernel) (49.6.0.post20210108)\n",
      "Requirement already satisfied: backcall in /opt/conda/lib/python3.8/site-packages (from ipython>=5.0.0->ipykernel) (0.2.0)\n",
      "Requirement already satisfied: decorator in /opt/conda/lib/python3.8/site-packages (from ipython>=5.0.0->ipykernel) (4.4.2)\n",
      "Requirement already satisfied: pexpect>4.3 in /opt/conda/lib/python3.8/site-packages (from ipython>=5.0.0->ipykernel) (4.8.0)\n",
      "Requirement already satisfied: pickleshare in /opt/conda/lib/python3.8/site-packages (from ipython>=5.0.0->ipykernel) (0.7.5)\n",
      "Requirement already satisfied: prompt-toolkit!=3.0.0,!=3.0.1,<3.1.0,>=2.0.0 in /opt/conda/lib/python3.8/site-packages (from ipython>=5.0.0->ipykernel) (3.0.14)\n",
      "Requirement already satisfied: parso<0.9.0,>=0.8.0 in /opt/conda/lib/python3.8/site-packages (from jedi>=0.16->ipython>=5.0.0->ipykernel) (0.8.1)\n",
      "Requirement already satisfied: ptyprocess>=0.5 in /opt/conda/lib/python3.8/site-packages (from pexpect>4.3->ipython>=5.0.0->ipykernel) (0.7.0)\n",
      "Requirement already satisfied: wcwidth in /opt/conda/lib/python3.8/site-packages (from prompt-toolkit!=3.0.0,!=3.0.1,<3.1.0,>=2.0.0->ipython>=5.0.0->ipykernel) (0.2.5)\n",
      "Requirement already satisfied: ipython-genutils in /opt/conda/lib/python3.8/site-packages (from traitlets>=4.1.0->ipykernel) (0.2.0)\n",
      "Requirement already satisfied: python-dateutil>=2.1 in /opt/conda/lib/python3.8/site-packages (from jupyter-client->ipykernel) (2.8.1)\n",
      "Requirement already satisfied: pyzmq>=13 in /opt/conda/lib/python3.8/site-packages (from jupyter-client->ipykernel) (22.0.1)\n",
      "Requirement already satisfied: jupyter-core>=4.6.0 in /opt/conda/lib/python3.8/site-packages (from jupyter-client->ipykernel) (4.7.1)\n",
      "Requirement already satisfied: six>=1.5 in /opt/conda/lib/python3.8/site-packages (from python-dateutil>=2.1->jupyter-client->ipykernel) (1.15.0)\n",
      "Note: you may need to restart the kernel to use updated packages.\n"
     ]
    }
   ],
   "source": [
    "pip install ipykernel"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "from cryptography.fernet import Fernet\n",
    "from glob import glob as glob\n",
    "import json\n",
    "import os\n",
    "import pathlib\n",
    "import re\n",
    "import tarfile\n",
    "import time\n",
    "import zipfile\n",
    "\n",
    "import folium\n",
    "import pandas as pd\n",
    "import geopandas as gpd\n",
    "import requests\n",
    "import rioxarray as rxr\n",
    "import xarray as xr\n",
    "\n",
    "working_dir = os.path.join(\n",
    "    pathlib.Path.home(), 'earth-analytics', 'data', 'fire-management')\n",
    "if not os.path.exists(working_dir):\n",
    "    os.makedirs(working_dir)\n",
    "\n",
    "os.chdir(working_dir)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "deletable": false,
    "editable": false,
    "nbgrader": {
     "cell_type": "markdown",
     "checksum": "5f3d65319f10810fc23ed0b8bc60fced",
     "grade": false,
     "grade_id": "cell-c18d242310199458",
     "locked": true,
     "schema_version": 3,
     "solution": false,
     "task": false
    }
   },
   "source": [
    "## Background: Fire Management in California, USA\n",
    "\n",
    "[Review this paper comparing runoff ratio in two California watersheds](https://link.springer.com/article/10.1007/s10021-016-0048-1). (You should have access from the CU libraries using your IdentiKey)\n",
    "\n",
    "In the cell below, write a summary of the article, including a site description. What are the implications of this study for wildfire management practices?"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "deletable": false,
    "nbgrader": {
     "cell_type": "markdown",
     "checksum": "bb46a83193852f597f75b7c36fbff236",
     "grade": true,
     "grade_id": "cell-4a07b3e5d8858146",
     "locked": false,
     "points": 10,
     "schema_version": 3,
     "solution": true,
     "task": false
    }
   },
   "source": [
    "Illiouette Creek, situated in Yosemite National Park in California, has experienced at least 150 fires since the 1970's due to its large forest cover. Since the park's establishment, forest fires were ultimately supresssed, no matter the cause. Fires that did escape suppression action were large, burned intensely, and resulted in high severity.\n",
    "\n",
    "Runoff ratio is defined as the runoff for each watershed divided by the precipitation for that watershed, in other words, the proportion of rainfall that does not infiltrate and is not taken up by evapotranspiration.\n",
    "\n",
    "This study highlights the ecohydrological benefits of managed wildfire in this watershed, leading to either stabilized or increased runoff yield and relatively low associated drought-related mortality."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Define your study area\n",
    "\n",
    "You are interested in checking the NDVI over time at the Illilouette watershed.\n",
    "\n",
    "### Download watershed boundary\n",
    "\n",
    "1. Start by downloading and caching the watershed boundary dataset for 2-digit HUC 18 (roughly California). Watershed Boundary Dataset (WBD) download urls can be found at [USGS's National Map Staged Products site](https://prd-tnm.s3.amazonaws.com/index.html?prefix=StagedProducts/Hydrography/WBD/HU2/Shape/) **Open your zip file path with 'wb' (binary write) permissions in order to dump the response content there.**\n",
    "\n",
    "2. The zip file will contain shapefiles of watersheds of different [Hydrologic Unit Code (HUC) lengths](https://nas.er.usgs.gov/hucs.aspx). You will need to unzip the downloaded file using the standard library `zipfile`. To access the WBD data. The `Shape` > `WBDHU12.shp` file contains the basins for this study.\n",
    "  * Check out this [example of how to access `.zip` file contents](https://docs.python.org/3/library/zipfile.html#zipfile.ZipFile.open). Once you have a zipfile object, use the `.extractall()` method to unzip.\n",
    "  * A second example may be found in the EarthExplorerDownloader class defined below\n",
    "\n",
    "3. Select your watershed of interest from the `GeoDataFrame`. Note that the WBD does **not** contain gage numbers as are referenced in the paper, so you will have to find the watershed by name. You can **search for strings in a GeoDataFrame column using the `.str.contains()` method** of GeoSeries.\n",
    "\n",
    "**Return the filtered GeoDataFrame with one row per watershed**"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {
    "deletable": false,
    "nbgrader": {
     "cell_type": "code",
     "checksum": "cd893c7c359ef1f5e27f9a32f1e01568",
     "grade": false,
     "grade_id": "cell-e4d31b67c4835429",
     "locked": false,
     "schema_version": 3,
     "solution": true,
     "task": false
    }
   },
   "outputs": [],
   "source": [
    "override_cache = False\n",
    "wbd_18_url = (\n",
    "    \"https://prd-tnm.s3.amazonaws.com/StagedProducts/\"\n",
    "    \"Hydrography/WBD/HU2/Shape/WBD_18_HU2_Shape.zip\")\n",
    "wbd_18_dir = 'water-boundary-dataset-hu18'\n",
    "wbd_18_path = os.path.join(wbd_18_dir, wbd_18_dir + '.zip')\n",
    "\n",
    "# Cache WBD file\n",
    "if not os.path.exists(wbd_18_dir):\n",
    "    os.makedirs(wbd_18_dir)\n",
    "\n",
    "if (not os.path.exists(wbd_18_path)) or override_cache:\n",
    "    # Download full WBD 18 as zipfile\n",
    "    response = requests.get(wbd_18_url)\n",
    "    with open (wbd_18_path, 'wb') as wbd_18_file:\n",
    "        wbd_18_file.write(response.content)\n",
    "\n",
    "    # Decompress\n",
    "    with zipfile.Zipfile(wbd_18_path, 'r') as wbd_zipfile:\n",
    "        wbd_zipfile.extractall(wbd_18_dir)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Generate a site map\n",
    "\n",
    "Your `folium` map should contains your watershed boundaries along with a terrain basemap. Bonus - label each watershed boundary layer and tooltip with its name. \n",
    "\n",
    "Check out some [example code from the folium documentation](https://python-visualization.github.io/folium/quickstart.html#GeoJSON/TopoJSON-Overlays)."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "ename": "DriverError",
     "evalue": "water-boundary-dataset-hu18/Shape/WBDHU12.shp: No such file or directory",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mCPLE_OpenFailedError\u001b[0m                      Traceback (most recent call last)",
      "\u001b[0;32mfiona/_shim.pyx\u001b[0m in \u001b[0;36mfiona._shim.gdal_open_vector\u001b[0;34m()\u001b[0m\n",
      "\u001b[0;32mfiona/_err.pyx\u001b[0m in \u001b[0;36mfiona._err.exc_wrap_pointer\u001b[0;34m()\u001b[0m\n",
      "\u001b[0;31mCPLE_OpenFailedError\u001b[0m: water-boundary-dataset-hu18/Shape/WBDHU12.shp: No such file or directory",
      "\nDuring handling of the above exception, another exception occurred:\n",
      "\u001b[0;31mDriverError\u001b[0m                               Traceback (most recent call last)",
      "\u001b[0;32m<ipython-input-4-bd95eb29a94a>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m\u001b[0m\n\u001b[1;32m      1\u001b[0m \u001b[0mwbd_18_path\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mos\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mpath\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mjoin\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mwbd_18_dir\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;34m'Shape'\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;34m'WBDHU12.shp'\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m----> 2\u001b[0;31m \u001b[0mwbd_18_gdf\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mgpd\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mread_file\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mwbd_18_path\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m      3\u001b[0m \u001b[0mill_gdf\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mwbd_18_gdf\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0mwbd_18_gdf\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mname\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mstr\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mcontains\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m'Illilouette'\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      4\u001b[0m \u001b[0mill_gdf\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m/opt/conda/lib/python3.8/site-packages/geopandas/io/file.py\u001b[0m in \u001b[0;36m_read_file\u001b[0;34m(filename, bbox, mask, rows, **kwargs)\u001b[0m\n\u001b[1;32m     94\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     95\u001b[0m     \u001b[0;32mwith\u001b[0m \u001b[0mfiona_env\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 96\u001b[0;31m         \u001b[0;32mwith\u001b[0m \u001b[0mreader\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mpath_or_bytes\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;34m**\u001b[0m\u001b[0mkwargs\u001b[0m\u001b[0;34m)\u001b[0m \u001b[0;32mas\u001b[0m \u001b[0mfeatures\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     97\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     98\u001b[0m             \u001b[0;31m# In a future Fiona release the crs attribute of features will\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m/opt/conda/lib/python3.8/site-packages/fiona/env.py\u001b[0m in \u001b[0;36mwrapper\u001b[0;34m(*args, **kwargs)\u001b[0m\n\u001b[1;32m    398\u001b[0m     \u001b[0;32mdef\u001b[0m \u001b[0mwrapper\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m*\u001b[0m\u001b[0margs\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;34m**\u001b[0m\u001b[0mkwargs\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    399\u001b[0m         \u001b[0;32mif\u001b[0m \u001b[0mlocal\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_env\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 400\u001b[0;31m             \u001b[0;32mreturn\u001b[0m \u001b[0mf\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m*\u001b[0m\u001b[0margs\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;34m**\u001b[0m\u001b[0mkwargs\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    401\u001b[0m         \u001b[0;32melse\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    402\u001b[0m             \u001b[0;32mif\u001b[0m \u001b[0misinstance\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0margs\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;36m0\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mstr\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m/opt/conda/lib/python3.8/site-packages/fiona/__init__.py\u001b[0m in \u001b[0;36mopen\u001b[0;34m(fp, mode, driver, schema, crs, encoding, layer, vfs, enabled_drivers, crs_wkt, **kwargs)\u001b[0m\n\u001b[1;32m    254\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    255\u001b[0m         \u001b[0;32mif\u001b[0m \u001b[0mmode\u001b[0m \u001b[0;32min\u001b[0m \u001b[0;34m(\u001b[0m\u001b[0;34m'a'\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;34m'r'\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 256\u001b[0;31m             c = Collection(path, mode, driver=driver, encoding=encoding,\n\u001b[0m\u001b[1;32m    257\u001b[0m                            layer=layer, enabled_drivers=enabled_drivers, **kwargs)\n\u001b[1;32m    258\u001b[0m         \u001b[0;32melif\u001b[0m \u001b[0mmode\u001b[0m \u001b[0;34m==\u001b[0m \u001b[0;34m'w'\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m/opt/conda/lib/python3.8/site-packages/fiona/collection.py\u001b[0m in \u001b[0;36m__init__\u001b[0;34m(self, path, mode, driver, schema, crs, encoding, layer, vsi, archive, enabled_drivers, crs_wkt, ignore_fields, ignore_geometry, **kwargs)\u001b[0m\n\u001b[1;32m    160\u001b[0m             \u001b[0;32mif\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mmode\u001b[0m \u001b[0;34m==\u001b[0m \u001b[0;34m'r'\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    161\u001b[0m                 \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0msession\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mSession\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 162\u001b[0;31m                 \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0msession\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mstart\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;34m**\u001b[0m\u001b[0mkwargs\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    163\u001b[0m             \u001b[0;32melif\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mmode\u001b[0m \u001b[0;32min\u001b[0m \u001b[0;34m(\u001b[0m\u001b[0;34m'a'\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;34m'w'\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    164\u001b[0m                 \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0msession\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mWritingSession\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32mfiona/ogrext.pyx\u001b[0m in \u001b[0;36mfiona.ogrext.Session.start\u001b[0;34m()\u001b[0m\n",
      "\u001b[0;32mfiona/_shim.pyx\u001b[0m in \u001b[0;36mfiona._shim.gdal_open_vector\u001b[0;34m()\u001b[0m\n",
      "\u001b[0;31mDriverError\u001b[0m: water-boundary-dataset-hu18/Shape/WBDHU12.shp: No such file or directory"
     ]
    }
   ],
   "source": [
    "wbd_18_path = os.path.join(wbd_18_dir, 'Shape', 'WBDHU12.shp')\n",
    "wbd_18_gdf = gpd.read_file(wbd_18_path)\n",
    "ill_gdf = wbd_18_gdf[wbd_18_gdf.name.str.contains('Illilouette')]\n",
    "ill_gdf"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {
    "deletable": false,
    "nbgrader": {
     "cell_type": "code",
     "checksum": "88b5d56acf2445153b8090b0d541f505",
     "grade": false,
     "grade_id": "cell-a1c7a78987f0afd9",
     "locked": false,
     "schema_version": 3,
     "solution": true,
     "task": false
    }
   },
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'ill_gdf' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[0;32m<ipython-input-6-b707c860c2ea>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m\u001b[0m\n\u001b[1;32m      1\u001b[0m m = folium.Map(\n\u001b[0;32m----> 2\u001b[0;31m     \u001b[0mlocation\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0mill_gdf\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mcentroid\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0my\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mill_gdf\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mcentroid\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mx\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m      3\u001b[0m     \u001b[0mtitles\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0;34m'cartodbpositron'\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      4\u001b[0m     \u001b[0mzoom_start\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0;36m11\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      5\u001b[0m )\n",
      "\u001b[0;31mNameError\u001b[0m: name 'ill_gdf' is not defined"
     ]
    }
   ],
   "source": [
    "m = folium.Map(\n",
    "    location=[ill_gdf.centroid.y, ill_gdf.centroid.x],\n",
    "    titles='cartodbpositron',\n",
    "    zoom_start=11\n",
    ")\n",
    "\n",
    "folium.GeoJson(ill_gdf, name='Illilouette Basin').add_to(m)\n",
    "m"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "deletable": false,
    "editable": false,
    "nbgrader": {
     "cell_type": "markdown",
     "checksum": "e112875dd738b87c6386582c408f32c1",
     "grade": false,
     "grade_id": "cell-8bb64b442465fb40",
     "locked": true,
     "points": 10,
     "schema_version": 3,
     "solution": false,
     "task": true
    }
   },
   "source": [
    "## Download Multispectral Data Using the Machine to Machine (M2M) Earth Explorer API\n",
    "\n",
    "**You will need to have your Earth Explorer account activated to work with M2M to complete this section**\n",
    "\n",
    "To start, download 6 months of multispectral surface reflectance data using the following parameters:\n",
    "  - Use the \"Landsat 4-9 C2 U.S. ARD\" dataset\n",
    "  - Use the watershed boundary as the spatial boundary\n",
    "  - 6 months of data (you will find that you need to make changes to the code to download more than 100 scenes)\n",
    "\n",
    "The cell below contains two classes that can help you with the download. Your task here is to:\n",
    "  * **Add descriptive docstrings to each class and method in the cell below**. What does each method do?\n",
    "  * In the cell below, initialize the class and use it to complete the Earth Explorer download. You should only need a few lines of code to complete the download (note that it can take in the vicinity of 20 minutes for Earth Explorer to prepare your download, and the class below should update you on the status of your download every 30 seconds.)\n",
    "  \n",
    "The steps for downloading using the classes below are:\n",
    "  1. Define the bounding box\n",
    "  2. Initialize the EarthExplorerDownloader instance\n",
    "    * one year of data (Start with less to test your code!)\n",
    "    * only download data needed to cover the watershed boundary\n",
    "    * Dataset: \"Landsat 4-9 C2 U.S. ARD\"\n",
    "  3. Submit a download request\n",
    "  4. Download"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "class BBox:\n",
    "    def __init__(self, llx, lly, urx, ury):\n",
    "        self.llx, self.lly, self.urx, self.ury = llx, lly, urx, ury\n",
    "\n",
    "    @property\n",
    "    def spatial_filter(self):\n",
    "        return {\n",
    "            'filterType': \"mbr\",\n",
    "            'lowerLeft': {'latitude': self.lly, 'longitude': self.llx},\n",
    "            'upperRight': {'latitude': self.ury, 'longitude': self.urx}}\n",
    "\n",
    "class EarthExplorerDownloader:\n",
    "\n",
    "    base_url = \"https://m2m.cr.usgs.gov/api/api/json/stable/{endpoint}\"\n",
    "    product_filter = {'productName': 'C2 ARD Tile Surface Reflectance Bundle Download'}\n",
    "    dld_file_tmpl = '{display_id}.tar'\n",
    "\n",
    "    def __init__(self, dataset, label, bbox, start, end):\n",
    "        self.api_key = None\n",
    "        self.login()\n",
    "        \n",
    "        self.dataset, self.label = dataset, label\n",
    "        self.bbox, self.start, self.end = bbox, start, end\n",
    "        \n",
    "        self.temporal_filter = {'start': start, 'end': end}\n",
    "        self.acquisition_filter = self.temporal_filter\n",
    "        \n",
    "        self.path_tmpl = os.path.join(self.label, self.dld_file_tmpl)\n",
    "        if not os.path.exists(label):\n",
    "            os.makedirs(label)\n",
    "        \n",
    "        self._dataset_alias = None\n",
    "\n",
    "    def get_ee_login_info(self, info_type):\n",
    "        # Generate and store key\n",
    "        key_path = os.path.join(pathlib.Path.home(), '.ee_key')\n",
    "        if not os.path.exists(key_path):\n",
    "            print('Generating new key...')\n",
    "            key = Fernet.generate_key()\n",
    "            with open(key_path, 'wb') as key_file:\n",
    "                key_file.write(key)\n",
    "        with open(key_path, 'rb') as key_file:\n",
    "            key = key_file.read()\n",
    "        fernet = Fernet(key)\n",
    "\n",
    "        # Collect and store login info\n",
    "        info_path = os.path.join(\n",
    "            pathlib.Path.home(),\n",
    "            '.ee_{}'.format(info_type))\n",
    "        if not os.path.exists(info_path):\n",
    "            info = input('Enter {}: '.format(info_type))\n",
    "            with open(info_path, 'wb') as info_file:\n",
    "                info_file.write(fernet.encrypt(bytes(info, 'utf-8')))\n",
    "        with open(info_path, 'rb') as info_file:\n",
    "            return fernet.decrypt(info_file.read()).decode(\"utf-8\")\n",
    "\n",
    "    def login(self):\n",
    "        if self.api_key is None:\n",
    "            login_payload = {\n",
    "                'username': self.get_ee_login_info('username'), \n",
    "                'password': self.get_ee_login_info('password')}\n",
    "            self.api_key = self.post(\"login\", login_payload)\n",
    "            print('Login Successful')\n",
    "        \n",
    "    @property\n",
    "    def headers(self):\n",
    "        if self.api_key is None:\n",
    "            return None\n",
    "        return  {'X-Auth-Token': self.api_key}\n",
    "    \n",
    "    def logout(self):\n",
    "        self.post(\"logout\", None)\n",
    "        print(\"Logged Out\\n\\n\")\n",
    "\n",
    "    def post(self, endpoint, data):\n",
    "        # Send POST requests\n",
    "        url = self.base_url.format(endpoint=endpoint)\n",
    "        response = requests.post(url, json.dumps(data), headers=self.headers)\n",
    "        \n",
    "        # Raise any HTTP Errors\n",
    "        response.raise_for_status()\n",
    "        \n",
    "        # Return data\n",
    "        return response.json()['data']\n",
    "    \n",
    "    @property\n",
    "    def dataset_alias(self):\n",
    "        if self._dataset_alias is None:\n",
    "            print(\"Searching datasets...\")\n",
    "            params = {\n",
    "                'datasetName': self.dataset,\n",
    "                'spatialFilter': self.bbox.spatial_filter,\n",
    "                'temporalFilter': self.temporal_filter}\n",
    "            datasets = self.post(\"dataset-search\", params)\n",
    "            \n",
    "            # Get a single dataset alias\n",
    "            if len(datasets) > 1:\n",
    "                print(datasets)\n",
    "                raise ValueError('Multiple datasets found - refine search.')\n",
    "            self._dataset_alias = datasets[0]['datasetAlias']\n",
    "            \n",
    "            print('Using dataset alias: {}'.format(self._dataset_alias))\n",
    "        return self._dataset_alias\n",
    "    \n",
    "    def find_scene_ids(self):\n",
    "        params = {\n",
    "            'datasetName': self.dataset_alias,\n",
    "            'startingNumber': 1,\n",
    "            \n",
    "            'sceneFilter': {\n",
    "                'spatialFilter': self.bbox.spatial_filter,\n",
    "                'acquisitionFilter': self.acquisition_filter}}\n",
    "        \n",
    "        print(\"Searching scenes...\")\n",
    "        scenes = self.post(\"scene-search\", params)\n",
    "        print('Found {} scenes'.format(scenes['recordsReturned']))\n",
    "        return scenes\n",
    "    \n",
    "    def find_available_product_info(self):\n",
    "        scenes = self.find_scene_ids()\n",
    "        params = {\n",
    "            'datasetName': self.dataset_alias, \n",
    "            'entityIds': [scene['entityId'] for scene in scenes['results']]}\n",
    "        products = self.post(\"download-options\", params)\n",
    "\n",
    "        # Aggregate a list of available products\n",
    "        product_info = []\n",
    "        for product in products:\n",
    "            # Make sure the product is available for this scene\n",
    "            if product['available']==True or product['proxied']==True:\n",
    "                product_info.append({\n",
    "                    'entityId': product['entityId'],\n",
    "                    'productId': product['id']})\n",
    "        if not product_info:\n",
    "            raise ValueError('No available products.')\n",
    "        return product_info\n",
    "\n",
    "    def submit_download_request(self):\n",
    "        product_info = self.find_available_product_info()\n",
    "        # Did we find products?\n",
    "        if product_info:\n",
    "            # Request downloads\n",
    "            params = {\n",
    "                'downloads': product_info,\n",
    "                'label': self.label}\n",
    "            downloads = self.post(\"download-request\", params)\n",
    "            print('Downloads staging...')\n",
    "        else:\n",
    "            raise ValueError(\n",
    "                'No products found with the specified boundaries.')\n",
    "    \n",
    "    def check_download_status(self):\n",
    "        params = {'label': self.label}\n",
    "        downloads = self.post(\"download-retrieve\", params)\n",
    "        return downloads\n",
    "    \n",
    "    def wait_for_available_downloads(self, timeout=None):\n",
    "        keep_waiting = True\n",
    "        while keep_waiting:\n",
    "            downloads = self.check_download_status()\n",
    "            n_queued = downloads['queueSize']\n",
    "            keep_waiting = n_queued > 0\n",
    "            if keep_waiting:\n",
    "                print(\"\\n\", n_queued,\n",
    "                      \"downloads queued but not yet available. \"\n",
    "                      \"Waiting for 30 seconds.\\n\")\n",
    "                time.sleep(30)\n",
    "            \n",
    "            if not timeout is None:\n",
    "                timeout -= 30\n",
    "                if timeout < 0:\n",
    "                    break\n",
    "\n",
    "        return downloads\n",
    "        \n",
    "    def download(self, wait=True, timeout=None, override=True):\n",
    "        # Check download status\n",
    "        if wait:\n",
    "            downloads = self.wait_for_available_downloads(timeout=timeout)\n",
    "        else:\n",
    "            downloads = self.check_download_status()\n",
    "            \n",
    "        available_or_proxied = (\n",
    "            downloads['available'] \n",
    "            + [dld for dld in downloads['requested'] if dld['statusCode']=='P'])\n",
    "        if not available_or_proxied:\n",
    "            raise ValueError('No available downloads.')\n",
    "        \n",
    "        # Download available downloads\n",
    "        for download in available_or_proxied:\n",
    "            # Filter out products\n",
    "            if not self.product_filter is None:\n",
    "                match = [download[k]==v for k, v in self.product_filter.items()]\n",
    "                if not all(match):\n",
    "                    continue\n",
    "            \n",
    "            # Download and save compressed file\n",
    "            dld_path = self.path_tmpl.format(display_id=download['displayId'])\n",
    "            # Cache downloads\n",
    "            if override or not os.path.exists(dld_path):\n",
    "                print('Saving download: {}'.format(download['displayId']))\n",
    "                with open(dld_path, 'wb') as dld_file:\n",
    "                    response = requests.get(download['url'])\n",
    "                    dld_file.write(response.content)\n",
    "            \n",
    "            self.uncompress(dld_path)\n",
    "                    \n",
    "    def uncompress(self, download_path):\n",
    "        # Extract compressed files\n",
    "        with tarfile.TarFile(download_path, 'r') as dld_tarfile:\n",
    "            dld_tarfile.extractall(self.label)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "ill_bbox = BBox(*ill_gdf.total_bounds)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "deletable": false,
    "nbgrader": {
     "cell_type": "code",
     "checksum": "ca763f527b6699ef7b00a04b759283d6",
     "grade": true,
     "grade_id": "cell-510047e3b6fb8ed8",
     "locked": false,
     "points": 20,
     "schema_version": 3,
     "solution": true,
     "task": false
    }
   },
   "outputs": [],
   "source": [
    "# Initialize downloader\n",
    "landsat_downloader = EarthExplorerDownloader(\n",
    "    dataset='Landsat 4-9 C2 U.S. ARD',\n",
    "    label='landsat-ard-ill-2020-mini',\n",
    "    bbox=ill_bbox,\n",
    "    start='2020-01-01',\n",
    "    end='2020-01-14')\n",
    "landsat_downloader"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'landsat_downloader' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[0;32m<ipython-input-7-d0d66b87109c>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m\u001b[0m\n\u001b[0;32m----> 1\u001b[0;31m \u001b[0mlandsat_downloader\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mstart\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mlandsat_downloader\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mend\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[0;31mNameError\u001b[0m: name 'landsat_downloader' is not defined"
     ]
    }
   ],
   "source": [
    "landsat_downloader.start, landsat_downloader.end"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "landsat_downloader.submit_download_request()\n",
    "landsat_downloader.download(override=False)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "deletable": false,
    "editable": false,
    "nbgrader": {
     "cell_type": "markdown",
     "checksum": "58d52128e85a1fd7a6e59682c1753a04",
     "grade": false,
     "grade_id": "ndvi-mean-site-instructions",
     "locked": true,
     "schema_version": 3,
     "solution": false,
     "task": false
    }
   },
   "source": [
    "# A Time Series of Mean NDVI For the Illilouette Watershed\n",
    "\n",
    "Now that you have downloaded some multispectral data, you can compute NDVI over time. Over a long period of time, these computations can help to characterize the fire management regimes in different watersheds.\n",
    "\n",
    "## Get information about the files you downloaded\n",
    "Using the `glob` library, create a `DataFrame` containing the following information about each scene you downloaded:\n",
    "  - Band raster file path\n",
    "  - Corresponding cloud/aerosol QA path (file ending in 'QA_AEROSOL.TIF')\n",
    "  - Date\n",
    "  - Band\n",
    "\n",
    "Hints:\n",
    " * If you have a list of dictionaries with matching keys, you can make a DataFrame using `pd.DataFrame(data=list_of_dictionaries)`.\n",
    " * Need to look at some example file names? Use the code `ls | head -n 25` in `bash` to view the first 25 of the files you downloaded."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "ls ~/earth-analytics/data/fire-management/landsat-ard-ill-2020-mini"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "glob(os.path.join(landsat_dir, '*SR*QA*TIF'))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "landsat_dir = landsat_downloader.label\n",
    "tif_paths = sorted(glob(os.path.join(landsat_dir, 'LC08*SR_B*.TIF')))\n",
    "\n",
    "def get_band_info(tif_path):\n",
    "    \"\"\"Extracts band and date info from Landsat file path\"\"\"\n",
    "    tif_re = re.compile(r'(?P<base>LC08_CU_003009_(?P<date>\\d+)_\\d+_02_SR_)B(?P<band>\\d).TIF')\n",
    "    tif_match = tif_re.search(tif_path)\n",
    "    return {\n",
    "        'band_path': tif_path,\n",
    "        'date': pd.to_datetime(tif_match.group('date')),\n",
    "        'band': int(tif_match.group('band')),\n",
    "        'qa_path': tif_match.group('base') + 'QA_AEROSOL.TIF'}\n",
    "\n",
    "band_df = pd.DataFrame([get_band_info(pth) for pth in tif_paths])\n",
    "band_df"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "deletable": false,
    "editable": false,
    "nbgrader": {
     "cell_type": "markdown",
     "checksum": "05256960cbb34795d2f2862014804f2c",
     "grade": false,
     "grade_id": "cell-7bcbb6a14f49ee08",
     "locked": true,
     "points": 25,
     "schema_version": 3,
     "solution": false,
     "task": true
    }
   },
   "source": [
    "## Clip and mask Landsat data\n",
    "\n",
    "Write a function, multiple functions or a class to reproducibly perform the following steps:\n",
    "  * open a raster in your DataFrame\n",
    "  * clip it to the watershed boundary\n",
    "  * mask data outside the valid range of 0-40000\n",
    "  * mask data covered by clouds\n",
    "    * open the corresponding aerosol QA raster\n",
    "    * mask locations with values in [328, 392, 840, 904, 1350, 352, 368, 416, 432, 480, 864, 880, 928, 944, 992, 480, 992]\n",
    "  * filter out data that is more than 50% masked\n",
    "  \n",
    "Not every step must be in the function - use your judgement about the most readable and DRY approach. "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Product: DataFrame with band paths, band numbers, dates, and qa paths\n",
    "Outcome: DataArray (x, y, date) of Landsat 8 NBR\n",
    "\n",
    "For each date:\n",
    "- Grab bands 5 AND 7\n",
    "- For each band:\n",
    "    1. Open band, masked, and squeezed\n",
    "    2. Clip to study area\n",
    "    3. Mask valid range\n",
    "    4. Cloud mask\n",
    "    5. Merge bands 5 and 7 into NBR\n",
    "- Concatenate NBR DataArrays\n",
    "- Filter out empty or nearly empty data arrays"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'band_df' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[0;32m<ipython-input-8-82d04081228c>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m\u001b[0m\n\u001b[1;32m      2\u001b[0m \u001b[0mill_ls_gdf\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0;32mNone\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      3\u001b[0m \u001b[0mnbr_das\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0;34m[\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m----> 4\u001b[0;31m \u001b[0;32mfor\u001b[0m \u001b[0mdate\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mone_date_df\u001b[0m \u001b[0;32min\u001b[0m \u001b[0mband_df\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0mband_df\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mband\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0misin\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;36m5\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;36m7\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mgroupby\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m'date'\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m      5\u001b[0m    \u001b[0mone_date_bands\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0;34m{\u001b[0m\u001b[0;34m}\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      6\u001b[0m    \u001b[0;32mfor\u001b[0m \u001b[0mi\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mband\u001b[0m \u001b[0;32min\u001b[0m \u001b[0mone_date_df\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0miterrows\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;31mNameError\u001b[0m: name 'band_df' is not defined"
     ]
    }
   ],
   "source": [
    "# Load in each scene from dataframe\n",
    "ill_ls_gdf = None\n",
    "nbr_das = []\n",
    "for date, one_date_df in band_df[band_df.band.isin([5, 7])].groupby('date'):\n",
    "   one_date_bands = {}\n",
    "   for i, band in one_date_df.iterrows():\n",
    "      # Open DataArray\n",
    "      band_da = (\n",
    "         rxr.open_rasterio(band.band_path, masked=True)\n",
    "         .squeeze())\n",
    "      band_da.name = 'reflectance'\n",
    "   \n",
    "      # Reproject boundary (only once)\n",
    "      if ill_ls_gdf is None:\n",
    "         ill_ls_gdf = ill_gdf.to_crs(band_da.rio.crs)\n",
    "         bbox = BBox(*ill_ls_gdf.total_bounds)\n",
    "      \n",
    "      # Clip to the bounding box\n",
    "      band_da = band_da.rio.clip_box(\n",
    "               minx=ill_bbox.llx, miny=ill_bbox.lly,\n",
    "               maxx=ill_bbox.urx, maxy=ill_bbox.ury)\n",
    "   \n",
    "      band_da = band_da.assign_coords(date=band.date)\n",
    "      one_date_bands[band.band] = band_da\n",
    "\n",
    "   nbr_da = ((one_date_bands[5] - one_date_bands[7])\n",
    "             / (one_date_bands[5] + one_date_bands[7]))\n",
    "   \n",
    "   nbr_das.append(nbr_da)\n",
    "nbr_das[0]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "deletable": false,
    "editable": false,
    "nbgrader": {
     "cell_type": "markdown",
     "checksum": "8cd89e1a8aac24a2558d847ca9a1541b",
     "grade": false,
     "grade_id": "cell-99a4412518925557",
     "locked": true,
     "points": 4,
     "schema_version": 3,
     "solution": false,
     "task": true
    }
   },
   "source": [
    "Test your process by plotting your data using the following code:\n",
    "\n",
    "```python\n",
    "landsat_ds.plot(col='date', col_wrap=5, \n",
    "                subplot_kws={'xticklabels': 'off',\n",
    "                             'yticklabels': 'off'})\n",
    "```"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {
    "deletable": false,
    "nbgrader": {
     "cell_type": "code",
     "checksum": "8043bfba2449fb959ec6c3c29fd21520",
     "grade": false,
     "grade_id": "cell-5b3f7f3bb8094d5a",
     "locked": false,
     "schema_version": 3,
     "solution": true,
     "task": false
    }
   },
   "outputs": [
    {
     "ename": "ValueError",
     "evalue": "must supply at least one object to concatenate",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mStopIteration\u001b[0m                             Traceback (most recent call last)",
      "\u001b[0;32m/opt/conda/lib/python3.8/site-packages/xarray/core/concat.py\u001b[0m in \u001b[0;36mconcat\u001b[0;34m(objs, dim, data_vars, coords, compat, positions, fill_value, join, combine_attrs)\u001b[0m\n\u001b[1;32m    171\u001b[0m     \u001b[0;32mtry\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 172\u001b[0;31m         \u001b[0mfirst_obj\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mobjs\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mutils\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mpeek_at\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mobjs\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    173\u001b[0m     \u001b[0;32mexcept\u001b[0m \u001b[0mStopIteration\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m/opt/conda/lib/python3.8/site-packages/xarray/core/utils.py\u001b[0m in \u001b[0;36mpeek_at\u001b[0;34m(iterable)\u001b[0m\n\u001b[1;32m    182\u001b[0m     \u001b[0mgen\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0miter\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0miterable\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 183\u001b[0;31m     \u001b[0mpeek\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mnext\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mgen\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    184\u001b[0m     \u001b[0;32mreturn\u001b[0m \u001b[0mpeek\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mitertools\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mchain\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0mpeek\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mgen\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;31mStopIteration\u001b[0m: ",
      "\nDuring handling of the above exception, another exception occurred:\n",
      "\u001b[0;31mValueError\u001b[0m                                Traceback (most recent call last)",
      "\u001b[0;32m<ipython-input-9-fbc3020bd083>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m\u001b[0m\n\u001b[0;32m----> 1\u001b[0;31m \u001b[0mall_nbr_da\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mxr\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mconcat\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mnbr_das\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mdim\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0;34m'date'\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m      2\u001b[0m all_nbr_da.plot(col='date', col_wrap=5,\n\u001b[1;32m      3\u001b[0m                 subplot_kws={'xticklabels': 'off',\n\u001b[1;32m      4\u001b[0m                              'yticklabels': 'off'})\n",
      "\u001b[0;32m/opt/conda/lib/python3.8/site-packages/xarray/core/concat.py\u001b[0m in \u001b[0;36mconcat\u001b[0;34m(objs, dim, data_vars, coords, compat, positions, fill_value, join, combine_attrs)\u001b[0m\n\u001b[1;32m    172\u001b[0m         \u001b[0mfirst_obj\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mobjs\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mutils\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mpeek_at\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mobjs\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    173\u001b[0m     \u001b[0;32mexcept\u001b[0m \u001b[0mStopIteration\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 174\u001b[0;31m         \u001b[0;32mraise\u001b[0m \u001b[0mValueError\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"must supply at least one object to concatenate\"\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    175\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    176\u001b[0m     \u001b[0;32mif\u001b[0m \u001b[0mcompat\u001b[0m \u001b[0;32mnot\u001b[0m \u001b[0;32min\u001b[0m \u001b[0m_VALID_COMPAT\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;31mValueError\u001b[0m: must supply at least one object to concatenate"
     ]
    }
   ],
   "source": [
    "all_nbr_da = xr.concat(nbr_das, dim='date')\n",
    "all_nbr_da.plot(col='date', col_wrap=5,\n",
    "                subplot_kws={'xticklabels': 'off',\n",
    "                             'yticklabels': 'off'})"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "deletable": false,
    "editable": false,
    "nbgrader": {
     "cell_type": "markdown",
     "checksum": "5f3e9e5c2f4dd0daa63700529270d660",
     "grade": false,
     "grade_id": "cell-c65b14e2297bad61",
     "locked": true,
     "points": 5,
     "schema_version": 3,
     "solution": false,
     "task": true
    }
   },
   "source": [
    "## Plot the mean NBR over time\n",
    "\n",
    "In the cell below, summarize and plot your DataArray"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "deletable": false,
    "nbgrader": {
     "cell_type": "markdown",
     "checksum": "0a18a93bef486192c421801113778ebc",
     "grade": true,
     "grade_id": "cell-f5226184b5a8e6ed",
     "locked": false,
     "points": 5,
     "schema_version": 3,
     "solution": true,
     "task": false
    }
   },
   "source": [
    "nbr_mean = nbr_das.groupby('date').mean(...)\n",
    "\n",
    "nbr_mean.plot(label='Mean NBR', color='red')"
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
     "points": 5,
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
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
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
   "version": "3.7.13"
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
   "toc_position": {},
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
  },
  "vscode": {
   "interpreter": {
    "hash": "916dbcbb3f70747c44a77c7bcd40155683ae19c65e1c03b4aa3499c5328201f1"
   }
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
