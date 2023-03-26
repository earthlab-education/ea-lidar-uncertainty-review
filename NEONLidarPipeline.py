class NEONLidarPipeline:
    """
    A class to execute a pipeline for NEON lidar data.

    Attributes:
        site_name (str): The name of the NEON site.
        separator (str): The separator used in the insitu data file.
        base_dir (str): The base directory for the site data.
        insitu_path (str): The path to the insitu vegetation structure data.
        chm_path (str): The path to the lidar canopy height (CHM) data.
        plot_path (str): The path to the plot centroid shapefile.
    """
    import os
    import pandas as pd
    import geopandas as gpd
    import rasterstats as rs

    def __init__(self, site_name: str, separator: str):
        """
        Initialize the NEONLidarPipeline class.
        With given site_name and separator.

        Parameters
        ----------
        site_name : str
            Name of the site to process.
        separator : str
            Separator used in the file paths.
        """
        import os

        self.base_dir = os.path.join(
            'california',
            'neon-{site_name}-site').format(site_name=site_name)

        self.insitu_path = os.path.join(
            self.base_dir,
            '2013',
            'insitu',
            'veg{separator}structure',
            'D17_2013_{site_name}_vegStr.csv').format(
               site_name=str.upper(site_name), separator=separator)

        self.chm_path = os.path.join(
            self.base_dir,
            '2013',
            'lidar',
            '{site_name}_lidarCHM.tif').format(
                site_name=str.upper(site_name))
        # There is a difference in how the plot centroids are named
        # for SJER and the other sites.  Since we are only using
        # two sites, we don't make this more general.
        # This is a suboptimal solution to make a general class.
        if site_name == 'sjer':
            self.plot_path = os.path.join(
                self.base_dir,
                'vector_data',
                '{site_name}_plot_centroids.shp').format(
                    site_name=str.upper(site_name))
        else:
            self.plot_path = os.path.join(
                self.base_dir,
                'vector_data',
                '{site_name}_centroids.shp').format(
                    site_name=str.upper(site_name))

    def get_plot_centroids(self):
        """
        Reads the plot centroid shapefile and buffers the geometry.

        Returns
        -------
        plots_gdf : geopandas.GeoDataFrame
            A geopandas dataframe with the buffered plot centroids.
        """
        import geopandas as gpd
        plots_gdf = gpd.read_file(self.plot_path)
        plots_gdf.geometry = plots_gdf.geometry.buffer(20)

        return plots_gdf

    def calculate_zonal_stats(self, plots_gdf):
        """
        Calculate zonal statistics (mean and max) for the given
        GeoDataFrame using the lidar canopy height model (CHM).

        Parameters
        ----------
        plots_gdf : geopandas.GeoDataFrame
            A geopandas dataframe containing plot geometries.
        Returns
        -------
        geopandas.GeoDataFrame
            A geopandas dataframe containing the zonal statistics
            (mean and max) for each plot.
        """
        import geopandas as gpd
        import rasterstats as rs
        site_chm_stats = rs.zonal_stats(
            plots_gdf,
            self.chm_path,
            stats=['mean', 'max'],
            geojson_out=True,
            nodata=0,
            copy_properties=True)

        site_chm_stat_gdf = gpd.GeoDataFrame.from_features(site_chm_stats)
        site_chm_stat_gdf.rename(
            columns={'max': 'lidar_max', 'mean': 'lidar_mean'},
            inplace=True)

        return site_chm_stat_gdf

    def get_insitu_data(self):
        """
        Reads the insitu vegetation structure data and calculates
        the maximum and mean canopy height for each plot.

        Returns
        -------
        geopandas.GeoDataFrame
            A geopandas dataframe containing the maximum and mean
            canopy height for each plot.
        """
        import pandas as pd
        insitu_df = (pd.read_csv(self.insitu_path)
                     [['plotid', 'stemheight']]
                     .groupby('plotid')
                     .stemheight
                     .agg(['max', 'mean'])
                     .rename(columns={'max': 'insitu_canopy_ht_max',
                                      'mean': 'insitu_canopy_ht_mean'})
                     .reset_index()
                     )
        insitu_df.rename(
            columns={'stemheight': 'insitu_canopy_ht'},
            inplace=True)

        return insitu_df

    def merge_insitu_data(self, site_name: str):
        """
        Merge the insitu data with the lidar-derived zonal statistics
        data.

        Parameters
        ----------
        site_name : str
            The name of the site to process.
            We need this to know how to merge the insitu data.
            Not a general solution.

        Returns
        -------
        geopandas.GeoDataFrame
            A geopandas dataframe containing merged insitu and
            lidar-derived zonal statistics data.
        """
        insitu_df = self.get_insitu_data()
        site_chm_stat_gdf = self.execute_pipeline()

        if site_name == 'sjer':
            site_chm_stat_gdf = site_chm_stat_gdf.merge(
                insitu_df, left_on='Plot_ID', right_on='plotid', how='left')
        else:
            site_chm_stat_gdf['plotid'] = (['SOAP' + id_numb for id_numb
                                            in site_chm_stat_gdf.ID.to_list()])
            site_chm_stat_gdf = site_chm_stat_gdf.merge(
                insitu_df, left_on='plotid', right_on='plotid', how='left')

        return site_chm_stat_gdf.dropna(axis=0)

    def execute_pipeline(self):
        """
        Executes the pipleline by getting the plot centroids and
        calculating the zonal statistics.

        Returns
        -------
        geopandas.GeoDataFrame
            A geopandas dataframe containing the zonal statistics
            for each plot.
        """
        plots_gdf = self.get_plot_centroids()

        return self.calculate_zonal_stats(plots_gdf)
