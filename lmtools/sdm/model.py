"""Module containing tools for creating an SDM."""
import glob
import os

from lmpy.point import Point, PointCsvWriter
from lmpy.tools.create_rare_species_model import (
    create_rare_species_model,
    read_points,
)

from lmtools.sdm.maxent import create_maxent_model, DEFAULT_MAXENT_OPTIONS


# .....................................................................................
def sym_link_env(in_dir, out_dir):
    """Create a work env directory and sym link input layers.

    Args:
        in_dir (str): Directory containing input layers.
        out_dir (str): New directory that should include sym links.
    """
    if not os.path.exists(out_dir):
        os.makedirs(out_dir)
    for fn in glob.glob(f'{in_dir}/*'):
        os.symlink(fn, os.path.join(out_dir, os.path.basename(fn)))


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
    y_key='y',
    create_mask=True,
):
    """Entry point method for creating an SDM."""
    point_tuples = read_points(csv_filename, sp_key, x_key, y_key)
    species_name = 'species'
    report = {
        'num_points': len(point_tuples)
    }

    if len(point_tuples) < min_points:
        model_raster_filename = os.path.join(work_dir, f'{species_name}.tif')
        create_rare_species_model(point_tuples, ecoregions_filename, model_raster_filename)
        report['method'] = 'rare_species_model'
    else:
        # Create model env layer directory in work dir
        work_env_dir = os.path.join(work_dir, 'model_layers')
        sym_link_env(env_dir, work_env_dir)
        model_raster_filename = os.path.join(work_dir, f'{species_name}.asc')

        if create_mask:
            create_rare_species_model(
                point_tuples, ecoregions_filename, os.path.join(work_env_dir, 'mask.asc')
            )
            maxent_arguments += ' togglelayertype=mask'

        # TODO: Projections

        me_csv_filename = os.path.join(work_dir, 'species_points.csv')
        with PointCsvWriter(me_csv_filename, ['species_name', 'x', 'y']) as writer:
            writer.write_points([Point(species_name, x, y) for x, y in point_tuples])
        create_maxent_model(me_csv_filename, work_env_dir, work_dir, maxent_arguments)
        report['method'] = 'maxent'

    return model_raster_filename, report
