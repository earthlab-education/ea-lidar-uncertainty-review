def set_paths(study_site):
    """ 
    Set up paths, directories, and study site name variable for the project.

    Parameters:
    ----------

    """

    import os
    import pathlib

    home_dir = os.path.join(
        pathlib.Path.home(),
        'earth-analytics',
        'data',
        'spatial-vector-lidar'
    )

    base_dir = os.path.join(
        'california',
        "neon-{}-site".format(study_site),
    )

    # Create an output dir for created files.
    output_path = os.path.join(home_dir, 'outputs')
    if not os.path.isdir(output_path):
        os.makedir(output_path)

    # ----------------------------------

    # Ground based measurement file.
    if (study_site == 'sjer'):
        insitu_path = os.path.join(
            base_dir,
            '2013',
            'insitu',
            'veg_structure',
            "D17_2013_{}_vegStr.csv".format(study_site.upper()),
        )
    elif (study_site == 'soap'):
        insitu_path = os.path.join(
            base_dir,
            '2013',
            'insitu',
            'veg-structure',
            "D17_2013_{}_vegStr.csv".format(study_site.upper()),
        )

    # Lidar Canopy Height Model
    lidar_chm_path = os.path.join(
        base_dir,
        '2013',
        'lidar',
        "{}_lidarCHM.tif".format(study_site),
    )

    # plots_path: Path to study site point locations.
    if (study_site == 'sjer'):
        plots_path = os.path.join(
            base_dir,
            'vector_data',
            "{}_plot_centroids.shp".format(study_site)
        )
    elif (study_site == 'soap'):
        plots_path = os.path.join(
            base_dir,
            'vector_data',
            "{}_centroids.shp".format(study_site)
        )

    # USA country boundary file.
    usa_bndry_path = os.path.join(
        home_dir, 'usa', 'usa-boundary-dissolved.shp')

    # States boundary file.
    states_bndry_path = os.path.join(
        home_dir, 'usa', 'usa-states-census-2014.shp')

    # Road geometry in study area.
    if (study_site == 'sjer'):
        county = 'madera'
        roads_shp = 'tl_2013_06039_roads.shp'

    elif (study_site == 'soap'):
        county = 'fresno'
        roads_shp = 'tl_2018_06019_roads.shp'

    roads_path = os.path.join(
        home_dir,
        'california',
        "{}-county-roads".format(county),
        roads_shp
    )

    # Study site boundary geometry file.
    aoi_path = os.path.join(
        base_dir,
        'vector_data',
        "{}_crop.shp".format(study_site.upper())
    )

    os.chdir(home_dir)

    return (
        home_dir, plots_path, insitu_path,
        lidar_chm_path, output_path, usa_bndry_path,
        states_bndry_path, roads_path,
        aoi_path
    )
