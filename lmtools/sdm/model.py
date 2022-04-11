"""Module containing tools for creating an SDM."""
from lmpy.point import PointCsvWriter
from lmpy.tools.create_rare_species_model import (
    create_rare_species_model,
    read_points,
)

from lmtools.sdm.maxent import create_maxent_model, DEFAULT_MAXENT_OPTIONS


# .....................................................................................
def create_sdm(
    min_points,
    csv_filename,
    env_dir,
    ecoregions_filename,
    work_dir,
    maxent_arguments=DEFAULT_MAXENT_OPTIONS,
    sp_key='species_name',
    x_key='x',
    y_key='y'
):
    """Entry point method for creating an SDM."""
    points = read_points(csv_filename, sp_key, x_key, y_key)

    if len(points) < min_points:
        create_rare_species_model(points, ecoregions_filename, model_raster_filename)
    else:
        me_csv_filename = os.path.join(work_dir, 'species_points.csv')
        with PointCsvWriter(me_csv_filename, ['species_name', 'x', 'y']) as writer:
            writer.write_points(points)
        create_maxent_model(me_csv_filename, env_dir, work_dir, maxent_arguments)
