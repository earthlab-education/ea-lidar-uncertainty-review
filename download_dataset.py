def download_dataset(home_dir):
    """ 
    Get project dataset from Earthpy.
    """

    import os
    import earthpy as et

    # Getting the list of directories
    dir = os.listdir(home_dir)

    # Check if dataset has already been downloaded.
    # Checking if the list is empty or not
    if len(dir) == 0:
        et.data.get_data('spatial-vector-lidar')
    else:
        print("SJER LIDAR DATA EXISTS.")
