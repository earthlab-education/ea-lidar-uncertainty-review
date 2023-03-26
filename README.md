# ea-05-lidar-uncertainty-worflow

This repository is to recreate the LiDAR data analysis exploring tree heigh from the canopy heigh model.  This analysis will compare these measurements to the same types of measurements made by humans in the field.

The necessary data can be retreived from the `EarthPy` pacakge.

https://earthpy.readthedocs.io/en/latest/

This package, and other necessary packages can be installed into your local environment by installing the `environment.yml` file.  For example:

- `conda env create -f environment.yml`

It may be helpful to review the notes from EarthLab on creating and installing Conda Environments.

https://www.earthdatascience.org/courses/intro-to-earth-data-science/python-code-fundamentals/use-python-packages/use-conda-environments-and-install-packages/

Once you have the necessary packages installed you can download the data necessary to run this notebook as:

`et.data.get_data('spatial-vector-lidar')`

This notebook will:

- For both the SJER and SOAP field sites, create scatterplots (with regression and 1:1 lines) that compare:
    - **MAXIMUM** canopy height model height in meters, extracted within a 20 meter radius, compared to **MAXIMUM** tree
- height derived from the *insitu* field site data.
    - **MEAN** canopy height model height in meters, extracted within a 20 meter radius, compared to **MEAN** tree height derived from the *insitu* field site data.

